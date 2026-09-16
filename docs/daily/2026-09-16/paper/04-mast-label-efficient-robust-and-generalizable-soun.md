---
candidateId: "arxiv--2609.15221-1"
category: "Paper"
date: "2026-09-16"
rank: 4
title: "MAST: Label-Efficient, Robust, and Generalizable Sound Detection for Biodiversity Monitoring via Masked Audio Pretraining and Self-Training"
authors:
  - "Tianyi Xu"
  - "Daniel Pimentel-Alarcón"
  - "Zuzana Buřivalová"
  - "Claudia Solís-Lemus"
research_direction:
  - "被动声学监测"
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "被动声学监测可大尺度测量生物多样性，但动物发声的时频标注昂贵、地点特异且难以规模化。本文提出MAST框架，结合掩码音频预训练与轻量检测器，在梅尔频谱图上实现标签高效、鲁棒且可泛化的声音检测，并通过未标注音频的迭代自训练进一步提升性能。研究目标是降低标注依赖，提升跨站点检测泛化能力。"
keywords:
  - "detection"
  - "localization"
  - "passive acoustic monitoring"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2609.15221v1"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2609.15221v1"
previewImage: "/daily/2026-09-16/assets/arxiv--2609.15221-1/preview.png"
---

## 核心内容

被动声学监测可大尺度测量生物多样性，但动物发声的时频标注昂贵、地点特异且难以规模化。本文提出MAST框架，结合掩码音频预训练与轻量检测器，在梅尔频谱图上实现标签高效、鲁棒且可泛化的声音检测，并通过未标注音频的迭代自训练进一步提升性能。研究目标是降低标注依赖，提升跨站点检测泛化能力。

## 关键技术与数据

MAST首先在未标注录音上通过掩码重建预训练ViT编码器，学习通用声学表征；随后在梅尔频谱图上训练轻量检测器，利用少量标注数据；再通过迭代自训练，用高置信度伪标签扩充训练集。关键技术包括掩码音频预训练、ViT编码器、梅尔频谱图检测器及自训练策略。数据可能来自多站点生物声学录音，涵盖多种动物发声。

## 结果与结论

实验表明，MAST在标签高效场景下优于基线方法，检测精度与鲁棒性显著提升，且跨站点泛化能力增强。自训练进一步利用未标注数据，缩小与全监督方法的差距。创新点在于将掩码音频预训练与自训练结合，为生物多样性监测提供可扩展、低标注成本的声音检测方案。

## 来源链接

- arXiv：http://arxiv.org/abs/2609.15221v1
- PDF：http://arxiv.org/pdf/2609.15221v1