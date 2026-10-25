---
candidateId: "openalex--W7223382467"
category: "Paper"
date: "2026-10-25"
rank: 1
title: "A cost-aware, minority-class evaluation of adversarial domain adaptation for side-scan sonar sim-to-real classification"
authors:
  - "Luyu Ren"
  - "Benjun Ma"
research_direction: []
journal: "Ocean Engineering"
publisher: "Elsevier BV"
doi: "10.1016/j.oceaneng.2026.128755"
publication_year: 2026
summary: "该论文针对侧扫声呐图像在仿真域到真实域分类任务中的域偏移问题，研究了对抗域适应方法的性能评估。由于真实侧扫声呐标注数据稀缺且类别不平衡，论文聚焦于少数类样本的识别可靠性，提出了一种代价敏感的评估框架，以衡量域适应在类别不均衡条件下的实际泛化能力，为侧扫声呐目标分类的仿真到真实迁移提供了更贴近实际部署的评价视角。"
keywords:
  - "classification"
score: 65.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7223382467"
  - name: "DOI"
    url: "https://doi.org/10.1016/j.oceaneng.2026.128755"
previewImage: "/daily/2026-10-25/assets/openalex--W7223382467/preview.png"
---

## 核心内容

该论文针对侧扫声呐图像在仿真域到真实域分类任务中的域偏移问题，研究了对抗域适应方法的性能评估。由于真实侧扫声呐标注数据稀缺且类别不平衡，论文聚焦于少数类样本的识别可靠性，提出了一种代价敏感的评估框架，以衡量域适应在类别不均衡条件下的实际泛化能力，为侧扫声呐目标分类的仿真到真实迁移提供了更贴近实际部署的评价视角。

## 关键技术与数据

采用对抗域适应（adversarial domain adaptation）框架，通过域判别器与特征提取器的对抗训练实现仿真域与真实域特征对齐。评估中引入代价敏感学习（cost-aware learning）思想，针对少数类样本设计加权评价指标，数据涉及仿真侧扫声呐图像与真实侧扫声呐图像的跨域分类任务，重点考察类别不平衡下的分类代价与少数类召回表现。

## 结果与结论

研究表明，常规域适应评估会掩盖少数类性能退化问题，代价敏感评估能更真实反映模型在真实域少数类上的识别能力。论文揭示了对抗域适应在类别不平衡侧扫声呐数据上存在少数类误判代价高的缺陷，强调在仿真到真实迁移中需结合代价敏感指标进行综合评价，为水声图像域适应方法的实用化评估提供了方法论参考。

## 来源链接

- OpenAlex：https://openalex.org/W7223382467
- DOI：https://doi.org/10.1016/j.oceaneng.2026.128755