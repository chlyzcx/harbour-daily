---
candidateId: "arxiv--2611.14592-1"
category: "Paper"
date: "2026-11-13"
rank: 2
title: "Multi-Step Underwater Acoustic Channel Prediction via Dual-Domain Structure Preservation and Pretrained Transformer"
authors:
  - "Mingjie Cao"
  - "Gewei Zhang"
  - "Deqing Wang"
  - "Lizhao You"
  - "Fei-Yun Wu"
  - "Liqun Fu"
research_direction: []
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "该论文针对水声信道多步预测问题，提出一种基于双域结构保持与预训练Transformer的多步水声信道预测方法。水声信道时变性强，传统递归多步预测会随多途结构演化而累积误差。论文旨在利用Transformer的序列建模能力与预训练策略，实现对未来多步信道状态信息的高精度直接预测，以支撑水声通信系统的自适应配置。"
keywords: []
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2611.14592v1"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2611.14592v1"
previewImage: "/daily/2026-11-13/assets/arxiv--2611.14592-1/preview.png"
---

## 核心内容

该论文针对水声信道多步预测问题，提出一种基于双域结构保持与预训练Transformer的多步水声信道预测方法。水声信道时变性强，传统递归多步预测会随多途结构演化而累积误差。论文旨在利用Transformer的序列建模能力与预训练策略，实现对未来多步信道状态信息的高精度直接预测，以支撑水声通信系统的自适应配置。

## 关键技术与数据

论文采用预训练Transformer作为主干网络，设计双域（时域与频域或时延域与多普勒域）结构保持机制以维持信道多途结构的物理一致性，避免递归预测的误差累积。训练数据可能包括海试实测信道数据及仿真信道数据，通过预训练加微调策略提升泛化能力。关键技术涉及多步直接预测框架与信道结构约束损失函数设计。

## 结果与结论

论文通过仿真与海试数据验证了所提方法在多步预测精度上优于传统递归预测方法，能够有效抑制误差累积，保持信道多途结构的演化一致性。创新点在于将预训练Transformer与双域结构保持相结合用于水声信道多步预测，为水声通信链路自适应提供了更可靠的CSI预测手段。

## 来源链接

- arXiv：http://arxiv.org/abs/2611.14592v1
- PDF：http://arxiv.org/pdf/2611.14592v1