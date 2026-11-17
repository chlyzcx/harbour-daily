---
candidateId: "openalex--W7233546208"
category: "Paper"
date: "2026-11-17"
rank: 1
title: "Direction-adaptive expert decomposition via structural-prior Mixture-of-Experts for self-supervised sonar image despeckling"
authors:
  - "Can Guo"
  - "Yuduo Zhang"
  - "Kaijun Yue"
  - "Fei Tian"
  - "Jinshuo Ma"
research_direction: []
journal: "Ocean Engineering"
publisher: "Elsevier BV"
doi: "10.1016/j.oceaneng.2026.129372"
publication_year: 2026
summary: "该论文针对声呐图像斑点噪声抑制问题，提出一种方向自适应专家分解方法。研究背景为自监督声呐图像去斑中，单一网络难以同时适应不同方向的结构特征与噪声分布。论文目标是构建基于结构先验的混合专家框架，实现无需干净标签的自监督去斑，并提升边缘与纹理保持能力。主要内容包括结构先验引导的专家分解模块、方向自适应路由机制以及自监督训练策略。"
keywords: []
score: 65.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7233546208"
  - name: "DOI"
    url: "https://doi.org/10.1016/j.oceaneng.2026.129372"
previewImage: "/daily/2026-11-17/assets/openalex--W7233546208/preview.png"
---

## 核心内容

该论文针对声呐图像斑点噪声抑制问题，提出一种方向自适应专家分解方法。研究背景为自监督声呐图像去斑中，单一网络难以同时适应不同方向的结构特征与噪声分布。论文目标是构建基于结构先验的混合专家框架，实现无需干净标签的自监督去斑，并提升边缘与纹理保持能力。主要内容包括结构先验引导的专家分解模块、方向自适应路由机制以及自监督训练策略。

## 关键技术与数据

关键技术为结构先验混合专家（Mixture-of-Experts）架构，包含方向自适应专家分解、结构先验引导的路由网络和自监督去斑损失函数。方法通过多专家分别建模不同方向结构，并由路由网络依据局部结构先验自适应分配专家权重。数据方面使用声呐图像数据集进行自监督训练与评估，未依赖配对干净图像。

## 结果与结论

实验表明该方法在自监督条件下有效抑制斑点噪声，并在边缘保持与结构连续性方面优于对比方法。结论指出结构先验引导的专家分解可提升方向自适应能力，混合专家机制增强了对复杂声呐场景的泛化性。创新点在于将结构先验与混合专家结合用于自监督声呐图像去斑，实现方向自适应噪声抑制。

## 来源链接

- OpenAlex：https://openalex.org/W7233546208
- DOI：https://doi.org/10.1016/j.oceaneng.2026.129372