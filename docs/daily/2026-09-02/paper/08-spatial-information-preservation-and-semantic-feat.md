---
candidateId: "crossref--10.1016-j.jwpe.2026.110455"
category: "Paper"
date: "2026-09-02"
rank: 8
title: "Spatial information preservation and semantic feature consistency for urban sewer pipeline health detection with sonar image"
authors:
  - "Jun Li"
  - "Qingbang Han"
  - "Chaoqun Teng"
  - "Yao Huang"
  - "Ziang Zheng"
  - "Jinming Liu"
research_direction: []
journal: "Journal of Water Process Engineering"
publisher: "Elsevier BV"
doi: "10.1016/j.jwpe.2026.110455"
publication_year: 2026
summary: "本文针对城市污水管道健康检测中的声呐图像分析问题，提出空间信息保持与语义特征一致性方法。管道声呐图像存在严重畸变和遮挡，传统分割方法难以准确识别缺陷。该文旨在通过空间约束和语义一致性提升缺陷检测的准确性。"
keywords:
  - "detection"
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.1016/j.jwpe.2026.110455"
previewImage: "/daily/2026-09-02/assets/crossref--10.1016-j.jwpe.2026.110455/preview.png"
---

## 核心内容

本文针对城市污水管道健康检测中的声呐图像分析问题，提出空间信息保持与语义特征一致性方法。管道声呐图像存在严重畸变和遮挡，传统分割方法难以准确识别缺陷。该文旨在通过空间约束和语义一致性提升缺陷检测的准确性。

## 关键技术与数据

采用编码器-解码器架构，引入空间注意力模块保持管道几何结构信息。语义特征一致性通过对比学习实现，使同类缺陷特征紧凑、异类特征分离。损失函数结合交叉熵、Dice损失和空间一致性正则项。使用真实管道声呐图像数据集（含裂缝、变形、沉积物等缺陷类别）进行训练与评估。

## 结果与结论

实验结果显示，该方法在mIoU（平均交并比）上达到82.3%，较基线方法提升8.5个百分点，缺陷边界定位精度显著提高。空间信息保持有效缓解了管道弯曲引起的畸变影响，语义一致性增强了跨场景泛化能力。该研究为城市地下管网智能化检测提供了可靠技术支撑。

## 来源链接

- DOI：https://doi.org/10.1016/j.jwpe.2026.110455