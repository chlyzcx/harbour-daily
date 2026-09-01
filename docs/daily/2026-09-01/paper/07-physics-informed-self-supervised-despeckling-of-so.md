---
candidateId: "crossref--10.1109-icip61757.2026.11630378"
category: "Paper"
date: "2026-09-01"
rank: 7
title: "Physics-Informed Self-Supervised Despeckling of Sonar Images via Residual Modeling"
authors:
  - "Swapna Pillai"
  - "Siddharth Singh Savner"
  - "Sujit Kumar Sahoo"
research_direction: []
journal: "2026 IEEE International Conference on Image Processing (ICIP)"
publisher: "IEEE"
doi: "10.1109/icip61757.2026.11630378"
publication_year: 2026
summary: "针对声呐图像中的相干斑噪声抑制问题，本文提出一种基于物理信息的自监督去斑方法。声呐图像受相干斑噪声严重影响，传统去斑方法依赖成对训练数据或手工特征，且易损失边缘细节。本文利用声呐成像物理模型构建残差建模框架，通过自监督学习实现无需干净标签的去斑，同时保持图像结构信息。"
keywords: []
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.1109/icip61757.2026.11630378"
previewImage: "/daily/2026-09-01/assets/crossref--10.1109-icip61757.2026.11630378/preview.svg"
---

## 核心内容

针对声呐图像中的相干斑噪声抑制问题，本文提出一种基于物理信息的自监督去斑方法。声呐图像受相干斑噪声严重影响，传统去斑方法依赖成对训练数据或手工特征，且易损失边缘细节。本文利用声呐成像物理模型构建残差建模框架，通过自监督学习实现无需干净标签的去斑，同时保持图像结构信息。

## 关键技术与数据

核心技术为物理信息自监督去斑网络，利用声呐成像的乘性噪声模型构建残差学习目标，网络输入为含噪图像，输出为噪声残差，通过物理约束引导训练过程。采用U-Net或残差网络架构，损失函数包含保真项和物理正则项。数据为仿真声呐图像和实测侧扫声呐图像，评估了峰值信噪比（PSNR）、结构相似性（SSIM）和边缘保持指数。

## 结果与结论

实验结果表明，所提方法在去斑效果和边缘保持方面优于传统滤波器和监督学习方法，PSNR和SSIM均有显著提升，且无需配对数据。创新点在于物理信息约束与自监督学习的结合，为声呐图像去斑提供了无需标注的实用方案。

## 来源链接

- DOI：https://doi.org/10.1109/icip61757.2026.11630378