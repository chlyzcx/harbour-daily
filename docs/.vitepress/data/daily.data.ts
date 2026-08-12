import { createContentLoader } from 'vitepress'

export interface ArticleSource {
  name: string
  url: string
}

export type ArticleCategory = 'Paper'

export type ResearchDirection =
  | '水声通信信道'
  | '水声通信'
  | '水声侦察'
  | '海洋生物声学信号处理'

export interface DailyArticle {
  candidateId: string
  date: string
  rank: number
  title: string
  authors: string[]
  summary: string
  keywords: string[]
  score: number
  sources: ArticleSource[]
  category: ArticleCategory
  research_direction: ResearchDirection[]
  journal?: string
  publisher?: string
  doi?: string
  publication_year?: number
  previewImage?: string
  url: string
}

export interface Facet {
  name: string
  count: number
}

export interface DirectionFacet {
  value: ResearchDirection
  label: string
  count: number
}

export interface DailyGroup {
  date: string
  articles: DailyArticle[]
  directions: DirectionFacet[]
  keywords: Facet[]
}

export interface DailyArchive {
  dates: DailyGroup[]
  articleCount: number
}

function requiredString(value: unknown, field: string, path: string): string {
  if (typeof value !== 'string' || !value.trim()) {
    throw new Error(`${path}: front matter "${field}" must be a non-empty string`)
  }
  return value
}

function requiredNumber(value: unknown, field: string, path: string): number {
  if (typeof value !== 'number' || !Number.isFinite(value)) {
    throw new Error(`${path}: front matter "${field}" must be a number`)
  }
  return value
}

function requiredCategory(value: unknown, path: string): ArticleCategory {
  if (value !== 'Paper') {
    throw new Error(`${path}: front matter "category" must be Paper`)
  }
  return value
}

function requiredDate(value: unknown, path: string): string {
  if (value instanceof Date && !Number.isNaN(value.valueOf())) {
    return value.toISOString().slice(0, 10)
  }
  return requiredString(value, 'date', path)
}

function optionalPreviewImage(value: unknown, path: string): string | undefined {
  if (value === undefined || value === null) return undefined
  const image = requiredString(value, 'previewImage', path)
  const isValid = (image.startsWith('/daily/') || image.startsWith('/journal-covers/')) && !image.includes('..')
  if (!isValid) {
    throw new Error(`${path}: front matter "previewImage" must be null or a local /daily/ or /journal-covers/ path`)
  }
  return image
}

function optionalString(value: unknown, field: string, path: string): string | undefined {
  if (value === undefined || value === null) return undefined
  return requiredString(value, field, path)
}

function optionalNumber(value: unknown, field: string, path: string): number | undefined {
  if (value === undefined || value === null) return undefined
  return requiredNumber(value, field, path)
}

function stringList(value: unknown, field: string, path: string): string[] {
  if (!Array.isArray(value) || value.some((item) => typeof item !== 'string')) {
    throw new Error(`${path}: front matter "${field}" must be an array of strings`)
  }
  return value
}

function directionList(value: unknown, path: string): ResearchDirection[] {
  const validDirections: ResearchDirection[] = [
    '水声通信信道',
    '水声通信',
    '水声侦察',
    '海洋生物声学信号处理'
  ]
  if (!Array.isArray(value)) {
    throw new Error(`${path}: front matter "research_direction" must be an array`)
  }
  return value.map((item) => {
    if (!validDirections.includes(item as ResearchDirection)) {
      throw new Error(
        `${path}: front matter "research_direction" contains invalid value "${item}"`
      )
    }
    return item as ResearchDirection
  })
}

function parseSources(value: unknown, path: string): ArticleSource[] {
  if (!Array.isArray(value) || value.length === 0) {
    throw new Error(`${path}: front matter "sources" must contain at least one source`)
  }

  return value.map((source, index) => {
    if (!source || typeof source !== 'object') {
      throw new Error(`${path}: source ${index + 1} must contain name and url`)
    }
    const item = source as Record<string, unknown>
    return {
      name: requiredString(item.name, `sources[${index}].name`, path),
      url: requiredString(item.url, `sources[${index}].url`, path)
    }
  })
}

