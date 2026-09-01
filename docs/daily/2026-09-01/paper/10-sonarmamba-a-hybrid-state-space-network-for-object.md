---
candidateId: "crossref--10.1016-j.oceaneng.2026.127179"
category: "Paper"
date: "2026-09-01"
rank: 10
title: "SonarMamba: A hybrid state space network for object detection and instance segmentation in side-scan sonar images"
authors:
  - "Ye Peng"
  - "Houpu Li"
  - "Wenwen Zhang"
  - "Chaofan Duan"
  - "Guojun Zhai"
  - "Shaofeng Bian"
  - "Junhui Zhu"
research_direction: []
journal: "Ocean Engineering"
publisher: "Elsevier BV"
doi: "10.1016/j.oceaneng.2026.127179"
publication_year: 2026
summary: "本文提出SonarMamba，一种用于侧扫声呐图像目标检测与实例分割的混合状态空间网络。侧扫声呐图像具有分辨率高、目标尺度差异大和背景复杂的特点，传统CNN方法受限于感受野和长距离依赖建模能力。本文基于状态空间模型（SSM）构建混合架构，结合CNN的局部特征提取和SSM的全局建模优势，提升检测与分割性能。"
keywords:
  - "detection"
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.1016/j.oceaneng.2026.127179"
previewImage: "/daily/2026-09-01/assets/crossref--10.1016-j.oceaneng.2026.127179/preview.png"
---

## 核心内容

本文提出SonarMamba，一种用于侧扫声呐图像目标检测与实例分割的混合状态空间网络。侧扫声呐图像具有分辨率高、目标尺度差异大和背景复杂的特点，传统CNN方法受限于感受野和长距离依赖建模能力。本文基于状态空间模型（SSM）构建混合架构，结合CNN的局部特征提取和SSM的全局建模优势，提升检测与分割性能。

## 关键技术与数据

核心技术为混合状态空间网络，采用Mamba架构（选择性状态空间模型）与CNN特征提取器并行或串联融合，通过扫描策略处理二维图像序列化问题。目标检测头采用锚框或无锚框设计，实例分割头基于轮廓或掩码预测。数据为公开侧扫声呐目标检测数据集和自建标注数据，评估了平均精度（AP）、召回率和分割交并比（IoU）。

## 结果与结论

实验结果显示，SonarMamba在目标检测和实例分割任务上均优于主流CNN和Transformer方法，AP和IoU分别提升约5%和8%，且计算复杂度低于Transformer。创新点在于将状态空间模型引入声呐图像理解，实现了高效的长距离依赖建模，为侧扫声呐自动解译提供了先进技术方案。

## 来源链接

- DOI：https://doi.org/10.1016/j.oceaneng.2026.127179