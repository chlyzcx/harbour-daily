---
candidateId: "openalex--W4404432410"
category: "Paper"
date: "2026-08-21"
rank: 7
title: "DEMONet: Underwater acoustic target recognition based on multi-expert network and cross-temporal variational autoencoder"
authors:
  - "Yuan Xie"
  - "Xiaowei Zhang"
  - "Jiawei Ren"
  - "Xu Ji"
research_direction:
  - "信号识别"
journal: "Knowledge-Based Systems"
publisher: "Elsevier BV"
doi: "10.1016/j.knosys.2026.116820"
publication_year: 2026
summary: "该论文针对水下声学目标识别中特征表达单一、时序依赖利用不足的问题，提出了基于多专家网络和跨时间变分自编码器（VAE）的DEMONet框架。研究背景是舰船辐射噪声的调制谱（DEMON谱）和线谱特征互补，但传统方法难以联合建模。目标是构建一个能融合多域特征并捕获跨时间相关性的识别网络。"
keywords:
  - "underwater acoustic target recognition"
score: 63.2
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W4404432410"
  - name: "DOI"
    url: "https://doi.org/10.1016/j.knosys.2026.116820"
previewImage: "/daily/2026-08-21/assets/openalex--W4404432410/preview.png"
---

## 核心内容

该论文针对水下声学目标识别中特征表达单一、时序依赖利用不足的问题，提出了基于多专家网络和跨时间变分自编码器（VAE）的DEMONet框架。研究背景是舰船辐射噪声的调制谱（DEMON谱）和线谱特征互补，但传统方法难以联合建模。目标是构建一个能融合多域特征并捕获跨时间相关性的识别网络。

## 关键技术与数据

关键技术包括多专家网络，分别处理DEMON谱、LOFAR谱和原始时域波形等不同特征；跨时间变分自编码器，用于学习时间序列的潜在分布并生成鲁棒特征表示；通过注意力机制融合多专家输出。数据可能采用实测舰船噪声数据库，包含多种船型和工况。

## 结果与结论

实验结果显示，DEMONet在目标识别准确率上优于单一特征网络和传统融合方法，尤其在样本量有限时表现出更好的泛化性能。跨时间VAE有效建模了调制谱的时变特性。创新点在于将多专家架构与变分自编码器结合，实现了多域特征与时序信息的深度联合利用。

## 来源链接

- OpenAlex：https://openalex.org/W4404432410
- DOI：https://doi.org/10.1016/j.knosys.2026.116820