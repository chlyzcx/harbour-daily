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
summary: "该论文针对生物声学记录中环境噪声干扰严重、且缺乏干净训练数据限制深度去噪模型应用的问题，提出了一种训练集合成方法。研究以小鼠声学信号为案例，旨在构建监督去噪模型，提升对微弱或噪声重叠发声的提取能力，推动CNN在生物声学领域的实际应用。"
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

该论文针对生物声学记录中环境噪声干扰严重、且缺乏干净训练数据限制深度去噪模型应用的问题，提出了一种训练集合成方法。研究以小鼠声学信号为案例，旨在构建监督去噪模型，提升对微弱或噪声重叠发声的提取能力，推动CNN在生物声学领域的实际应用。

## 关键技术与数据

论文采用U-Net架构的卷积神经网络作为去噪核心，创新点在于训练数据的合成策略：通过将干净的小鼠发声信号与多种真实环境噪声按不同信噪比混合生成配对训练样本。关键技术包括噪声建模、数据增强以及时频域特征提取，以增强模型对未知噪声的泛化能力。

## 结果与结论

实验证明，基于合成训练集的U-Net模型能有效抑制背景噪声，显著提升小鼠发声信号的清晰度和可检测性，其性能优于传统谱减法等基线方法。该研究验证了训练集合成策略在生物声学去噪中的可行性，为缺乏大规模干净标注数据的声学监测任务提供了新思路。

## 来源链接

- arXiv：http://arxiv.org/abs/2608.10054v1
- PDF：http://arxiv.org/pdf/2608.10054v1