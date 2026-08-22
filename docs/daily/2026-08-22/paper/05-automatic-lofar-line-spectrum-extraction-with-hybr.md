---
candidateId: "openalex--W7203636981"
category: "Paper"
date: "2026-08-22"
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
summary: "舰船辐射噪声中的线谱特征对被动声呐目标分析识别至关重要。然而，由于强背景波动和干扰，从LOFAR谱图中自动提取线谱仍具挑战性，且监督学习方法受限于人工标注数据不足。该论文提出一种结合混合数据集构建和连续性感知U-Net的自动线谱提取方法。"
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

舰船辐射噪声中的线谱特征对被动声呐目标分析识别至关重要。然而，由于强背景波动和干扰，从LOFAR谱图中自动提取线谱仍具挑战性，且监督学习方法受限于人工标注数据不足。该论文提出一种结合混合数据集构建和连续性感知U-Net的自动线谱提取方法。

## 关键技术与数据

方法包括：构建混合训练数据集，融合仿真线谱、真实噪声背景及人工标注，以扩充样本多样性；设计连续性感知U-Net，在标准U-Net中引入时序连续性约束或注意力机制，以增强线谱在时频域上的轨迹连贯性，抑制离散噪声点。

## 结果与结论

实验结果表明，该方法在检测率、虚警率和线谱连续性方面均优于传统图像处理方法和标准U-Net，能有效从强干扰背景中提取稳定、完整的线谱轨迹。该研究为被动声呐的自动目标识别提供了更可靠的特征提取工具。

## 来源链接

- OpenAlex：https://openalex.org/W7203636981
- DOI：https://doi.org/10.3390/jmse14161511