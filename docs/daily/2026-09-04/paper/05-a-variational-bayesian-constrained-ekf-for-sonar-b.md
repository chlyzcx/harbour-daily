---
candidateId: "crossref--10.3390-s26175591"
category: "Paper"
date: "2026-09-04"
rank: 5
title: "A Variational Bayesian Constrained EKF for Sonar-Based Underwater Target Tracking in Shallow Water"
authors:
  - "Hongkun Zhou"
  - "Yunfei Ding"
  - "Hanlin Gao"
  - "Gang Wang"
  - "Tong Ge"
  - "Ying Zhang"
research_direction:
  - "目标跟踪"
journal: "Sensors"
publisher: "MDPI AG"
doi: "10.3390/s26175591"
publication_year: 2026
summary: "该论文针对浅海主动声呐目标跟踪中非线性声呐几何、角度误差放大、噪声统计不确定及环境约束等问题，提出了一种变分贝叶斯约束扩展卡尔曼滤波（VB-C-EKF）。研究目标是在复杂浅海环境下实现对水下弱机动目标的精确、稳定跟踪。"
keywords:
  - "doppler"
  - "localization"
  - "time-varying"
  - "tracking"
  - "underwater target tracking"
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.3390/s26175591"
previewImage: "/daily/2026-09-04/assets/crossref--10.3390-s26175591/preview.png"
---

## 核心内容

该论文针对浅海主动声呐目标跟踪中非线性声呐几何、角度误差放大、噪声统计不确定及环境约束等问题，提出了一种变分贝叶斯约束扩展卡尔曼滤波（VB-C-EKF）。研究目标是在复杂浅海环境下实现对水下弱机动目标的精确、稳定跟踪。

## 关键技术与数据

算法采用弱机动运动模型与距离-方位-俯仰-多普勒量测模型。关键技术包括：利用变分贝叶斯方法在线估计时变量测噪声协方差；结合环境约束（如海底边界）对状态估计进行投影修正。数据可能来源于仿真浅海环境或海试数据，对比了标准EKF与无约束滤波。

## 结果与结论

仿真与实验结果显示，VB-C-EKF在量测噪声突变及存在环境约束时，跟踪精度与稳定性显著优于传统EKF，有效降低了滤波发散风险。结论指出，该算法通过自适应噪声处理与约束融合，为浅海复杂环境下的声呐目标跟踪提供了一种鲁棒且实用的解决方案。

## 来源链接

- DOI：https://doi.org/10.3390/s26175591