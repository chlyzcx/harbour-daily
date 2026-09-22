---
candidateId: "crossref--10.3390-jmse14181733"
category: "Paper"
date: "2026-09-22"
rank: 5
title: "Risk-Aware Hybrid Decision-Making Combining Reinforcement Learning and Receding Horizon Control for AUV Bistatic Sonar Target Tracking"
authors:
  - "Weicong Zhan"
  - "Yu Tian"
  - "Feng Zheng"
  - "Jiancheng Yu"
  - "Yan Huang"
research_direction: []
journal: "Journal of Marine Science and Engineering"
publisher: "MDPI AG"
doi: "10.3390/jmse14181733"
publication_year: 2026
summary: "该论文提出了一种风险感知混合决策框架，将强化学习（RL）与滚动时域控制（RHC）相结合，用于AUV双基地声呐目标跟踪。RL可引导AUV机动以优化源-目标-接收器几何构型，但可靠策略训练需大量环境交互。论文旨在通过RL与选择性RHC的混合架构降低策略训练需求，同时保证跟踪性能和安全性。"
keywords:
  - "sparse"
  - "tracking"
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.3390/jmse14181733"
previewImage: "/daily/2026-09-22/assets/crossref--10.3390-jmse14181733/preview.png"
---

## 核心内容

该论文提出了一种风险感知混合决策框架，将强化学习（RL）与滚动时域控制（RHC）相结合，用于AUV双基地声呐目标跟踪。RL可引导AUV机动以优化源-目标-接收器几何构型，但可靠策略训练需大量环境交互。论文旨在通过RL与选择性RHC的混合架构降低策略训练需求，同时保证跟踪性能和安全性。

## 关键技术与数据

核心技术包括软演员-评论家（SAC）强化学习算法与滚动时域控制（RHC）的混合决策框架。RHC在关键决策点选择性介入，降低对RL策略训练样本的依赖。风险感知机制用于评估决策安全性，避免高风险动作。仿真环境模拟AUV双基地声呐目标跟踪场景，包含声呐方程、几何构型优化和水下动力学约束。性能指标包括跟踪精度、策略训练效率和风险规避能力。

## 结果与结论

结果表明混合决策框架在减少RL训练交互次数的同时，保持了与纯RL方法相当的跟踪性能，且风险感知机制有效降低了高风险决策概率。RHC的选择性介入显著加速了策略收敛。创新点在于提出了RL与RHC的混合架构及风险感知机制，为AUV双基地声呐目标跟踪提供了一种高效、安全的决策方法，平衡了学习效率与任务性能。

## 来源链接

- DOI：https://doi.org/10.3390/jmse14181733