---
candidateId: "arxiv--2609.13659-1"
category: "Paper"
date: "2026-09-16"
rank: 6
title: "UniqueShip: Mitigating Data Leakage in Acoustic Ship Classification Benchmark Datasets"
authors:
  - "Connor Hashemi"
  - "Trevor Stout"
  - "Anthony Hoogs"
  - "Jason Parham"
research_direction:
  - "信号识别"
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "水声目标识别（UATR）适合机器学习，但缺乏大型、多样且公开的标注数据集阻碍进展。本文引入UniqueShip，一个面向UATR的机器学习就绪基准数据集，源自加拿大海洋网络（ONC）开放库。与先前数据集不同，UniqueShip显式控制训练与评估集间的“数据泄漏”，确保更可靠和可泛化的评估。研究目标是提供高质量基准，推动水声船舶分类研究。"
keywords:
  - "classification"
  - "machine learning"
  - "underwater acoustic target recognition"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2609.13659v1"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2609.13659v1"
previewImage: "/daily/2026-09-16/assets/arxiv--2609.13659-1/preview.png"
---

## 核心内容

水声目标识别（UATR）适合机器学习，但缺乏大型、多样且公开的标注数据集阻碍进展。本文引入UniqueShip，一个面向UATR的机器学习就绪基准数据集，源自加拿大海洋网络（ONC）开放库。与先前数据集不同，UniqueShip显式控制训练与评估集间的“数据泄漏”，确保更可靠和可泛化的评估。研究目标是提供高质量基准，推动水声船舶分类研究。

## 关键技术与数据

UniqueShip从ONC获取水声录音，包含多种船舶辐射噪声。关键技术包括数据泄漏控制（如按船舶、时间、地点划分）、标注质量控制及基准评估协议。数据集可能包含船舶类型、航速、距离等元数据。方法强调训练/测试集独立性，避免同一船舶或航次泄漏，确保模型泛化评估。

## 结果与结论

UniqueShip提供大规模、多样化且无泄漏的UATR基准，揭示先前数据集因泄漏导致性能高估。实验表明，在该数据集上评估的模型性能更真实反映泛化能力。创新点在于首次系统性地控制水声船舶分类中的数据泄漏，为UATR提供可靠基准，推动领域可复现研究。

## 来源链接

- arXiv：http://arxiv.org/abs/2609.13659v1
- PDF：http://arxiv.org/pdf/2609.13659v1