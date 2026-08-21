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
summary: "该论文针对生物声学录音中环境噪声干扰导致弱信号或重叠叫声分析困难的问题，提出了一种训练集合成方法。研究背景在于卷积神经网络（尤其是U-Net）在语音和音乐降噪中表现优异，但直接应用于生物声学信号受限于干净训练数据的稀缺。目标是开发一个基于合成训练集的监督降噪模型，以提升小鼠等模式动物的声学信号降噪性能。"
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

该论文针对生物声学录音中环境噪声干扰导致弱信号或重叠叫声分析困难的问题，提出了一种训练集合成方法。研究背景在于卷积神经网络（尤其是U-Net）在语音和音乐降噪中表现优异，但直接应用于生物声学信号受限于干净训练数据的稀缺。目标是开发一个基于合成训练集的监督降噪模型，以提升小鼠等模式动物的声学信号降噪性能。

## 关键技术与数据

关键技术是训练集合成，即通过模拟或混合干净叫声与真实/模拟噪声构建配对数据，用于训练U-Net架构的降噪模型。方法可能涉及对小鼠超声叫声的合成、噪声库构建及信噪比混合策略。数据方面，可能使用公开的小鼠叫声数据库和多种环境噪声样本，生成大规模、多样化的训练集，并采用真实录音作为测试集以验证模型的泛化能力。

## 结果与结论

实验结果表明，基于合成训练集训练的U-Net模型能有效抑制背景噪声，增强弱叫声信号，其降噪性能在客观指标（如信噪比提升、语音质量感知评估）和主观听觉测试上均优于传统方法。该研究验证了数据合成策略在解决生物声学领域标注数据稀缺问题上的有效性。创新点在于提供了一种可扩展的训练数据生成框架，为深度学习在生物声学信号处理中的应用铺平了道路。

## 来源链接

- arXiv：http://arxiv.org/abs/2608.10054v1
- PDF：http://arxiv.org/pdf/2608.10054v1