---
candidateId: "openalex--W7213984046"
category: "Paper"
date: "2026-09-23"
rank: 4
title: "Task-driven joint denoising and super-resolution of side-scan sonar images based on knowledge distillation"
authors:
  - "Rui Tang"
  - "Yimin Chen"
  - "Shaowen Hao"
  - "Jian Gao"
  - "Yuhao Huang"
research_direction:
  - "目标检测"
journal: "Engineering Applications of Artificial Intelligence"
publisher: "Elsevier BV"
doi: "10.1016/j.engappai.2026.116304"
publication_year: 2026
summary: "侧扫声呐（SSS）图像的去噪与超分辨率对水下目标检测等高层视觉任务至关重要。然而，独立处理去噪和超分辨率会导致两个过程相互干扰；且视觉质量的提升不一定带来下游任务性能的改善。本文以检测任务为导向，研究基于知识蒸馏的联合去噪与超分辨率方法，旨在实现任务驱动的SSS图像增强。"
keywords:
  - "detection"
  - "tracking"
  - "underwater object detection"
score: 66.0
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7213984046"
  - name: "DOI"
    url: "https://doi.org/10.1016/j.engappai.2026.116304"
previewImage: "/daily/2026-09-23/assets/openalex--W7213984046/preview.png"
---

## 核心内容

侧扫声呐（SSS）图像的去噪与超分辨率对水下目标检测等高层视觉任务至关重要。然而，独立处理去噪和超分辨率会导致两个过程相互干扰；且视觉质量的提升不一定带来下游任务性能的改善。本文以检测任务为导向，研究基于知识蒸馏的联合去噪与超分辨率方法，旨在实现任务驱动的SSS图像增强。

## 关键技术与数据

关键技术包括：1）联合去噪与超分辨率框架，避免两过程相互干扰；2）知识蒸馏策略，将下游检测任务的知识融入增强网络训练；3）任务驱动的优化目标，以检测性能而非视觉质量为导向。方法可能采用教师-学生网络结构，教师网络包含检测任务信息，学生网络执行联合增强。数据为侧扫声呐图像及对应检测标注。

## 结果与结论

摘要信息不完整，未获取具体性能指标。预期结论为：任务驱动的联合增强方法在检测精度上优于独立去噪+超分辨率方案，且知识蒸馏能有效将检测任务知识迁移至增强网络。创新点在于：1）联合处理去噪与超分辨率避免干扰；2）以检测任务驱动增强过程；3）知识蒸馏实现任务知识迁移。

## 来源链接

- OpenAlex：https://openalex.org/W7213984046
- DOI：https://doi.org/10.1016/j.engappai.2026.116304