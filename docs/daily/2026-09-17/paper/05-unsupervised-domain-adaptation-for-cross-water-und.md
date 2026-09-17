---
candidateId: "openalex--W7213235209"
category: "Paper"
date: "2026-09-17"
rank: 5
title: "Unsupervised Domain Adaptation for Cross-Water Underwater Acoustic Target Recognition: A Four-Corpus Benchmark on Oceanship, QiandaoEar22, an AIS-Auto-Labeled VTUAD Reconstruction, and ShipsEar"
authors:
  - "Hao Yuan"
  - "Wenbo Wang"
  - "Xiwu Li"
  - "Guici Chen"
  - "Fan Huang"
  - "Bei Li"
research_direction:
  - "信号识别"
journal: "Preprints.org"
doi: "10.20944/preprints202609.1124.v1"
publication_year: 2026
summary: "水下声目标识别（UATR）模型跨水域迁移时性能急剧下降，无监督域适应（UDA）是目标水域无标签时的标准补救措施。本文在四个语料库（Oceanship、QiandaoEar22、AIS自动标注的VTUAD重建、ShipsEar）上对四种UDA范式进行基准测试，包括仅源训练、CORAL、多核MMD和域对抗训练（DANN、CDAN），并与监督目标Oracle对比。"
keywords:
  - "underwater acoustic target recognition"
score: 64.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7213235209"
  - name: "DOI"
    url: "https://doi.org/10.20944/preprints202609.1124.v1"
previewImage: "/daily/2026-09-17/assets/openalex--W7213235209/preview.svg"
---

## 核心内容

水下声目标识别（UATR）模型跨水域迁移时性能急剧下降，无监督域适应（UDA）是目标水域无标签时的标准补救措施。本文在四个语料库（Oceanship、QiandaoEar22、AIS自动标注的VTUAD重建、ShipsEar）上对四种UDA范式进行基准测试，包括仅源训练、CORAL、多核MMD和域对抗训练（DANN、CDAN），并与监督目标Oracle对比。

## 关键技术与数据

采用冻结的二分类协议，跨四个语料库；UDA方法包括CORAL、多核MMD、DANN、CDAN；评估指标为跨域识别准确率；数据集涵盖开放海洋、淡水湖、AIS自动标注和船舶噪声等多域数据。

## 结果与结论

实验表明，UDA方法能部分恢复跨水域性能，但均未达到监督Oracle水平；不同方法在不同语料库上表现差异显著，CORAL和DANN在某些场景下较优。研究揭示了跨水域UATR的域适应挑战，为后续方法选择提供了基准参考。

## 来源链接

- OpenAlex：https://openalex.org/W7213235209
- DOI：https://doi.org/10.20944/preprints202609.1124.v1