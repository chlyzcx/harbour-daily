---
candidateId: "openalex--W7204167684"
category: "Paper"
date: "2026-08-27"
rank: 4
title: "BenthicDINO: Physics-Informed Self-Distillation for View-Invariant Side-Scan Sonar Representations"
authors:
  - "Taqi Hamoda"
  - "Hayat Rajani"
  - "Nuno Gracias"
research_direction: []
journal: "arXiv (Cornell University)"
publisher: "Cornell University"
doi: "10.48550/arxiv.2608.23215"
publication_year: 2026
summary: "该论文针对侧扫声呐图像中物理声学伪影严重阻碍自动感知的问题，提出一种物理信息引导的自蒸馏框架BenthicDINO。研究背景在于现有自监督学习方法基于自然图像增强设计，未考虑声学退化机制和视角不变性。论文旨在学习对视角变化鲁棒的海底反射率表征。"
keywords: []
score: 56.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7204167684"
  - name: "DOI"
    url: "https://doi.org/10.48550/arxiv.2608.23215"
previewImage: "/daily/2026-08-27/assets/openalex--W7204167684/preview.png"
---

## 核心内容

该论文针对侧扫声呐图像中物理声学伪影严重阻碍自动感知的问题，提出一种物理信息引导的自蒸馏框架BenthicDINO。研究背景在于现有自监督学习方法基于自然图像增强设计，未考虑声学退化机制和视角不变性。论文旨在学习对视角变化鲁棒的海底反射率表征。

## 关键技术与数据

关键技术包括：物理信息增强模块，模拟声呐成像中的声学退化过程（如斑点噪声、阴影、掠射角效应）；自蒸馏架构，通过教师-学生网络实现视角不变表征学习；对比学习损失函数结合物理约束。数据采用真实侧扫声呐图像，涵盖不同海底类型和地形条件，并构建视角变化对用于训练。

## 结果与结论

实验表明BenthicDINO在海底分类和目标检测任务上优于现有自监督方法，尤其在跨视角匹配场景下性能提升显著。该框架有效分离了海底固有反射率与观测几何的影响，为侧扫声呐图像的自动化解译提供了更稳健的表征基础，推动了物理感知与深度学习的深度融合。

## 来源链接

- OpenAlex：https://openalex.org/W7204167684
- DOI：https://doi.org/10.48550/arxiv.2608.23215