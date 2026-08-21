---
candidateId: "s2--0b8abe046e81470e09b7bb0c649da6736e04bd78"
category: "Paper"
date: "2026-08-21"
rank: 3
title: "Physics-Guided Neural Radiance Fields for Forward-Looking Sonar Imaging"
authors:
  - "Cao Huang"
  - "Jinchang Ren"
  - "Hongyu Yang"
  - "Yulong Ji"
research_direction:
  - "主动声呐"
journal: "IEEE Signal Processing Letters"
publisher: "Semantic Scholar"
publication_year: 2026
summary: "该论文针对神经辐射场（NeRF）在光学成像成功但难以直接应用于前视声呐（FLS）的问题，提出了Sonar-NeRF物理引导神经渲染框架。研究目标是根据主动声呐方程推导显式前向渲染模型，替代传统体渲染，实现高保真的FLS新视角合成，弥补声学传播物理机制差异带来的空白。"
keywords:
  - "active sonar"
score: 62.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.1109/LSP.2026.3673652"
  - name: "Semantic Scholar"
    url: "https://www.semanticscholar.org/paper/0b8abe046e81470e09b7bb0c649da6736e04bd78"
previewImage: "/daily/2026-08-21/assets/s2--0b8abe046e81470e09b7bb0c649da6736e04bd78/preview.svg"
---

## 核心内容

该论文针对神经辐射场（NeRF）在光学成像成功但难以直接应用于前视声呐（FLS）的问题，提出了Sonar-NeRF物理引导神经渲染框架。研究目标是根据主动声呐方程推导显式前向渲染模型，替代传统体渲染，实现高保真的FLS新视角合成，弥补声学传播物理机制差异带来的空白。

## 关键技术与数据

核心技术为物理引导的神经渲染，利用主动声呐方程构建声传播与散射模型，结合NeRF网络学习场景隐式表示。数据可能采用仿真声呐图像或实测FLS数据，用于训练和评估新视角合成质量，并与标准NeRF及插值方法对比。

## 结果与结论

实验结果表明，Sonar-NeRF在FLS新视角合成中显著优于现有方法，生成的图像具有更高的几何一致性和纹理保真度。创新点在于将声呐物理模型深度融入NeRF框架，为水声成像三维重建提供了新范式。

## 来源链接

- DOI：https://doi.org/10.1109/LSP.2026.3673652
- Semantic Scholar：https://www.semanticscholar.org/paper/0b8abe046e81470e09b7bb0c649da6736e04bd78