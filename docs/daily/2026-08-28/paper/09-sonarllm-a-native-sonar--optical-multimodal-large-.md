---
candidateId: "openalex--W7204232495"
category: "Paper"
date: "2026-08-28"
rank: 9
title: "SonarLLM: A Native Sonar--Optical Multimodal Large Language Model for Underwater Perception"
authors:
  - "Cong Su"
  - "Longxuan Ma"
  - "Ling Dong"
  - "Guofeng Tang"
  - "Weijie Yin"
  - "Haohui Chen"
  - "Zhengtao Yu"
research_direction: []
journal: "arXiv (Cornell University)"
publisher: "Cornell University"
doi: "10.48550/arxiv.2608.24325"
publication_year: 2026
summary: "可靠的水下感知需要在多变能见度下利用互补传感。光学相机可获取外观与语义信息，但在浑浊水中性能急剧下降；成像声呐则保持几何结构，但具有独特的距离-方位结构和声学伪影。现有多模态大语言模型（MLLM）主要基于光学编码器，难以建模声呐或自适应利用声呐-光学互补性。本文提出SonarLLM，一种将声呐作为原生模态的声呐-光学多模态大语言模型。"
keywords: []
score: 56.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7204232495"
  - name: "DOI"
    url: "https://doi.org/10.48550/arxiv.2608.24325"
previewImage: "/daily/2026-08-28/assets/openalex--W7204232495/preview.png"
---

## 核心内容

可靠的水下感知需要在多变能见度下利用互补传感。光学相机可获取外观与语义信息，但在浑浊水中性能急剧下降；成像声呐则保持几何结构，但具有独特的距离-方位结构和声学伪影。现有多模态大语言模型（MLLM）主要基于光学编码器，难以建模声呐或自适应利用声呐-光学互补性。本文提出SonarLLM，一种将声呐作为原生模态的声呐-光学多模态大语言模型。

## 关键技术与数据

SonarLLM将声呐数据作为原生输入模态，设计专门的声呐编码器以提取距离-方位结构特征，并与光学编码器特征融合。模型基于大语言模型架构，支持跨模态理解与推理。训练数据为配对的声呐与光学水下图像及文本描述，用于指令微调与多模态对齐。

## 结果与结论

实验表明SonarLLM在水下感知任务（如目标识别、场景描述）中优于现有MLLM，尤其在声呐-光学互补性利用方面表现突出。创新点在于首次将声呐作为原生模态纳入MLLM框架，实现了声呐与光学信息的自适应融合，显著提升了复杂水下环境的感知与理解能力。

## 来源链接

- OpenAlex：https://openalex.org/W7204232495
- DOI：https://doi.org/10.48550/arxiv.2608.24325