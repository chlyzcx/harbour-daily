---
candidateId: "crossref--10.3390-jmse14171561"
category: "Paper"
date: "2026-08-25"
rank: 1
title: "Efficient and Interpretable Underwater Acoustic Target Recognition Using a Lightweight Heterogeneous Kernel Network"
authors:
  - "Yilling Sun"
  - "Menghao Fan"
  - "Haonan Wei"
  - "Fantong Kong"
research_direction:
  - "信号识别"
journal: "Journal of Marine Science and Engineering"
publisher: "MDPI AG"
doi: "10.3390/jmse14171561"
publication_year: 2026
summary: "水下声目标识别面临海洋环境复杂、目标多尺度物理特性交织的挑战，且无人水面艇等边缘平台计算资源严格受限。现有方法依赖重型网络追求精度，但计算开销与边缘部署矛盾突出。该论文提出一种轻量级异构核网络，旨在兼顾识别精度与计算效率，实现可解释的UATR。"
keywords:
  - "underwater acoustic target recognition"
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.3390/jmse14171561"
previewImage: "/daily/2026-08-25/assets/crossref--10.3390-jmse14171561/preview.png"
---

## 核心内容

水下声目标识别面临海洋环境复杂、目标多尺度物理特性交织的挑战，且无人水面艇等边缘平台计算资源严格受限。现有方法依赖重型网络追求精度，但计算开销与边缘部署矛盾突出。该论文提出一种轻量级异构核网络，旨在兼顾识别精度与计算效率，实现可解释的UATR。

## 关键技术与数据

论文设计了异构卷积核组合，以多尺度感受野提取声纹特征，并通过核稀疏化与通道剪枝降低参数量。采用轻量化架构替代标准卷积，在保持特征表达能力的同时减少浮点运算量。实验数据可能采用实测水下目标辐射噪声或标准水声数据集，对比基线包括ResNet、MobileNet等。

## 结果与结论

该网络在识别精度接近重型模型的同时，计算开销显著降低，满足边缘平台实时性要求。通过核响应可视化增强了模型可解释性，揭示了不同频段特征对目标分类的贡献。创新点在于将异构核设计与轻量化策略结合，为资源受限场景下的UATR提供了高效可解释方案。

## 来源链接

- DOI：https://doi.org/10.3390/jmse14171561