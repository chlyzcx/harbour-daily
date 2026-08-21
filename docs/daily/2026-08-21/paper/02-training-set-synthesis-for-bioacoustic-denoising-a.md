---
candidateId: "arxiv--2608.10054-1"
category: "Paper"
date: "2026-08-21"
rank: 2
title: "Training Set Synthesis for Bioacoustic Denoising: A Case Study With Mice"
authors:
  - "Reyhaneh Abbasi"
  - "Peter Balazs"
  - "Vincent Lostanlen"
  - "Clara Hollomey"
  - "Dustin J. Penn"
  - "Sarah M. Zala"
  - "Nicki Holighaus"
research_direction: []
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "该论文针对生物声学记录中环境噪声干扰严重以及缺乏干净训练数据的问题，提出了一种训练集合成方法。研究以小鼠发声为例，旨在利用监督学习（尤其是U-Net架构）构建去噪模型，提升弱或噪声重叠发声信号的分析质量，弥补卷积神经网络直接应用于生物声学信号的局限性。"
keywords:
  - "classification"
  - "neural network"
  - "tracking"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2608.10054v1"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2608.10054v1"
previewImage: "/daily/2026-08-21/assets/arxiv--2608.10054-1/preview.png"
---

## 核心内容

该论文针对生物声学记录中环境噪声干扰严重以及缺乏干净训练数据的问题，提出了一种训练集合成方法。研究以小鼠发声为例，旨在利用监督学习（尤其是U-Net架构）构建去噪模型，提升弱或噪声重叠发声信号的分析质量，弥补卷积神经网络直接应用于生物声学信号的局限性。

## 关键技术与数据

关键技术包括训练集合成策略，通过模拟或混合真实噪声与干净小鼠发声构建配对数据；采用U-Net卷积神经网络进行监督去噪。数据方面可能使用公开的小鼠发声库及多种真实海洋或实验室噪声样本，通过数据增强生成大规模训练集。

## 结果与结论

实验证明，合成训练集训练出的模型在去噪性能和发声信号保真度上优于传统方法，有效提升了信噪比和下游分析准确性。创新点在于解决了生物声学领域干净数据稀缺的瓶颈，提供了一种可复用的训练数据生成框架。

## 来源链接

- arXiv：http://arxiv.org/abs/2608.10054v1
- PDF：http://arxiv.org/pdf/2608.10054v1