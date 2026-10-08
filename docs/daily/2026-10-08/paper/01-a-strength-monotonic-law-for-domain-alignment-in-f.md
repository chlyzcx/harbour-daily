---
candidateId: "arxiv--2610.09737-1"
category: "Paper"
date: "2026-10-08"
rank: 1
title: "A Strength-Monotonic Law for Domain Alignment in Frozen-Embedding Bioacoustic Classification"
authors:
  - "Yucheng Gong"
  - "Rui Zhou"
  - "Binbin Zeng"
  - "Qiang Ren"
  - "Hongjin Hui"
research_direction: []
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "该论文研究冻结基础模型嵌入在跨声学域生物声学分类中的域对齐问题，聚焦跨域蚊虫物种分类任务。作者提出“强度单调律”：编码器在目标任务上越强，其未见域泛化越依赖分布对齐（MMD）项，且越易受域重平衡采样损害。研究覆盖四种编码器家族及HuBERT层扫描，旨在揭示分布对齐与模型强度之间的规律性关系。"
keywords:
  - "classification"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2610.09737v1"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2610.09737v1"
previewImage: "/daily/2026-10-08/assets/arxiv--2610.09737-1/preview.png"
---

## 核心内容

该论文研究冻结基础模型嵌入在跨声学域生物声学分类中的域对齐问题，聚焦跨域蚊虫物种分类任务。作者提出“强度单调律”：编码器在目标任务上越强，其未见域泛化越依赖分布对齐（MMD）项，且越易受域重平衡采样损害。研究覆盖四种编码器家族及HuBERT层扫描，旨在揭示分布对齐与模型强度之间的规律性关系。

## 关键技术与数据

采用冻结基础模型嵌入与分布对齐（MMD）方法，结合域重平衡采样策略。实验涉及四种编码器家族，并对HuBERT进行层间扫描（n=8），以蚊虫物种声学分类为跨域任务，评估不同编码器强度下的域泛化性能。

## 结果与结论

发现强度单调律：编码器越强，MMD对齐项对未见域泛化越关键，而域重平衡采样反而有害。该规律在多种编码器及HuBERT层间一致成立，为冻结嵌入生物声学分类中的域适应策略选择提供了理论依据与实证支持。

## 来源链接

- arXiv：http://arxiv.org/abs/2610.09737v1
- PDF：http://arxiv.org/pdf/2610.09737v1