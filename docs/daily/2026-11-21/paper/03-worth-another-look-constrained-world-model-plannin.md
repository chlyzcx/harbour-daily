---
candidateId: "openalex--W7235877962"
category: "Paper"
date: "2026-11-21"
rank: 3
title: "Worth Another Look: Constrained World-Model Planning for Visual Inspection"
authors:
  - "Ziyue KANG"
  - "Zixi Qi"
  - "Yuchen Dai"
  - "Nana Lv"
  - "Xirong Cheng"
  - "Liang Liu"
  - "Ying Li"
  - "Haoyang Wei"
  - "Haiyang Yao"
research_direction: []
journal: "arXiv (Cornell University)"
publisher: "Cornell University"
doi: "10.48550/arxiv.2611.24187"
publication_year: 2026
summary: "该论文面向野外机器人与环境监测中的视觉巡检任务，研究在严格计算与传感约束下多目标定位的规划问题。针对穷举扫描浪费调用、短视策略易受异构代价峭壁影响以及视口编辑价值需重查询后才显现等难题，提出约束世界模型规划方法，将冻结检测器上的巡检建模为部分可观测下的神经符号观测规划问题。"
keywords: []
score: 56.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7235877962"
  - name: "DOI"
    url: "https://doi.org/10.48550/arxiv.2611.24187"
previewImage: "/daily/2026-11-21/assets/openalex--W7235877962/preview.png"
---

## 核心内容

该论文面向野外机器人与环境监测中的视觉巡检任务，研究在严格计算与传感约束下多目标定位的规划问题。针对穷举扫描浪费调用、短视策略易受异构代价峭壁影响以及视口编辑价值需重查询后才显现等难题，提出约束世界模型规划方法，将冻结检测器上的巡检建模为部分可观测下的神经符号观测规划问题。

## 关键技术与数据

将巡检问题形式化为部分可观测条件下的神经符号观测规划，解耦紧凑循环世界模型（WM）与检测器调用决策；利用世界模型预测视口编辑的长期价值，结合约束规划在计算与传感预算内选择观测动作，并在仿真巡检场景中与穷举、短视及无搜索策略进行对比评估。

## 结果与结论

结果表明，所提约束世界模型规划在有限计算与传感预算下显著提升多目标定位效率，减少对缺席类别的无效检测调用，并能识别需重查询后才显现价值的视口编辑。结论证明世界模型与符号约束结合可有效应对异构代价峭壁，创新点在于将巡检规划解耦为世界模型预测与约束决策的神经符号框架。

## 来源链接

- OpenAlex：https://openalex.org/W7235877962
- DOI：https://doi.org/10.48550/arxiv.2611.24187