---
candidateId: "openalex--W7224897031"
category: "Paper"
date: "2026-11-02"
rank: 4
title: "Improved SegNeXt Algorithm for Semantic Segmentation of Underwater Targets in Optical Images"
authors:
  - "You Zhou"
  - "Xiaofei Liao"
  - "Guangyu Li"
  - "Zheyu Lyu"
  - "Bohang Chao"
research_direction: []
journal: "Concurrency and Computation Practice and Experience"
publisher: "Wiley"
doi: "10.1002/cpe.71016"
publication_year: 2026
summary: "该论文针对光学图像水下目标语义分割受波长相关衰减、散射、非均匀光照及目标—背景低对比度影响而性能退化的问题，对SegNeXt算法进行改进。研究目标是通过增强通道重校准和小目标边界特征保留，提升水下语义分割精度与实时性，并在SUIM数据集上验证改进效果。"
keywords: []
score: 56.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7224897031"
  - name: "DOI"
    url: "https://doi.org/10.1002/cpe.71016"
previewImage: "/daily/2026-11-02/assets/openalex--W7224897031/preview.svg"
---

## 核心内容

该论文针对光学图像水下目标语义分割受波长相关衰减、散射、非均匀光照及目标—背景低对比度影响而性能退化的问题，对SegNeXt算法进行改进。研究目标是通过增强通道重校准和小目标边界特征保留，提升水下语义分割精度与实时性，并在SUIM数据集上验证改进效果。

## 关键技术与数据

改进方法包括在MSCAN中集成高效压缩—激励（eSE）通道重校准模块，以增强特征通道响应；用HGStem替换Hamburger解码头，以保留小目标与边界线索。实验采用SUIM数据集，统一300轮训练协议，评价指标为aAcc、mAcc、mIoU和FPS，并与原SegNeXt等模型对比。

## 结果与结论

改进模型在SUIM上取得84.35% aAcc、63.05% mAcc、37.35% mIoU和36.84 FPS，精度较基线提升的同时保持较好实时性。结论表明eSE通道重校准与HGStem解码头能有效改善水下低对比度与小目标分割性能。创新点在于将通道重校准与边界保留结构引入SegNeXt，兼顾分割精度与推理速度。

## 来源链接

- OpenAlex：https://openalex.org/W7224897031
- DOI：https://doi.org/10.1002/cpe.71016