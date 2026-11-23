---
candidateId: "openalex--W7237337774"
category: "Paper"
date: "2026-11-23"
rank: 2
title: "Single-point underwater acoustic transmission loss prediction via source–receiver–environment encoding and Attention-Driven Multi-scale feature aggregation"
authors:
  - "Hanchang Xu"
  - "Li Li"
  - "Ran Cao"
  - "Jikang Sun"
research_direction: []
journal: "Ocean Engineering"
publisher: "Elsevier BV"
doi: "10.1016/j.oceaneng.2026.129070"
publication_year: 2026
summary: "该论文面向水下声传播损失（TL）快速预测需求，提出一种基于“源—接收—环境”联合编码与注意力驱动多尺度特征聚合的单点传输损失预测方法。研究目标是仅利用单点收发配置与环境参数实现高精度TL估计，避免传统抛物方程或射线追踪方法的高计算开销。主要内容包括设计环境参数编码模块、多尺度特征提取网络及注意力融合机制，以捕捉声速剖面、海深、底质与距离等因素对传播损失的非线性影响。"
keywords: []
score: 65.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7237337774"
  - name: "DOI"
    url: "https://doi.org/10.1016/j.oceaneng.2026.129070"
previewImage: "/daily/2026-11-23/assets/openalex--W7237337774/preview.png"
---

## 核心内容

该论文面向水下声传播损失（TL）快速预测需求，提出一种基于“源—接收—环境”联合编码与注意力驱动多尺度特征聚合的单点传输损失预测方法。研究目标是仅利用单点收发配置与环境参数实现高精度TL估计，避免传统抛物方程或射线追踪方法的高计算开销。主要内容包括设计环境参数编码模块、多尺度特征提取网络及注意力融合机制，以捕捉声速剖面、海深、底质与距离等因素对传播损失的非线性影响。

## 关键技术与数据

关键技术包括源—接收—环境三元编码策略、多尺度卷积/特征金字塔结构以及注意力驱动的特征聚合模块，用于自适应加权不同尺度信息。方法上采用监督学习框架，输入为收发几何与环境参数，输出为对应频点的传输损失。数据集由水声传播模型仿真生成，覆盖多种声速剖面、海底类型、频率与距离组合，用于训练与测试模型泛化能力。

## 结果与结论

实验结果显示，该单点TL预测模型在测试集上取得较高精度，误差优于传统经验公式与单一尺度网络，且推理速度快、适合实时或大范围声场快速评估。结论表明，源—接收—环境联合编码与注意力多尺度聚合能有效提升单点传播损失预测的准确性与稳定性，为水声信道建模与声呐作用距离预估提供了高效数据驱动方案。

## 来源链接

- OpenAlex：https://openalex.org/W7237337774
- DOI：https://doi.org/10.1016/j.oceaneng.2026.129070