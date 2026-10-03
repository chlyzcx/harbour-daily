---
candidateId: "openalex--W7215033457"
category: "Paper"
date: "2026-10-03"
rank: 5
title: "Cross-Water Acoustic Domain Adaptation Is Direction-Dependent: A Four-Corpus UDA Benchmark with Negative Transfer"
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
doi: "10.20944/preprints202609.1124.v3"
publication_year: 2026
summary: "在一个水域训练的UATR模型可能无法泛化到另一水域，当目标水域无标签时，无监督域适应（UDA）是标准补救手段。该论文在四个语料库上构建冻结二分类协议，基准测试三种UDA方法族，系统研究跨水域声学域适应的方向依赖性，并首次报告了负迁移现象，揭示了UDA在UATR中的适用边界。"
keywords:
  - "underwater acoustic target recognition"
score: 64.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7215033457"
  - name: "DOI"
    url: "https://doi.org/10.20944/preprints202609.1124.v3"
previewImage: "/daily/2026-10-03/assets/openalex--W7215033457/preview.svg"
---

## 核心内容

在一个水域训练的UATR模型可能无法泛化到另一水域，当目标水域无标签时，无监督域适应（UDA）是标准补救手段。该论文在四个语料库上构建冻结二分类协议，基准测试三种UDA方法族，系统研究跨水域声学域适应的方向依赖性，并首次报告了负迁移现象，揭示了UDA在UATR中的适用边界。

## 关键技术与数据

使用四个语料库：海洋语料Oceanship（乔治亚海峡）、淡水湖语料QiandaoEar22、AIS自动标注的VTUAD重建语料和近岸语料ShipsEar。基准测试三种UDA方法族：相关对齐（CORAL）等。采用冻结二分类协议，系统评估不同源-目标域组合下的适应性能，考察方向依赖性。

## 结果与结论

实验发现跨水域UDA性能具有显著方向依赖性，某些方向出现负迁移，即适应后性能反而低于未适应基线。该工作首次系统揭示了UATR中UDA的方向依赖性和负迁移风险，指出盲目应用UDA可能有害，为跨水域UATR部署提供了重要的实证依据和警示。

## 来源链接

- OpenAlex：https://openalex.org/W7215033457
- DOI：https://doi.org/10.20944/preprints202609.1124.v3