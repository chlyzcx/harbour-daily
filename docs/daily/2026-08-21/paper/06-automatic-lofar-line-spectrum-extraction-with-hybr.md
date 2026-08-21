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
summary: "该论文针对舰船辐射噪声LOFAR谱图中线谱特征自动提取困难的问题，提出了一种结合混合数据集构建和连续性感知U-Net的方法。研究背景是线谱对被动声纳目标识别至关重要，但背景起伏和干扰导致人工标注和自动提取均具挑战。目标是实现鲁棒的线谱自动提取，并解决监督学习训练数据不足的问题。"
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

该论文针对舰船辐射噪声LOFAR谱图中线谱特征自动提取困难的问题，提出了一种结合混合数据集构建和连续性感知U-Net的方法。研究背景是线谱对被动声纳目标识别至关重要，但背景起伏和干扰导致人工标注和自动提取均具挑战。目标是实现鲁棒的线谱自动提取，并解决监督学习训练数据不足的问题。

## 关键技术与数据

关键技术包括混合数据集构建，融合仿真线谱（可控参数）与实测噪声背景生成训练样本；连续性感知U-Net，在标准U-Net中引入时序连续性约束（如CRF或时序注意力），以保持线谱在时间轴上的轨迹连贯性。数据方面使用实测舰船辐射噪声LOFAR谱图，并辅以仿真数据扩充。

## 结果与结论

实验表明，所提方法在线谱检测率、虚警率和提取连续性上优于传统图像处理方法和普通U-Net，在强干扰背景下仍能准确提取弱线谱。混合数据集有效提升了模型泛化能力。创新点在于将线谱的时序连续性先验融入深度学习架构，并提出了实用的训练数据合成方案。

## 来源链接

- OpenAlex：https://openalex.org/W7203636981
- DOI：https://doi.org/10.3390/jmse14161511