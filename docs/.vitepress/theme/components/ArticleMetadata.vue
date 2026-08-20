<script setup lang="ts">
import { computed } from 'vue'
import { useData } from 'vitepress'

const { frontmatter } = useData()
const isArticle = computed(() => Boolean(frontmatter.value.candidateId))
</script>

<template>
  <div
    v-if="isArticle"
    hidden
    data-article-contract="true"
    :data-candidate-id="frontmatter.candidateId"
    :data-date="frontmatter.date"
    :data-category="frontmatter.category"
    :data-rank="frontmatter.rank"
    :data-score="frontmatter.score"
  />
</template>
