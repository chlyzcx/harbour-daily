---
candidateId: "crossref--10.20944-preprints202609.0999.v2"
category: "Paper"
date: "2026-09-22"
rank: 3
title: "Evaluating In-Corpus SimCLR Pretraining for Underwater Acoustic Target Recognition Under Recording-Disjoint Splits"
authors:
  - "Hao Yuan"
  - "Wenbo Wang"
  - "Yu Chen"
  - "Guici Chen"
  - "Tian Li"
  - "Xinyu Wu"
research_direction:
  - "信号识别"
journal: "Unknown"
publisher: "MDPI AG"
doi: "10.20944/preprints202609.0999.v2"
publication_year: 2026
summary: "该论文评估了在录音不相交划分条件下，语料内SimCLR预训练对水声目标识别（UATR）的有效性。标签稀缺制约了UATR发展，自监督学习可利用大量无标签水听器录音，但当评估严格避免训练与测试录音重叠时，自监督预训练的收益尚不明确。论文通过控制性先导研究，系统评估SimCLR预训练在录音不相交划分下的实际效果。"
keywords:
  - "underwater acoustic target recognition"
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.20944/preprints202609.0999.v2"
previewImage: "/daily/2026-09-22/assets/crossref--10.20944-preprints202609.0999.v2/preview.svg"
---

## 核心内容

该论文评估了在录音不相交划分条件下，语料内SimCLR预训练对水声目标识别（UATR）的有效性。标签稀缺制约了UATR发展，自监督学习可利用大量无标签水听器录音，但当评估严格避免训练与测试录音重叠时，自监督预训练的收益尚不明确。论文通过控制性先导研究，系统评估SimCLR预训练在录音不相交划分下的实际效果。

## 关键技术与数据

采用SimCLR自监督对比学习框架，在176,481个无标签log-mel片段上进行语料内预训练，数据汇集自Oceanship、QiandaoEar22等数据集的训练分区。关键技术包括数据增强策略设计、对比损失优化、以及录音不相交（recording-disjoint）划分协议。下游任务采用微调评估，严格控制训练与测试录音无重叠，确保评估的严谨性。

## 结果与结论

研究发现在录音不相交划分下，SimCLR预训练带来的性能提升有限，甚至在某些条件下不如随机初始化。结果表明自监督预训练的收益高度依赖于评估协议，当录音重叠被严格排除后，预训练优势显著减弱。创新点在于揭示了UATR领域自监督学习评估中的关键陷阱，强调录音不相交划分对结论可靠性的重要性，为后续自监督水声识别研究提供了方法学参考。

## 来源链接

- DOI：https://doi.org/10.20944/preprints202609.0999.v2