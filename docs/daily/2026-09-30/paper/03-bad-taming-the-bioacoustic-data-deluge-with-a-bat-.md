---
candidateId: "arxiv--2609.37518-1"
category: "Paper"
date: "2026-09-30"
rank: 3
title: "Bad: Taming the Bioacoustic Data Deluge with a Bat Acticity Detector"
authors:
  - "Stefano Ciapponi"
  - "Santiago Martinez Balvanera"
  - "Andrea Cesaretti"
  - "Elisabetta Farella"
  - "Kate E. Jones"
research_direction:
  - "被动声学监测"
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "该论文针对蝙蝠被动声学监测产生海量超声数据（每节点每晚>27 GB）导致边缘存储与电池寿命受限的问题，提出硬件感知的蝙蝠活动检测器（BAD）。传统触发器难以区分蝙蝠叫声与生物及环境混淆声，深度模型又超出微控制器资源限制。BAD旨在以低功耗边缘设备实现跨采样率（192–384 kHz）的蝙蝠叫声与混淆声判别。"
keywords:
  - "passive acoustic monitoring"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2609.37518v1"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2609.37518v1"
previewImage: "/daily/2026-09-30/assets/arxiv--2609.37518-1/preview.png"
---

## 核心内容

该论文针对蝙蝠被动声学监测产生海量超声数据（每节点每晚>27 GB）导致边缘存储与电池寿命受限的问题，提出硬件感知的蝙蝠活动检测器（BAD）。传统触发器难以区分蝙蝠叫声与生物及环境混淆声，深度模型又超出微控制器资源限制。BAD旨在以低功耗边缘设备实现跨采样率（192–384 kHz）的蝙蝠叫声与混淆声判别。

## 关键技术与数据

关键技术为硬件感知的蝙蝠活动检测器（BAD），针对Silicon Labs EFM32PG26（MVP）微控制器优化，采用8位整数量化。方法需在变采样率192–384 kHz下区分蝙蝠叫声与硬生物及环境混淆声。摘要未给出具体数据集名称，但涉及蝙蝠超声录音与混淆声样本，用于训练和评估边缘部署性能。

## 结果与结论

论文预期BAD在微控制器上实现低功耗、低内存的实时检测，性能优于传统触发器且可部署于边缘节点，显著减少数据传输与存储压力。创新点在于硬件感知设计、8位整数量化与跨采样率鲁棒性。结论强调BAD可缓解生物声学数据洪流问题，具体功耗、精度与召回率需参见原文。

## 来源链接

- arXiv：http://arxiv.org/abs/2609.37518v1
- PDF：http://arxiv.org/pdf/2609.37518v1