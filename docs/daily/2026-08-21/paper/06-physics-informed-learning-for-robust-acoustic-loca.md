---
candidateId: "openalex--W7202207427"
category: "Paper"
date: "2026-08-21"
rank: 6
title: "Physics-Informed Learning for Robust Acoustic Localization with Calibrated Uncertainty"
authors:
  - "Jennifer N. Kampe"
  - "Changwoo J. Lee"
  - "Xin Shen"
  - "Ari Lehtiö"
  - "Sandro von Brandenburg"
  - "Ossi Nokelainen"
  - "David B. Dunson"
  - "Otso Ovaskainen"
research_direction: []
journal: "arXiv (Cornell University)"
publisher: "Cornell University"
doi: "10.48550/arxiv.2608.08911"
publication_year: 2026
summary: "该论文针对被动声学监测（PAM）中经典定位方法（双曲线法、评分法）在真实户外声景中因多径主导、近场效应和复杂传播而失效的问题，提出了一种基于物理信息学习的鲁棒声学定位方法，并引入校准的不确定性估计，旨在实现高精度、可扩展的生态空间点过程数据获取。"
keywords:
  - "detection"
  - "localization"
score: 49.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7202207427"
  - name: "DOI"
    url: "https://doi.org/10.48550/arxiv.2608.08911"
previewImage: "/daily/2026-08-21/assets/openalex--W7202207427/preview.png"
---

## 核心内容

该论文针对被动声学监测（PAM）中经典定位方法（双曲线法、评分法）在真实户外声景中因多径主导、近场效应和复杂传播而失效的问题，提出了一种基于物理信息学习的鲁棒声学定位方法，并引入校准的不确定性估计，旨在实现高精度、可扩展的生态空间点过程数据获取。

## 关键技术与数据

论文将声传播物理模型（如衰减、时延）嵌入深度学习框架，构建物理信息神经网络（PINN）进行定位回归。关键技术包括多径与近场效应的物理约束损失函数设计、蒙特卡洛dropout或深度集成用于不确定性量化，以及真实户外声学数据集（可能含多种声源和传感器阵列）进行验证。

## 结果与结论

实验显示，该方法在复杂声场中的定位精度显著优于经典方法，且不确定性估计具有良好的校准性，能可靠反映预测置信度。论文创新性地融合物理先验与数据驱动，提升了定位的鲁棒性和泛化能力，为大规模生态声学监测提供了可靠的技术支撑。

## 来源链接

- OpenAlex：https://openalex.org/W7202207427
- DOI：https://doi.org/10.48550/arxiv.2608.08911