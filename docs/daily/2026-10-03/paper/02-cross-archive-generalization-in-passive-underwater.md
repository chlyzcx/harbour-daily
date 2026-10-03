---
candidateId: "openalex--W7215054615"
category: "Paper"
date: "2026-10-03"
rank: 2
title: "Cross-Archive Generalization in Passive Underwater Acoustic Sensing: A Four-Dataset Benchmark of Label and Recording-Condition Shifts"
authors:
  - "Hao Yuan"
  - "Wenbo Wang"
  - "Lingjiang Zeng"
  - "Guici Chen"
  - "Tian Li"
  - "Xuan Hou"
research_direction:
  - "信号识别"
  - "被动声呐"
journal: "Preprints.org"
doi: "10.20944/preprints202609.0919.v3"
publication_year: 2026
summary: "海底有缆观测站和沿岸水听器站积累了海量船舶辐射噪声档案，水下声目标识别（UATR）系统需跨档案工作，但深度网络几乎仅在单一数据集内训练和评估，跨档案泛化能力尚未被测量。该论文构建了四个船舶辐射噪声数据集的跨档案泛化基准，系统评估标签偏移和录音条件偏移对UATR性能的影响，填补了跨档案泛化评估的空白。"
keywords:
  - "passive underwater acoustic"
  - "underwater acoustic target recognition"
score: 72.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7215054615"
  - name: "DOI"
    url: "https://doi.org/10.20944/preprints202609.0919.v3"
previewImage: "/daily/2026-10-03/assets/openalex--W7215054615/preview.svg"
---

## 核心内容

海底有缆观测站和沿岸水听器站积累了海量船舶辐射噪声档案，水下声目标识别（UATR）系统需跨档案工作，但深度网络几乎仅在单一数据集内训练和评估，跨档案泛化能力尚未被测量。该论文构建了四个船舶辐射噪声数据集的跨档案泛化基准，系统评估标签偏移和录音条件偏移对UATR性能的影响，填补了跨档案泛化评估的空白。

## 关键技术与数据

使用四个船舶辐射噪声数据集：来自乔治亚海峡的Oceanship、淡水湖的QiandaoEar22、基于公开数据重建的VTUAD等。构建跨档案评估协议，分别考察标签偏移（目标类别分布差异）和录音条件偏移（水听器、环境噪声等差异）对识别性能的影响，采用深度网络进行基准测试。

## 结果与结论

实验表明跨档案泛化性能显著低于档案内评估，标签偏移和录音条件偏移均导致性能下降，且录音条件偏移影响更为严重。该工作首次系统量化了UATR跨档案泛化差距，为构建鲁棒的水声目标识别系统提供了基准和方向，强调了多档案联合训练和域适应的重要性。

## 来源链接

- OpenAlex：https://openalex.org/W7215054615
- DOI：https://doi.org/10.20944/preprints202609.0919.v3