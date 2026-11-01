---
candidateId: "openalex--W7224844184"
category: "Paper"
date: "2026-11-01"
rank: 10
title: "Universal Short-Time Fourier Transform: Data-Adaptive Window-Length Selection for Time-Frequency Analysis"
authors:
  - "Manan Mittal"
  - "Kanad Sarkar"
  - "Ryan M. Corey"
  - "John R. Buck"
  - "Andrew C. Singer"
research_direction: []
journal: "arXiv (Cornell University)"
publisher: "Cornell University"
doi: "10.48550/arxiv.2610.37795"
publication_year: 2026
summary: "针对短时傅里叶变换（STFT）中时间分辨率与频率分辨率固有折衷的问题，该论文提出通用短时傅里叶变换（U-STFT），实现数据自适应的窗长选择。研究目标是使STFT能够根据信号局部特性自动选择最优分析窗长，从而同时兼顾瞬态信号的时间定位与密集谐波的频率分辨。论文构建了窗长自适应选择机制，在时频分析中动态平衡时间与频率分辨率。"
keywords:
  - "time-varying"
  - "tracking"
score: 55.2
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7224844184"
  - name: "DOI"
    url: "https://doi.org/10.48550/arxiv.2610.37795"
previewImage: "/daily/2026-11-01/assets/openalex--W7224844184/preview.png"
---

## 核心内容

针对短时傅里叶变换（STFT）中时间分辨率与频率分辨率固有折衷的问题，该论文提出通用短时傅里叶变换（U-STFT），实现数据自适应的窗长选择。研究目标是使STFT能够根据信号局部特性自动选择最优分析窗长，从而同时兼顾瞬态信号的时间定位与密集谐波的频率分辨。论文构建了窗长自适应选择机制，在时频分析中动态平衡时间与频率分辨率。

## 关键技术与数据

关键技术包括STFT、数据自适应窗长选择、时频分辨率折衷分析。方法上通过信号局部特征驱动窗长选择，使分析窗能够随信号非平稳性自适应调整，从而在瞬态与谐波成分共存时获得更优的时频表征。数据方面基于时变信号开展方法验证，具体数据集因摘要截断未完整列出。

## 结果与结论

研究表明U-STFT能够根据信号局部特性自适应选择窗长，有效缓解了固定窗长STFT在时间分辨率与频率分辨率之间的折衷限制。结论指出数据自适应窗长选择提升了时频分析对瞬态与密集谐波共存信号的表征能力，为水声等非平稳信号的时频处理提供了通用改进框架。具体性能指标因摘要截断未完整列出。

## 来源链接

- OpenAlex：https://openalex.org/W7224844184
- DOI：https://doi.org/10.48550/arxiv.2610.37795