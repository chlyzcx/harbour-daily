<script setup lang="ts">
import { computed, ref } from 'vue'
import { withBase } from 'vitepress'
import type { DailyArchive, DailyArticle, ResearchDirection } from '../../data/daily.data'

const props = defineProps<{ archive: DailyArchive }>()

const selectedDate = ref(props.archive.dates[0]?.date ?? '')
const selectedDirection = ref<ResearchDirection | 'all'>('all')
const selectedKeyword = ref('全部')
const selectedSort = ref('rank')

const currentGroup = computed(() =>
  props.archive.dates.find((group) => group.date === selectedDate.value)
)

const directionFacets = computed(() => [
  { value: 'all' as const, label: '全部', count: currentGroup.value?.articles.length ?? 0 },
  ...(currentGroup.value?.directions ?? [])
])

const keywordFacets = computed(() => [
  { name: '全部', count: currentGroup.value?.articles.length ?? 0 },
  ...(currentGroup.value?.keywords ?? [])
])

const matchingArticles = computed(() => {
  const articles = (currentGroup.value?.articles ?? []).filter((article) => {
    const directionMatched = selectedDirection.value === 'all' ||
      article.research_direction.includes(selectedDirection.value)
    const keywordMatched = selectedKeyword.value === '全部' ||
      article.keywords.includes(selectedKeyword.value)
    return directionMatched && keywordMatched
  })

  return articles.sort((left, right) => {
    if (selectedSort.value === 'score') return right.score - left.score || left.rank - right.rank
    if (selectedSort.value === 'title') return left.title.localeCompare(right.title, 'zh-CN')
    return left.rank - right.rank
  })
})

function formatDate(dateStr: string): string {
  const date = new Date(dateStr + 'T00:00:00')
  return date.toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    weekday: 'long'
  })
}

function journalClass(journal?: string): string {
  if (!journal) return 'journal-other'
  const normalized = journal.toLowerCase()
  if (normalized.includes('jasa') || normalized.includes('acoustical society')) return 'journal-jasa'
  if (normalized.includes('ieee journal of oceanic')) return 'journal-joe'
  if (normalized.includes('ieee transactions on signal processing')) return 'journal-tsp'
  if (normalized.includes('ieee transactions on communications')) return 'journal-tcom'
  if (normalized.includes('ieee transactions on aerospace')) return 'journal-taes'
  if (normalized.includes('applied acoustics')) return 'journal-aa'
  if (normalized.includes('ocean engineering')) return 'journal-oe'
  return 'journal-other'
}
</script>

<template>
  <div class="daily-index">
    <div class="archive-header">
      <h1>水声工程每日精选</h1>
      <p class="subtitle">
        每日精选水声通信信道、水声通信、水声侦察、海洋生物声学信号处理领域高质量论文
      </p>
      <div class="stats">
        共收录 {{ archive.articleCount }} 篇 · {{ archive.dates.length }} 期
      </div>
    </div>

    <div class="controls">
      <div class="control-group">
        <label>日期</label>
        <select v-model="selectedDate">
          <option v-for="group in archive.dates" :key="group.date" :value="group.date">
            {{ formatDate(group.date) }} ({{ group.articles.length }} 篇)
          </option>
        </select>
      </div>

      <div class="control-group">
        <label>研究方向</label>
        <select v-model="selectedDirection">
          <option v-for="facet in directionFacets" :key="facet.value" :value="facet.value">
            {{ facet.label }} ({{ facet.count }})
          </option>
        </select>
      </div>

      <div class="control-group">
        <label>关键词</label>
        <select v-model="selectedKeyword">
          <option v-for="facet in keywordFacets" :key="facet.name" :value="facet.name">
            {{ facet.name }} ({{ facet.count }})
          </option>
        </select>
      </div>

      <div class="control-group">
        <label>排序</label>
        <select v-model="selectedSort">
          <option value="rank">按推荐排序</option>
          <option value="score">按评分排序</option>
          <option value="title">按标题排序</option>
        </select>
      </div>
    </div>

    <div class="article-list">
      <article
        v-for="article in matchingArticles"
        :key="article.candidateId"
        class="article-card"
      >
        <div class="article-rank">{{ article.rank }}</div>
        <div class="article-content">
          <div class="article-header">
            <h2 class="article-title">
              <a :href="withBase(article.url)">{{ article.title }}</a>
            </h2>
            <div class="article-score">{{ article.score }}</div>
          </div>

          <div class="article-meta">
            <span class="authors">{{ article.authors.join(', ') }}</span>
            <span v-if="article.journal" class="journal" :class="journalClass(article.journal)">
              {{ article.journal }}
            </span>
            <span v-if="article.publication_year" class="year">{{ article.publication_year }}</span>
          </div>

          <div class="article-directions">
            <span
              v-for="dir in article.research_direction"
              :key="dir"
              class="direction-tag"
            >
              {{ dir }}
            </span>
          </div>

          <p class="article-summary">{{ article.summary }}</p>

          <div class="article-keywords">
            <span
              v-for="kw in article.keywords"
              :key="kw"
              class="keyword-tag"
              @click="selectedKeyword = kw"
            >
              {{ kw }}
            </span>
          </div>

          <div class="article-sources">
            <a
              v-for="source in article.sources"
              :key="source.name"
              :href="source.url"
              target="_blank"
              rel="noopener noreferrer"
              class="source-link"
            >
              {{ source.name }} ↗
            </a>
          </div>
        </div>
      </article>
    </div>

    <div v-if="matchingArticles.length === 0" class="empty-state">
      当前筛选条件下暂无文章
    </div>
  </div>
