---
candidateId: "crossref--10.31235-osf.io-w59nx_v1"
category: "Paper"
date: "2026-08-26"
rank: 7
title: "Deleting the call does not delete the evidence: a within-recording validity test for passive-acoustic whale-call detection benchmarks"
authors:
  - "Dharit Shah"
research_direction:
  - "被动声学监测"
journal: "Unknown"
publisher: "Center for Open Science"
doi: "10.31235/osf.io/w59nx_v1"
publication_year: 2026
summary: "该论文针对被动声学监测中鲸类叫声检测基准测试存在的潜在数据泄漏问题，提出了一种记录内有效性检验方法。研究指出，检测基准由时间上聚集的事件构建，包含标注叫声的时间段与从未包含叫声的时间段之间的差异可能不仅仅是叫声本身，导致模型可能利用捷径学习而非真正的声学特征。"
keywords:
  - "detection"
  - "passive acoustic monitoring"
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.31235/osf.io/w59nx_v1"
previewImage: "/daily/2026-08-26/assets/crossref--10.31235-osf.io-w59nx_v1/preview.svg"
---

## 核心内容

该论文针对被动声学监测中鲸类叫声检测基准测试存在的潜在数据泄漏问题，提出了一种记录内有效性检验方法。研究指出，检测基准由时间上聚集的事件构建，包含标注叫声的时间段与从未包含叫声的时间段之间的差异可能不仅仅是叫声本身，导致模型可能利用捷径学习而非真正的声学特征。

## 关键技术与数据

诊断方法为：从正样本窗口中删除标注的叫声，用同一窗口的背景噪声替换该区间，保持其余样本不变，然后计算消融AUC（ablation AUC），即删除叫声后的正样本得分高于真负样本的概率。零假设值为0.5，值越高表示捷径学习越严重。该方法可应用于任意基于窗口的被动声学检测基准数据集。

## 结果与结论

该研究提供了一种简单有效的诊断工具，用于评估检测基准中是否存在因时间聚集导致的捷径学习问题。通过消融AUC指标，研究者可以量化模型对叫声本身而非上下文线索的依赖程度。该工作对被动声学监测中基准测试的可靠性和模型评估的公平性具有重要方法学意义。

## 来源链接

- DOI：https://doi.org/10.31235/osf.io/w59nx_v1