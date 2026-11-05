---
candidateId: "arxiv--2611.06725-1"
category: "Paper"
date: "2026-11-05"
rank: 1
title: "Drowning in Noise: On Signal Saliency in Self-Supervised Learning for Ocean Acoustics"
authors:
  - "Shikhar Bharadwaj"
  - "Samuele Cornell"
  - "Shinji Watanabe"
  - "Malcolm Slaney"
research_direction: []
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "该论文针对海洋声学自监督学习（SSL）中训练数据信噪比失衡问题展开研究。被动水声录音以海浪、风噪声和静默为主，生物声信号仅占极小比例，导致SSL模型将表征容量分配给声学上无意义的成分。论文旨在揭示这种噪声过表征现象对SSL表征质量的影响机制，并探索提升信号显著性感知的预训练策略。"
keywords:
  - "classification"
  - "sparse"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2611.06725v1"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2611.06725v1"
previewImage: "/daily/2026-11-05/assets/arxiv--2611.06725-1/preview.png"
---

## 核心内容

该论文针对海洋声学自监督学习（SSL）中训练数据信噪比失衡问题展开研究。被动水声录音以海浪、风噪声和静默为主，生物声信号仅占极小比例，导致SSL模型将表征容量分配给声学上无意义的成分。论文旨在揭示这种噪声过表征现象对SSL表征质量的影响机制，并探索提升信号显著性感知的预训练策略。

## 关键技术与数据

采用自监督学习框架，分析海洋声学被动录音数据集中的信号显著性分布。通过表征容量分配分析、信号显著性度量及预训练语料构成实验，评估噪声主导数据对模型学习的影响，并提出针对性的数据筛选或加权策略以增强生物声事件的表征学习。

## 结果与结论

研究表明，海洋声学被动录音中噪声的过度表征使SSL模型偏向学习声学琐碎特征，削弱了对稀疏生物声信号的建模能力。论文揭示了语料规模与学习信号质量之间的非平凡关系，提出信号显著性感知的预训练改进方向，为海洋声学SSL的数据构建与模型设计提供指导。

## 来源链接

- arXiv：http://arxiv.org/abs/2611.06725v1
- PDF：http://arxiv.org/pdf/2611.06725v1