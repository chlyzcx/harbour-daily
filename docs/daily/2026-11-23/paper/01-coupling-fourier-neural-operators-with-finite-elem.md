---
candidateId: "openalex--W7202175379"
category: "Paper"
date: "2026-11-23"
rank: 1
title: "Coupling Fourier neural operators with finite-element guided graph refinement for ocean acoustic field prediction"
authors:
  - "Rui Xia"
  - "Huajian Zhang"
  - "H. Gao"
  - "Genglin Li"
  - "Xiao‐Wei Guo"
  - "Jie Liu"
research_direction: []
journal: "Ocean Engineering"
publisher: "Elsevier BV"
doi: "10.1016/j.oceaneng.2026.129518"
publication_year: 2026
summary: "该论文针对海洋声场预测这一水声工程核心问题，提出将傅里叶神经算子（FNO）与有限元引导的图细化方法相耦合的混合建模框架。研究目标是提升复杂海洋环境下声传播损失的预测精度与泛化能力，同时降低对大规模数值求解的依赖。主要内容包括构建FNO作为全局算子学习主干，并引入有限元网格信息指导图结构细化，以捕捉海底地形与声速剖面的局部突变特征，从而实现高效、高保真的声场重构与预测。"
keywords: []
score: 70.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7202175379"
  - name: "DOI"
    url: "https://doi.org/10.1016/j.oceaneng.2026.129518"
previewImage: "/daily/2026-11-23/assets/openalex--W7202175379/preview.png"
---

## 核心内容

该论文针对海洋声场预测这一水声工程核心问题，提出将傅里叶神经算子（FNO）与有限元引导的图细化方法相耦合的混合建模框架。研究目标是提升复杂海洋环境下声传播损失的预测精度与泛化能力，同时降低对大规模数值求解的依赖。主要内容包括构建FNO作为全局算子学习主干，并引入有限元网格信息指导图结构细化，以捕捉海底地形与声速剖面的局部突变特征，从而实现高效、高保真的声场重构与预测。

## 关键技术与数据

关键技术融合了傅里叶神经算子（在频域学习偏微分方程解算子）、有限元法（提供物理约束与网格先验）以及图神经网络细化模块（对非规则边界与界面进行局部修正）。方法上采用多尺度特征聚合与物理引导训练策略，数据来源于有限元求解器生成的海洋声场仿真样本，涵盖不同声速剖面、海底底质与边界条件，用于训练与验证耦合模型的预测性能。

## 结果与结论

实验表明，耦合FNO与有限元引导图细化的模型在声传播损失预测上优于纯数据驱动算子方法，尤其在强非均匀介质与复杂海底地形条件下误差显著降低，同时保持较低推理成本。结论指出，将数值方法的物理先验嵌入神经算子可有效提升海洋声场预测的准确性与鲁棒性，为水声环境快速建模与声呐性能评估提供了新途径。

## 来源链接

- OpenAlex：https://openalex.org/W7202175379
- DOI：https://doi.org/10.1016/j.oceaneng.2026.129518