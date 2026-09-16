---
candidateId: "arxiv--2609.16796-1"
category: "Paper"
date: "2026-09-16"
rank: 2
title: "Time-warping estimation via stationarity-based learning of the de-warped signal"
authors:
  - "Corentin Presvôts"
  - "Adrien Meynard"
research_direction: []
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "时间弯折估计是信号处理中的基础问题，应用于生物声学、雷达和生物医学分析。本文提出可训练时间弯折估计模型TWET，从单次观测中估计时间弯折函数。该方法将时间弯折估计建模为小波域中的平稳化问题，利用分层空洞卷积架构估计弯折函数，并引入可微分机制实现端到端训练。研究目标是提升非平稳信号中时间弯折估计的精度与鲁棒性。"
keywords: []
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2609.16796v1"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2609.16796v1"
previewImage: "/daily/2026-09-16/assets/arxiv--2609.16796-1/preview.png"
---

## 核心内容

时间弯折估计是信号处理中的基础问题，应用于生物声学、雷达和生物医学分析。本文提出可训练时间弯折估计模型TWET，从单次观测中估计时间弯折函数。该方法将时间弯折估计建模为小波域中的平稳化问题，利用分层空洞卷积架构估计弯折函数，并引入可微分机制实现端到端训练。研究目标是提升非平稳信号中时间弯折估计的精度与鲁棒性。

## 关键技术与数据

TWET采用小波变换将信号映射至时频域，通过分层空洞卷积网络捕捉多尺度依赖关系，估计使去弯折信号趋于平稳的弯折函数。关键组件包括可微分重采样、小波域平稳性度量及空洞卷积架构。训练数据可能为合成非平稳信号及生物声学、雷达等真实信号，通过监督学习优化弯折函数估计。方法强调单次观测下的泛化能力。

## 结果与结论

实验表明，TWET在合成与真实数据上均优于传统时间弯折估计方法，能准确恢复弯折函数并提升去弯折信号的平稳性。该模型为生物声学中的蝙蝠/鲸类呼叫分析、雷达目标微动特征提取及生物医学信号处理提供有效工具。创新点在于将时间弯折估计转化为可学习的小波域平稳化问题，并设计可微分端到端架构。

## 来源链接

- arXiv：http://arxiv.org/abs/2609.16796v1
- PDF：http://arxiv.org/pdf/2609.16796v1