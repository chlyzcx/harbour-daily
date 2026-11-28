---
candidateId: "openalex--W7240043958"
category: "Paper"
date: "2026-11-28"
rank: 1
title: "Geometry-Time Graph Attention for 3-D TOA Localization in Underwater Acoustic Sensor Networks"
authors:
  - "Wei Huang"
  - "常鸿飞"
  - "Kaitao Meng"
  - "Tianhe Xu"
  - "Hao Zhang"
  - "Yanan Wu"
  - "Qian Sun"
research_direction:
  - "水下传感器网络"
journal: "arXiv"
publisher: "arXiv"
doi: "10.48550/arxiv.2611.33587"
publication_year: 2026
summary: "针对水下声速随深度变化导致声线折射、进而使基于传播模型的到达时间（TOA）定位产生偏差的问题，该论文提出一种几何-时间图注意力机制用于三维TOA定位。研究目标是摆脱对假定或估计声速剖面（SSP）的依赖，通过融合同步到达时间信息与节点几何关系，提升水下声学传感器网络中目标定位的鲁棒性与精度。"
keywords:
  - "localization"
  - "underwater acoustic sensor network"
score: 64.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7240043958"
  - name: "DOI"
    url: "https://doi.org/10.48550/arxiv.2611.33587"
previewImage: "/daily/2026-11-28/assets/openalex--W7240043958/preview.png"
---

## 核心内容

针对水下声速随深度变化导致声线折射、进而使基于传播模型的到达时间（TOA）定位产生偏差的问题，该论文提出一种几何-时间图注意力机制用于三维TOA定位。研究目标是摆脱对假定或估计声速剖面（SSP）的依赖，通过融合同步到达时间信息与节点几何关系，提升水下声学传感器网络中目标定位的鲁棒性与精度。

## 关键技术与数据

提出水下图注意力网络（UGAN），将传感器节点建模为图结构，融合同步TOA测量与几何拓扑信息，利用图注意力机制自适应学习节点间权重以抑制SSP失配带来的误差。输入为多节点TOA观测及节点位置几何关系，通过注意力聚合实现三维坐标回归，避免显式声速剖面建模。

## 结果与结论

UGAN在SSP失配条件下仍能保持较高定位精度，相较依赖传播模型的方法显著降低位置估计偏差，验证了图注意力融合几何与时间信息在三维水声定位中的有效性，为无精确SSP场景下的目标定位提供了新思路。

## 来源链接

- OpenAlex：https://openalex.org/W7240043958
- DOI：https://doi.org/10.48550/arxiv.2611.33587