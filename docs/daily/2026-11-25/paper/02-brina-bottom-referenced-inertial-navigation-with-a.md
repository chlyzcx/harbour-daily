---
candidateId: "openalex--W7238724183"
category: "Paper"
date: "2026-11-25"
rank: 2
title: "BRINA: Bottom-Referenced Inertial Navigation with AKAZE, a Sonar SLAM for Autonomous Marine Vehicles"
authors:
  - "Adolfo Damiano Cafaro"
  - "Patrízio Mariani"
  - "Roberto Galeazzi"
research_direction:
  - "水下导航"
  - "水声成像"
journal: "arXiv"
publisher: "arXiv"
doi: "10.48550/arxiv.2611.27817"
publication_year: 2026
summary: "前视声呐在光学受限水域可提供可靠感知，但每次回波高程不可观测导致声呐图像直接估计运动存在未知尺度。论文提出BRINA——结合AKAZE特征与底部参考的声呐惯性SLAM系统，面向自主海洋航行器，以FLS作为唯一外感受传感器，解决无DVL条件下的尺度可观测与导航问题。"
keywords:
  - "Doppler velocity log"
  - "doppler"
  - "forward-looking sonar"
score: 71.2
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7238724183"
  - name: "DOI"
    url: "https://doi.org/10.48550/arxiv.2611.27817"
previewImage: "/daily/2026-11-25/assets/openalex--W7238724183/preview.png"
---

## 核心内容

前视声呐在光学受限水域可提供可靠感知，但每次回波高程不可观测导致声呐图像直接估计运动存在未知尺度。论文提出BRINA——结合AKAZE特征与底部参考的声呐惯性SLAM系统，面向自主海洋航行器，以FLS作为唯一外感受传感器，解决无DVL条件下的尺度可观测与导航问题。

## 关键技术与数据

系统融合FLS图像与惯性测量，采用AKAZE特征提取与匹配构建声呐视觉约束；利用底部参考（bottom-referenced）思想恢复未知度量尺度，形成声呐-惯性SLAM后端优化框架；以FLS为唯一外感受源，避免依赖多普勒速度计（DVL）。

## 结果与结论

提出了一种无需DVL即可解决声呐图像未知尺度问题的声呐-惯性SLAM方案，实现了以FLS为唯一外感受传感器的海洋航行器导航，提升了光学受限环境下导航的自主性与可用性。

## 来源链接

- OpenAlex：https://openalex.org/W7238724183
- DOI：https://doi.org/10.48550/arxiv.2611.27817