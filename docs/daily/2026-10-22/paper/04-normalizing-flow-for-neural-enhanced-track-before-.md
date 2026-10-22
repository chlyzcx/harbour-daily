---
candidateId: "openalex--W7223055489"
category: "Paper"
date: "2026-10-22"
rank: 4
title: "Normalizing Flow for Neural-Enhanced Track-Before-Detect"
authors:
  - "Shaoxiu Wei"
  - "Bhaskar Rao"
  - "Florian Meyer"
research_direction: []
journal: "arXiv (Cornell University)"
publisher: "Cornell University"
doi: "10.48550/arxiv.2610.25044"
publication_year: 2026
summary: "多目标跟踪（MOT）是自主导航、雷达与声呐系统及6G通感一体化网络的基础能力。本文提出一种神经增强的检测前跟踪（TkBD）框架，直接处理复值原始信号，并在运行过程中学习未建模传播效应的潜在表征；通过引入环境相关的潜在强度变量刻画各目标信号功率，提升复杂传播条件下的多目标检测跟踪性能。"
keywords:
  - "tracking"
score: 55.2
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7223055489"
  - name: "DOI"
    url: "https://doi.org/10.48550/arxiv.2610.25044"
previewImage: "/daily/2026-10-22/assets/openalex--W7223055489/preview.png"
---

## 核心内容

多目标跟踪（MOT）是自主导航、雷达与声呐系统及6G通感一体化网络的基础能力。本文提出一种神经增强的检测前跟踪（TkBD）框架，直接处理复值原始信号，并在运行过程中学习未建模传播效应的潜在表征；通过引入环境相关的潜在强度变量刻画各目标信号功率，提升复杂传播条件下的多目标检测跟踪性能。

## 关键技术与数据

关键技术包括检测前跟踪（TkBD）框架、复值原始信号直接处理、环境相关潜在强度变量建模，以及归一化流（Normalizing Flow）用于潜变量分布学习；方法在运行时在线学习未建模传播效应。数据为复值原始信号（仿真/实测未在摘要中明确），以多目标跟踪场景验证。

## 结果与结论

该框架能够在存在未建模传播效应的条件下直接从原始复值信号实现多目标检测与跟踪，环境相关潜在强度变量增强了对信号功率变化的适应性。创新点在于将归一化流与TkBD结合并直接处理复值信号，提升雷达/声呐多目标跟踪的鲁棒性（摘要未给出具体性能指标）。

## 来源链接

- OpenAlex：https://openalex.org/W7223055489
- DOI：https://doi.org/10.48550/arxiv.2610.25044