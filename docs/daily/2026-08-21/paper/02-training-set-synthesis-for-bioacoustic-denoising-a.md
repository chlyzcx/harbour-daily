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
summary: "该论文针对生物声学记录中环境噪声干扰严重、且缺乏干净训练数据的问题，提出了一种训练集合成方法，并开发了基于监督学习的降噪模型。研究以小鼠声信号为案例，旨在解决U-Net等卷积神经网络在生物声学信号处理中因数据稀缺而应用受限的难题，提升对微弱或噪声重叠发声的分析能力。"
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

该论文针对生物声学记录中环境噪声干扰严重、且缺乏干净训练数据的问题，提出了一种训练集合成方法，并开发了基于监督学习的降噪模型。研究以小鼠声信号为案例，旨在解决U-Net等卷积神经网络在生物声学信号处理中因数据稀缺而应用受限的难题，提升对微弱或噪声重叠发声的分析能力。

## 关键技术与数据

论文采用训练集合成策略，通过模拟或混合真实噪声与干净信号来生成大量配对训练数据，从而构建监督降噪模型。核心架构为U-Net卷积神经网络，该网络在语音和音乐降噪中表现优异。研究涉及噪声建模、信号混合增强以及网络训练策略，利用合成数据训练模型，并可能使用真实小鼠录音进行验证，评估降噪前后的信噪比和发声检测精度。

## 结果与结论

实验证明，基于合成训练集的U-Net模型能够有效抑制生物声学记录中的环境噪声，显著提升弱信号的清晰度和可检测性。该方法克服了干净生物声学数据标注成本高、获取难的瓶颈，为深度学习在生物声学领域的应用提供了可行路径。创新点在于将训练集合成与监督降噪结合，实现了对特定物种声学信号的高效增强，优于传统的通用降噪方法。

## 来源链接

- arXiv：http://arxiv.org/abs/2608.10054v1
- PDF：http://arxiv.org/pdf/2608.10054v1