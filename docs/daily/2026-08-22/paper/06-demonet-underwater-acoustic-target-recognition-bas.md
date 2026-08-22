---
candidateId: "openalex--W4404432410"
category: "Paper"
date: "2026-08-22"
rank: 6
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
summary: "水下目标识别中，单一网络模型难以全面捕捉复杂多变的声学特征。该论文提出DEMONet，一种基于多专家网络和跨时间变分自编码器的水下声学目标识别方法，旨在通过集成学习和深度生成模型提升识别性能。"
keywords:
  - "underwater acoustic target recognition"
score: 63.2
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W4404432410"
  - name: "DOI"
    url: "https://doi.org/10.1016/j.knosys.2026.116820"
previewImage: "/daily/2026-08-22/assets/openalex--W4404432410/preview.png"
---

## 核心内容

水下目标识别中，单一网络模型难以全面捕捉复杂多变的声学特征。该论文提出DEMONet，一种基于多专家网络和跨时间变分自编码器的水下声学目标识别方法，旨在通过集成学习和深度生成模型提升识别性能。

## 关键技术与数据

DEMONet包含多个专家子网络，每个专家专注于提取特定频段或特定调制方式（如DEMON谱分析）的特征。跨时间变分自编码器用于学习声学特征在时间维度上的潜在分布和动态变化，并融合多专家输出进行最终分类。训练数据可能包含实测舰船、潜艇等目标辐射噪声。

## 结果与结论

实验证明，DEMONet在多个水下目标识别任务上取得了优于单网络和传统融合方法的准确率，尤其在目标状态变化或噪声干扰下表现出良好的泛化能力。创新点在于将多专家架构与变分自编码器结合，有效建模了水声信号的时变特性。

## 来源链接

- OpenAlex：https://openalex.org/W4404432410
- DOI：https://doi.org/10.1016/j.knosys.2026.116820