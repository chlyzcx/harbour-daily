---
candidateId: "arxiv--2610.39371-1"
category: "Paper"
date: "2026-10-30"
rank: 4
title: "Lightweight Underwater Acoustic Vessel Classification for Embedded Deployment"
authors:
  - "Abishek Soti"
  - "Thura Pyae Sone"
  - "Naqib Ibnul"
  - "Jim Huang"
  - "Sergio Chevtchenko"
  - "Henry Zhong"
  - "Gregory Cohen"
  - "Ying Xu"
research_direction: []
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "该论文面向近海声学监视中连接、带宽与功率受限的边缘部署场景，提出基于树莓派的轻量级水下目标（船舶）分类系统。利用ShipsEar数据集，在树莓派5上构建从音频到预测的完整流水线，比较六种分类器的分类性能与资源开销，旨在实现嵌入式平台上的高效水下船舶分类。"
keywords:
  - "classification"
  - "neural network"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2610.39371v1"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2610.39371v1"
previewImage: "/daily/2026-10-30/assets/arxiv--2610.39371-1/preview.png"
---

## 核心内容

该论文面向近海声学监视中连接、带宽与功率受限的边缘部署场景，提出基于树莓派的轻量级水下目标（船舶）分类系统。利用ShipsEar数据集，在树莓派5上构建从音频到预测的完整流水线，比较六种分类器的分类性能与资源开销，旨在实现嵌入式平台上的高效水下船舶分类。

## 关键技术与数据

使用ShipsEar水声船舶辐射噪声数据集；构建音频预处理与特征提取流水线，比较六种分类器；评估声学特征选择、统计池化与Transformer模式等辅助实验；在树莓派5上测量处理时延、CPU占用、内存消耗与功耗。

## 结果与结论

论文给出六种分类器在树莓派5上的分类性能与资源消耗对比，揭示精度与延迟/功耗间的权衡；辅助实验表明特征选择与池化策略对嵌入式性能有显著影响。结论支持在受限边缘设备上实现轻量水声船舶分类的可行性。创新点在于面向嵌入式部署的系统级性能—资源联合评估。

## 来源链接

- arXiv：http://arxiv.org/abs/2610.39371v1
- PDF：http://arxiv.org/pdf/2610.39371v1