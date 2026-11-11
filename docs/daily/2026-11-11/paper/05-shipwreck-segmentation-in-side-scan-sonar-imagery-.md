---
candidateId: "openalex--W7225610196"
category: "Paper"
date: "2026-11-11"
rank: 5
title: "Shipwreck Segmentation in Side-Scan Sonar Imagery Through Encoder Block Repetition and Label-Free Block Selection"
authors:
  - "Jiani Dai"
  - "Jie He"
research_direction: []
journal: "Mathematics"
publisher: "Multidisciplinary Digital Publishing Institute"
doi: "10.3390/math14214080"
publication_year: 2026
summary: "该论文研究侧扫声呐图像中的沉船分割问题，探讨重复冻结编码器块能否提升Segment Anything Model（SAM）在该任务上的性能，以及如何在无标注验证掩码条件下选择重复块位置。论文提出重复块Segment Anything Model（RB-SAM），旨在改善侧扫声呐沉船分割效果。"
keywords: []
score: 55.2
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7225610196"
  - name: "DOI"
    url: "https://doi.org/10.3390/math14214080"
previewImage: "/daily/2026-11-11/assets/openalex--W7225610196/preview.svg"
---

## 核心内容

该论文研究侧扫声呐图像中的沉船分割问题，探讨重复冻结编码器块能否提升Segment Anything Model（SAM）在该任务上的性能，以及如何在无标注验证掩码条件下选择重复块位置。论文提出重复块Segment Anything Model（RB-SAM），旨在改善侧扫声呐沉船分割效果。

## 关键技术与数据

RB-SAM将冻结编码器块额外执行一次并保留全部预训练权重；提出图传输至扩展效率（GTEE）评分，在无标注参考数据上选择块重复位置。方法基于SAM架构，利用侧扫声呐图像数据进行沉船分割实验，无需标注验证掩码即可完成块选择。

## 结果与结论

研究表明重复冻结编码器块可提升SAM在侧扫声呐沉船分割中的性能，GTEE评分能够在无标注条件下有效选择重复位置。RB-SAM为侧扫声呐图像沉船分割提供了一种无需标注验证的编码器增强策略，提升了分割任务的适应性。

## 来源链接

- OpenAlex：https://openalex.org/W7225610196
- DOI：https://doi.org/10.3390/math14214080