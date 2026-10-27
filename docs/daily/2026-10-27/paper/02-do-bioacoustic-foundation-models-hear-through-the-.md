---
candidateId: "arxiv--2610.33068-1"
category: "Paper"
date: "2026-10-27"
rank: 2
title: "Do bioacoustic foundation models hear through the noise ? SNR and generalization in underwater detection"
authors:
  - "Lucie Jean-Labadye"
  - "Nicolas Farrugia"
  - "Axel Marmoret"
  - "Dorian Cazau"
  - "Olivier Adam"
research_direction: []
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "针对生物声学基础模型声称可跨类群和录音条件泛化、但主要基于陆生高质量聚焦录音训练并在偏重架构的基准上评估的问题，本文在水下检测任务上系统评估了四类生物声学基础模型的泛化能力。研究利用Kerguelen高原连续录音数据，以冻结编码器加线性探测的方式，考察模型在不同信噪比条件下的检测性能，揭示数据条件对模型泛化的影响。"
keywords:
  - "detection"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2610.33068v1"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2610.33068v1"
previewImage: "/daily/2026-10-27/assets/arxiv--2610.33068-1/preview.png"
---

## 核心内容

针对生物声学基础模型声称可跨类群和录音条件泛化、但主要基于陆生高质量聚焦录音训练并在偏重架构的基准上评估的问题，本文在水下检测任务上系统评估了四类生物声学基础模型的泛化能力。研究利用Kerguelen高原连续录音数据，以冻结编码器加线性探测的方式，考察模型在不同信噪比条件下的检测性能，揭示数据条件对模型泛化的影响。

## 关键技术与数据

采用四种生物声学基础模型作为冻结特征编码器，在下游水下检测任务上进行线性探测（linear probing）。构建四个规模相同、仅信噪比（SNR）不同的数据集，以隔离信噪比因素对性能的影响。数据来源为Kerguelen高原的连续水声录音，评估聚焦于模型在真实噪声条件下的检测泛化表现。

## 结果与结论

实验揭示了基础模型在水下检测任务中随信噪比下降的性能退化规律，表明模型泛化能力受数据条件显著制约，挑战了其跨域泛化的宣称。研究强调了评估中数据条件控制的重要性，为生物声学基础模型在水声场景的适用性提供了实证依据，创新点在于以信噪比为控制变量系统检验基础模型的噪声鲁棒性与泛化边界。

## 来源链接

- arXiv：http://arxiv.org/abs/2610.33068v1
- PDF：http://arxiv.org/pdf/2610.33068v1