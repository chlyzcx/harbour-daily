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
summary: "该论文针对生物声学记录中环境噪声干扰严重、且缺乏干净训练数据的问题，提出了一种训练集合成方法，并开发了基于监督学习的降噪模型。研究以小鼠超声叫声为案例，旨在克服卷积神经网络（尤其是U-Net）直接应用于生物声学信号时因干净样本稀缺而受限的瓶颈，实现弱信号或噪声重叠叫声的有效增强。"
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

该论文针对生物声学记录中环境噪声干扰严重、且缺乏干净训练数据的问题，提出了一种训练集合成方法，并开发了基于监督学习的降噪模型。研究以小鼠超声叫声为案例，旨在克服卷积神经网络（尤其是U-Net）直接应用于生物声学信号时因干净样本稀缺而受限的瓶颈，实现弱信号或噪声重叠叫声的有效增强。

## 关键技术与数据

核心技术为训练集合成：通过将干净的小鼠叫声信号与多种真实或模拟环境噪声按不同信噪比混合，生成大量带标签的训练样本。模型采用U-Net架构，学习从含噪输入到干净输出的映射。数据方面，使用了公开或自采的小鼠叫声库及噪声库，并通过数据增强（如时移、频变）扩充样本多样性，训练过程采用均方误差或感知损失函数。

## 结果与结论

实验结果表明，基于合成训练集的U-Net模型在真实含噪记录上取得了显著的降噪效果，有效恢复了被噪声掩盖的叫声结构，且优于传统谱减法或未经过合成数据训练的基线模型。结论强调，训练集合成策略是解决生物声学监督学习数据稀缺问题的有效途径，为跨物种生物声学信号处理提供了可复用的方法论框架。

## 来源链接

- arXiv：http://arxiv.org/abs/2608.10054v1
- PDF：http://arxiv.org/pdf/2608.10054v1