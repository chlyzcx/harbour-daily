---
candidateId: "crossref--10.3390-jmse14212022"
category: "Paper"
date: "2026-10-29"
rank: 9
title: "Evaluating Dataset-Aware Masked Supervision for Joint Segmentation of Heterogeneous Side-Scan Sonar Datasets"
authors:
  - "Yang Liu"
  - "Yang Lin"
  - "Chang Zou"
  - "Haitao Gu"
  - "Siquan Yu"
research_direction: []
journal: "Journal of Marine Science and Engineering"
publisher: "MDPI AG"
doi: "10.3390/jmse14212022"
publication_year: 2026
summary: "该论文评估数据集感知掩蔽监督（dataset-aware masked supervision）在异构侧扫声呐数据集联合分割中的作用。研究背景是不同声呐数据集声学分布与标注范围不一致，联合训练时跨数据集类别监督可能产生错误负监督。目标是分析掩蔽交叉熵在减少错误负监督与削弱跨类竞争之间的权衡。"
keywords: []
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.3390/jmse14212022"
previewImage: "/daily/2026-10-29/assets/crossref--10.3390-jmse14212022/preview.png"
---

## 核心内容

该论文评估数据集感知掩蔽监督（dataset-aware masked supervision）在异构侧扫声呐数据集联合分割中的作用。研究背景是不同声呐数据集声学分布与标注范围不一致，联合训练时跨数据集类别监督可能产生错误负监督。目标是分析掩蔽交叉熵在减少错误负监督与削弱跨类竞争之间的权衡。

## 关键技术与数据

关键技术包括数据集感知掩蔽交叉熵、软衰减策略与共享四类空间联合分割；使用AI4Shipwrecks、MCM、SubPipe三个侧扫声呐数据集，比较未掩蔽交叉熵、软衰减与掩蔽监督的分割性能。

## 结果与结论

结果表明掩蔽监督可减少标注范围外类别的错误负监督，但会削弱跨类竞争，影响分割性能；软衰减可在两者间取得折中。创新点在于系统评估数据集感知掩蔽监督在异构侧扫声呐联合分割中的利弊，为多数据集联合训练提供指导。

## 来源链接

- DOI：https://doi.org/10.3390/jmse14212022