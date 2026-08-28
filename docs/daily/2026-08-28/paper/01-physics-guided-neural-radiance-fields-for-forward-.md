---
candidateId: "s2--0b8abe046e81470e09b7bb0c649da6736e04bd78"
category: "Paper"
date: "2026-08-28"
rank: 1
title: "Physics-Guided Neural Radiance Fields for Forward-Looking Sonar Imaging"
authors:
  - "Cao Huang"
  - "Jinchang Ren"
  - "Hongyu Yang"
  - "Yulong Ji"
research_direction:
  - "主动声呐"
  - "水声成像"
journal: "IEEE Signal Processing Letters"
publisher: "Semantic Scholar"
doi: "10.1109/LSP.2026.3673652"
publication_year: 2026
summary: "神经辐射场（NeRF）在光学成像中取得了显著成功，但由于声学传播物理机制的根本差异，其在前视声呐（FLS）中的应用尚未充分探索。本文提出Sonar-NeRF，一种物理引导的神经渲染框架，旨在实现高保真FLS新视角合成。该方法用基于主动声呐方程的显式前向渲染模型替代体渲染，以适配声学成像特性。"
keywords:
  - "active sonar"
  - "forward-looking sonar"
score: 62.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.1109/LSP.2026.3673652"
  - name: "Semantic Scholar"
    url: "https://www.semanticscholar.org/paper/0b8abe046e81470e09b7bb0c649da6736e04bd78"
previewImage: "/daily/2026-08-28/assets/s2--0b8abe046e81470e09b7bb0c649da6736e04bd78/preview.svg"
---

## 核心内容

神经辐射场（NeRF）在光学成像中取得了显著成功，但由于声学传播物理机制的根本差异，其在前视声呐（FLS）中的应用尚未充分探索。本文提出Sonar-NeRF，一种物理引导的神经渲染框架，旨在实现高保真FLS新视角合成。该方法用基于主动声呐方程的显式前向渲染模型替代体渲染，以适配声学成像特性。

## 关键技术与数据

核心技术为物理引导的神经渲染，将主动声呐方程融入前向渲染模型，替代传统NeRF的体渲染过程。方法显式建模声波传播、散射与接收过程，利用神经网络隐式表示场景几何与声学属性。训练数据为FLS采集的多视角声呐图像序列，通过物理模型约束网络学习，实现新视角声呐图像合成。

## 结果与结论

实验表明Sonar-NeRF在FLS新视角合成任务中显著优于现有方法，生成的声呐图像具有更高的保真度和几何一致性。创新点在于将声呐物理模型与神经渲染深度耦合，解决了传统NeRF直接迁移至声呐成像时的物理失配问题，为声呐图像渲染与场景重建提供了新范式。

## 来源链接

- DOI：https://doi.org/10.1109/LSP.2026.3673652
- Semantic Scholar：https://www.semanticscholar.org/paper/0b8abe046e81470e09b7bb0c649da6736e04bd78