---
candidateId: "openalex--W7216128482"
category: "Paper"
date: "2026-10-04"
rank: 3
title: "SonarVoxNet: Diver Detection in 3D Bounding Box using 3D Sonar"
authors:
  - "Eugene Park"
  - "Jiwon Lee"
  - "Seyoung Kan"
  - "Trung Dong"
  - "Xiaomin Lin"
  - "Jane Shin"
research_direction:
  - "水声成像"
journal: "arXiv (Cornell University)"
publisher: "Cornell University"
doi: "10.48550/arxiv.2610.01644"
publication_year: 2026
summary: "辅助人类潜水员的自主水下航行器需持续跟踪潜水员三维位置及全身朝向，但水下视觉感知不可靠，前视声纳虽广泛使用却丢失高度信息，无法估计朝向。近期商用3D声纳保留高度信息但产生稀疏、噪声回波，现有检测器针对2D声纳设计。本文提出SonarVoxNet，利用3D声纳实现潜水员三维边界框检测。"
keywords:
  - "detection"
  - "forward-looking sonar"
  - "sparse"
score: 64.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7216128482"
  - name: "DOI"
    url: "https://doi.org/10.48550/arxiv.2610.01644"
previewImage: "/daily/2026-10-04/assets/openalex--W7216128482/preview.png"
---

## 核心内容

辅助人类潜水员的自主水下航行器需持续跟踪潜水员三维位置及全身朝向，但水下视觉感知不可靠，前视声纳虽广泛使用却丢失高度信息，无法估计朝向。近期商用3D声纳保留高度信息但产生稀疏、噪声回波，现有检测器针对2D声纳设计。本文提出SonarVoxNet，利用3D声纳实现潜水员三维边界框检测。

## 关键技术与数据

SonarVoxNet针对3D声纳稀疏、噪声点云特性设计，采用三维边界框检测网络，融合声纳成像机制与深度学习。输入为3D声纳点云数据，输出潜水员三维位置与朝向。训练与测试数据来自3D声纳采集的潜水员目标回波，需处理稀疏性与噪声干扰。

## 结果与结论

SonarVoxNet实现了基于3D声纳的潜水员三维边界框检测，能够同时估计位置与全身朝向，克服了前视声纳丢失高度信息的根本局限。在稀疏、噪声回波条件下保持检测性能，创新在于首次将3D声纳与三维边界框检测结合用于潜水员跟踪，为AUV辅助潜水提供了可靠的感知手段。

## 来源链接

- OpenAlex：https://openalex.org/W7216128482
- DOI：https://doi.org/10.48550/arxiv.2610.01644