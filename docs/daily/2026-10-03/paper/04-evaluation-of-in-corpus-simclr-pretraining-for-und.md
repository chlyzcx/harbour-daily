---
candidateId: "openalex--W7215044165"
category: "Paper"
date: "2026-10-03"
rank: 4
title: "Evaluation of In-Corpus SimCLR Pretraining for Underwater Acoustic Target Recognition Under Recording-Disjoint Splits"
authors:
  - "Hao Yuan"
  - "Wenbo Wang"
  - "Yu Chen"
  - "Guici Chen"
  - "Tian Li"
  - "Xinyu Wu"
research_direction:
  - "信号识别"
journal: "Preprints.org"
doi: "10.20944/preprints202609.0999.v3"
publication_year: 2026
summary: "标签稀缺限制了水下声目标识别（UATR），促使在大型无标签水听器档案上进行自监督学习，但当训练和测试录音不重叠时其收益尚不明确。该论文在录音不相交划分下，对语料内SimCLR预训练进行受控试点评估，使用来自Oceanship、QiandaoEar22和重建VTUAD训练分区的176,481个无标签log-mel片段，系统考察自监督预训练在录音不相交条件下的有效性。"
keywords:
  - "underwater acoustic target recognition"
score: 64.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7215044165"
  - name: "DOI"
    url: "https://doi.org/10.20944/preprints202609.0999.v3"
previewImage: "/daily/2026-10-03/assets/openalex--W7215044165/preview.svg"
---

## 核心内容

标签稀缺限制了水下声目标识别（UATR），促使在大型无标签水听器档案上进行自监督学习，但当训练和测试录音不重叠时其收益尚不明确。该论文在录音不相交划分下，对语料内SimCLR预训练进行受控试点评估，使用来自Oceanship、QiandaoEar22和重建VTUAD训练分区的176,481个无标签log-mel片段，系统考察自监督预训练在录音不相交条件下的有效性。

## 关键技术与数据

采用SimCLR自监督预训练方法，在176,481个无标签log-mel片段上训练ResNet-18编码器。在Oceanship、QiandaoEar22和重建VTUAD三个语料上，分别以录音不相交和片段不相交划分进行评估，对比预训练与从头训练的性能差异。

## 结果与结论

实验表明在录音不相交划分下，语料内SimCLR预训练的收益显著降低甚至消失，说明当训练和测试录音不重叠时，自监督学习的泛化优势有限。该发现对UATR中自监督学习的实际部署具有重要警示意义，指出需关注录音级数据泄漏问题，并探索跨录音泛化能力更强的预训练策略。

## 来源链接

- OpenAlex：https://openalex.org/W7215044165
- DOI：https://doi.org/10.20944/preprints202609.0999.v3