</template>

<style scoped>
.daily-index {
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem 1rem;
}

.archive-header {
  text-align: center;
  margin-bottom: 2rem;
}

.archive-header h1 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
  color: var(--vp-c-text-1);
}

.subtitle {
  color: var(--vp-c-text-2);
  font-size: 0.95rem;
  margin-bottom: 0.5rem;
}

.stats {
  color: var(--vp-c-text-3);
  font-size: 0.85rem;
}

.controls {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 2rem;
  padding: 1rem;
  background: var(--vp-c-bg-soft);
  border-radius: 8px;
}

.control-group {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.control-group label {
  font-size: 0.8rem;
  color: var(--vp-c-text-2);
  font-weight: 500;
}

.control-group select {
  padding: 0.4rem 0.6rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 4px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  font-size: 0.9rem;
  min-width: 140px;
}

.article-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.article-card {
  display: flex;
  gap: 1rem;
  padding: 1.25rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  background: var(--vp-c-bg);
  transition: box-shadow 0.2s;
}

.article-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.article-rank {
  flex-shrink: 0;
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--vp-c-brand);
  color: white;
  border-radius: 50%;
  font-weight: bold;
  font-size: 1.1rem;
}

.article-content {
  flex: 1;
  min-width: 0;
}

.article-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
  margin-bottom: 0.5rem;
}

.article-title {
  font-size: 1.1rem;
  margin: 0;
  line-height: 1.4;
}

.article-title a {
  color: var(--vp-c-text-1);
  text-decoration: none;
}

.article-title a:hover {
  color: var(--vp-c-brand);
}

.article-score {
  flex-shrink: 0;
  padding: 0.2rem 0.5rem;
  background: var(--vp-c-bg-soft);
  border-radius: 4px;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--vp-c-text-2);
}

.article-meta {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
  font-size: 0.85rem;
  color: var(--vp-c-text-2);
  margin-bottom: 0.5rem;
}

.journal {
  padding: 0.1rem 0.4rem;
  border-radius: 3px;
  font-size: 0.8rem;
  font-weight: 500;
}

.journal-jasa { background: #e3f2fd; color: #1565c0; }
.journal-joe { background: #e8f5e9; color: #2e7d32; }
.journal-tsp { background: #fff3e0; color: #e65100; }
.journal-tcom { background: #f3e5f5; color: #7b1fa2; }
.journal-taes { background: #fce4ec; color: #c2185b; }
.journal-aa { background: #e0f7fa; color: #00838f; }
.journal-oe { background: #fff8e1; color: #ff8f00; }
.journal-other { background: var(--vp-c-bg-soft); color: var(--vp-c-text-2); }

.article-directions {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-bottom: 0.75rem;
}

.direction-tag {
  padding: 0.2rem 0.6rem;
  background: var(--vp-c-brand);
  color: white;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 500;
}

.article-summary {
  font-size: 0.9rem;
  line-height: 1.6;
  color: var(--vp-c-text-2);
  margin-bottom: 0.75rem;
}

.article-keywords {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-bottom: 0.75rem;
}

.keyword-tag {
  padding: 0.15rem 0.5rem;
  background: var(--vp-c-bg-soft);
  border-radius: 4px;
  font-size: 0.8rem;
  color: var(--vp-c-text-2);
  cursor: pointer;
  transition: background 0.2s;
}

.keyword-tag:hover {
  background: var(--vp-c-divider);
}

.article-sources {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.source-link {
  font-size: 0.85rem;
  color: var(--vp-c-brand);
  text-decoration: none;
}

.source-link:hover {
  text-decoration: underline;
}

.empty-state {
  text-align: center;
  padding: 3rem;
  color: var(--vp-c-text-3);
  font-size: 0.95rem;
}

@media (max-width: 640px) {
  .article-card {
    flex-direction: column;
  }

  .article-rank {
    width: 2rem;
    height: 2rem;
    font-size: 1rem;
  }

  .controls {
    flex-direction: column;
  }

  .control-group select {
    width: 100%;
  }
}
</style>
