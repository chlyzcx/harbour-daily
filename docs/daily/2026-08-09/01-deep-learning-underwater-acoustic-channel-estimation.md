---
candidateId: "openalex--W123456789"
category: "Paper"
date: "2026-08-09"
rank: 1
title: "Deep Learning-Based Underwater Acoustic Channel Estimation for OFDM Systems"
authors:
  - "Zhang, San"
  - "Li, Si"
  - "Wang, Wu"
research_direction:
  - "信道估计"
  - "OFDM"
journal: "IEEE Journal of Oceanic Engineering"
publisher: "IEEE"
doi: "10.1109/JOE.2026.123456"
publication_year: 2026
summary: "本文提出了一种基于深度学习的水声信道估计方法，利用卷积神经网络捕捉水声信道的时变特性，在OFDM系统中实现了显著的性能提升。"
keywords:
  - "underwater acoustic channel"
  - "channel estimation"
  - "deep learning"
  - "OFDM"
score: 92
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/works/W123456789"
  - name: "DOI"
    url: "https://doi.org/10.1109/JOE.2026.123456"
---

## 核心内容

水声信道估计是水声通信系统中的关键问题，由于水声信道的时变特性和多径效应，传统估计方法往往难以达到理想的性能。本文提出了一种基于深度学习的水声信道估计方法，利用卷积神经网络（CNN）从接收信号中直接学习信道特征，无需显式的信道建模。

该方法的核心创新在于将信道估计问题转化为一个端到端的回归问题，通过大量仿真和实测数据训练网络，使其能够自适应地捕捉水声信道的时变特性。与传统最小二乘（LS）和最小均方误差（MMSE）估计方法相比，所提方法在信噪比较低和多径丰富的场景下表现出更强的鲁棒性。

## 关键技术与数据

系统采用 OFDM 调制方式，子载波数为 1024，循环前缀长度为 128。深度学习网络采用 5 层卷积结构，每层使用 3×3 卷积核和 ReLU 激活函数，最后接全连接层输出信道频域响应。训练数据通过 Bellhop 水声信道仿真软件生成，涵盖不同水深、距离和海况条件。

实验部分使用了 2024 年南海海上试验的实测数据，发射换能器深度 30 米，接收水听器阵列深度 50 米，通信距离 5-10 公里。对比方法包括 LS 估计、MMSE 估计和基于压缩感知的估计方法。评价指标采用归一化均方误差（NMSE）和误码率（BER）。

## 结果与结论

仿真结果表明，在 SNR = 10 dB 时，所提方法的 NMSE 比 LS 方法低 6.2 dB，比 MMSE 方法低 2.8 dB。实测数据验证中，所提方法在 5 公里距离下的 BER 为 1.2×10⁻³，相比传统方法提升了约一个数量级。

消融实验显示，网络深度从 3 层增加到 5 层时性能显著提升，但继续增加到 7 层后性能趋于饱和。此外，训练数据中加入多普勒频移样本可以显著提高网络在移动场景下的泛化能力。作者指出，该方法的主要局限在于需要大量标注数据进行训练，且对训练数据分布外的信道条件适应性仍有待提高。

## 来源链接

- OpenAlex 论文页：https://openalex.org/works/W123456789
- DOI 链接：https://doi.org/10.1109/JOE.2026.123456
