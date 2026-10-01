---
candidateId: "arxiv--2609.37518-2"
category: "Paper"
date: "2026-10-01"
rank: 3
title: "Bad: Taming the Bioacoustic Data Deluge with a Bat Activity Detector"
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
summary: "针对蝙蝠被动声学监测产生海量超声数据（每节点每晚超27GB）导致边缘存储和电池寿命受限的问题，本文提出一种硬件感知的蝙蝠活动检测器（BAD），专门用于在192-384 kHz可变采样率下区分蝙蝠叫声与生物及环境干扰。研究目标是在微控制器上实现高效边缘检测。"
keywords:
  - "passive acoustic monitoring"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2609.37518v2"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2609.37518v2"
previewImage: "/daily/2026-10-01/assets/arxiv--2609.37518-2/preview.png"
---

## 核心内容

针对蝙蝠被动声学监测产生海量超声数据（每节点每晚超27GB）导致边缘存储和电池寿命受限的问题，本文提出一种硬件感知的蝙蝠活动检测器（BAD），专门用于在192-384 kHz可变采样率下区分蝙蝠叫声与生物及环境干扰。研究目标是在微控制器上实现高效边缘检测。

## 关键技术与数据

BAD针对Silicon Labs EFM32PG26微控制器设计，采用8位整数运算优化，硬件感知模型压缩。技术包括轻量级深度学习模型、针对蝙蝠叫声与声学干扰物的判别特征提取。数据涵盖192-384 kHz采样率的蝙蝠超声录音，包含多种生物和环境干扰信号。

## 结果与结论

BAD在微控制器上实现了实时蝙蝠活动检测，有效区分蝙蝠叫声与硬性生物及环境干扰物，显著降低数据传输量和存储需求。结果表明该硬件感知方案在资源受限边缘设备上具有可行性，创新性地解决了多采样率下蝙蝠检测的嵌入式部署难题。

## 来源链接

- arXiv：http://arxiv.org/abs/2609.37518v2
- PDF：http://arxiv.org/pdf/2609.37518v2