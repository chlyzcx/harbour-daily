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
summary: "该论文针对侧扫声纳（SSS）图像目标边界模糊和强噪声干扰导致识别困难的问题，提出了轻量级边缘-频率驱动的实时检测Transformer（LEF-RT-DETR）。研究目标是在保持高精度的同时实现实时检测，适应水下自主平台的算力限制。"
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

该论文针对侧扫声纳（SSS）图像目标边界模糊和强噪声干扰导致识别困难的问题，提出了轻量级边缘-频率驱动的实时检测Transformer（LEF-RT-DETR）。研究目标是在保持高精度的同时实现实时检测，适应水下自主平台的算力限制。

## 关键技术与数据

LEF-RT-DETR基于RT-DETR架构，引入边缘驱动模块（如边缘卷积或梯度先验）增强目标边界特征，以及频率驱动模块（如小波变换或频域注意力）抑制噪声。轻量化设计可能采用深度可分离卷积和知识蒸馏。数据集可能包含实测SSS图像（沉船、水雷等），评估指标为mAP和FPS。

## 结果与结论

实验证明，该框架在SSS目标检测任务中取得了优于YOLO系列和标准DETR的精度-速度平衡，mAP提升且推理速度满足实时要求。创新点在于将边缘与频率先验融入Transformer检测器，并实现轻量化部署，为水下机器人实时目标识别提供了高效方案。

## 来源链接

- OpenAlex：https://openalex.org/W7202399338
- DOI：https://doi.org/10.3389/fmars.2026.1797307