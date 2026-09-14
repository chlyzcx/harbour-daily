---
candidateId: "crossref--10.20944-preprints202609.0919.v1"
category: "Paper"
date: "2026-09-14"
rank: 7
title: "When Underwater Acoustic Recognition Fails Across Datasets: A Cross-Dataset Benchmark Revealing Zero-Transfer and Label Shift"
authors:
  - "Hao Yuan"
  - "Wenbo Wang"
  - "Lingjiang Zeng"
  - "Guici Chen"
  - "Tian Li"
  - "Xuan Hou"
research_direction:
  - "信号识别"
journal: "Unknown"
publisher: "MDPI AG"
doi: "10.20944/preprints202609.0919.v1"
publication_year: 2026
summary: "该论文针对水声目标识别（UATR）中深度网络跨数据集泛化能力未经验证的问题，开展了跨数据集基准测试。研究背景是UATR深度网络几乎仅在单一数据集上训练与评估，跨数据集泛化性未知。研究目标是通过四个船舶辐射噪声数据集的基准测试，揭示零迁移与标签偏移现象。主要内容包括统一预处理流程下的跨数据集评估。"
keywords:
  - "underwater acoustic target recognition"
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.20944/preprints202609.0919.v1"
previewImage: "/daily/2026-09-14/assets/crossref--10.20944-preprints202609.0919.v1/preview.svg"
---

## 核心内容

该论文针对水声目标识别（UATR）中深度网络跨数据集泛化能力未经验证的问题，开展了跨数据集基准测试。研究背景是UATR深度网络几乎仅在单一数据集上训练与评估，跨数据集泛化性未知。研究目标是通过四个船舶辐射噪声数据集的基准测试，揭示零迁移与标签偏移现象。主要内容包括统一预处理流程下的跨数据集评估。

## 关键技术与数据

关键技术包括统一预处理链、冻结录音级划分、ImageNet预训练ResNet-18分类器、跨数据集基准测试方法。数据集包括四个船舶辐射噪声语料库：开阔大洋Oceanship、淡水湖QiandaoEar22、基于AIS自动标注的VTUAD（来自Ocean Networks Canada公开档案）以及近岸港口ShipsEar。

## 结果与结论

结果表明UATR模型在跨数据集场景下存在严重的零迁移与标签偏移问题，即在一个数据集上训练的模型无法有效泛化到其他数据集。创新点在于首次系统性地量化了UATR领域的跨数据集泛化差距，揭示了标签偏移是导致性能退化的关键因素，为未来鲁棒UATR模型设计提供了重要基准与方向。

## 来源链接

- DOI：https://doi.org/10.20944/preprints202609.0919.v1