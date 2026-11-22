---
candidateId: "openalex--W7237059392"
category: "Paper"
date: "2026-11-22"
rank: 5
title: "Blind tests of a simple-body model of submarine target strength on open benchmarks"
authors:
  - "Sunil Tyagi"
research_direction: []
journal: "arXiv (Cornell University)"
publisher: "Cornell University"
doi: "10.48550/arxiv.2611.25977"
publication_year: 2026
summary: "该论文针对潜艇目标强度建模问题，提出简化体模型SSR-Sim并对开放基准进行盲测验证。有限元和边界元模型需要网格与求解器且计算成本随频率快速增加，SSR-Sim采用解析路线：将艇体分解为若干简单体，各简单体回波由几何声学或Kirchhoff近似给出闭式结果，表面通过平面波反射系数引入，回波按能量叠加。"
keywords: []
score: 56.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7237059392"
  - name: "DOI"
    url: "https://doi.org/10.48550/arxiv.2611.25977"
previewImage: "/daily/2026-11-22/assets/openalex--W7237059392/preview.png"
---

## 核心内容

该论文针对潜艇目标强度建模问题，提出简化体模型SSR-Sim并对开放基准进行盲测验证。有限元和边界元模型需要网格与求解器且计算成本随频率快速增加，SSR-Sim采用解析路线：将艇体分解为若干简单体，各简单体回波由几何声学或Kirchhoff近似给出闭式结果，表面通过平面波反射系数引入，回波按能量叠加。

## 关键技术与数据

关键技术为基于几何声学与Kirchhoff近似的解析目标强度建模方法，将潜艇艇体与围壳简化为若干简单几何体，各体回波采用闭式解计算，表面声学特性由平面波反射系数表征，总回波按能量相加。论文描述了该方法及艇体与围壳的简化过程，并在开放基准上开展盲测验证，具体基准数据未在摘要中详述。

## 结果与结论

论文通过开放基准盲测检验了SSR-Sim简化体模型的有效性，表明该解析方法能够在避免有限元/边界元网格与求解器成本的前提下给出潜艇目标强度预报，其创新点在于以简单体分解与闭式回波叠加实现高频段低计算成本的目标强度快速预估，为声呐回声仿真提供了高效替代途径。

## 来源链接

- OpenAlex：https://openalex.org/W7237059392
- DOI：https://doi.org/10.48550/arxiv.2611.25977