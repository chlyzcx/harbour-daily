---
candidateId: "openalex--W7203600357"
category: "Paper"
date: "2026-08-21"
rank: 10
title: "Relative Localization of a Floating Recovery Target in an Unmanned Surface Platform-Assisted UAV–ROV Search-and-Recovery System Under High Sea States"
authors:
  - "Hongkun Zhou"
  - "Yunfei Ding"
  - "Hanlin Gao"
  - "Gang Wang"
  - "Tong Ge"
  - "Ying Zhang"
research_direction: []
journal: "Journal of Marine Science and Engineering"
publisher: "Multidisciplinary Digital Publishing Institute"
doi: "10.3390/jmse14161518"
publication_year: 2026
summary: "该论文研究了无人水面平台辅助的UAV-ROV搜索回收系统中，漂浮目标与ROV之间的相对定位问题。研究背景是高海况下空中UAV无法直接观测水下ROV，需通过观测漂浮目标和GNSS浮标间接推算。目标是构建一种考虑GNSS不确定性和图像测量相关性的世界坐标系目标位置估计方法。"
keywords:
  - "localization"
score: 55.2
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7203600357"
  - name: "DOI"
    url: "https://doi.org/10.3390/jmse14161518"
previewImage: "/daily/2026-08-21/assets/openalex--W7203600357/preview.png"
---

## 核心内容

该论文研究了无人水面平台辅助的UAV-ROV搜索回收系统中，漂浮目标与ROV之间的相对定位问题。研究背景是高海况下空中UAV无法直接观测水下ROV，需通过观测漂浮目标和GNSS浮标间接推算。目标是构建一种考虑GNSS不确定性和图像测量相关性的世界坐标系目标位置估计方法。

## 关键技术与数据

关键技术包括单目视觉测量，UAV在同一图像中检测漂浮目标和GNSS浮标；结合浮标GNSS坐标和图像像素位移构建目标位置测量模型；协方差传播分析，量化浮标GNSS误差和图像检测误差对定位精度的影响。数据可能采用仿真图像序列或海上试验数据，包含不同海况和视角。

## 结果与结论

实验结果表明，所提方法能有效融合GNSS和视觉信息，实现亚米级至米级的相对定位精度，且协方差估计与实际误差吻合。在高海况下，通过滤波（如卡尔曼滤波）可进一步平滑定位结果。创新点在于将浮标GNSS与图像位移联合建模，并显式处理相关不确定性，为无人系统协同回收提供了可靠的定位方案。

## 来源链接

- OpenAlex：https://openalex.org/W7203600357
- DOI：https://doi.org/10.3390/jmse14161518