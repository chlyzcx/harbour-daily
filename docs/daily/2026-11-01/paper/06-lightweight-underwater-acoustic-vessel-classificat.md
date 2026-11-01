---
candidateId: "openalex--W7224749276"
category: "Paper"
date: "2026-11-01"
rank: 6
title: "Lightweight Underwater Acoustic Vessel Classification for Embedded Deployment"
authors:
  - "Abishek Soti"
  - "Thura Pyae Sone"
  - "Naqib Ibnul"
  - "Jim Huang"
  - "Sergio Chevtchenko"
  - "Henry Zhong"
  - "Gregory Cohen"
  - "Ying Xu"
research_direction: []
journal: "arXiv (Cornell University)"
publisher: "Cornell University"
doi: "10.48550/arxiv.2610.39371"
publication_year: 2026
summary: "针对海上声学监视中连接受限、带宽与功耗受限的边缘部署需求，该论文提出基于树莓派的水下船舶分类系统。研究目标是在嵌入式平台上实现完整的音频到预测管线，比较六种分类器的分类性能、处理时延、CPU占用、内存消耗与功耗。论文基于ShipsEar数据集开展实验，并辅以声学特征选择、统计池化与Transformer结构的支持性实验。"
keywords:
  - "classification"
  - "neural network"
score: 56.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7224749276"
  - name: "DOI"
    url: "https://doi.org/10.48550/arxiv.2610.39371"
previewImage: "/daily/2026-11-01/assets/openalex--W7224749276/preview.png"
---

## 核心内容

针对海上声学监视中连接受限、带宽与功耗受限的边缘部署需求，该论文提出基于树莓派的水下船舶分类系统。研究目标是在嵌入式平台上实现完整的音频到预测管线，比较六种分类器的分类性能、处理时延、CPU占用、内存消耗与功耗。论文基于ShipsEar数据集开展实验，并辅以声学特征选择、统计池化与Transformer结构的支持性实验。

## 关键技术与数据

关键技术包括嵌入式部署、轻量级分类器、声学特征提取、统计池化与Transformer模式。方法上在树莓派5上构建端到端音频处理与分类管线，比较六种分类器的性能与资源开销。数据方面使用ShipsEar船舶辐射噪声数据集，支持性实验考察特征选择与池化策略对性能的影响。

## 结果与结论

论文给出了六种分类器在树莓派5上的分类性能与资源消耗对比，结果表明轻量级模型能够在嵌入式平台上实现可接受的分类精度与实时处理能力，处理时延、CPU占用与功耗处于边缘部署可行范围。结论指出特征选择与统计池化对轻量级船舶分类性能具有重要影响，为海上声学监视的边缘部署提供了工程参考。具体量化指标因摘要截断未完整列出。

## 来源链接

- OpenAlex：https://openalex.org/W7224749276
- DOI：https://doi.org/10.48550/arxiv.2610.39371