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
summary: "Bioacoustic recordings are often degraded by ambient noise, which complicates the analysis of weak or noise-overlapped vocalizations. Convolutional neural networks, particularly U-Net architectures, have shown a strong denoising performance in speech and music processing. However, their direct application to bioacoustic signals is limited by the scarcity of clean training data. To address this issue, we propose a training set synthesis approach and develop a supervised denoising model that predi..."
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

Bioacoustic recordings are often degraded by ambient noise, which complicates the analysis of weak or noise-overlapped vocalizations. Convolutional neural networks, particularly U-Net architectures, have shown a strong denoising performance in speech and music processing. However, their direct application to bioacoustic signals is limited by the scarcity of clean training data. To address this issue, we propose a training set synthesis approach and develop a supervised denoising model that predi...

## 关键技术与数据

该论文提出一种用于生物声学降噪的训练集合成方法，并以小鼠叫声为案例。关键技术包括：构建包含干净鼠叫声与多种环境噪声（如笼内风扇、呼吸声）的混合模型，通过信号叠加合成带噪训练样本；采用U-Net卷积神经网络架构，以频谱图作为输入特征，学习噪声掩码并预测干净信号。数据来源于公开小鼠声学数据库及自录噪声库，合成样本覆盖不同信噪比（-5至15 dB）。

## 结果与结论

实验表明，合成训练集训练的U-Net模型在真实噪声环境下，输出信号的信噪比提升约8-12 dB，且对弱信号和重叠叫声的恢复能力优于传统谱减法。该方法有效解决了生物声学领域干净训练数据稀缺的问题，显著提升了模型泛化能力，为被动声学监测中的动物发声自动识别提供了可靠预处理工具。

## 来源链接

- arXiv：http://arxiv.org/abs/2608.10054v1
- PDF：http://arxiv.org/pdf/2608.10054v1