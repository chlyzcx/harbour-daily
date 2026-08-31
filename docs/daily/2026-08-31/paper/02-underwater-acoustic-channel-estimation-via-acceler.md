---
candidateId: "s2--0408a3509199d165c8d17a70c62e02bd641ee5ea"
category: "Paper"
date: "2026-08-31"
rank: 2
title: "Underwater Acoustic Channel Estimation via Accelerated TMSBL With KSVD-Based Denoising and Robust Initialization"
authors:
  - "Chuanxi Xing"
  - "Yiwen Hou"
  - "Yihan Meng"
  - "Tinglong Huang"
  - "Weiqiang Li"
  - "Minglinhan Hu"
research_direction:
  - "信道估计"
  - "OFDM"
journal: "IEEE Signal Processing Letters"
publisher: "Semantic Scholar"
doi: "10.1109/LSP.2025.3645580"
publication_year: 2026
summary: "该论文针对浅海环境中时间多重稀疏贝叶斯学习（TMSBL）算法复杂度高、对噪声敏感的问题，提出了一种鲁棒的信道估计方案。研究目标是提升浅海水声信道估计的精度与稳定性。论文通过级联去噪与稀疏初始化策略，在保持稀疏贝叶斯框架优势的同时，显著降低计算负担并增强抗噪能力。"
keywords:
  - "OFDM"
  - "channel estimation"
  - "ofdm"
  - "sparse"
  - "underwater acoustic channel estimation"
score: 64.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.1109/LSP.2025.3645580"
  - name: "Semantic Scholar"
    url: "https://www.semanticscholar.org/paper/0408a3509199d165c8d17a70c62e02bd641ee5ea"
previewImage: "/daily/2026-08-31/assets/s2--0408a3509199d165c8d17a70c62e02bd641ee5ea/preview.svg"
---

## 核心内容

该论文针对浅海环境中时间多重稀疏贝叶斯学习（TMSBL）算法复杂度高、对噪声敏感的问题，提出了一种鲁棒的信道估计方案。研究目标是提升浅海水声信道估计的精度与稳定性。论文通过级联去噪与稀疏初始化策略，在保持稀疏贝叶斯框架优势的同时，显著降低计算负担并增强抗噪能力。

## 关键技术与数据

论文采用K-奇异值分解（KSVD）算法对接收导频矩阵进行去噪预处理，利用其字典学习能力提取信号稀疏结构；随后采用分段正交匹配追踪（StOMP）算法获取鲁棒的稀疏先验，用于初始化TMSBL迭代框架。实验数据基于浅海多径信道仿真，对比了不同信噪比和导频配置下的估计性能。

## 结果与结论

实验结果表明，所提方案在信道估计精度上优于原始TMSBL及传统压缩感知方法，同时计算复杂度显著降低，尤其在低信噪比下表现出更强的鲁棒性。创新点在于将KSVD去噪与StOMP初始化有机结合，有效解决了TMSBL对初值敏感和噪声放大问题，为浅海水声信道估计提供了高效实用的解决方案。

## 来源链接

- DOI：https://doi.org/10.1109/LSP.2025.3645580
- Semantic Scholar：https://www.semanticscholar.org/paper/0408a3509199d165c8d17a70c62e02bd641ee5ea