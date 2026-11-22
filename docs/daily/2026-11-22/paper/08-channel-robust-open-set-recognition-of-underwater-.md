---
candidateId: "openalex--W7237174717"
category: "Paper"
date: "2026-11-22"
rank: 8
title: "Channel-Robust Open-Set Recognition of Underwater Acoustic Targets via Supervised Contrastive Learning and Multi-Measure Fusion"
authors:
  - "Zhijian Li"
  - "Yining Liu"
  - "Lingji Xu"
  - "Hongtao Wen"
  - "Xiaodi Wu"
  - "Yushen Wu"
research_direction: []
journal: "Journal of Marine Science and Engineering"
publisher: "Multidisciplinary Digital Publishing Institute"
doi: "10.3390/jmse14222206"
publication_year: 2026
summary: "该论文研究未知目标类别与传播信道失配同时存在时舰船辐射噪声的开集识别问题。提出一种结合监督对比学习与多测度融合的框架：在成对信道视图上进行监督对比训练，并设计Fused8逻辑回归门控器，融合分类器logits与四种导出统计量用于未知类拒识，在ShipsEar数据集上采用记录不重叠的五折协议评估。"
keywords: []
score: 56.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7237174717"
  - name: "DOI"
    url: "https://doi.org/10.3390/jmse14222206"
previewImage: "/daily/2026-11-22/assets/openalex--W7237174717/preview.png"
---

## 核心内容

该论文研究未知目标类别与传播信道失配同时存在时舰船辐射噪声的开集识别问题。提出一种结合监督对比学习与多测度融合的框架：在成对信道视图上进行监督对比训练，并设计Fused8逻辑回归门控器，融合分类器logits与四种导出统计量用于未知类拒识，在ShipsEar数据集上采用记录不重叠的五折协议评估。

## 关键技术与数据

关键技术包括成对信道视图的监督对比学习训练策略，以增强特征对信道变化的鲁棒性；Fused8门控器基于逻辑回归融合分类器logits与四种派生统计量实现未知目标拒识。数据集为ShipsEar舰船辐射噪声数据集，评估协议为记录不重叠的五折交叉验证，确保训练与测试记录无重叠，模拟信道失配与开集条件。

## 结果与结论

采用成对视图训练后，Fused8在ShipsEar数据集上取得总体准确率提升（摘要截断未给出完整数值），表明监督对比学习与多测度融合相结合可有效应对信道失配下的开集识别挑战。创新点在于将信道鲁棒表征学习与统计量融合的未知拒识机制统一于一个框架，提升了复杂水声信道下舰船目标开集识别的可靠性。

## 来源链接

- OpenAlex：https://openalex.org/W7237174717
- DOI：https://doi.org/10.3390/jmse14222206