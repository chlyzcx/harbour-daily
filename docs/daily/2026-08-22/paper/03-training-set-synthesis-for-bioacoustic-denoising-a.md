---
candidateId: "arxiv--2608.10054-1"
category: "Paper"
date: "2026-08-22"
rank: 3
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
summary: "生物声学记录常受环境噪声污染，影响对微弱或重叠叫声的分析。虽然U-Net在语音和音乐降噪中表现优异，但缺乏干净的生物声学训练数据限制了其应用。该论文提出一种训练集合成方法，用于开发针对小鼠超声叫声的监督降噪模型。"
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
previewImage: "/daily/2026-08-22/assets/arxiv--2608.10054-1/preview.png"
---

## 核心内容

生物声学记录常受环境噪声污染，影响对微弱或重叠叫声的分析。虽然U-Net在语音和音乐降噪中表现优异，但缺乏干净的生物声学训练数据限制了其应用。该论文提出一种训练集合成方法，用于开发针对小鼠超声叫声的监督降噪模型。

## 关键技术与数据

方法核心是合成带噪训练数据：将干净的小鼠叫声信号与多种真实或模拟的环境噪声（如背景白噪声、笼内机械噪声）按不同信噪比混合，生成大量带标签的训练样本。模型采用U-Net架构，学习从带噪时频谱图到干净时频谱图的映射。

## 结果与结论

实验证明，基于合成数据训练的降噪模型能有效抑制实际记录中的环境噪声，显著提升小鼠叫声的信噪比和可懂度，且优于传统谱减法。该研究验证了训练集合成策略在生物声学降噪中的可行性，为数据稀缺场景下的深度学习应用提供了有效范式。

## 来源链接

- arXiv：http://arxiv.org/abs/2608.10054v1
- PDF：http://arxiv.org/pdf/2608.10054v1