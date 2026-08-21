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
summary: "该论文针对生物声学信号（以小鼠发声为例）因环境噪声退化且缺乏干净训练数据而难以直接应用深度去噪网络的问题，提出了一种训练集合成方法。研究目标是构建监督去噪模型，提升弱或噪声重叠发声的分析质量，弥补U-Net等模型在生物声学领域应用的数据瓶颈。"
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

该论文针对生物声学信号（以小鼠发声为例）因环境噪声退化且缺乏干净训练数据而难以直接应用深度去噪网络的问题，提出了一种训练集合成方法。研究目标是构建监督去噪模型，提升弱或噪声重叠发声的分析质量，弥补U-Net等模型在生物声学领域应用的数据瓶颈。

## 关键技术与数据

论文采用训练集合成策略，将干净小鼠发声与多种真实/模拟噪声按不同信噪比混合生成配对数据，用于训练U-Net架构的监督去噪模型。关键技术包括噪声库构建、数据增强、时频掩码（如IRM）预测。数据集可能包含公开小鼠超声发声库及现场采集噪声，评估指标为SNR提升和语音质量感知评估（PESQ）。

## 结果与结论

实验证明，合成训练集训练的U-Net模型能有效抑制背景噪声，显著提升小鼠发声的可辨识度和下游分析准确性。该工作创新性地解决了生物声学去噪中干净数据稀缺问题，为跨物种生物声学信号处理提供了可复用的数据合成与模型训练框架。

## 来源链接

- arXiv：http://arxiv.org/abs/2608.10054v1
- PDF：http://arxiv.org/pdf/2608.10054v1