---
candidateId: "openalex--W7213306341"
category: "Paper"
date: "2026-09-17"
rank: 7
title: "Source-Free Domain Adaptation for Underwater Acoustic Target Recognition: When Batch Normalization Statistics Alone Suffice"
authors:
  - "Hao Yuan"
  - "Wenbo Wang"
  - "Fan Huang"
  - "Guici Chen"
  - "Xiwu Li"
  - "Fanyu Wang"
research_direction:
  - "信号识别"
journal: "Preprints.org"
doi: "10.20944/preprints202609.1126.v1"
publication_year: 2026
summary: "水下声目标识别（UATR）深度分类器在部署水域与训练水域不同时性能崩溃。无监督域适应（UDA）可恢复部分损失，但需联合访问源数据，而军事和商业声纳记录通常保密或专有，该假设不成立。本文研究无源域适应（SFUDA），仅用目标域无标签数据调整冻结源模型，探索仅靠批归一化统计量是否足够。"
keywords:
  - "detection"
  - "underwater acoustic target recognition"
score: 64.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7213306341"
  - name: "DOI"
    url: "https://doi.org/10.20944/preprints202609.1126.v1"
previewImage: "/daily/2026-09-17/assets/openalex--W7213306341/preview.svg"
---

## 核心内容

水下声目标识别（UATR）深度分类器在部署水域与训练水域不同时性能崩溃。无监督域适应（UDA）可恢复部分损失，但需联合访问源数据，而军事和商业声纳记录通常保密或专有，该假设不成立。本文研究无源域适应（SFUDA），仅用目标域无标签数据调整冻结源模型，探索仅靠批归一化统计量是否足够。

## 关键技术与数据

采用SFUDA框架，仅更新批归一化（BN）统计量；源模型冻结；使用目标域无标签数据；数据集为水声目标识别语料库，具体未详述；评估跨域识别准确率。

## 结果与结论

结果表明，仅调整BN统计量即可显著提升跨水域UATR性能，接近完整UDA方法的效果，且无需源数据。创新点在于揭示了BN统计量在SFUDA中的关键作用，为保密场景下的UATR部署提供了轻量级解决方案。

## 来源链接

- OpenAlex：https://openalex.org/W7213306341
- DOI：https://doi.org/10.20944/preprints202609.1126.v1