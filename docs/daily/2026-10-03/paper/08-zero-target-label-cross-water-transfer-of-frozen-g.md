---
candidateId: "openalex--W7215116743"
category: "Paper"
date: "2026-10-03"
rank: 8
title: "Zero-Target-Label Cross-Water Transfer of Frozen General-Purpose Audio Foundation Models for Underwater Acoustic Target Recognition"
authors:
  - "Hao Yuan"
  - "Wenbo Wang"
  - "Mengbo Hua"
  - "Guici Chen"
  - "Chong He"
  - "Xuan Hou"
research_direction:
  - "信号识别"
journal: "Preprints.org"
doi: "10.20944/preprints202609.1744.v3"
publication_year: 2026
summary: "通用音频基础模型（FM）尚未在跨水域UATR中被系统评估，即使在水声数据上训练的模型其迁移性能也会灾难性下降。该论文将八种公开基础模型作为冻结特征提取器，在本系列四个UATR语料库（258,893个片段）上进行基准测试，涵盖语料内评估和跨水域迁移，系统评估零目标标签条件下通用音频FM的跨水域迁移能力。"
keywords:
  - "underwater acoustic target recognition"
score: 64.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7215116743"
  - name: "DOI"
    url: "https://doi.org/10.20944/preprints202609.1744.v3"
previewImage: "/daily/2026-10-03/assets/openalex--W7215116743/preview.svg"
---

## 核心内容

通用音频基础模型（FM）尚未在跨水域UATR中被系统评估，即使在水声数据上训练的模型其迁移性能也会灾难性下降。该论文将八种公开基础模型作为冻结特征提取器，在本系列四个UATR语料库（258,893个片段）上进行基准测试，涵盖语料内评估和跨水域迁移，系统评估零目标标签条件下通用音频FM的跨水域迁移能力。

## 关键技术与数据

评估八种公开基础模型：wav2vec2-base/large、HuBERT-base、WavLM-base+、AST、CLAP-HTSAT、PANNs-CNN14、BEATs。作为冻结特征提取器，在四个UATR语料库（258,893个片段）上进行基准测试，涵盖语料内评估和跨水域迁移评估，零目标标签条件下考察迁移性能。

## 结果与结论

实验表明通用音频基础模型在跨水域UATR中迁移性能显著下降，即使冻结特征提取也未能弥合水域间的声学域差距。不同基础模型间性能差异明显，但整体跨水域泛化能力有限。该工作为UATR中基础模型选型提供了系统基准，指出需针对水声域特性进行专门适配。

## 来源链接

- OpenAlex：https://openalex.org/W7215116743
- DOI：https://doi.org/10.20944/preprints202609.1744.v3