---
candidateId: "openalex--W7221462478"
category: "Paper"
date: "2026-10-13"
rank: 1
title: "A QMIX-driven routing protocol for dynamic Underwater Acoustic Sensor Networks"
authors:
  - "Adi Surendra Mohanraju M."
  - "Anjaneyulu Lokam"
  - "Kiran Dasari"
research_direction:
  - "水下传感器网络"
journal: "Scientific Reports"
publisher: "Nature Portfolio"
doi: "10.1038/s41598-026-74771-2"
publication_year: 2026
summary: "针对水声传感器网络（UASN）中电池容量受限、传播时延大、拓扑动态变化及链路不可靠等导致的数据收集难题，本文提出一种基于协作多智能体强化学习（CMARL）的动态UASN数据路由框架。将路由问题建模为去中心化部分可观测马尔可夫决策过程（Dec-POMDP），并引入QMIX算法实现多节点协同决策，旨在提升动态水声环境下数据收集的可靠性与能量效率。"
keywords:
  - "underwater acoustic sensor network"
score: 64.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7221462478"
  - name: "DOI"
    url: "https://doi.org/10.1038/s41598-026-74771-2"
previewImage: "/daily/2026-10-13/assets/openalex--W7221462478/preview.png"
---

## 核心内容

针对水声传感器网络（UASN）中电池容量受限、传播时延大、拓扑动态变化及链路不可靠等导致的数据收集难题，本文提出一种基于协作多智能体强化学习（CMARL）的动态UASN数据路由框架。将路由问题建模为去中心化部分可观测马尔可夫决策过程（Dec-POMDP），并引入QMIX算法实现多节点协同决策，旨在提升动态水声环境下数据收集的可靠性与能量效率。

## 关键技术与数据

核心技术为QMIX驱动的协作多智能体强化学习路由协议，采用Dec-POMDP建模，通过混合网络将各智能体局部Q值非线性聚合为全局Q值，实现集中训练、分散执行。利用水声信道传播模型与动态拓扑仿真环境生成训练数据，智能体依据局部观测（邻居状态、剩余能量、链路质量等）进行转发决策。

## 结果与结论

仿真结果表明，该协议在数据包投递率、端到端时延和能量消耗方面优于传统路由协议及独立强化学习基线，能有效适应拓扑动态变化与链路不可靠场景。创新点在于将QMIX引入水声路由，实现多节点隐式协作与全局优化，为动态UASN提供可靠节能的数据收集方案。

## 来源链接

- OpenAlex：https://openalex.org/W7221462478
- DOI：https://doi.org/10.1038/s41598-026-74771-2