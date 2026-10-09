---
candidateId: "openalex--W7220833167"
category: "Paper"
date: "2026-10-09"
rank: 3
title: "Physics-constrained diffusion-based data augmentation for active sonar under low-SNR sea conditions"
authors:
  - "Wenjie Zhou"
  - "Lei Wang"
  - "Cong Peng"
  - "Haoran Ji"
  - "Boyu Zhao"
  - "Xiaokun Jia"
  - "Shi Liu"
research_direction:
  - "主动声呐"
journal: "Ocean Engineering"
publisher: "Elsevier BV"
doi: "10.1016/j.oceaneng.2026.128558"
publication_year: 2026
summary: "主动声呐检测模型训练受限于真实海试目标回波样本稀缺，仿真回波虽可扩充样本但分布与真实海洋环境差异大。本文提出物理约束的扩散模型数据增强方法，针对低信噪比海况下主动声呐LFM回波谱图进行增强。目标是生成分布接近真实海洋环境的合成样本，提升数据驱动主动声呐检测模型的训练效果与泛化能力。"
keywords:
  - "active sonar"
  - "detection"
score: 78.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7220833167"
  - name: "DOI"
    url: "https://doi.org/10.1016/j.oceaneng.2026.128558"
previewImage: "/daily/2026-10-09/assets/openalex--W7220833167/preview.png"
---

## 核心内容

主动声呐检测模型训练受限于真实海试目标回波样本稀缺，仿真回波虽可扩充样本但分布与真实海洋环境差异大。本文提出物理约束的扩散模型数据增强方法，针对低信噪比海况下主动声呐LFM回波谱图进行增强。目标是生成分布接近真实海洋环境的合成样本，提升数据驱动主动声呐检测模型的训练效果与泛化能力。

## 关键技术与数据

关键技术包括物理约束两阶段无条件扩散模型、去噪扩散概率模型（DDPM）、LFM回波谱图生成。第一阶段训练无条件扩散模型学习谱图分布，第二阶段引入物理约束优化生成样本以匹配主动声呐回波特性。数据采用主动声呐LFM回波谱图，涵盖低信噪比海况下的真实海试样本与仿真样本用于训练与评估。

## 结果与结论

实验表明，所提物理约束扩散增强方法生成的谱图在分布上更接近真实海试回波，显著提升检测模型在低信噪比条件下的性能。两阶段设计兼顾生成质量与物理一致性。创新点在于将物理约束融入扩散模型数据增强，缓解主动声呐样本稀缺与仿真-真实域差异问题，为低信噪比海况下主动声呐检测提供有效数据扩充手段。

## 来源链接

- OpenAlex：https://openalex.org/W7220833167
- DOI：https://doi.org/10.1016/j.oceaneng.2026.128558