---
candidateId: "arxiv--2609.35863-1"
category: "Paper"
date: "2026-09-30"
rank: 4
title: "Beyond Discrimination: Calibrated Geoprior Fusion for Bioacoustic Monitoring"
authors:
  - "Neha Sajja"
  - "Bart van Merriënboer"
  - "Burcu Karagol Ayan"
  - "Tom Denton"
research_direction: []
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "该论文针对现代生物声学基础模型（如Perch、BirdNET）虽判别精度高但置信度未校准、难以解释为真实出现概率的问题，提出校准地理先验融合方法。目标是将模型输出转化为可用于生态推断的校准概率，超越简单阈值检测。利用全球标注声学数据集WABAD生成校准先验，并可可选融入物种级信息，提升生态监测中的可靠性。"
keywords:
  - "detection"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2609.35863v1"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2609.35863v1"
previewImage: "/daily/2026-09-30/assets/arxiv--2609.35863-1/preview.png"
---

## 核心内容

该论文针对现代生物声学基础模型（如Perch、BirdNET）虽判别精度高但置信度未校准、难以解释为真实出现概率的问题，提出校准地理先验融合方法。目标是将模型输出转化为可用于生态推断的校准概率，超越简单阈值检测。利用全球标注声学数据集WABAD生成校准先验，并可可选融入物种级信息，提升生态监测中的可靠性。

## 关键技术与数据

关键技术包括校准先验构建、地理先验融合（Geoprior Fusion）与可选物种级信息融合。使用全球标注声学数据集WABAD生成校准先验。方法涉及对Perch、BirdNET等基础模型输出进行后处理校准，使其置信度更接近真实出现概率。摘要提及引入新方法，但未详述具体算法细节。

## 结果与结论

论文预期校准后的概率输出在生态推断中优于原始置信度，提升阈值检测之外的可用性。创新点在于利用WABAD构建校准先验并融合地理信息，增强模型输出的可解释性与生态有效性。结论表明该方法可推动生物声学监测从判别任务向概率化生态推断发展，具体校准指标需参见原文。

## 来源链接

- arXiv：http://arxiv.org/abs/2609.35863v1
- PDF：http://arxiv.org/pdf/2609.35863v1