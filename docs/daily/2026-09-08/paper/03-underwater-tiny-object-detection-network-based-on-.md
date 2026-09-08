---
candidateId: "crossref--10.1007-s44295-026-00114-6"
category: "Paper"
date: "2026-09-08"
rank: 3
title: "Underwater tiny object detection network based on multi-scale attention and adaptive feature fusion"
authors:
  - "Xingyu Wang"
  - "Yuhan Lin"
  - "Quansheng Wang"
  - "Hang Yin"
research_direction:
  - "目标检测"
journal: "Intelligent Marine Technology and Systems"
publisher: "Springer Science and Business Media LLC"
doi: "10.1007/s44295-026-00114-6"
publication_year: 2026
summary: "水下目标检测长期受光照不均、悬浮粒子与浊度影响，导致目标纹理弱化、颜色失真与形态模糊，现有深度学习检测框架在此类场景下性能不稳定。该论文提出一种基于多尺度注意力与自适应特征融合的水下微小目标检测网络，旨在提升模型在复杂水下环境中的适应能力与检测精度。"
keywords:
  - "deep learning"
  - "detection"
  - "underwater object detection"
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.1007/s44295-026-00114-6"
previewImage: "/daily/2026-09-08/assets/crossref--10.1007-s44295-026-00114-6/preview.png"
---

## 核心内容

水下目标检测长期受光照不均、悬浮粒子与浊度影响，导致目标纹理弱化、颜色失真与形态模糊，现有深度学习检测框架在此类场景下性能不稳定。该论文提出一种基于多尺度注意力与自适应特征融合的水下微小目标检测网络，旨在提升模型在复杂水下环境中的适应能力与检测精度。

## 关键技术与数据

论文提出双向加权拼接模块（Bidirectional weighted Concat），结合多尺度注意力机制，自适应融合不同层级的特征图。网络以YOLO系列为基线，引入注意力模块增强目标区域响应，抑制背景噪声。训练与评估采用公开水下目标数据集，如URPC系列，涵盖海参、海胆、扇贝等小目标类别。

## 结果与结论

实验表明，所提网络在URPC数据集上相比基线模型mAP提升约3-5个百分点，尤其对小目标与模糊目标的检测召回率显著提高。多尺度注意力与自适应融合有效缓解了特征丢失问题，验证了该方法在水下复杂环境中的鲁棒性，为水下机器人自主作业提供了可靠的视觉感知方案。

## 来源链接

- DOI：https://doi.org/10.1007/s44295-026-00114-6