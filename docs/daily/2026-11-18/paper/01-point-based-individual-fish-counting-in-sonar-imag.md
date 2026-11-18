---
candidateId: "openalex--W7234603680"
category: "Paper"
date: "2026-11-18"
rank: 1
title: "Point-based individual fish counting in sonar images using dual-stream feature subtraction and multi-scale fusion"
authors:
  - "Mingrui Kong"
  - "Hongyu Pan"
  - "Chenlong Li"
  - "Lan Huang"
  - "Qingling Duan"
research_direction: []
journal: "Ocean Engineering"
publisher: "Elsevier BV"
doi: "10.1016/j.oceaneng.2026.129488"
publication_year: 2026
summary: "该论文针对声呐图像中鱼类个体计数问题，提出基于点标注的计数方法。传统声呐图像鱼群计数常受目标重叠、回波微弱和背景噪声干扰，难以实现个体级精确计数。论文旨在利用深度学习框架，从声呐图像中直接回归鱼体目标点，实现无需边界框标注的轻量化个体计数，为渔业资源声学评估提供新手段。"
keywords: []
score: 65.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7234603680"
  - name: "DOI"
    url: "https://doi.org/10.1016/j.oceaneng.2026.129488"
previewImage: "/daily/2026-11-18/assets/openalex--W7234603680/preview.png"
---

## 核心内容

该论文针对声呐图像中鱼类个体计数问题，提出基于点标注的计数方法。传统声呐图像鱼群计数常受目标重叠、回波微弱和背景噪声干扰，难以实现个体级精确计数。论文旨在利用深度学习框架，从声呐图像中直接回归鱼体目标点，实现无需边界框标注的轻量化个体计数，为渔业资源声学评估提供新手段。

## 关键技术与数据

采用双流特征相减模块抑制静态背景混响，突出运动鱼体回波；引入多尺度融合结构聚合不同感受野下的鱼体特征，提升小目标与密集目标响应；以点标注真值训练计数网络，输出鱼体中心点热力图并积分得到计数。数据为实测声呐图像序列，经人工点标注构建训练与测试集。

## 结果与结论

实验表明双流相减与多尺度融合可有效抑制背景干扰并改善密集鱼群计数精度，计数误差较基线网络下降，验证了点监督范式在声呐图像个体计数中的可行性。创新点在于将特征相减思想引入声呐鱼群计数，兼顾轻量标注与多尺度目标适应能力。

## 来源链接

- OpenAlex：https://openalex.org/W7234603680
- DOI：https://doi.org/10.1016/j.oceaneng.2026.129488