---
candidateId: "arxiv--2609.37540-1"
category: "Paper"
date: "2026-09-30"
rank: 2
title: "Rate-Agnostic Bioacoustics: Heterogeneous Multi-Taxa Classification with Continuous Filterbanks and Fourier Neural Operators"
authors:
  - "Stefano Ciapponi"
  - "Francesco Ardan Dal Rı"
  - "Nicola Conci"
  - "Elisabetta Farella"
research_direction: []
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "该论文针对生物声学分类中传统模型依赖固定采样率、需重采样导致高频信息损失的问题，提出采样频率无关（SFI）前端与傅里叶神经算子（FNO）骨干网络相结合的框架。目标是在异构采样率、多类群录音条件下直接进行连续滤波与分类，避免重采样带来的信息损失与计算开销，提升多物种分类的鲁棒性和通用性。"
keywords:
  - "classification"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2609.37540v1"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2609.37540v1"
previewImage: "/daily/2026-09-30/assets/arxiv--2609.37540-1/preview.png"
---

## 核心内容

该论文针对生物声学分类中传统模型依赖固定采样率、需重采样导致高频信息损失的问题，提出采样频率无关（SFI）前端与傅里叶神经算子（FNO）骨干网络相结合的框架。目标是在异构采样率、多类群录音条件下直接进行连续滤波与分类，避免重采样带来的信息损失与计算开销，提升多物种分类的鲁棒性和通用性。

## 关键技术与数据

关键技术包括采样频率无关前端（SFI），直接以原始采样率处理录音；傅里叶神经算子（FNO）骨干，具备渐进时间尺度融合能力；连续滤波器组替代固定频带表示。方法避免固定率重采样和高频信息丢失。摘要未列出具体数据集，但面向异构采样率、多类群生物声学数据，需覆盖不同采样率与物种。

## 结果与结论

论文预期在异构采样率多类群分类任务中取得优于固定率重采样基线的性能，同时保留高频信息并降低预处理复杂度。创新点在于将SFI前端与FNO结合，实现速率无关的连续滤波与多尺度融合。结论表明该框架可提升生物声学分类的泛化性与部署灵活性，具体指标需参见原文。

## 来源链接

- arXiv：http://arxiv.org/abs/2609.37540v1
- PDF：http://arxiv.org/pdf/2609.37540v1