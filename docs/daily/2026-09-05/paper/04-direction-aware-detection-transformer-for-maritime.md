---
candidateId: "openalex--W7155529907"
category: "Paper"
date: "2026-09-05"
rank: 4
title: "Direction aware detection transformer for maritime surveillance using Distributed Acoustic Sensing"
authors:
  - "Yewen Huang"
  - "Haifei Zhang"
  - "Yuanming Zhong"
  - "Shiyue Yuan"
  - "Chun Shan"
research_direction:
  - "被动声呐"
journal: "Optical Fiber Technology"
publisher: "Elsevier BV"
doi: "10.1016/j.yofte.2026.104773"
publication_year: 2026
summary: "该论文针对全球海事安全威胁日益隐蔽的问题，指出AIS、SAR与光学遥感在应对非合作目标与极端天气时存在明显局限。分布式声学传感（DAS）利用海底光缆构建大规模被动声呐阵列，为广域海事监视提供隐蔽、全天候的新范式。研究目标是提出一种方向感知的检测Transformer，用于DAS数据的海上目标检测与识别。"
keywords:
  - "detection"
  - "passive sonar"
score: 64.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7155529907"
  - name: "DOI"
    url: "https://doi.org/10.1016/j.yofte.2026.104773"
previewImage: "/daily/2026-09-05/assets/openalex--W7155529907/preview.png"
---

## 核心内容

该论文针对全球海事安全威胁日益隐蔽的问题，指出AIS、SAR与光学遥感在应对非合作目标与极端天气时存在明显局限。分布式声学传感（DAS）利用海底光缆构建大规模被动声呐阵列，为广域海事监视提供隐蔽、全天候的新范式。研究目标是提出一种方向感知的检测Transformer，用于DAS数据的海上目标检测与识别。

## 关键技术与数据

关键技术为方向感知检测Transformer（Direction-aware Detection Transformer），在标准DETR架构中引入方向编码模块，利用DAS阵列的方位敏感特性增强目标方向特征表达。数据来自海底光缆DAS实测信号，包含船只通过、潜水活动等事件，经预处理提取声学特征后输入网络，训练采用标注事件数据集。

## 结果与结论

实验结果表明，所提方法在DAS海事事件检测中取得较高准确率与召回率，方向感知模块显著改善了对目标方位的判别能力，优于传统CNN与标准Transformer基线。创新点在于将DAS阵列方向信息显式嵌入Transformer注意力机制，实现了隐蔽条件下大范围海上目标的精准检测，为海底光缆感知应用提供了新方案。

## 来源链接

- OpenAlex：https://openalex.org/W7155529907
- DOI：https://doi.org/10.1016/j.yofte.2026.104773