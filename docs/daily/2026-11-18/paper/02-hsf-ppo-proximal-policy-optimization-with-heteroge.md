---
candidateId: "openalex--W7233575367"
category: "Paper"
date: "2026-11-18"
rank: 2
title: "HSF-PPO: Proximal policy optimization with heterogeneous spatiotemporal feature fusion for dynamic path planning of autonomous underwater vehicles"
authors:
  - "Peng Li"
  - "Nan Zang"
  - "Jianhua Cheng"
  - "Shaoyang Liu"
  - "Ziqi Gao"
  - "Zhiming Chen"
  - "Haochuan Dong"
research_direction: []
journal: "Ocean Engineering"
publisher: "Elsevier BV"
doi: "10.1016/j.oceaneng.2026.129499"
publication_year: 2026
summary: "该论文面向自主水下航行器动态路径规划，提出融合异构时空特征近端策略优化算法HSF-PPO。水下环境存在洋流扰动、障碍动态变化和感知噪声，传统PPO对时空关联特征提取不足，规划策略收敛慢且易陷入局部最优。研究目标是构建能同时刻画局部障碍几何与全局流场时序演化的强化学习规划框架，提高AUV动态避障与路径跟踪性能。"
keywords: []
score: 65.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7233575367"
  - name: "DOI"
    url: "https://doi.org/10.1016/j.oceaneng.2026.129499"
previewImage: "/daily/2026-11-18/assets/openalex--W7233575367/preview.png"
---

## 核心内容

该论文面向自主水下航行器动态路径规划，提出融合异构时空特征近端策略优化算法HSF-PPO。水下环境存在洋流扰动、障碍动态变化和感知噪声，传统PPO对时空关联特征提取不足，规划策略收敛慢且易陷入局部最优。研究目标是构建能同时刻画局部障碍几何与全局流场时序演化的强化学习规划框架，提高AUV动态避障与路径跟踪性能。

## 关键技术与数据

在PPO框架中嵌入异构时空特征融合模块，分别提取空间栅格障碍特征与时序洋流/目标运动特征并跨模态融合；设计面向路径长度、避碰安全与能耗的复合奖励函数；在含动态障碍与洋流的水下仿真环境中训练与评测，对比传统PPO及主流深度强化学习规划算法。

## 结果与结论

仿真结果显示HSF-PPO在路径成功率、平均路径长度与避碰安全性指标上优于对比算法，收敛速度更快，动态障碍场景下重规划稳定性提升。创新点在于将异构时空特征融合引入PPO策略网络，增强AUV对动态水下环境的表征与决策能力。

## 来源链接

- OpenAlex：https://openalex.org/W7233575367
- DOI：https://doi.org/10.1016/j.oceaneng.2026.129499