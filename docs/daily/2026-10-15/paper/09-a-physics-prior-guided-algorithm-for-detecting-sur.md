---
candidateId: "openalex--W7221134555"
category: "Paper"
date: "2026-10-15"
rank: 9
title: "A physics-prior-guided algorithm for detecting surface cracks in underwater bridge structures"
authors:
  - "Kaiwen Li"
  - "Shize Zhou"
  - "Shihao Li"
  - "Jia Lu"
  - "He Li"
research_direction: []
journal: "Results in Engineering"
publisher: "Elsevier BV"
doi: "10.1016/j.rineng.2026.113457"
publication_year: 2026
summary: "水下桥梁裂缝检测受水体光吸收与散射影响，图像存在色偏、光照不均、低对比度及复杂背景干扰，且标注样本稀缺。本文针对上述问题，提出一种物理先验引导的水下桥梁裂缝检测方法，将裂缝相关物理先验提取与SegFormer框架相融合，通过引入五种裂缝相关物理先验特征，提升模型在退化水下光学图像中的裂缝辨识能力，实现水下桥梁结构表面裂缝的自动检测。"
keywords:
  - "detection"
score: 55.2
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7221134555"
  - name: "DOI"
    url: "https://doi.org/10.1016/j.rineng.2026.113457"
previewImage: "/daily/2026-10-15/assets/openalex--W7221134555/preview.png"
---

## 核心内容

水下桥梁裂缝检测受水体光吸收与散射影响，图像存在色偏、光照不均、低对比度及复杂背景干扰，且标注样本稀缺。本文针对上述问题，提出一种物理先验引导的水下桥梁裂缝检测方法，将裂缝相关物理先验提取与SegFormer框架相融合，通过引入五种裂缝相关物理先验特征，提升模型在退化水下光学图像中的裂缝辨识能力，实现水下桥梁结构表面裂缝的自动检测。

## 关键技术与数据

方法以SegFormer为骨干分割网络，融合裂缝相关物理先验引导模块，提取五种与裂缝几何及灰度分布相关的先验特征，将其嵌入编码器或解码器以增强裂缝区域响应。针对水下标注样本稀缺问题，采用物理先验约束降低对大规模标注数据的依赖。摘要未完整给出具体数据集名称、样本量及训练细节，需查阅全文确认。

## 结果与结论

摘要未完整披露定量实验结果与性能指标。结论表明，将裂缝物理先验与SegFormer结合可有效应对水下图像退化与样本不足问题，提升水下桥梁裂缝检测的鲁棒性与准确性。创新点在于提出物理先验引导的检测算法，将裂缝相关物理特征与Transformer分割框架融合，为水下结构裂缝检测提供新思路。

## 来源链接

- OpenAlex：https://openalex.org/W7221134555
- DOI：https://doi.org/10.1016/j.rineng.2026.113457