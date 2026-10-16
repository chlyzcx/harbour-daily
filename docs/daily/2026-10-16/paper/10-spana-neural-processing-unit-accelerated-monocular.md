---
candidateId: "crossref--10.51316-jst.194.dsai.2026.36.1.4"
category: "Paper"
date: "2026-10-16"
rank: 10
title: "<span>A Neural Processing Unit-Accelerated Monocular Perception Pipeline for Remotely Operated Underwater Vehicle Station Keeping</span>"
authors:
  - "Gyan Louisin"
  - "Vinh La The"
  - "Trung Ngo Lam"
  - "Nga Nguyen Thi Thanh"
  - "Dung Nguyen Anh"
  - "Duc Duong Minh"
  - "Hiep Hoang Van"
research_direction: []
journal: "Data Science and Artificial Intelligence"
publisher: "Hanoi University of Science and Technology"
doi: "10.51316/jst.194.dsai.2026.36.1.4"
publication_year: 2026
summary: "本文面向遥控水下航行器（ROV）的定点保持任务，针对仅配备单目相机且计算须全部在艇上运行的约束，报告了在Qualcomm QCS8550平台上基于Hexagon HTP/NPU加速器部署完整视觉定点保持感知流水线的工作，其中INT8目标检测器与稠密单目深度模型共享单一加速器。"
keywords: []
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.51316/jst.194.dsai.2026.36.1.4"
previewImage: "/daily/2026-10-16/assets/crossref--10.51316-jst.194.dsai.2026.36.1.4/preview.svg"
---

## 核心内容

本文面向遥控水下航行器（ROV）的定点保持任务，针对仅配备单目相机且计算须全部在艇上运行的约束，报告了在Qualcomm QCS8550平台上基于Hexagon HTP/NPU加速器部署完整视觉定点保持感知流水线的工作，其中INT8目标检测器与稠密单目深度模型共享单一加速器。

## 关键技术与数据

关键技术包括神经处理单元（NPU）加速、INT8量化目标检测、稠密单目深度估计、单目视觉定点保持感知流水线。方法上两个网络共享QCS8550的Hexagon HTP/NPU加速器，实现艇上实时推理。数据为ROV定点保持场景下的单目图像及深度估计与检测结果。

## 结果与结论

该流水线在QCS8550平台上实现了艇上实时运行，验证了NPU加速下单目视觉定点保持感知的可行性。结论表明INT8检测与稠密深度网络共享NPU的方案能满足ROV定点保持的实时性要求，创新点在于面向嵌入式平台的NPU加速单目感知流水线部署。

## 来源链接

- DOI：https://doi.org/10.51316/jst.194.dsai.2026.36.1.4