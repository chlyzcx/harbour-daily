---
candidateId: "openalex--W7207653516"
category: "Paper"
date: "2026-09-05"
rank: 3
title: "A physics-informed and data-driven framework for AUV side-scan sonar imaging quality prediction under motion-induced degradation"
authors:
  - "Zhenyu Wang"
  - "Haibo Lei"
  - "Hao Feng"
  - "Jianan Qiao"
  - "Yan Huang"
  - "Jiancheng Yu"
research_direction: []
journal: "Ocean Engineering"
publisher: "Elsevier BV"
doi: "10.1016/j.oceaneng.2026.127967"
publication_year: 2026
summary: "该论文提出一种物理信息与数据驱动融合的框架，用于预测AUV侧扫声呐在运动退化条件下的成像质量。背景是AUV航行中的姿态波动、航速变化等运动扰动导致侧扫声呐图像畸变与模糊，影响海底目标判读。目标是通过融合物理模型与深度学习，实现成像质量的提前预测，为航迹规划与参数调整提供支持。"
keywords: []
score: 65.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7207653516"
  - name: "DOI"
    url: "https://doi.org/10.1016/j.oceaneng.2026.127967"
previewImage: "/daily/2026-09-05/assets/openalex--W7207653516/preview.png"
---

## 核心内容

该论文提出一种物理信息与数据驱动融合的框架，用于预测AUV侧扫声呐在运动退化条件下的成像质量。背景是AUV航行中的姿态波动、航速变化等运动扰动导致侧扫声呐图像畸变与模糊，影响海底目标判读。目标是通过融合物理模型与深度学习，实现成像质量的提前预测，为航迹规划与参数调整提供支持。

## 关键技术与数据

关键技术包括声呐成像物理模型（考虑波束几何、运动补偿误差）与深度神经网络结合，物理模型生成运动退化特征作为网络输入先验，数据驱动部分采用卷积或循环网络学习质量映射关系。数据来源为仿真侧扫声呐图像与实测AUV运动参数，涵盖不同航速、横滚、升沉等退化条件，输出为图像质量指标（如分辨率、对比度）。

## 结果与结论

实验显示该框架能较准确预测不同运动条件下的成像质量，预测误差低于纯数据驱动方法，且对未见运动场景具有一定泛化能力。结论是物理约束有效提升模型可解释性与预测精度，创新点在于将声呐成像机理嵌入深度学习预测流程，为AUV自适应声呐采集提供了智能决策工具。

## 来源链接

- OpenAlex：https://openalex.org/W7207653516
- DOI：https://doi.org/10.1016/j.oceaneng.2026.127967