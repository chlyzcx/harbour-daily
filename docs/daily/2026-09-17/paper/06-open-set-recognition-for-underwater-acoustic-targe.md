---
candidateId: "openalex--W7213294314"
category: "Paper"
date: "2026-09-17"
rank: 6
title: "Open-Set Recognition for Underwater Acoustic Target Recognition: A Six-Protocol Pilot Exposing Confidence Inversion Across Water Areas"
authors:
  - "Hao Yuan"
  - "Wenbo Wang"
  - "Lingjiang Zeng"
  - "Guici Chen"
  - "Yu Chen"
  - "庞正鹏"
research_direction:
  - "信号识别"
journal: "Preprints.org"
doi: "10.20944/preprints202609.1125.v1"
publication_year: 2026
summary: "部署的水下声目标识别（UATR）分类器会遇到未训练过的船舶类型，但标准流程的应对能力缺乏系统测量。本文在四个记录不相交语料库上开展六协议开集识别（OSR）试点，包括四个数据集内类留出协议和两个跨库协议（一个语料库已知，另一个测试类全未知），将零迁移发现扩展至OSR场景。"
keywords:
  - "underwater acoustic target recognition"
score: 64.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7213294314"
  - name: "DOI"
    url: "https://doi.org/10.20944/preprints202609.1125.v1"
previewImage: "/daily/2026-09-17/assets/openalex--W7213294314/preview.svg"
---

## 核心内容

部署的水下声目标识别（UATR）分类器会遇到未训练过的船舶类型，但标准流程的应对能力缺乏系统测量。本文在四个记录不相交语料库上开展六协议开集识别（OSR）试点，包括四个数据集内类留出协议和两个跨库协议（一个语料库已知，另一个测试类全未知），将零迁移发现扩展至OSR场景。

## 关键技术与数据

采用ResNet-18分类器，交叉熵训练；六协议包括类留出和跨库设置；评估指标为开集识别性能，如AUROC、闭集准确率等；数据集为四个记录不相交的水声语料库。

## 结果与结论

实验暴露了跨水域场景下的置信度反转现象，即模型对未知类给出高置信度预测，导致OSR性能显著下降。研究揭示了标准UATR流程在开集条件下的脆弱性，为鲁棒开集识别方法设计提供了警示和基准。

## 来源链接

- OpenAlex：https://openalex.org/W7213294314
- DOI：https://doi.org/10.20944/preprints202609.1125.v1