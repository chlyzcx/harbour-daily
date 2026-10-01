---
candidateId: "openalex--W7214716911"
category: "Paper"
date: "2026-10-01"
rank: 1
title: "Ocean acoustic field prediction method based on dual-branch physics-informed neural network under insufficient environmental parameters"
authors:
  - "Zeyu Wang"
  - "Yongxian Wang"
  - "Yanqun Wu"
  - "Zhao Sun"
  - "Yunxiang Zhang"
  - "Houwang Tu"
research_direction: []
journal: "Ocean Engineering"
publisher: "Elsevier BV"
doi: "10.1016/j.oceaneng.2026.128177"
publication_year: 2026
summary: "针对海洋声压场精确计算依赖完整环境先验（如全深度声速剖面和海底地声参数）的问题，本文提出一种双分支物理信息神经网络（DB-PINN），在海底地声参数不确定和声速剖面深度截断的条件下预测声压场。研究目标是降低对完整环境参数的依赖，实现不充分环境信息下的声场重构与预测。"
keywords:
  - "neural network"
  - "sparse"
score: 70.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7214716911"
  - name: "DOI"
    url: "https://doi.org/10.1016/j.oceaneng.2026.128177"
previewImage: "/daily/2026-10-01/assets/openalex--W7214716911/preview.png"
---

## 核心内容

针对海洋声压场精确计算依赖完整环境先验（如全深度声速剖面和海底地声参数）的问题，本文提出一种双分支物理信息神经网络（DB-PINN），在海底地声参数不确定和声速剖面深度截断的条件下预测声压场。研究目标是降低对完整环境参数的依赖，实现不充分环境信息下的声场重构与预测。

## 关键技术与数据

采用双分支物理信息神经网络架构，将物理方程约束嵌入神经网络损失函数，分别处理声速剖面截断与海底参数不确定性两个分支。通过物理信息约束实现数据驱动与模型驱动的融合，利用声传播物理规律（如Helmholtz方程）作为正则化项。训练数据来自数值模型生成的声压场样本，涵盖不同声速剖面和海底参数组合。

## 结果与结论

DB-PINN在环境参数不充分条件下实现了较高精度的声压场预测，性能优于传统数值模型和单一分支网络。结果表明该方法能有效缓解海底地声参数不确定和声速剖面截断带来的误差，为实际海洋声场快速预报提供了新途径，创新性地将双分支结构与物理信息神经网络结合用于水声场预测。

## 来源链接

- OpenAlex：https://openalex.org/W7214716911
- DOI：https://doi.org/10.1016/j.oceaneng.2026.128177