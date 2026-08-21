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
summary: "该论文聚焦于生物声学信号降噪中训练数据稀缺的问题。研究背景在于环境噪声严重干扰对微弱或重叠动物发声的分析，而U-Net等卷积神经网络在语音和音乐降噪中表现优异，但其直接应用于生物声学信号受限于干净训练样本的匮乏。论文目标是通过提出一种训练集合成方法，构建监督降噪模型，以提升生物声学信号的信噪比。"
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

该论文聚焦于生物声学信号降噪中训练数据稀缺的问题。研究背景在于环境噪声严重干扰对微弱或重叠动物发声的分析，而U-Net等卷积神经网络在语音和音乐降噪中表现优异，但其直接应用于生物声学信号受限于干净训练样本的匮乏。论文目标是通过提出一种训练集合成方法，构建监督降噪模型，以提升生物声学信号的信噪比。

## 关键技术与数据

关键技术为训练集合成策略，即通过将干净的小鼠发声信号与多种真实或模拟的环境噪声以不同信噪比混合，生成大量带标签的训练样本。模型架构采用U-Net卷积神经网络，学习从含噪输入到干净输出的映射。数据方面，使用了小鼠发声数据集及多种噪声库（如实验室环境噪声、笼内噪声），并可能通过数据增强技术扩充样本多样性。

## 结果与结论

实验结果显示，基于合成训练集训练的U-Net模型在真实含噪小鼠发声数据上取得了显著的降噪效果，有效恢复了被噪声掩盖的发声结构，优于传统谱减法等基线方法。该研究证明了训练集合成策略在解决生物声学领域数据稀缺问题上的有效性。主要创新点在于提出了一种低成本、可扩展的监督降噪训练范式，为后续生物声学自动分析提供了高质量预处理工具。

## 来源链接

- arXiv：http://arxiv.org/abs/2608.10054v1
- PDF：http://arxiv.org/pdf/2608.10054v1