---
candidateId: "openalex--W7224919307"
category: "Paper"
date: "2026-11-01"
rank: 1
title: "Sonar2DGS: Differentiable 2D Gaussian Splatting for forward-looking sonar 3D reconstruction"
authors:
  - "Yibo Zhao"
  - "Xin Wang"
  - "Jiangang Li"
research_direction:
  - "水声成像"
journal: "Ocean Engineering"
publisher: "Elsevier BV"
doi: "10.1016/j.oceaneng.2026.129010"
publication_year: 2026
summary: "针对前视声呐三维重建中传统方法对噪声敏感、几何一致性差的问题，该论文提出Sonar2DGS框架，将可微分二维高斯泼溅（2D Gaussian Splatting）引入前视声呐图像的三维重建任务。研究目标是构建端到端可优化的声呐图像表征与重建管线，利用高斯原语对声呐回波进行显式建模，并通过可微渲染实现位姿与场景结构的联合优化，从而提升前视声呐在低信噪比、强混响条件下的三维重建精度与效率。"
keywords:
  - "forward-looking sonar"
score: 73.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7224919307"
  - name: "DOI"
    url: "https://doi.org/10.1016/j.oceaneng.2026.129010"
previewImage: "/daily/2026-11-01/assets/openalex--W7224919307/preview.png"
---

## 核心内容

针对前视声呐三维重建中传统方法对噪声敏感、几何一致性差的问题，该论文提出Sonar2DGS框架，将可微分二维高斯泼溅（2D Gaussian Splatting）引入前视声呐图像的三维重建任务。研究目标是构建端到端可优化的声呐图像表征与重建管线，利用高斯原语对声呐回波进行显式建模，并通过可微渲染实现位姿与场景结构的联合优化，从而提升前视声呐在低信噪比、强混响条件下的三维重建精度与效率。

## 关键技术与数据

关键技术包括二维高斯泼溅表示、可微分渲染、声呐成像模型的前向建模与梯度反传。方法上将场景表示为各向异性二维高斯原语集合，通过可微光栅化生成模拟声呐图像，并以真实声呐图像监督优化高斯参数与传感器位姿。数据方面使用前视声呐采集的多视角图像序列进行训练与评测，具体数据集名称因摘要缺失未明确。

## 结果与结论

论文通过可微分高斯泼溅实现了前视声呐的三维重建，验证了显式高斯表征在声呐图像上的可优化性与渲染效率。结论表明该方法能够在复杂水下环境中恢复场景几何结构，较传统体素或隐式神经表示方法具有更高的重建效率与渲染速度，为前视声呐三维感知提供了新的可微渲染范式。具体量化指标因摘要缺失未列出。

## 来源链接

- OpenAlex：https://openalex.org/W7224919307
- DOI：https://doi.org/10.1016/j.oceaneng.2026.129010