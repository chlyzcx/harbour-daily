---
candidateId: "openalex--W7213544396"
category: "Paper"
date: "2026-09-19"
rank: 1
title: "A Preconditioned Krylov Iterative Solver for the Spectrally Discretized Underwater Acoustic Parabolic Equation"
authors:
  - "Zihao Deng"
  - "Yongxian Wang"
  - "Houwang Tu"
research_direction:
  - "声传播建模"
journal: "Chinese Physics B"
publisher: "IOP Publishing"
doi: "10.1088/1674-1056/aea96a"
publication_year: 2026
summary: "水声抛物方程谱离散模型能提供高精度数值解，但其全局离散策略产生非对称、局部稠密的块结构系统，界面与边界耦合稀疏，给直接求解器带来计算与内存瓶颈。本文针对该问题，提出一种基于预处理Krylov子空间迭代的高效求解器，旨在突破传统直接法在大规模水声传播计算中的可扩展性限制，实现谱离散抛物方程模型的快速数值求解。"
keywords:
  - "parabolic equation"
  - "sparse"
score: 66.0
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7213544396"
  - name: "DOI"
    url: "https://doi.org/10.1088/1674-1056/aea96a"
previewImage: "/daily/2026-09-19/assets/openalex--W7213544396/preview.svg"
---

## 核心内容

水声抛物方程谱离散模型能提供高精度数值解，但其全局离散策略产生非对称、局部稠密的块结构系统，界面与边界耦合稀疏，给直接求解器带来计算与内存瓶颈。本文针对该问题，提出一种基于预处理Krylov子空间迭代的高效求解器，旨在突破传统直接法在大规模水声传播计算中的可扩展性限制，实现谱离散抛物方程模型的快速数值求解。

## 关键技术与数据

关键技术为预处理Krylov子空间迭代方法，针对谱离散抛物方程产生的非对称局部稠密块结构系统设计专用预条件子，利用界面和边界耦合的稀疏性降低计算复杂度。采用迭代求解替代直接求解以缓解内存瓶颈。摘要未提及具体数据集，推测以标准水声传播算例进行数值验证。

## 结果与结论

摘要信息不完整，未给出具体实验数据与性能指标。可推断该求解器在保持谱离散高精度的同时显著降低计算与内存开销，提升大规模水声传播问题的求解效率，为抛物方程模型的实际应用提供可扩展的迭代求解方案，创新点在于将预处理Krylov方法适配于谱离散抛物方程的特殊块结构系统。

## 来源链接

- OpenAlex：https://openalex.org/W7213544396
- DOI：https://doi.org/10.1088/1674-1056/aea96a