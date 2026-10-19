---
candidateId: "openalex--W7221749955"
category: "Paper"
date: "2026-10-19"
rank: 2
title: "UDDPG-Net: Energy- and fairness-aware deep reinforcement learning for resource allocation in underwater communication networks"
authors:
  - "Guohong Gao"
  - "Fengshuo Tian"
  - "J B Wang"
  - "Zhiwei Li"
  - "Haofan Bai"
  - "Yan Wang"
  - "Qian Li"
  - "Chenping Zhao"
research_direction: []
journal: "Applied Soft Computing"
publisher: "Elsevier BV"
doi: "10.1016/j.asoc.2026.116626"
publication_year: 2026
summary: "该论文提出UDDPG-Net，一种面向水下通信网络资源分配的深度强化学习方法，兼顾能量效率与公平性。研究背景为水下通信网络资源受限、能量供应困难且节点间公平性难以保障。论文目标是设计一种能够同时优化能量消耗和用户公平性的资源分配策略。主要内容包括构建水下通信网络模型，定义能量与公平性联合优化目标，提出基于深度确定性策略梯度（DDPG）的改进算法UDDPG-Net进行资源分配决策。"
keywords: []
score: 50.2
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7221749955"
  - name: "DOI"
    url: "https://doi.org/10.1016/j.asoc.2026.116626"
previewImage: "/daily/2026-10-19/assets/openalex--W7221749955/preview.png"
---

## 核心内容

该论文提出UDDPG-Net，一种面向水下通信网络资源分配的深度强化学习方法，兼顾能量效率与公平性。研究背景为水下通信网络资源受限、能量供应困难且节点间公平性难以保障。论文目标是设计一种能够同时优化能量消耗和用户公平性的资源分配策略。主要内容包括构建水下通信网络模型，定义能量与公平性联合优化目标，提出基于深度确定性策略梯度（DDPG）的改进算法UDDPG-Net进行资源分配决策。

## 关键技术与数据

采用深度强化学习框架，基于DDPG算法进行连续动作空间资源分配；引入能量效率和公平性指标构建多目标奖励函数；设计UDDPG-Net网络结构以提升训练稳定性和收敛速度；考虑水下信道特性、节点能量约束和干扰模型；通过仿真环境生成训练数据，与基准算法（如传统DDPG、随机分配等）进行对比评估。

## 结果与结论

仿真结果表明，UDDPG-Net在能量效率和公平性方面均优于基准算法，能够有效延长网络寿命并提升资源分配的公平性；算法收敛速度较快，适应动态水下环境。结论指出该深度强化学习方法可有效解决水下通信网络资源分配中的能量与公平性权衡问题；创新点在于将公平性约束融入DDPG框架并提出改进网络结构，实现了能量与公平性联合优化的自适应资源分配。

## 来源链接

- OpenAlex：https://openalex.org/W7221749955
- DOI：https://doi.org/10.1016/j.asoc.2026.116626