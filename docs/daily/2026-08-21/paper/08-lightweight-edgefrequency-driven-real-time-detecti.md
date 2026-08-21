---
candidateId: "openalex--W7202399338"
category: "Paper"
date: "2026-08-21"
rank: 8
title: "Lightweight Edge–Frequency Driven Real-Time Detection Transformer for side-scan sonar target detection"
authors:
  - "Feihu Zhang"
  - "Zhengpeng Li"
  - "Xin Wen"
  - "Chensheng Cheng"
  - "Biao Deng"
  - "Taiyuan Zhang"
  - "Guang Pan"
research_direction:
  - "目标检测"
journal: "Frontiers in Marine Science"
publisher: "Frontiers Media"
doi: "10.3389/fmars.2026.1797307"
publication_year: 2026
summary: "该论文针对侧扫声纳（SSS）图像中目标边界模糊和强噪声干扰导致高精度目标识别困难的问题，提出了一种轻量级边缘-频率驱动的实时检测Transformer（LEF-RT-DETR）框架。研究背景是声纳成像机制和水下环境的复杂性。目标是设计一种兼顾高精度与实时性的轻量级目标检测网络。"
keywords:
  - "detection"
  - "underwater target detection"
score: 63.2
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7202399338"
  - name: "DOI"
    url: "https://doi.org/10.3389/fmars.2026.1797307"
previewImage: "/daily/2026-08-21/assets/openalex--W7202399338/preview.png"
---

## 核心内容

该论文针对侧扫声纳（SSS）图像中目标边界模糊和强噪声干扰导致高精度目标识别困难的问题，提出了一种轻量级边缘-频率驱动的实时检测Transformer（LEF-RT-DETR）框架。研究背景是声纳成像机制和水下环境的复杂性。目标是设计一种兼顾高精度与实时性的轻量级目标检测网络。

## 关键技术与数据

关键技术包括轻量级骨干网络设计、边缘信息增强模块（用于锐化目标边界）以及频率域特征驱动模块（用于抑制噪声并突出目标纹理）。方法上，基于RT-DETR架构进行改进，引入边缘损失或频率域注意力机制。数据方面，可能使用公开的侧扫声纳图像数据集（如SCTD）或自建实测数据集，并进行数据增强以模拟不同噪声和模糊程度。

## 结果与结论

实验结果表明，LEF-RT-DETR在保持高检测精度的同时，模型参数量和计算量显著降低，推理速度满足实时处理要求。边缘和频率信息的引入有效改善了模糊目标的检测效果，尤其在低对比度场景下性能提升明显。创新点在于将边缘先验与频率域分析融入Transformer检测器，实现了精度、速度与模型复杂度的良好平衡。

## 来源链接

- OpenAlex：https://openalex.org/W7202399338
- DOI：https://doi.org/10.3389/fmars.2026.1797307