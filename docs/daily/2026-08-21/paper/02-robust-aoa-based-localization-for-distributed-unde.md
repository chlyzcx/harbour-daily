---
candidateId: "openalex--W7203462286"
category: "Paper"
date: "2026-08-21"
rank: 2
title: "Robust AOA-based localization for distributed underwater acoustic sensor networks under heterogeneous impulsive noise"
authors:
  - "Zihao Zhou"
  - "Yang Shi"
  - "Lu Wang"
  - "Long Yang"
  - "Yixin Yang"
  - "xiaoyuan li"
research_direction:
  - "水下传感器网络"
journal: "Ocean Engineering"
publisher: "Elsevier BV"
doi: "10.1016/j.oceaneng.2026.127460"
publication_year: 2026
summary: "该论文研究分布式水声传感器网络中的目标定位问题，针对异构脉冲噪声环境下传统到达角（AOA）定位方法性能退化的问题，提出了一种鲁棒定位算法。研究背景是水声信道中海洋环境噪声和生物噪声常呈现非高斯、重尾分布特性，严重破坏基于最小二乘或高斯假设的定位精度。目标是构建对脉冲噪声不敏感的AOA定位框架。"
keywords:
  - "localization"
  - "underwater acoustic sensor network"
score: 72.2
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7203462286"
  - name: "DOI"
    url: "https://doi.org/10.1016/j.oceaneng.2026.127460"
previewImage: "/daily/2026-08-21/assets/openalex--W7203462286/preview.png"
---

## 核心内容

该论文研究分布式水声传感器网络中的目标定位问题，针对异构脉冲噪声环境下传统到达角（AOA）定位方法性能退化的问题，提出了一种鲁棒定位算法。研究背景是水声信道中海洋环境噪声和生物噪声常呈现非高斯、重尾分布特性，严重破坏基于最小二乘或高斯假设的定位精度。目标是构建对脉冲噪声不敏感的AOA定位框架。

## 关键技术与数据

关键技术包括鲁棒统计估计方法，如Huber损失或加权中位数替代传统L2范数；利用AOA测量模型的几何约束构建优化问题，并采用凸松弛或迭代重加权算法求解。数据方面可能采用蒙特卡洛仿真生成不同混合率的高斯-脉冲噪声（如α稳定分布）下的AOA测量值，并考虑传感器节点位置误差。

## 结果与结论

实验结果显示，在强脉冲噪声和异构噪声分布条件下，所提算法的定位均方根误差显著低于传统AOA定位方法，且接近克拉美-罗下界。算法在噪声参数未知时仍能保持稳定性能。创新点在于将鲁棒统计理论与分布式水声网络定位结合，解决了实际海洋环境中噪声非高斯特性带来的挑战。

## 来源链接

- OpenAlex：https://openalex.org/W7203462286
- DOI：https://doi.org/10.1016/j.oceaneng.2026.127460