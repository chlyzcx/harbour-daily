---
candidateId: "openalex--W7203636981"
category: "Paper"
date: "2026-08-21"
rank: 5
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
summary: "该论文针对被动声纳中舰船辐射噪声的LOFAR谱图线谱特征自动提取难题，提出了一种结合混合数据集构建与连续性感知U-Net的自动提取方法。由于背景波动强、干扰多，且人工标注数据稀缺，传统监督学习方法受限。研究旨在实现高鲁棒性的线谱自动提取，以支撑目标识别与分类。"
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

该论文针对被动声纳中舰船辐射噪声的LOFAR谱图线谱特征自动提取难题，提出了一种结合混合数据集构建与连续性感知U-Net的自动提取方法。由于背景波动强、干扰多，且人工标注数据稀缺，传统监督学习方法受限。研究旨在实现高鲁棒性的线谱自动提取，以支撑目标识别与分类。

## 关键技术与数据

关键技术包括混合数据集构建：融合仿真线谱（基于物理模型）与真实海试数据，生成带精确标注的训练样本，解决数据稀缺问题。网络设计采用U-Net变体，引入连续性感知模块（如条件随机场或时序卷积）以强化线谱在频率-时间域上的连续结构先验。数据方面，使用LOFAR谱图作为输入，标注像素级线谱掩码。

## 结果与结论

实验结果表明，该方法在真实舰船噪声数据上实现了较高的线谱提取精度和连续性，优于传统图像处理方法和未引入连续性约束的U-Net基线。结论指出，混合数据训练与结构先验嵌入有效提升了模型泛化能力，为被动声纳自动目标识别提供了可靠的预处理工具。

## 来源链接

- OpenAlex：https://openalex.org/W7203636981
- DOI：https://doi.org/10.3390/jmse14161511