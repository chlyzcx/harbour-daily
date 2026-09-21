---
candidateId: "crossref--10.20944-preprints202609.1125.v2"
category: "Paper"
date: "2026-09-21"
rank: 7
title: "Confidence Inversion in Open-Set Underwater Acoustic Target Recognition: A Leakage-Safe Multi-Corpus Pilot"
authors:
  - "Hao Yuan"
  - "Wenbo Wang"
  - "Lingjiang Zeng"
  - "Guici Chen"
  - "Yu Chen"
  - "Zhengpeng Pang"
research_direction:
  - "信号识别"
journal: "Unknown"
publisher: "MDPI AG"
doi: "10.20944/preprints202609.1125.v2"
publication_year: 2026
summary: "水下声学目标识别系统通常在闭集标签空间评估，但实际部署面临未知目标与采集条件偏移。本文在开放集UATR中研究置信度反转现象，评估五种分数/损失配置在六个记录不相交协议下的表现，涵盖四个语料库，旨在揭示开放集识别中的泄漏安全评估问题。"
keywords:
  - "detection"
  - "underwater acoustic target recognition"
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.20944/preprints202609.1125.v2"
previewImage: "/daily/2026-09-21/assets/crossref--10.20944-preprints202609.1125.v2/preview.svg"
---

## 核心内容

水下声学目标识别系统通常在闭集标签空间评估，但实际部署面临未知目标与采集条件偏移。本文在开放集UATR中研究置信度反转现象，评估五种分数/损失配置在六个记录不相交协议下的表现，涵盖四个语料库，旨在揭示开放集识别中的泄漏安全评估问题。

## 关键技术与数据

采用ResNet-18分类器，分别以交叉熵（CE）或熵开放集损失（EOS）训练，评分采用最大softmax概率（MSP）、能量分数或OpenMax。实验设计六个记录不相交协议，跨四个语料库，每个配置3个随机种子，包括四个语料内协议及跨语料协议，确保泄漏安全评估。

## 结果与结论

研究发现开放集UATR中存在置信度反转现象，即未知目标可能获得高于已知目标的置信度，导致拒识失败。创新点在于通过多语料、多协议泄漏安全评估揭示该问题，指出常用开放集评分在UATR中的局限性，为可靠开放集识别提供警示，但摘要未列出具体反转率数值。

## 来源链接

- DOI：https://doi.org/10.20944/preprints202609.1125.v2