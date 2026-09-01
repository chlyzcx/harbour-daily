---
candidateId: "crossref--10.1016-j.oceaneng.2026.127523"
category: "Paper"
date: "2026-09-01"
rank: 5
title: "Wave height prediction for underwater vehicles based on a bayesian-optimized U-shaped hybrid neural network"
authors:
  - "Yonghao Wang"
  - "Junpeng Zhu"
  - "Chunyu Guo"
  - "Yang Han"
  - "Shihao Wang"
  - "Guanjun Liang"
research_direction: []
journal: "Ocean Engineering"
publisher: "Elsevier BV"
doi: "10.1016/j.oceaneng.2026.127523"
publication_year: 2026
summary: "针对水下航行器作业中波浪高度预测的需求，本文提出一种基于贝叶斯优化的U型混合神经网络模型。波浪高度直接影响水下航行器的稳定性和安全性，准确预测对路径规划与姿态控制至关重要。传统数值预报方法计算量大，而单一神经网络模型难以捕捉波浪的时空非线性特征。本文构建U型混合架构并结合贝叶斯优化进行超参数调优。"
keywords:
  - "neural network"
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.1016/j.oceaneng.2026.127523"
previewImage: "/daily/2026-09-01/assets/crossref--10.1016-j.oceaneng.2026.127523/preview.png"
---

## 核心内容

针对水下航行器作业中波浪高度预测的需求，本文提出一种基于贝叶斯优化的U型混合神经网络模型。波浪高度直接影响水下航行器的稳定性和安全性，准确预测对路径规划与姿态控制至关重要。传统数值预报方法计算量大，而单一神经网络模型难以捕捉波浪的时空非线性特征。本文构建U型混合架构并结合贝叶斯优化进行超参数调优。

## 关键技术与数据

核心技术为U型混合神经网络，结合卷积神经网络（CNN）提取空间特征和长短期记忆网络（LSTM）或Transformer捕捉时间依赖，形成编码器-解码器结构。贝叶斯优化用于自动搜索网络深度、卷积核尺寸、学习率等超参数。数据来源于浮标实测波浪数据和再分析气象数据，评估了不同预测时域下的均方根误差和相关系数。

## 结果与结论

实验结果显示，所提模型在短期波浪预测中精度优于单一CNN或LSTM模型，均方根误差降低约20%，且贝叶斯优化显著减少了调参时间。创新点在于U型混合架构与贝叶斯优化的结合，为水下航行器作业环境感知提供了高精度预测工具。

## 来源链接

- DOI：https://doi.org/10.1016/j.oceaneng.2026.127523