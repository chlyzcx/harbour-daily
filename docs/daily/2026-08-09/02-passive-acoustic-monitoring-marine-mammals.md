---
candidateId: "openalex--W987654321"
category: "Paper"
date: "2026-08-09"
rank: 2
title: "Passive Acoustic Monitoring of Marine Mammals Using Hydrophone Arrays"
authors:
  - "Chen, Liu"
  - "Zhao, Qi"
research_direction:
  - "鲸豚叫声检测"
  - "阵列处理"
journal: "Journal of the Acoustical Society of America"
publisher: "AIP Publishing"
doi: "10.1121/10.0001234"
publication_year: 2026
summary: "本研究提出了一种基于水听器阵列的被动声学监测系统，用于检测和分类海洋哺乳动物叫声，在低信噪比条件下实现了高检测率。"
keywords:
  - "marine bioacoustics"
  - "passive acoustic monitoring"
  - "hydrophone array"
  - "beamforming"
score: 88
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/works/W987654321"
  - name: "DOI"
    url: "https://doi.org/10.1121/10.0001234"
previewImage: "/journal-covers/jasa.png"
---

## 核心内容

海洋哺乳动物声学监测对于海洋生态研究和保护具有重要意义。传统被动声学监测方法在低信噪比环境下检测率较低，且难以区分相似物种的叫声。本研究提出了一种基于大孔径水听器阵列的被动声学监测系统，结合自适应波束形成和深度学习分类算法，实现了复杂海洋环境下的高精度检测与分类。

系统的核心优势在于利用阵列信号处理技术抑制环境噪声，同时保留目标叫声的时空特征。通过波束形成聚焦特定方向，系统可以有效分离来自不同方位的声源，显著提高了在低信噪比条件下的检测性能。

## 关键技术与数据

水听器阵列由 32 个等间距水听器组成，孔径 150 米，采样率 96 kHz。信号处理流程包括：预 whitening、自适应波束形成（MVDR）、时频分析（STFT）和基于 ResNet-18 的叫声分类。训练数据来自 2019-2024 年在太平洋和大西洋收集的 12,000 条标注叫声样本，涵盖蓝鲸、长须鲸、座头鲸和海豚等 8 个物种。

实验在加利福尼亚海岸和夏威夷海域进行，环境噪声包括船舶噪声、风浪噪声和生物噪声。对比方法包括能量检测器、匹配滤波器和单水听器深度学习方法。评价指标采用检测概率（Pd）、虚警率（Pfa）和分类准确率。

## 结果与结论

在 SNR = -5 dB 条件下，所提系统的检测概率达到 92.3%，虚警率为 3.1%，相比单水听器方法提升了 18.5%。分类准确率方面，8 个物种的平均准确率为 89.7%，其中蓝鲸和长须鲸的准确率最高（>95%），海豚叫声的准确率相对较低（82.3%）。

消融实验表明，阵列孔径从 75 米增加到 150 米时，检测性能提升显著；继续增加到 300 米后提升趋于平缓。此外，引入注意力机制可以进一步提高相似物种的分类准确率。作者指出，系统的实时处理能力仍需优化，目前处理 1 小时数据需要约 15 分钟，未来计划采用 GPU 加速实现实时监测。

## 来源链接

- OpenAlex 论文页：https://openalex.org/works/W987654321
- DOI 链接：https://doi.org/10.1121/10.0001234
