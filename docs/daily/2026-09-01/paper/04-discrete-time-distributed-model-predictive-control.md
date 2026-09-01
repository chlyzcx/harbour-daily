---
candidateId: "crossref--10.1016-j.isatra.2026.06.033"
category: "Paper"
date: "2026-09-01"
rank: 4
title: "Discrete-time distributed model predictive control-based collision-avoidance formation tracking control for multiple unmanned underwater vehicles"
authors:
  - "Haomiao Yu"
  - "Yue Wang"
research_direction: []
journal: "ISA Transactions"
publisher: "Elsevier BV"
doi: "10.1016/j.isatra.2026.06.033"
publication_year: 2026
summary: "本文研究多无人水下航行器（UUV）编队跟踪控制中的避碰问题，提出一种基于离散时间分布式模型预测控制（DMPC）的编队控制方案。多UUV协同作业时需同时满足轨迹跟踪、编队保持和避碰约束，集中式控制计算量大且鲁棒性差。本文采用分布式架构，各UUV基于局部信息独立求解优化问题，实现协同避碰跟踪。"
keywords:
  - "tracking"
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.1016/j.isatra.2026.06.033"
previewImage: "/daily/2026-09-01/assets/crossref--10.1016-j.isatra.2026.06.033/preview.png"
---

## 核心内容

本文研究多无人水下航行器（UUV）编队跟踪控制中的避碰问题，提出一种基于离散时间分布式模型预测控制（DMPC）的编队控制方案。多UUV协同作业时需同时满足轨迹跟踪、编队保持和避碰约束，集中式控制计算量大且鲁棒性差。本文采用分布式架构，各UUV基于局部信息独立求解优化问题，实现协同避碰跟踪。

## 关键技术与数据

关键技术为离散时间分布式模型预测控制，每个UUV利用邻居状态预测构建局部优化问题，目标函数包含跟踪误差、编队误差和控制能量项，避碰约束通过势函数或硬约束形式引入。采用纳什均衡或迭代求解策略处理耦合。数据为多UUV编队仿真场景，包含不同初始位置和障碍物分布，对比了集中式MPC和一致性控制方法。

## 结果与结论

仿真结果表明，所提DMPC方案在保证避碰的前提下实现了良好的编队跟踪性能，跟踪误差和避碰距离均满足设定要求，计算效率较集中式方法显著提升。创新点在于离散时间分布式框架下的避碰约束处理，为多UUV协同控制提供了可扩展的解决方案。

## 来源链接

- DOI：https://doi.org/10.1016/j.isatra.2026.06.033