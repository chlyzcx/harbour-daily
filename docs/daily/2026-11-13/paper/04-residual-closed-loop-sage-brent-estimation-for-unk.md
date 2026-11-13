---
candidateId: "openalex--W7225826905"
category: "Paper"
date: "2026-11-13"
rank: 4
title: "Residual-Closed-Loop SAGE-Brent Estimation for Unknown-Order Wideband Underwater Acoustic Channels"
authors:
  - "Wenxu Bi"
  - "Peng Chen"
  - "Wei Wang"
research_direction: []
journal: "arXiv (Cornell University)"
publisher: "Cornell University"
doi: "10.48550/arxiv.2611.13699"
publication_year: 2026
summary: "该论文针对未知阶数宽带水声信道估计中的网格失配问题，提出残差闭环SAGE-Brent（RC-SAGE-Brent）估计器。宽带信道估计中网格失配导致强路径扣除后残留结构化抵消残差，产生虚假相关峰或掩盖弱到达，将连续参数误差转化为路径数误差。论文旨在联合精化连续时延-尺度参数并校正未知阶数路径集，提升宽带水声信道估计精度。"
keywords:
  - "channel estimation"
  - "detection"
  - "sparse"
score: 56.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7225826905"
  - name: "DOI"
    url: "https://doi.org/10.48550/arxiv.2611.13699"
previewImage: "/daily/2026-11-13/assets/openalex--W7225826905/preview.png"
---

## 核心内容

该论文针对未知阶数宽带水声信道估计中的网格失配问题，提出残差闭环SAGE-Brent（RC-SAGE-Brent）估计器。宽带信道估计中网格失配导致强路径扣除后残留结构化抵消残差，产生虚假相关峰或掩盖弱到达，将连续参数误差转化为路径数误差。论文旨在联合精化连续时延-尺度参数并校正未知阶数路径集，提升宽带水声信道估计精度。

## 关键技术与数据

论文提出残差闭环估计框架，在每个反馈周期内采用模糊约束交替Brent搜索抑制强路径残差，联合估计连续时延与尺度参数，并通过残差反馈校正路径集阶数。关键技术包括SAGE算法框架、Brent一维搜索、模糊约束及残差闭环反馈机制。数据可能包括仿真宽带水声信道及实测数据，用于验证参数估计精度与路径数校正能力。

## 结果与结论

论文通过仿真与实测数据验证了RC-SAGE-Brent在未知阶数宽带水声信道估计中能够有效抑制网格失配引起的虚假峰与弱路径掩盖，连续参数估计精度和路径数校正准确率均优于传统SAGE方法。创新点在于将残差闭环反馈与交替Brent搜索相结合，实现连续参数与离散路径集的联合优化。

## 来源链接

- OpenAlex：https://openalex.org/W7225826905
- DOI：https://doi.org/10.48550/arxiv.2611.13699