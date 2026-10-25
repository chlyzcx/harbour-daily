---
candidateId: "openalex--W7223333821"
category: "Paper"
date: "2026-10-25"
rank: 9
title: "Self-Supervised Multibeam Sonar Restoration via Coherent Forward Modeling"
authors:
  - "Zixin Wang"
  - "James Hopgood"
  - "Mike Davies"
research_direction: []
journal: "arXiv (Cornell University)"
publisher: "Cornell University"
doi: "10.48550/arxiv.2610.31490"
publication_year: 2026
summary: "该论文研究多波束成像声呐的自监督复原问题。多波束成像声呐产生的强度图像受相干斑噪声与系统模糊退化，而干净反射率目标难以获取。现有去斑方法多依赖简化强度域噪声模型、合成干净目标或盲点自监督，且通常不联合建模去模糊与去斑。论文提出一种物理一致的自监督框架，实现多波束成像声呐的联合去斑与去模糊。"
keywords: []
score: 56.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7223333821"
  - name: "DOI"
    url: "https://doi.org/10.48550/arxiv.2610.31490"
previewImage: "/daily/2026-10-25/assets/openalex--W7223333821/preview.png"
---

## 核心内容

该论文研究多波束成像声呐的自监督复原问题。多波束成像声呐产生的强度图像受相干斑噪声与系统模糊退化，而干净反射率目标难以获取。现有去斑方法多依赖简化强度域噪声模型、合成干净目标或盲点自监督，且通常不联合建模去模糊与去斑。论文提出一种物理一致的自监督框架，实现多波束成像声呐的联合去斑与去模糊。

## 关键技术与数据

提出基于相干前向建模（coherent forward modeling）的自监督框架，利用声呐成像的物理前向模型约束网络学习，实现联合去斑（despeckling）与去模糊（deblurring）。方法不依赖合成干净目标或盲点自监督，而是通过物理一致的成像模型构建自监督信号。数据为多波束成像声呐强度图像，涵盖相干斑与系统模糊退化情形。

## 结果与结论

框架通过物理一致的前向建模实现了去斑与去模糊的联合优化，克服了现有方法分离处理与依赖简化噪声模型的局限。结论表明相干前向建模可为多波束声呐复原提供有效的自监督约束，在无干净参考条件下提升图像质量，创新点在于将声呐成像物理模型嵌入自监督学习，实现联合去斑去模糊的物理一致复原。

## 来源链接

- OpenAlex：https://openalex.org/W7223333821
- DOI：https://doi.org/10.48550/arxiv.2610.31490