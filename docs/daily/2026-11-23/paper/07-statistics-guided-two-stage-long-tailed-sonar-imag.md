---
candidateId: "openalex--W7237053405"
category: "Paper"
date: "2026-11-23"
rank: 7
title: "Statistics-guided two-stage long-tailed sonar image recognition"
authors:
  - "Jia-yi Han"
  - "Jian-wei Liu"
research_direction: []
journal: "Engineering Applications of Artificial Intelligence"
publisher: "Elsevier BV"
doi: "10.1016/j.engappai.2026.116685"
publication_year: 2026
summary: "该论文针对声呐图像识别中的长尾分布问题，提出统计引导的两阶段长尾声呐图像识别方法。研究背景是实际声呐数据集类别分布极不均衡，少数类样本稀缺导致深度模型识别性能下降。主要内容包括第一阶段利用统计信息进行特征/分类器校准或重平衡，第二阶段进行针对性微调与决策优化，以提升尾部类别识别精度并保持头部类别性能。"
keywords: []
score: 51.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7237053405"
  - name: "DOI"
    url: "https://doi.org/10.1016/j.engappai.2026.116685"
previewImage: "/daily/2026-11-23/assets/openalex--W7237053405/preview.png"
---

## 核心内容

该论文针对声呐图像识别中的长尾分布问题，提出统计引导的两阶段长尾声呐图像识别方法。研究背景是实际声呐数据集类别分布极不均衡，少数类样本稀缺导致深度模型识别性能下降。主要内容包括第一阶段利用统计信息进行特征/分类器校准或重平衡，第二阶段进行针对性微调与决策优化，以提升尾部类别识别精度并保持头部类别性能。

## 关键技术与数据

关键技术包括长尾分布统计分析、两阶段训练策略（如重采样/重加权、分类器校准、解耦训练与微调）以及统计引导的决策边界调整。方法上结合深度卷积网络特征提取与类别平衡优化。数据为声呐图像数据集，具有典型长尾分布特征，用于训练与评估模型在头部与尾部类别上的识别性能。

## 结果与结论

实验表明，统计引导的两阶段方法在长尾声呐图像识别上优于常规训练与单一重采样策略，显著提升尾部类别准确率与整体平衡性能，同时保持头部类别精度。结论指出，结合数据分布统计信息进行分阶段优化可有效缓解声呐图像识别中的长尾偏差问题，提升模型在实际不平衡数据集上的鲁棒性。

## 来源链接

- OpenAlex：https://openalex.org/W7237053405
- DOI：https://doi.org/10.1016/j.engappai.2026.116685