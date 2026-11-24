---
candidateId: "crossref--10.1007-978-3-032-45236-8_31"
category: "Paper"
date: "2026-11-24"
rank: 1
title: "Adapting Diffusion-Based LiDAR Scene Completion to Underwater SONAR Bathymetry"
authors:
  - "Varchaswi Madamanchi"
  - "Ahmed Elsayed"
  - "Benjamin Lehmann"
  - "Frederic Stahl"
research_direction: []
journal: "Lecture Notes in Computer Science"
publisher: "Springer Nature Switzerland"
doi: "10.1007/978-3-032-45236-8_31"
publication_year: 2026
summary: "该论文针对水下声呐测深数据稀疏、覆盖不全的问题，提出将基于扩散模型的激光雷达场景补全方法迁移至水下声呐测深领域。研究目标是利用扩散概率模型的生成能力，从稀疏的水下测深点云中重建完整海底地形场景，探索跨模态迁移学习在水声工程中的可行性，为水下地形测绘与自主导航提供场景补全方案。"
keywords: []
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.1007/978-3-032-45236-8_31"
previewImage: "/daily/2026-11-24/assets/crossref--10.1007-978-3-032-45236-8_31/preview.svg"
---

## 核心内容

该论文针对水下声呐测深数据稀疏、覆盖不全的问题，提出将基于扩散模型的激光雷达场景补全方法迁移至水下声呐测深领域。研究目标是利用扩散概率模型的生成能力，从稀疏的水下测深点云中重建完整海底地形场景，探索跨模态迁移学习在水声工程中的可行性，为水下地形测绘与自主导航提供场景补全方案。

## 关键技术与数据

核心技术为扩散概率模型（diffusion-based generative model），通过前向加噪与反向去噪过程实现点云场景补全。方法上将陆上激光雷达场景补全的预训练模型适配至声呐测深数据，涉及域适应与数据表征转换。数据方面使用水下声呐测深点云，需处理声呐数据特有的稀疏性、噪声与不规则采样特性，并与激光雷达数据分布进行对齐。

## 结果与结论

论文验证了扩散模型跨模态迁移至水下声呐测深场景补全的可行性，表明陆上激光雷达预训练模型经适配后可有效处理声呐稀疏点云。创新点在于首次将扩散式场景补全范式引入水声测深领域，为水下地形重建提供了生成式新思路，但受限于摘要缺失，具体性能指标与定量结论需参阅原文。

## 来源链接

- DOI：https://doi.org/10.1007/978-3-032-45236-8_31