---
candidateId: "openalex--W7215052542"
category: "Paper"
date: "2026-10-03"
rank: 1
title: "Real-Time DETR Detection Benchmark and Domain-Shift Analysis on the UATD Multibeam Forward-Looking Sonar Dataset"
authors:
  - "Hao Yuan"
  - "Wenbo Wang"
  - "Tian Li"
  - "Lingjiang Zeng"
  - "Yu Chen"
  - "Fanyu Wang"
research_direction:
  - "目标检测"
  - "水声成像"
journal: "Preprints.org"
doi: "10.20944/preprints202609.0449.v3"
publication_year: 2026
summary: "多波束前视声呐（MFLS）是浑浊水域水下航行器的主要感知手段，但低分辨率、声学散斑和域偏移使检测仍具挑战。该论文针对公开UATD基准中验证集性能无法可靠预测测试集性能的问题（mAP@0.5持续存在13.3–17.8个百分点的差距），对基于DINOv3基础特征的DETR族检测器DEIMv2进行实时检测基准测试与域偏移分析，并与四种基线方法对比，旨在揭示域偏移对检测性能的影响机制。"
keywords:
  - "detection"
  - "forward-looking sonar"
  - "underwater acoustic target detection"
score: 72.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7215052542"
  - name: "DOI"
    url: "https://doi.org/10.20944/preprints202609.0449.v3"
previewImage: "/daily/2026-10-03/assets/openalex--W7215052542/preview.svg"
---

## 核心内容

多波束前视声呐（MFLS）是浑浊水域水下航行器的主要感知手段，但低分辨率、声学散斑和域偏移使检测仍具挑战。该论文针对公开UATD基准中验证集性能无法可靠预测测试集性能的问题（mAP@0.5持续存在13.3–17.8个百分点的差距），对基于DINOv3基础特征的DETR族检测器DEIMv2进行实时检测基准测试与域偏移分析，并与四种基线方法对比，旨在揭示域偏移对检测性能的影响机制。

## 关键技术与数据

采用DETR族检测器DEIMv2，以DINOv3基础模型特征为骨干，在UATD多波束前视声呐数据集上进行实时检测基准测试。对比四种基线检测器，分析验证集与测试集之间的域偏移现象，考察声学散斑、低分辨率等因素对检测性能的影响，并评估实时推理能力。

## 结果与结论

实验揭示了验证集与测试集之间mAP@0.5存在13.3–17.8个百分点的持续差距，表明域偏移是性能下降的主因。DEIMv2在实时性与检测精度间取得一定平衡，但域偏移问题仍未完全解决。该工作为MFLS检测提供了标准化基准和域偏移分析框架，指出了提升跨域泛化能力的必要性。

## 来源链接

- OpenAlex：https://openalex.org/W7215052542
- DOI：https://doi.org/10.20944/preprints202609.0449.v3