---
candidateId: "crossref--10.20944-preprints202609.0449.v2"
category: "Paper"
date: "2026-09-21"
rank: 8
title: "Benchmarking Real-Time DETR Detectors for Multibeam Forward-Looking Sonar: DEIMv2, Detector-Specific Test-Time Fusion, and Domain Shift Analysis on UATD"
authors:
  - "Hao Yuan"
  - "Wenbo Wang"
  - "Tian Li"
  - "Lingjiang Zeng"
  - "Yu Chen"
  - "Fanyu Wang"
research_direction:
  - "目标检测"
  - "水声成像"
journal: "Unknown"
publisher: "MDPI AG"
doi: "10.20944/preprints202609.0449.v2"
publication_year: 2026
summary: "多波束前视声呐（MFLS）目标检测受低空间分辨率、声学斑点与测量条件分布差异影响，仍具挑战。本文在UATD数据集上基准测试基于DINOv3的实时DETR族检测器DEIMv2，采用指定可复现的双测试划分协议，比较多种实时检测器，并分析域偏移影响。"
keywords:
  - "detection"
  - "forward-looking sonar"
  - "underwater acoustic target detection"
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.20944/preprints202609.0449.v2"
previewImage: "/daily/2026-09-21/assets/crossref--10.20944-preprints202609.0449.v2/preview.svg"
---

## 核心内容

多波束前视声呐（MFLS）目标检测受低空间分辨率、声学斑点与测量条件分布差异影响，仍具挑战。本文在UATD数据集上基准测试基于DINOv3的实时DETR族检测器DEIMv2，采用指定可复现的双测试划分协议，比较多种实时检测器，并分析域偏移影响。

## 关键技术与数据

基准对象包括DEIMv2、RT-DETR-R18、D-FINE-S、DEIM v1-S与YOLOv8-S，在统一数据划分、输入分辨率与训练配置下比较。采用双测试划分协议确保可复现性，数据集为水下声学目标检测（UATD）数据集。评估涵盖检测精度与实时性，并分析域偏移对性能的影响。

## 结果与结论

DEIMv2在MFLS目标检测中展现出实时检测能力，与其他DETR族及YOLO检测器相比具有竞争力。研究揭示了域偏移对检测性能的显著影响，创新点在于首次在UATD上系统基准测试DINOv3-based实时DETR并引入检测器特定测试时融合与域偏移分析，但摘要未给出具体mAP数值。

## 来源链接

- DOI：https://doi.org/10.20944/preprints202609.0449.v2