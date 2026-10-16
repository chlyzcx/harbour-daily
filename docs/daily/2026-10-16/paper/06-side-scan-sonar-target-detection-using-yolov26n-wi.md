---
candidateId: "openalex--W7221808101"
category: "Paper"
date: "2026-10-16"
rank: 6
title: "Side-scan sonar target detection using YOLOv26n with gated Output-16 and MPDIoU-NWD"
authors:
  - "Dandan Liu"
  - "Yuxiang Ding"
  - "Pengzheng Lei"
  - "Jiahua Zhu"
research_direction: []
journal: "Frontiers in Marine Science"
publisher: "Frontiers Media"
doi: "10.3389/fmars.2026.1963494"
publication_year: 2026
summary: "本文针对侧扫声呐小目标检测中视觉线索弱、边界模糊、海底背景复杂导致特征弱化和边界框回归不稳定的问题，提出基于YOLOv26n的改进检测器，引入Gated Output-16模块和MPDIoU-NWD损失函数，提升侧扫声呐图像目标检测性能。"
keywords:
  - "detection"
score: 56.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7221808101"
  - name: "DOI"
    url: "https://doi.org/10.3389/fmars.2026.1963494"
previewImage: "/daily/2026-10-16/assets/openalex--W7221808101/preview.png"
---

## 核心内容

本文针对侧扫声呐小目标检测中视觉线索弱、边界模糊、海底背景复杂导致特征弱化和边界框回归不稳定的问题，提出基于YOLOv26n的改进检测器，引入Gated Output-16模块和MPDIoU-NWD损失函数，提升侧扫声呐图像目标检测性能。

## 关键技术与数据

关键技术包括YOLOv26n检测框架、Gated Output-16门控输出模块、MPDIoU-NWD尺度感知边界框回归损失。Gated Output-16置于P3检测头C3k2输出之后，采用分组门控与EMA残差更新，门控初始为零以保留原始特征路径。MPDIoU-NWD提供尺度感知的框监督。数据为侧扫声呐图像数据集。

## 结果与结论

改进后的检测器在侧扫声呐小目标检测任务上取得更优性能，边界框回归稳定性和检测精度均有提升。结论表明Gated Output-16与MPDIoU-NWD的结合能有效应对侧扫声呐图像中小目标特征弱、边界模糊的挑战，创新点在于针对声呐图像特性设计了门控特征增强与尺度感知回归损失。

## 来源链接

- OpenAlex：https://openalex.org/W7221808101
- DOI：https://doi.org/10.3389/fmars.2026.1963494