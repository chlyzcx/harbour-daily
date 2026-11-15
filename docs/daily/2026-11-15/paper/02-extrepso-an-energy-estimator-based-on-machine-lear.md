---
candidateId: "openalex--W7225997697"
category: "Paper"
date: "2026-11-15"
rank: 2
title: "EXTREPSO: An Energy Estimator Based on Machine Learning with PSO Optimization for UASNs"
authors:
  - "Tauseef Mubeen"
  - "Miguel-Ángel Luque-Nieto"
  - "Pablo Otero"
research_direction:
  - "水下传感器网络"
journal: "Eng—Advances in Engineering"
publisher: "Multidisciplinary Digital Publishing Institute"
doi: "10.3390/eng7110645"
publication_year: 2026
summary: "该论文针对水下声学传感器网络（UASNs）中传播时延大、带宽受限和节点能量受限的问题，提出EXTREPSO机器学习框架，用于跳级能效预测器的离线超参数调优。目标是通过数据驱动方法提升UASN能量估计精度，为网络协议设计与能量管理提供支持。"
keywords:
  - "machine learning"
  - "underwater acoustic sensor network"
score: 64.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7225997697"
  - name: "DOI"
    url: "https://doi.org/10.3390/eng7110645"
previewImage: "/daily/2026-11-15/assets/openalex--W7225997697/preview.svg"
---

## 核心内容

该论文针对水下声学传感器网络（UASNs）中传播时延大、带宽受限和节点能量受限的问题，提出EXTREPSO机器学习框架，用于跳级能效预测器的离线超参数调优。目标是通过数据驱动方法提升UASN能量估计精度，为网络协议设计与能量管理提供支持。

## 关键技术与数据

EXTREPSO结合Extra Trees Regressor与粒子群优化（PSO）进行超参数寻优；目标值由Aqua-Sim NG仿真轨迹字段导出，输入特征包括载荷大小、仿真器Tx_power字段和观测到的跳时延。数据来源于Aqua-Sim NG仿真平台生成的网络轨迹。

## 结果与结论

该框架实现了基于机器学习的跳级能效预测，并通过PSO优化提升模型性能。创新点在于将Extra Trees回归与PSO结合用于UASN能量估计，利用仿真轨迹字段构建可复现的训练目标，为水下网络能量高效设计提供数据驱动工具。

## 来源链接

- OpenAlex：https://openalex.org/W7225997697
- DOI：https://doi.org/10.3390/eng7110645