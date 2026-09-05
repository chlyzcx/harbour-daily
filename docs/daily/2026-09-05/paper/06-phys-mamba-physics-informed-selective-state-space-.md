---
candidateId: "openalex--W7206156946"
category: "Paper"
date: "2026-09-05"
rank: 6
title: "Phys-Mamba: Physics-informed selective state-space fusion network for high-fidelity underwater image restoration"
authors:
  - "H. Li"
  - "Weishen Li"
  - "Y. Lao"
  - "Jie Li"
  - "Junjie He"
  - "Caihong Wu"
  - "Huilong Zhong"
  - "Shaoji Huang"
research_direction: []
journal: "PLoS ONE"
publisher: "Public Library of Science"
doi: "10.1371/journal.pone.0354030"
publication_year: 2026
summary: "该论文针对水下图像复原中生成式方法与Transformer架构的固有矛盾展开研究：GAN方法（如FUnIE-GAN）因缺乏显式光学约束易产生物理不一致伪影；Transformer虽能全局建模但计算复杂度为O(N²)，难以满足AUV/ROV实时需求。目标是在物理引导下实现高保真且高效的水下图像复原，提出物理信息选择性状态空间融合网络Phys-Mamba。"
keywords: []
score: 56.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7206156946"
  - name: "DOI"
    url: "https://doi.org/10.1371/journal.pone.0354030"
previewImage: "/daily/2026-09-05/assets/openalex--W7206156946/preview.png"
---

## 核心内容

该论文针对水下图像复原中生成式方法与Transformer架构的固有矛盾展开研究：GAN方法（如FUnIE-GAN）因缺乏显式光学约束易产生物理不一致伪影；Transformer虽能全局建模但计算复杂度为O(N²)，难以满足AUV/ROV实时需求。目标是在物理引导下实现高保真且高效的水下图像复原，提出物理信息选择性状态空间融合网络Phys-Mamba。

## 关键技术与数据

关键技术为选择性状态空间模型（Mamba）与物理信息融合，利用状态空间的线性复杂度替代Transformer的二次复杂度；物理信息模块嵌入水下光学衰减模型（如Jaffe-McGlamery模型）作为约束先验。训练数据采用合成水下图像数据集（基于深度与水质参数生成）与真实水下图像，评估指标包括PSNR、SSIM与感知质量。

## 结果与结论

实验表明Phys-Mamba在复原精度上优于FUnIE-GAN等GAN方法，消除物理不一致伪影；计算效率显著高于Transformer方法，在保持全局建模能力的同时实现线性复杂度，满足实时处理需求。创新点在于将物理光学模型与状态空间架构深度耦合，为水下视觉感知提供了兼顾质量与速度的解决方案。

## 来源链接

- OpenAlex：https://openalex.org/W7206156946
- DOI：https://doi.org/10.1371/journal.pone.0354030