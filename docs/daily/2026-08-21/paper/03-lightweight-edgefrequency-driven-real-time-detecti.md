---
candidateId: "openalex--W7202399338"
category: "Paper"
date: "2026-08-21"
rank: 3
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
  - "信号识别"
journal: "Frontiers in Marine Science"
publisher: "Frontiers Media"
doi: "10.3389/fmars.2026.1797307"
publication_year: 2026
summary: "该论文针对侧扫声呐图像中目标边界模糊、噪声干扰强导致检测精度低的问题，提出了一种轻量级边缘-频率驱动的实时检测Transformer（LEF-RT-DETR）。研究背景是侧扫声呐成像机理复杂，水下环境多变，传统目标检测方法难以兼顾精度与实时性。目标是设计一种适用于水下目标检测的高效、轻量级深度学习框架。"
keywords:
  - "detection"
  - "underwater target detection"
  - "underwater target recognition"
score: 71.2
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7202399338"
  - name: "DOI"
    url: "https://doi.org/10.3389/fmars.2026.1797307"
previewImage: "/daily/2026-08-21/assets/openalex--W7202399338/preview.png"
---

## 核心内容

该论文针对侧扫声呐图像中目标边界模糊、噪声干扰强导致检测精度低的问题，提出了一种轻量级边缘-频率驱动的实时检测Transformer（LEF-RT-DETR）。研究背景是侧扫声呐成像机理复杂，水下环境多变，传统目标检测方法难以兼顾精度与实时性。目标是设计一种适用于水下目标检测的高效、轻量级深度学习框架。

## 关键技术与数据

关键技术包括边缘驱动模块，通过提取图像边缘先验增强目标边界特征；频率驱动模块，利用频域变换（如小波或FFT）强化目标纹理信息；以及基于RT-DETR的实时检测头，结合轻量化骨干网络降低计算量。训练数据可能包含实测侧扫声呐图像和仿真生成的合成图像，并标注沉船、水雷等目标。

## 结果与结论

实验表明，LEF-RT-DETR在检测精度（如mAP）上优于YOLO系列和传统DETR，同时推理速度满足实时处理要求。边缘和频率信息的引入有效缓解了边界模糊问题，在低对比度目标上提升明显。创新点在于将边缘与频率先验融入Transformer检测框架，实现了精度与效率的平衡。

## 来源链接

- OpenAlex：https://openalex.org/W7202399338
- DOI：https://doi.org/10.3389/fmars.2026.1797307