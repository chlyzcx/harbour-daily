---
candidateId: "openalex--W7224818677"
category: "Paper"
date: "2026-11-01"
rank: 3
title: "Confidence Inversion in Open-Set Underwater Acoustic Target Recognition: A Leakage-Safe Multi-Corpus Pilot Study"
authors:
  - "Hao Yuan"
  - "Wenbo Wang"
  - "Lingjiang Zeng"
  - "Guici Chen"
  - "Yu Chen"
  - "庞正鹏"
  - "Xinlu Yang"
research_direction:
  - "信号识别"
journal: "Preprints.org"
doi: "10.20944/preprints202609.1125.v3"
publication_year: 2026
summary: "针对水声目标识别（UATR）系统在开放标签空间中面临未知目标与采集条件偏移时置信度失准的问题，该论文开展泄漏安全的多语料库试点研究，系统评估五种评分/损失配置在开放集识别场景下的置信度反转现象。研究目标是揭示闭集训练的识别系统在开放集部署中的置信度校准缺陷，并建立跨语料库、记录不重叠的评测协议以保证评估的泄漏安全性。"
keywords:
  - "detection"
  - "underwater acoustic target recognition"
score: 64.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7224818677"
  - name: "DOI"
    url: "https://doi.org/10.20944/preprints202609.1125.v3"
previewImage: "/daily/2026-11-01/assets/openalex--W7224818677/preview.svg"
---

## 核心内容

针对水声目标识别（UATR）系统在开放标签空间中面临未知目标与采集条件偏移时置信度失准的问题，该论文开展泄漏安全的多语料库试点研究，系统评估五种评分/损失配置在开放集识别场景下的置信度反转现象。研究目标是揭示闭集训练的识别系统在开放集部署中的置信度校准缺陷，并建立跨语料库、记录不重叠的评测协议以保证评估的泄漏安全性。

## 关键技术与数据

关键技术包括ResNet-18分类器、交叉熵（CE）损失、熵式开放集惩罚（EOS-L）、最大softmax概率（MSP）、能量分数与OpenMax评分。实验覆盖四个语料库与六种记录不重叠协议，每种协议采用3个随机种子，构建闭集与开放集对比评测。方法核心是比较不同损失与评分组合下的置信度分布与开放集识别性能。

## 结果与结论

研究发现开放集场景下存在显著的置信度反转现象，即未知目标或条件偏移样本获得过高置信度，导致误判风险上升。结论表明单一评分机制难以在跨语料库条件下保持校准一致性，泄漏安全的记录不重叠协议对评估开放集UATR至关重要。论文为水声目标识别的开放集部署提供了评测基准与置信度校准改进方向。具体量化指标因摘要截断未完整列出。

【结果与结论】
（补充说明：因摘要截断，具体数值结果未完整呈现，上述结论基于摘要可见内容归纳。）

## 来源链接

- OpenAlex：https://openalex.org/W7224818677
- DOI：https://doi.org/10.20944/preprints202609.1125.v3