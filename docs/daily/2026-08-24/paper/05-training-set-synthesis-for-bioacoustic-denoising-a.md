---
candidateId: "s2--75c05986318d3dc5aab0d40c52d558fa7d4f4119"
category: "Paper"
date: "2026-08-24"
rank: 5
title: "Training Set Synthesis for Bioacoustic Denoising: A Case Study With Mice"
authors:
  - "R. Abbasi"
  - "Péter Balázs"
  - "Vincent Lostanlen"
  - "Clara Hollomey"
  - "D. Penn"
  - "Sarah M. Zala"
  - "Nicki Holighaus"
research_direction: []
journal: "IEEE Transactions on Audio, Speech, and Language Processing"
publisher: "Semantic Scholar"
doi: "10.1109/TASLPRO.2026.3705687"
publication_year: 2026
summary: "生物声学记录常受环境噪声干扰，影响弱信号或重叠发声的分析。卷积神经网络（尤其是U-Net架构）在语音和音乐去噪中表现优异，但应用于生物声学去噪受限于干净训练数据的稀缺。本研究提出训练集合成方法，开发监督去噪模型，用于预测干净生物声学信号。"
keywords:
  - "classification"
  - "neural network"
  - "tracking"
score: 60.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.1109/TASLPRO.2026.3705687"
  - name: "Semantic Scholar"
    url: "https://www.semanticscholar.org/paper/75c05986318d3dc5aab0d40c52d558fa7d4f4119"
  - name: "PDF"
    url: "https://arxiv.org/pdf/2608.10054"
previewImage: "/daily/2026-08-24/assets/s2--75c05986318d3dc5aab0d40c52d558fa7d4f4119/preview.png"
---

## 核心内容

生物声学记录常受环境噪声干扰，影响弱信号或重叠发声的分析。卷积神经网络（尤其是U-Net架构）在语音和音乐去噪中表现优异，但应用于生物声学去噪受限于干净训练数据的稀缺。本研究提出训练集合成方法，开发监督去噪模型，用于预测干净生物声学信号。

## 关键技术与数据

核心技术为训练集合成策略，通过模拟噪声叠加生成配对训练数据，解决干净数据稀缺问题。采用U-Net架构作为去噪模型，学习从带噪信号到干净信号的映射。以小鼠发声为案例，构建合成训练集并验证模型性能。

## 结果与结论

合成训练集方法有效解决了生物声学去噪中训练数据不足的问题，U-Net模型在合成和真实数据上均表现出良好去噪效果。该方法为生物声学信号处理提供了可行的数据增强途径，创新性地将训练集合成应用于生物声学去噪领域。

## 来源链接

- DOI：https://doi.org/10.1109/TASLPRO.2026.3705687
- Semantic Scholar：https://www.semanticscholar.org/paper/75c05986318d3dc5aab0d40c52d558fa7d4f4119
- PDF：https://arxiv.org/pdf/2608.10054