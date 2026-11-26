---
candidateId: "arxiv--2611.33587-1"
category: "Paper"
date: "2026-11-26"
rank: 1
title: "Geometry-Time Graph Attention for 3-D TOA Localization in Underwater Acoustic Sensor Networks"
authors:
  - "Wei Huang"
  - "Hongfei Chang"
  - "Kaitao Meng"
  - "Tianhe Xu"
  - "Hao Zhang"
  - "Yanan Wu"
  - "Qian Sun"
research_direction:
  - "水下传感器网络"
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "该论文针对水下声学传感器网络中三维到达时间（TOA）定位问题展开研究。由于声速随深度变化导致声线折射，基于传播模型的方法依赖假设或估计的声速剖面（SSP），剖面失配会引入定位偏差。论文提出一种水下图注意力网络（UGAN），融合同步到达时间信息实现目标三维定位，旨在摆脱对精确声速剖面的依赖，提升复杂环境下定位精度。"
keywords:
  - "localization"
  - "underwater acoustic sensor network"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2611.33587v1"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2611.33587v1"
previewImage: "/daily/2026-11-26/assets/arxiv--2611.33587-1/preview.png"
---

## 核心内容

该论文针对水下声学传感器网络中三维到达时间（TOA）定位问题展开研究。由于声速随深度变化导致声线折射，基于传播模型的方法依赖假设或估计的声速剖面（SSP），剖面失配会引入定位偏差。论文提出一种水下图注意力网络（UGAN），融合同步到达时间信息实现目标三维定位，旨在摆脱对精确声速剖面的依赖，提升复杂环境下定位精度。

## 关键技术与数据

关键技术为水下图注意力网络（UGAN），将传感器节点与目标建模为图结构，融合同步TOA测量进行特征聚合与注意力加权；采用几何-时间图注意力机制编码节点几何关系与到达时间信息。数据方面基于仿真水声环境生成TOA测量，涉及不同声速剖面条件下的定位场景，并与基于传播模型的方法进行对比验证。

## 结果与结论

结果表明，UGAN在声速剖面失配条件下仍能保持较高定位精度，优于依赖假设SSP的传统传播模型方法，有效降低了环境失配对定位的偏差影响。结论指出融合几何与时间信息的图注意力机制可提升三维TOA定位的鲁棒性，创新点在于以数据驱动方式规避声速剖面估计误差，为水下传感器网络定位提供了新思路。

## 来源链接

- arXiv：http://arxiv.org/abs/2611.33587v1
- PDF：http://arxiv.org/pdf/2611.33587v1