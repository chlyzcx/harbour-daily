---
candidateId: "openalex--W7215078307"
category: "Paper"
date: "2026-10-03"
rank: 6
title: "BatSLAM 2.0: Sequence-Verified Sonar Place Recognition in a Robust Pose Graph"
authors:
  - "Jan Steckel"
research_direction:
  - "生物声呐"
journal: "arXiv (Cornell University)"
publisher: "Cornell University"
doi: "10.48550/arxiv.2609.40085"
publication_year: 2026
summary: "回声定位蝙蝠能利用声呐在黑暗杂乱空间中导航。十多年前BatSLAM展示了仿生双耳声呐机器人可通过识别接收声学信号中的位置构建拓扑地图，但声呐位置识别本质上是模糊的：走廊产生几乎相同的回波序列，错误的闭环会导致拓扑地图崩溃。该论文提出BatSLAM 2.0，一种基于序列验证的鲁棒位姿图声呐SLAM系统。"
keywords:
  - "echolocation"
score: 64.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7215078307"
  - name: "DOI"
    url: "https://doi.org/10.48550/arxiv.2609.40085"
previewImage: "/daily/2026-10-03/assets/openalex--W7215078307/preview.png"
---

## 核心内容

回声定位蝙蝠能利用声呐在黑暗杂乱空间中导航。十多年前BatSLAM展示了仿生双耳声呐机器人可通过识别接收声学信号中的位置构建拓扑地图，但声呐位置识别本质上是模糊的：走廊产生几乎相同的回波序列，错误的闭环会导致拓扑地图崩溃。该论文提出BatSLAM 2.0，一种基于序列验证的鲁棒位姿图声呐SLAM系统。

## 关键技术与数据

提出BatSLAM 2.0，核心创新为序列验证的声呐位置识别，通过验证候选闭环的声学序列一致性来拒绝错误闭环。将验证后的位置识别结果集成到鲁棒位姿图中，利用仿生双耳声呐进行纯声呐SLAM，在杂乱环境中构建拓扑地图。

## 结果与结论

BatSLAM 2.0通过序列验证机制有效抑制了错误闭环，避免了拓扑地图崩溃，在走廊等模糊环境中实现了鲁棒的声呐位置识别和SLAM。该系统为纯声呐SLAM提供了新方案，创新性地将序列验证引入声呐闭环检测，显著提升了拓扑地图的鲁棒性和一致性。

## 来源链接

- OpenAlex：https://openalex.org/W7215078307
- DOI：https://doi.org/10.48550/arxiv.2609.40085