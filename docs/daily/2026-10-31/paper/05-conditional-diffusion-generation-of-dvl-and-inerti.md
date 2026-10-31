---
candidateId: "openalex--W7224137929"
category: "Paper"
date: "2026-10-31"
rank: 5
title: "Conditional Diffusion Generation of DVL and Inertial Signals for Underwater Navigation"
authors:
  - "Michal Levin"
  - "Itzik Klein"
research_direction:
  - "水下导航"
journal: "arXiv (Cornell University)"
publisher: "Cornell University"
publication_year: 2026
summary: "针对自主水下航行器（AUV）无卫星定位、依赖多普勒速度计（DVL）与惯性传感器进行运动估计时深度学习训练数据需昂贵海上试验获取的问题，论文提出一种条件扩散生成框架，合成DVL与惯性信号以替代真实记录用于训练，从而降低数据获取成本。"
keywords:
  - "Doppler velocity log"
  - "deep learning"
  - "doppler"
  - "underwater navigation"
score: 63.2
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7224137929"
previewImage: "/daily/2026-10-31/assets/openalex--W7224137929/preview.png"
---

## 核心内容

针对自主水下航行器（AUV）无卫星定位、依赖多普勒速度计（DVL）与惯性传感器进行运动估计时深度学习训练数据需昂贵海上试验获取的问题，论文提出一种条件扩散生成框架，合成DVL与惯性信号以替代真实记录用于训练，从而降低数据获取成本。

## 关键技术与数据

采用条件扩散模型作为生成器，以航行器运动状态为条件生成合成DVL与惯性信号，替代真实海试数据用于深度学习训练。实验通过生成信号与真实记录的对比及下游导航任务验证生成数据的有效性与保真度。

## 结果与结论

条件扩散框架生成的合成DVL与惯性信号能够有效替代真实记录用于训练，在降低海试数据依赖的同时保持导航估计性能。创新点在于将条件扩散生成模型引入水下导航传感器数据增强，为AUV导航深度学习提供了低成本数据生成途径。

## 来源链接

- OpenAlex：https://openalex.org/W7224137929