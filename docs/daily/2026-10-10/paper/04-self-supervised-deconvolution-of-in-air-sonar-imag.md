---
candidateId: "openalex--W7221047600"
category: "Paper"
date: "2026-10-10"
rank: 4
title: "Self-Supervised Deconvolution of In-Air Sonar Images Using Sensor Ego-Motion"
authors:
  - "Jan Steckel"
research_direction: []
journal: "arXiv (Cornell University)"
publisher: "Cornell University"
doi: "10.48550/arxiv.2610.09682"
publication_year: 2026
summary: "该论文针对空中声纳图像去卷积问题，提出了一种利用传感器自运动的自监督去卷积方法。研究背景在于宽带空中声纳传感器通过延迟求和波束形成成像时存在高旁瓣和角度分辨率下降的问题，而去卷积需要精确的点扩散函数，实际中难以校准。论文目标是实现无需标定点扩散函数的自监督声纳图像去卷积。"
keywords:
  - "beamforming"
  - "sparse"
score: 56.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7221047600"
  - name: "DOI"
    url: "https://doi.org/10.48550/arxiv.2610.09682"
previewImage: "/daily/2026-10-10/assets/openalex--W7221047600/preview.png"
---

## 核心内容

该论文针对空中声纳图像去卷积问题，提出了一种利用传感器自运动的自监督去卷积方法。研究背景在于宽带空中声纳传感器通过延迟求和波束形成成像时存在高旁瓣和角度分辨率下降的问题，而去卷积需要精确的点扩散函数，实际中难以校准。论文目标是实现无需标定点扩散函数的自监督声纳图像去卷积。

## 关键技术与数据

关键技术包括：自监督学习框架，利用传感器自运动信息构建训练信号；去卷积方法，用于抑制旁瓣并提升角度分辨率；点扩散函数估计，通过自监督方式隐式学习成像链特性。数据方面基于空中声纳传感器采集的实测图像数据进行验证。

## 结果与结论

实验结果表明，所提自监督去卷积方法能够有效抑制旁瓣、提升图像角度分辨率，且无需显式校准点扩散函数，验证了利用传感器自运动进行自监督去卷积的可行性，为空中声纳图像质量提升提供了一种实用方法。

## 来源链接

- OpenAlex：https://openalex.org/W7221047600
- DOI：https://doi.org/10.48550/arxiv.2610.09682