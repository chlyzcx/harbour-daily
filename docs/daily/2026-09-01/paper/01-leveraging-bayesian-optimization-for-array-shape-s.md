---
candidateId: "arxiv--2608.30488-1"
category: "Paper"
date: "2026-09-01"
rank: 1
title: "Leveraging Bayesian Optimization for Array Shape Self-Calibration in Underwater DoA Estimation"
authors:
  - "Xin Gui"
  - "Tianang Li"
  - "Changjia Wang"
  - "Bowen Han"
  - "Yunchuan Zhang"
  - "Zhengying Li"
research_direction:
  - "网络协议"
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "针对柔性水听器阵列在水下声网络中因几何形变导致波达方向（DoA）估计性能退化的问题，现有自校准方法通常独立估计各阵元位置，在长阵列场景下形成高维优化难题。本文提出一种基于贝叶斯优化的几何估计（BOGE）策略，采用分层优化流程并结合物理信息参数化模型，以降低校准复杂度并提升估计精度。"
keywords:
  - "localization"
  - "tracking"
  - "underwater acoustic network"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2608.30488v1"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2608.30488v1"
previewImage: "/daily/2026-09-01/assets/arxiv--2608.30488-1/preview.png"
---

## 核心内容

针对柔性水听器阵列在水下声网络中因几何形变导致波达方向（DoA）估计性能退化的问题，现有自校准方法通常独立估计各阵元位置，在长阵列场景下形成高维优化难题。本文提出一种基于贝叶斯优化的几何估计（BOGE）策略，采用分层优化流程并结合物理信息参数化模型，以降低校准复杂度并提升估计精度。

## 关键技术与数据

核心技术为贝叶斯优化辅助的分层几何估计框架，利用物理信息参数化模型约束阵元形变空间，将高维位置估计分解为低维子问题逐层求解。方法涉及高斯过程代理模型与采集函数设计，用于高效探索参数空间。实验数据来源于仿真生成的柔性阵列形变场景及实测水声数据，验证了不同信噪比与形变程度下的算法鲁棒性。

## 结果与结论

实验结果表明，BOGE策略在阵元位置估计误差和DoA估计精度上均优于传统独立估计方法，尤其在长阵列和大形变条件下计算效率显著提升。创新点在于将贝叶斯优化与物理约束结合，实现了低复杂度高精度的阵列自校准，为柔性水听器阵列的实际应用提供了可行方案。

## 来源链接

- arXiv：http://arxiv.org/abs/2608.30488v1
- PDF：http://arxiv.org/pdf/2608.30488v1