const directionOptions: ReadonlyArray<{ value: ResearchDirection; label: string }> = [
  { value: '水声通信信道', label: '水声通信信道' },
  { value: '水声通信', label: '水声通信' },
  { value: '水声侦察', label: '水声侦察' },
  { value: '海洋生物声学信号处理', label: '海洋生物声学信号处理' }
]

function directionFacets(items: DailyArticle[]): DirectionFacet[] {
  return directionOptions.map(({ value, label }) => ({
    value,
    label,
    count: items.filter((article) => article.research_direction.includes(value)).length
  }))
}

function aggregate(items: DailyArticle[], values: (article: DailyArticle) => string[]): Facet[] {
  const counts = new Map<string, number>()
  for (const article of items) {
    for (const value of new Set(values(article))) {
      counts.set(value, (counts.get(value) ?? 0) + 1)
    }
  }

  return [...counts.entries()]
    .sort((left, right) => right[1] - left[1] || left[0].localeCompare(right[0], 'zh-CN'))
    .map(([name, count]) => ({ name, count }))
}

export default createContentLoader('daily/*/*.md', {
  transform(pages): DailyArchive {
    const articles = pages.map(({ url, frontmatter }) => {
      const article: DailyArticle = {
        candidateId: requiredString(frontmatter.candidateId, 'candidateId', url),
        date: requiredDate(frontmatter.date, url),
        rank: requiredNumber(frontmatter.rank, 'rank', url),
        title: requiredString(frontmatter.title, 'title', url),
        authors: stringList(frontmatter.authors, 'authors', url),
        summary: requiredString(frontmatter.summary, 'summary', url),
        keywords: stringList(frontmatter.keywords, 'keywords', url),
        score: requiredNumber(frontmatter.score, 'score', url),
        sources: parseSources(frontmatter.sources, url),
        category: requiredCategory(frontmatter.category, url),
        research_direction: directionList(frontmatter.research_direction, url),
        url
      }
      article.journal = optionalString(frontmatter.journal, 'journal', url)
      article.publisher = optionalString(frontmatter.publisher, 'publisher', url)
      article.doi = optionalString(frontmatter.doi, 'doi', url)
      article.publication_year = optionalNumber(frontmatter.publication_year, 'publication_year', url)
      article.previewImage = optionalPreviewImage(frontmatter.previewImage, url)
      return article
    })

    const grouped = new Map<string, DailyArticle[]>()
    for (const article of articles) {
      const items = grouped.get(article.date) ?? []
      items.push(article)
      grouped.set(article.date, items)
    }

    const dates = [...grouped.entries()]
      .sort(([left], [right]) => right.localeCompare(left))
      .map(([date, items]) => {
        if (items.length > 5) {
          throw new Error(`${date}: a daily archive may contain at most 5 articles`)
        }
        const candidateIds = new Set<string>()
        const ranks = new Set<number>()
        for (const article of items) {
          if (!Number.isInteger(article.rank) || article.rank < 1) {
            throw new Error(`${article.url}: front matter "rank" must be a positive integer`)
          }
          if (candidateIds.has(article.candidateId)) {
            throw new Error(`${date}: duplicate candidateId "${article.candidateId}"`)
          }
          if (ranks.has(article.rank)) {
            throw new Error(`${date}: duplicate rank ${article.rank}`)
          }
          candidateIds.add(article.candidateId)
          ranks.add(article.rank)
        }
        items.sort((left, right) => left.rank - right.rank || right.score - left.score)
        return {
          date,
          articles: items,
          directions: directionFacets(items),
          keywords: aggregate(items, (article) => article.keywords)
        }
      })

    return { dates, articleCount: articles.length }
  }
})
