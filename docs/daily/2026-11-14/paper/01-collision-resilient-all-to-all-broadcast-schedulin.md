---
candidateId: "arxiv--2611.16884-1"
category: "Paper"
date: "2026-11-14"
rank: 1
title: "Collision-Resilient All-to-All Broadcast Scheduling in Underwater Acoustic Networks"
authors:
  - "Guoliang Weng"
  - "Enqi Zhang"
  - "Lizhao You"
  - "Deqing Wang"
  - "Liqun Fu"
research_direction:
  - "网络协议"
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "该论文研究水下集群的全对全广播调度问题，针对具备碰撞恢复能力的物理层（可异步解码重叠数据包）展开。传统传播感知无碰撞调度器虽能协调数据包到达时间，却未考虑接收端的碰撞解码能力。论文旨在设计能利用该接收特性的调度方案，提升水下声学网络的全对全广播效率。"
keywords:
  - "underwater acoustic network"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2611.16884v1"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2611.16884v1"
previewImage: "/daily/2026-11-14/assets/arxiv--2611.16884-1/preview.png"
---

## 核心内容

该论文研究水下集群的全对全广播调度问题，针对具备碰撞恢复能力的物理层（可异步解码重叠数据包）展开。传统传播感知无碰撞调度器虽能协调数据包到达时间，却未考虑接收端的碰撞解码能力。论文旨在设计能利用该接收特性的调度方案，提升水下声学网络的全对全广播效率。

## 关键技术与数据

设计数据驱动的神经接收模型，捕捉每个干扰源的功率与时序效应；该模型预测精度优于SINR基线，并可转化为精确的混合整数线性规划形式。在此基础上构建碰撞恢复型调度器，将接收模型嵌入调度优化框架，实现传播感知与碰撞解码能力的联合优化。

## 结果与结论

神经接收模型在预测精度上超越传统SINR方法，且保持优化可解性。所提调度方案利用碰撞恢复能力显著提升全对全广播的调度效率与网络吞吐，证明了在物理层具备重叠包解码能力时，传统无碰撞调度并非最优，为水下集群通信协议设计提供了新思路。

## 来源链接

- arXiv：http://arxiv.org/abs/2611.16884v1
- PDF：http://arxiv.org/pdf/2611.16884v1