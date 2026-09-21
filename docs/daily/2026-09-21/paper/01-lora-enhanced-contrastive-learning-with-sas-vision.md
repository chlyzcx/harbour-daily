---
candidateId: "arxiv--2609.21061-1"
category: "Paper"
date: "2026-09-21"
rank: 1
title: "LoRA Enhanced Contrastive Learning with SAS Vision Transformers"
authors:
  - "Dan Zimmerman"
  - "Frank E. Bobe"
  - "Amelia L. McCormack"
  - "Matthew Cook"
  - "Gregory D. Vetaw"
research_direction:
  - "水声成像"
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "针对合成孔径声呐（SAS）自动目标识别（ATR）中目标图像稀缺、背景杂波强及人工判读依赖等问题，本文提出一种基于DINOv3视觉Transformer的参数高效迁移框架。研究目标是将自然图像预训练模型适配到水下SAS声学域，通过三阶段微调策略缓解声学传播特性与光学图像之间的域差异，提升小样本条件下的目标识别性能。"
keywords:
  - "deep learning"
  - "synthetic aperture sonar"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2609.21061v1"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2609.21061v1"
previewImage: "/daily/2026-09-21/assets/arxiv--2609.21061-1/preview.png"
---

## 核心内容

针对合成孔径声呐（SAS）自动目标识别（ATR）中目标图像稀缺、背景杂波强及人工判读依赖等问题，本文提出一种基于DINOv3视觉Transformer的参数高效迁移框架。研究目标是将自然图像预训练模型适配到水下SAS声学域，通过三阶段微调策略缓解声学传播特性与光学图像之间的域差异，提升小样本条件下的目标识别性能。

## 关键技术与数据

采用DINOv3 ViT作为骨干网络，第一阶段冻结骨干并引入低秩适配（LoRA）实现参数高效迁移；后续阶段逐步解冻并融合对比学习策略，以增强类间判别性。方法针对SAS图像域偏移设计，结合对比学习损失优化特征嵌入空间。实验基于SAS目标图像数据集，具体规模与来源未在摘要中详述。

## 结果与结论

该框架在SAS ATR任务中验证了LoRA增强对比学习与ViT结合的有效性，表明参数高效微调可弥合自然图像预训练与水下声学传播之间的鸿沟。创新点在于将LoRA与对比学习集成于SAS ViT识别流程，为数据稀缺场景下的水声目标识别提供了可迁移方案，但具体性能指标未在摘要中给出。

## 来源链接

- arXiv：http://arxiv.org/abs/2609.21061v1
- PDF：http://arxiv.org/pdf/2609.21061v1