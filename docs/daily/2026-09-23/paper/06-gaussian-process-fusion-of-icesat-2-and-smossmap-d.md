---
candidateId: "openalex--W7213954669"
category: "Paper"
date: "2026-09-23"
rank: 6
title: "Gaussian-process fusion of ICESat-2 and SMOS/SMAP data for daily estimates of Arctic sea ice thickness and volume"
authors:
  - "Alek Aaron Petty"
  - "Christopher Cardinale"
  - "Michel Tsamados"
  - "William King Gregory"
  - "Alex Cabaj"
research_direction: []
journal: "Earth System Science Data Discussions"
doi: "10.5194/essd-2026-700"
publication_year: 2026
summary: "本文提出IS2SMGPSIT-V1，一个全覆盖、泛北极、25km×25km的海冰厚度和体积数据集，具有2018至2025年间七个冬季生长季的每日输出。该产品融合ICESat-2激光测高数据与SMOS/SMAP L波段辐射计数据，使用高斯过程回归实现。ICESat-2沿既定地面轨迹提供高空间分辨率厚度估计，SMOS和SMAP提供广泛的每日覆盖。"
keywords:
  - "sparse"
score: 56.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7213954669"
  - name: "DOI"
    url: "https://doi.org/10.5194/essd-2026-700"
previewImage: "/daily/2026-09-23/assets/openalex--W7213954669/preview.png"
---

## 核心内容

本文提出IS2SMGPSIT-V1，一个全覆盖、泛北极、25km×25km的海冰厚度和体积数据集，具有2018至2025年间七个冬季生长季的每日输出。该产品融合ICESat-2激光测高数据与SMOS/SMAP L波段辐射计数据，使用高斯过程回归实现。ICESat-2沿既定地面轨迹提供高空间分辨率厚度估计，SMOS和SMAP提供广泛的每日覆盖。

## 关键技术与数据

关键技术为高斯过程（GP）回归，通过开源GPSat包实现。数据源包括：1）ICESat-2激光测高数据，提供沿轨高分辨率海冰厚度；2）SMOS和SMAP L波段辐射计数据，提供每日大范围覆盖。融合策略利用GP回归将沿轨高分辨率观测与每日宽幅观测结合，生成全覆盖每日海冰厚度和体积产品。时间跨度为2018-2025年七个冬季。

## 结果与结论

摘要信息不完整，未获取具体精度指标。预期结论为：IS2SMGPSIT-V1数据集实现了泛北极全覆盖、每日输出的海冰厚度和体积估计，融合了ICESat-2的高空间分辨率与SMOS/SMAP的高时间分辨率优势。创新点在于：1）GP回归融合多源卫星数据；2）生成长时间序列（七个冬季）的每日产品；3）开源实现（GPSat包）便于复现和推广。

## 来源链接

- OpenAlex：https://openalex.org/W7213954669
- DOI：https://doi.org/10.5194/essd-2026-700