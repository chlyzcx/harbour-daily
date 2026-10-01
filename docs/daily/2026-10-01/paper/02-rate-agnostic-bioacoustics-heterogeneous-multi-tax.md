---
candidateId: "arxiv--2609.37540-2"
category: "Paper"
date: "2026-10-01"
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
summary: "针对传统生物声学分类模型依赖固定采样率频谱表示、需重采样导致高频信息丢失的问题，本文提出一种采样频率无关（SFI）前端与Fourier神经算子（FNO）骨干网络相结合的框架，实现异构多物种生物声学分类。研究目标是直接在原始采样率下处理录音，避免重采样带来的信息损失。"
keywords:
  - "classification"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2609.37540v2"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2609.37540v2"
previewImage: "/daily/2026-10-01/assets/arxiv--2609.37540-2/preview.png"
---

## 核心内容

针对传统生物声学分类模型依赖固定采样率频谱表示、需重采样导致高频信息丢失的问题，本文提出一种采样频率无关（SFI）前端与Fourier神经算子（FNO）骨干网络相结合的框架，实现异构多物种生物声学分类。研究目标是直接在原始采样率下处理录音，避免重采样带来的信息损失。

## 关键技术与数据

核心技术包括采样频率无关前端，直接处理各录音的原生采样率；Fourier神经算子骨干网络，具备渐进式时间尺度融合能力；连续滤波器组替代固定速率频谱表示。数据涵盖多种采样率的生物声学录音，涉及多个物种分类任务，包括鸟类、蛙类等异质类群。

## 结果与结论

该框架在异构采样率条件下实现了鲁棒的多物种分类性能，避免了固定速率重采样和高频信息损失。结果表明SFI前端与FNO骨干的结合能有效处理变采样率数据，提升了跨采样率场景下的分类泛化能力，创新性地将Fourier神经算子引入生物声学分类领域。

## 来源链接

- arXiv：http://arxiv.org/abs/2609.37540v2
- PDF：http://arxiv.org/pdf/2609.37540v2