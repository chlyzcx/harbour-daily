---
candidateId: "openalex--W7202399338"
category: "Paper"
date: "2026-08-21"
rank: 7
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
summary: "该论文针对侧扫声纳（SSS）图像目标边界模糊、噪声干扰强导致高精度识别困难的问题，提出了一种轻量级边缘-频率驱动的实时检测Transformer（LEF-RT-DETR）。研究旨在在资源受限的水下平台实现高效、实时的目标检测，同时提升对弱边缘和频域特征的利用。"
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

该论文针对侧扫声纳（SSS）图像目标边界模糊、噪声干扰强导致高精度识别困难的问题，提出了一种轻量级边缘-频率驱动的实时检测Transformer（LEF-RT-DETR）。研究旨在在资源受限的水下平台实现高效、实时的目标检测，同时提升对弱边缘和频域特征的利用。

## 关键技术与数据

关键技术包括轻量化骨干网络（如MobileNet或更紧凑的Transformer结构）、边缘驱动模块（如Sobel算子或可学习边缘滤波器）和频率域注意力机制（如小波变换或FFT特征增强）。模型基于RT-DETR架构，采用无锚框的端到端检测范式。数据方面，使用侧扫声纳图像数据集（可能包含沉船、水雷、管道等目标），并进行数据增强模拟不同噪声和分辨率条件。

## 结果与结论

实验结果表明，LEF-RT-DETR在检测精度（mAP）和推理速度（FPS）之间取得了良好平衡，优于YOLO系列和标准DETR变体，尤其在低对比度目标上表现突出。结论指出，边缘与频率信息的显式注入有效增强了模型对声纳图像退化效应的鲁棒性，为实时水下探测系统提供了轻量化高精度方案。

## 来源链接

- OpenAlex：https://openalex.org/W7202399338
- DOI：https://doi.org/10.3389/fmars.2026.1797307