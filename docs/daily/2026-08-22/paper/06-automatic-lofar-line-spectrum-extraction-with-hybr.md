---
candidateId: "openalex--W7203636981"
category: "Paper"
date: "2026-08-22"
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
summary: "该论文针对被动声纳中舰船辐射噪声LOFAR谱图线谱提取困难、人工标注数据稀缺的问题，提出了一种自动提取方法。研究通过构建混合数据集并设计连续性感知的U-Net网络，旨在复杂水声背景下实现高精度、高连续性的线谱检测与提取。"
keywords:
  - "passive sonar"
score: 63.2
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7203636981"
  - name: "DOI"
    url: "https://doi.org/10.3390/jmse14161511"
previewImage: "/daily/2026-08-22/assets/openalex--W7203636981/preview.png"
---

## 核心内容

该论文针对被动声纳中舰船辐射噪声LOFAR谱图线谱提取困难、人工标注数据稀缺的问题，提出了一种自动提取方法。研究通过构建混合数据集并设计连续性感知的U-Net网络，旨在复杂水声背景下实现高精度、高连续性的线谱检测与提取。

## 关键技术与数据

关键技术包括：混合数据集构建，融合仿真线谱与真实海试噪声，生成大量带标注的LOFAR谱图；连续性感知U-Net，在标准U-Net中引入时序连续性约束或注意力模块，以增强线谱在频率-时间维度的连贯性。数据涵盖不同信噪比、不同干扰强度的谱图样本。

## 结果与结论

实验表明，该方法在检测精度、虚警率和线谱连续性指标上均优于传统图像处理方法和标准U-Net。该研究有效缓解了标注数据不足的问题，实现了端到端的线谱自动提取，为被动声纳目标识别提供了可靠的特征前端，具有较强工程应用价值。

## 来源链接

- OpenAlex：https://openalex.org/W7203636981
- DOI：https://doi.org/10.3390/jmse14161511