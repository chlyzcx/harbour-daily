---
candidateId: "openalex--W7214529111"
category: "Paper"
date: "2026-09-29"
rank: 2
title: "Acoustic recognition of tilapia feeding intensity via LoRA-fine-tuned multimodal large language models"
authors:
  - "Chen Yang"
  - "Shengli Fan"
  - "Peizheng He"
  - "Xinli Ma"
  - "Lang Wang"
  - "Michel Dossou"
  - "Weiming Cai"
research_direction: []
journal: "Aquaculture Reports"
publisher: "Elsevier BV"
doi: "10.1016/j.aqrep.2026.103857"
publication_year: 2026
summary: "针对集约化水产养殖中鱼类摄食强度实时评估依赖外部频谱预处理和大量标注数据的问题，该研究提出端到端方法，将摄食强度识别重构为音频指令跟随任务，利用多模态大语言模型Qwen2.5-Omni-3B直接处理原始音频与自然语言提示，实现按需投喂决策支持。"
keywords: []
score: 56.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7214529111"
  - name: "DOI"
    url: "https://doi.org/10.1016/j.aqrep.2026.103857"
previewImage: "/daily/2026-09-29/assets/openalex--W7214529111/preview.png"
---

## 核心内容

针对集约化水产养殖中鱼类摄食强度实时评估依赖外部频谱预处理和大量标注数据的问题，该研究提出端到端方法，将摄食强度识别重构为音频指令跟随任务，利用多模态大语言模型Qwen2.5-Omni-3B直接处理原始音频与自然语言提示，实现按需投喂决策支持。

## 关键技术与数据

采用LoRA对Qwen2.5-Omni-3B进行参数高效微调，输入为原始音频片段与自然语言提示，避免显式频谱图预处理。数据集为罗非鱼摄食声学录音及对应强度标签，方法融合多模态大语言模型与指令微调技术，属于水声信号处理与水产养殖交叉应用。

## 结果与结论

实验表明该端到端方法在摄食强度识别上取得良好性能，降低了对大规模标注数据和外部预处理的依赖，提升了实际部署可行性。创新点在于首次将多模态大语言模型与LoRA微调引入鱼类摄食声学识别，为智能投喂提供了新范式。

## 来源链接

- OpenAlex：https://openalex.org/W7214529111
- DOI：https://doi.org/10.1016/j.aqrep.2026.103857