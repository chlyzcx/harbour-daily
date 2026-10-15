---
candidateId: "arxiv--2610.16942-1"
category: "Paper"
date: "2026-10-15"
rank: 2
title: "UA-Bench: Benchmarking Large Audio-Language Models on Underwater Acoustic Recognition"
authors:
  - "Zhe Sun"
  - "Liang An"
  - "Jiayu Yao"
  - "Ronglai Qian"
  - "Jianing Cai"
  - "Ziwei Huang"
  - "Qing Fan"
  - "Zhiyuan Yang"
  - "Yujun Cai"
  - "Hongli Cao"
research_direction:
  - "信号识别"
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "针对大型音频-语言模型（LALMs）在通用声学任务中表现优异、但其在水声领域的迁移能力尚不明确的问题，本文提出首个面向水声信号识别的基准测试UA-Bench。水声目标监测、海上安全与海洋感知均依赖对水下声信号的准确识别，但相关标注数据获取成本高昂。论文旨在系统评估LALMs在水声识别任务中的性能边界，并构建可控、可扩展的合成评测框架以弥补真实数据稀缺的不足。"
keywords:
  - "classification"
  - "detection"
  - "underwater acoustic signal recognition"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2610.16942v1"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2610.16942v1"
previewImage: "/daily/2026-10-15/assets/arxiv--2610.16942-1/preview.png"
---

## 核心内容

针对大型音频-语言模型（LALMs）在通用声学任务中表现优异、但其在水声领域的迁移能力尚不明确的问题，本文提出首个面向水声信号识别的基准测试UA-Bench。水声目标监测、海上安全与海洋感知均依赖对水下声信号的准确识别，但相关标注数据获取成本高昂。论文旨在系统评估LALMs在水声识别任务中的性能边界，并构建可控、可扩展的合成评测框架以弥补真实数据稀缺的不足。

## 关键技术与数据

论文构建了融合多因素交互的水声合成数据生成流程，涵盖检测信号结构、信道传播效应、环境噪声与目标辐射噪声等关键要素，以逼近真实水声场景。基于该流程生成UA-Bench评测集，对多种主流LALMs开展零样本与少样本水声识别评测，任务涉及水声目标分类与信号检测等。评测同时对比模型在通用音频任务与水声任务上的性能差异，分析预训练知识迁移的有效性。

## 结果与结论

实验表明，现有LALMs在水声识别任务上性能显著低于通用音频任务，零样本条件下准确率下降明显，暴露了跨域迁移的局限性。合成数据可在一定程度上缩小评测缺口，但域间隙仍制约模型表现。论文结论指出，LALMs尚不能直接胜任水声识别，需引入领域自适应与专用声学表征。UA-Bench为水声多模态模型评测提供了可复现基准，是该方向首个系统性工作。

## 来源链接

- arXiv：http://arxiv.org/abs/2610.16942v1
- PDF：http://arxiv.org/pdf/2610.16942v1