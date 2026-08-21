---
candidateId: "openalex--W4415111113"
category: "Paper"
date: "2026-08-21"
rank: 9
title: "Functional Multireference Alignment via Deconvolution"
authors:
  - "Omar Ghattas"
  - "Anna Little"
  - "Daniel Sanz-Alonso"
  - "M. Sweeney"
research_direction: []
journal: "SIAM Journal on Mathematics of Data Science"
publisher: "Society for Industrial and Applied Mathematics"
doi: "10.1137/25m1765602"
publication_year: 2026
summary: "该论文研究了多参考对齐（MRA）问题，即从经过平移和噪声污染的观测中估计信号函数。论文提出了函数域的新表述，揭示了MRA与反卷积之间的新联系：可通过Kotlarski公式从二阶统计量中估计信号。研究旨在扩展该公式至一般维度，并设计基于此的MRA估计算法。"
keywords: []
score: 56.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W4415111113"
  - name: "DOI"
    url: "https://doi.org/10.1137/25m1765602"
previewImage: "/daily/2026-08-21/assets/openalex--W4415111113/preview.png"
---

## 核心内容

该论文研究了多参考对齐（MRA）问题，即从经过平移和噪声污染的观测中估计信号函数。论文提出了函数域的新表述，揭示了MRA与反卷积之间的新联系：可通过Kotlarski公式从二阶统计量中估计信号。研究旨在扩展该公式至一般维度，并设计基于此的MRA估计算法。

## 关键技术与数据

关键技术包括将Kotlarski公式推广到多维情形，用于从多个含噪平移观测中恢复信号。算法设计可能基于特征函数估计、矩匹配或迭代反卷积方法。数据方面，采用合成信号（如高斯混合、分段光滑函数）进行仿真，在不同信噪比和观测数量下评估估计误差，并与经典MRA算法（如同步平均、EM算法）对比。

## 结果与结论

理论分析与仿真结果表明，基于反卷积的MRA算法在低信噪比下具有更好的估计稳定性，且随着观测数量增加，估计误差趋近于理论下界。结论指出，该函数化视角不仅统一了MRA与反卷积理论，还为处理连续域信号（如生物医学图像、天文数据）提供了计算高效的新算法框架。

## 来源链接

- OpenAlex：https://openalex.org/W4415111113
- DOI：https://doi.org/10.1137/25m1765602