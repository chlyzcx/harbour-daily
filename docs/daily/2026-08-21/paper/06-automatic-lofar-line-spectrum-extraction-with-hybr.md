---
candidateId: "openalex--W7203636981"
category: "Paper"
date: "2026-08-21"
rank: 6
title: "Automatic LOFAR Line-Spectrum Extraction with Hybrid Dataset Construction and a Continuity-Aware U-Net"
authors:
  - "Zhongdi Liu"
  - "Chenmu Li"
  - "Bin Zhou"
  - "Qiming Ma"
  - "Liang Xie"
research_direction:
  - "被动声呐"
journal: "Journal of Marine Science and Engineering"
publisher: "Multidisciplinary Digital Publishing Institute"
doi: "10.3390/jmse14161511"
publication_year: 2026
summary: "该论文针对被动声纳中舰船辐射噪声LOFAR谱图的线谱自动提取难题，提出了一种结合混合数据集构建和连续性感知U-Net的自动提取方法。研究旨在克服强背景起伏和干扰下的鲁棒提取问题，并缓解监督学习对人工标注数据的依赖。"
keywords:
  - "passive sonar"
score: 63.2
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7203636981"
  - name: "DOI"
    url: "https://doi.org/10.3390/jmse14161511"
previewImage: "/daily/2026-08-21/assets/openalex--W7203636981/preview.png"
---

## 核心内容

该论文针对被动声纳中舰船辐射噪声LOFAR谱图的线谱自动提取难题，提出了一种结合混合数据集构建和连续性感知U-Net的自动提取方法。研究旨在克服强背景起伏和干扰下的鲁棒提取问题，并缓解监督学习对人工标注数据的依赖。

## 关键技术与数据

混合数据集构建可能融合仿真线谱、实测噪声底和人工标注片段。连续性感知U-Net在标准U-Net基础上引入时序连续性约束（如CRF或时序注意力），以增强线谱的轨迹连贯性。评估使用实测LOFAR谱图，指标包括线谱检测率、虚警率和提取精度。

## 结果与结论

实验显示，该方法在低信噪比和强干扰下仍能高精度提取线谱，显著优于传统图像处理方法和普通U-Net。创新点在于数据合成策略与网络结构中的连续性先验结合，有效解决了标注稀缺和线谱断裂问题，为被动声纳目标识别提供了可靠预处理工具。

## 来源链接

- OpenAlex：https://openalex.org/W7203636981
- DOI：https://doi.org/10.3390/jmse14161511