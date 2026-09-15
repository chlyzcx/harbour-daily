---
candidateId: "crossref--10.20944-preprints202609.0999.v1"
category: "Paper"
date: "2026-09-15"
rank: 6
title: "Self-Supervised Pretraining for Underwater Acoustic Target Recognition: A Three-Corpus SimCLR Pilot with a Sobering Verdict"
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
doi: "10.20944/preprints202609.0999.v1"
publication_year: 2026
summary: "该论文针对水声目标识别（UATR）中标签稀缺的问题，探索自监督预训练（SSL）的应用价值。研究背景在于水听器可低成本采集大量无标签音频，但验证过的舰船标签稀缺。论文通过三个语料库的SimCLR对照实验，系统评估SSL对舰船辐射噪声表征学习的实际效果，并给出了审慎的结论。"
keywords:
  - "underwater acoustic target recognition"
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.20944/preprints202609.0999.v1"
previewImage: "/daily/2026-09-15/assets/crossref--10.20944-preprints202609.0999.v1/preview.svg"
---

## 核心内容

该论文针对水声目标识别（UATR）中标签稀缺的问题，探索自监督预训练（SSL）的应用价值。研究背景在于水听器可低成本采集大量无标签音频，但验证过的舰船标签稀缺。论文通过三个语料库的SimCLR对照实验，系统评估SSL对舰船辐射噪声表征学习的实际效果，并给出了审慎的结论。

## 关键技术与数据

采用ResNet-18作为骨干网络，使用SimCLR自监督学习框架在176,481个无标签log-mel片段上进行预训练，数据汇集自三个语料库。关键技术包括自监督对比学习、log-mel特征提取、跨语料库迁移评估。研究设计了严格的对照实验以规避数据泄漏问题，并在下游UATR任务上评估预训练表征的性能。

## 结果与结论

实验结果表明SSL在舰船辐射噪声识别中的效果有限，跨语料库泛化性能不及预期，给出了较为审慎的结论。创新点在于首次在三个语料库上进行受控的SimCLR预训练实验，揭示了单语料库评估中可能存在的泄漏问题，为UATR领域自监督学习的后续研究提供了重要的基准和警示。

## 来源链接

- DOI：https://doi.org/10.20944/preprints202609.0999.v1