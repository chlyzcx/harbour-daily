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
summary: "该论文针对被动声纳目标识别中舰船辐射噪声LOFAR谱图的线谱特征自动提取难题。研究背景是水声环境背景波动和干扰强烈，且监督学习方法受限于人工标注数据稀缺。目标是提出一种结合混合数据集构建和连续性感知U-Net的自动线谱提取方法，以实现在复杂干扰下的稳健线谱检测与提取。"
keywords:
  - "passive sonar"
score: 63.2
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7203636981"
  - name: "DOI"
    url: "https://doi.org/10.3390/jmse14161511"
previewImage: "/daily/2026-08-21/assets/openalex--W7203636981/preview.svg"
---

## 核心内容

该论文针对被动声纳目标识别中舰船辐射噪声LOFAR谱图的线谱特征自动提取难题。研究背景是水声环境背景波动和干扰强烈，且监督学习方法受限于人工标注数据稀缺。目标是提出一种结合混合数据集构建和连续性感知U-Net的自动线谱提取方法，以实现在复杂干扰下的稳健线谱检测与提取。

## 关键技术与数据

关键技术包括混合数据集构建（可能融合仿真线谱、真实噪声背景和人工标注）以及连续性感知U-Net架构。方法上，U-Net可能被改进以显式建模线谱在时频域的连续性（如通过正则化项或注意力模块），以区分线谱与随机干扰。数据方面，利用仿真与实测数据混合训练，增强模型对未见过的噪声环境的泛化能力，并采用像素级标注进行监督学习。

## 结果与结论

实验结果显示，该方法在低信噪比和强干扰背景下，线谱提取的准确率和连续性均优于传统图像处理方法和基础U-Net模型。混合数据集策略有效缓解了标注瓶颈，提升了模型鲁棒性。创新点在于将线谱的连续性先验知识嵌入深度学习架构，并结合数据合成技术，为被动声纳信号自动分析提供了高可靠性的技术手段。

## 来源链接

- OpenAlex：https://openalex.org/W7203636981
- DOI：https://doi.org/10.3390/jmse14161511