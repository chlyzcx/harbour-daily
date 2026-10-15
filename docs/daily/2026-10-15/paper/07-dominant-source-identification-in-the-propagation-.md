---
candidateId: "openalex--W7221635720"
category: "Paper"
date: "2026-10-15"
rank: 7
title: "Dominant Source Identification in the Propagation of Ocean Observation Uncertainty to Underwater Detection Performance: A Differentiable End-To-End Framework"
authors:
  - "Shuangxin Wang"
  - "Zhen Yang"
  - "Xinmin Han"
research_direction:
  - "被动声呐"
journal: "Preprints.org"
doi: "10.20944/preprints202610.1096.v1"
publication_year: 2026
summary: "针对海洋观测不确定性经声速剖面（SSP）反演、声传播损失（TL）预测与被动声呐检测概率（Pd）估计非线性传播后制约水下探测性能的问题，论文提出一种可微端到端框架，将观测不确定性贯穿SSP反演、声传播与被动声呐Pd计算进行统一追踪，从而实现对主导不确定性源的定量排序，为海洋观测资源配置与探测性能保障提供依据。"
keywords:
  - "detection"
  - "passive sonar"
score: 64.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7221635720"
  - name: "DOI"
    url: "https://doi.org/10.20944/preprints202610.1096.v1"
previewImage: "/daily/2026-10-15/assets/openalex--W7221635720/preview.svg"
---

## 核心内容

针对海洋观测不确定性经声速剖面（SSP）反演、声传播损失（TL）预测与被动声呐检测概率（Pd）估计非线性传播后制约水下探测性能的问题，论文提出一种可微端到端框架，将观测不确定性贯穿SSP反演、声传播与被动声呐Pd计算进行统一追踪，从而实现对主导不确定性源的定量排序，为海洋观测资源配置与探测性能保障提供依据。

## 关键技术与数据

框架采用可微端到端建模，将SSP反演、声场TL预测与被动声呐Pd估计串联为可反向传播的计算图，并以不确定性传播梯度追踪各观测源对最终探测性能的贡献。关键技术涉及可微声传播近似、SSP反演模块与检测概率模型耦合，以及基于梯度的主导源排序。摘要未给出具体数据集、海试区域及网络结构细节。

## 结果与结论

论文应通过端到端梯度传播实现观测不确定性对水下探测性能影响的定量归因，给出主导不确定性源排序，并验证框架在SSP反演、TL预测与Pd估计链路中的可微性与一致性。结论表明该框架可识别对探测性能影响最大的观测源，创新点在于将可微端到端思想引入水声不确定性传播与主导源辨识，支撑观测方案优化。

## 来源链接

- OpenAlex：https://openalex.org/W7221635720
- DOI：https://doi.org/10.20944/preprints202610.1096.v1