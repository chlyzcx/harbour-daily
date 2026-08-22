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
summary: "该论文针对生物声学信号去噪中干净训练数据稀缺的问题，提出了一种训练集合成方法。研究以小鼠超声叫声为案例，旨在通过合成多样化的带噪训练样本，训练基于U-Net的监督去噪模型，从而提升对弱信号和噪声重叠叫声的恢复能力。"
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

该论文针对生物声学信号去噪中干净训练数据稀缺的问题，提出了一种训练集合成方法。研究以小鼠超声叫声为案例，旨在通过合成多样化的带噪训练样本，训练基于U-Net的监督去噪模型，从而提升对弱信号和噪声重叠叫声的恢复能力。

## 关键技术与数据

关键技术包括：基于信号模型的训练样本合成，将干净叫声与多种真实噪声（如环境噪声、设备噪声）按不同信噪比混合；采用U-Net架构进行时频掩码预测。数据方面，使用了公开的小鼠叫声数据库和采集的多种背景噪声库，构建了大规模配对训练集。

## 结果与结论

实验证明，基于合成数据集训练的模型在真实小鼠叫声去噪任务中，信噪比提升和主观听感均优于传统谱减法及未使用合成数据的模型。该研究验证了训练集合成策略在生物声学领域的有效性，为解决小样本监督学习问题提供了可行方案，具有较好的泛化能力。

## 来源链接

- arXiv：http://arxiv.org/abs/2608.10054v1
- PDF：http://arxiv.org/pdf/2608.10054v1