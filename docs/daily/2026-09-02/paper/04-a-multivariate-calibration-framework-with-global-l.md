---
candidateId: "crossref--10.1016-j.imavis.2026.106079"
category: "Paper"
date: "2026-09-02"
rank: 4
title: "A multivariate calibration framework with global-local interaction and edge-aware enhancement for sonar image despeckling"
authors:
  - "Xin Zhou"
  - "Xiangyuan Pang"
  - "Haokai Ma"
  - "Bo Ning"
  - "Yanhao Wang"
research_direction: []
journal: "Image and Vision Computing"
publisher: "Elsevier BV"
doi: "10.1016/j.imavis.2026.106079"
publication_year: 2026
summary: "本文提出一种用于声呐图像去斑的多变量标定框架，结合全局-局部交互和边缘感知增强技术。声呐图像受相干斑噪声严重影响，传统去斑方法易模糊边缘细节。该框架旨在在抑制噪声的同时保持图像边缘和纹理结构，提升后续目标识别和分类性能。"
keywords: []
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.1016/j.imavis.2026.106079"
previewImage: "/daily/2026-09-02/assets/crossref--10.1016-j.imavis.2026.106079/preview.png"
---

## 核心内容

本文提出一种用于声呐图像去斑的多变量标定框架，结合全局-局部交互和边缘感知增强技术。声呐图像受相干斑噪声严重影响，传统去斑方法易模糊边缘细节。该框架旨在在抑制噪声的同时保持图像边缘和纹理结构，提升后续目标识别和分类性能。

## 关键技术与数据

构建多变量标定模型，将像素强度、局部方差和梯度信息作为联合输入。全局-局部交互模块通过注意力机制融合多尺度特征，边缘感知增强采用可学习梯度算子约束损失函数。使用真实侧扫声呐图像和合成斑点噪声图像进行训练与测试，对比BM3D、SAR-BM3D和深度学习方法。

## 结果与结论

实验结果显示，该方法在峰值信噪比（PSNR）、结构相似性（SSIM）和边缘保持指数（EPI）上均优于对比算法，去斑后图像纹理清晰度显著提升。创新点在于多变量标定与边缘感知的有机结合，有效解决了去斑与细节保持的矛盾，适用于高噪声水下环境。

## 来源链接

- DOI：https://doi.org/10.1016/j.imavis.2026.106079