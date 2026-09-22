---
candidateId: "crossref--10.20944-preprints202609.1126.v2"
category: "Paper"
date: "2026-09-22"
rank: 2
title: "Source-Free Domain Adaptation for Underwater Acoustic Target Recognition: A Strong Batch-Normalization Statistics Baseline Under Cross-Water-Area Shift"
authors:
  - "Hao Yuan"
  - "Wenbo Wang"
  - "Fan Huang"
  - "Guici Chen"
  - "Xiwu Li"
  - "Fanyu Wang"
research_direction:
  - "信号识别"
journal: "Unknown"
publisher: "MDPI AG"
doi: "10.20944/preprints202609.1126.v2"
publication_year: 2026
summary: "该论文针对跨水域迁移导致水声目标识别（UATR）模型性能严重退化的问题，研究无源域数据的域自适应方法。传统无监督域自适应需要源域录音数据，但实际部署中源数据往往不可用。论文在Oceanship–QiandaoEar22两类协议上评估了无源域、无目标标签的自适应方法，旨在建立一种基于批归一化（BN）统计量的强基线，为跨水域UATR部署提供实用解决方案。"
keywords:
  - "underwater acoustic target recognition"
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.20944/preprints202609.1126.v2"
previewImage: "/daily/2026-09-22/assets/crossref--10.20944-preprints202609.1126.v2/preview.svg"
---

## 核心内容

该论文针对跨水域迁移导致水声目标识别（UATR）模型性能严重退化的问题，研究无源域数据的域自适应方法。传统无监督域自适应需要源域录音数据，但实际部署中源数据往往不可用。论文在Oceanship–QiandaoEar22两类协议上评估了无源域、无目标标签的自适应方法，旨在建立一种基于批归一化（BN）统计量的强基线，为跨水域UATR部署提供实用解决方案。

## 关键技术与数据

核心技术为基于批归一化运行统计量的无源域自适应方法，利用目标域数据更新BN层的均值和方差统计量，无需源域录音和目标标签。采用两个独立的五种子批次（共十个匹配源检查点）进行实验，数据集为Oceanship和QiandaoEar22，构建两类识别协议并在双向迁移方向上评估。对比方法包括BN统计量自适应与其他无源域自适应策略。

## 结果与结论

实验表明，基于BN统计量的简单基线在跨水域迁移场景下取得了具有竞争力的识别性能，显著优于未自适应模型。双向迁移结果验证了方法的鲁棒性，十个匹配检查点的统计结果增强了结论可靠性。创新点在于提出了一种无需源数据、无需目标标签的实用基线方法，为水声目标识别在实际跨水域部署中提供了低成本的域自适应方案。

## 来源链接

- DOI：https://doi.org/10.20944/preprints202609.1126.v2