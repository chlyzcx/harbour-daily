---
candidateId: "openalex--W7221604707"
category: "Paper"
date: "2026-10-15"
rank: 6
title: "Context‐Aware Reconstruction for DVL Outlier Detection in Robust AUV Navigation"
authors:
  - "Xin Zhang"
  - "Shaolei Li"
  - "Bo He"
  - "Li Sheng"
research_direction:
  - "水下导航"
journal: "Journal of Field Robotics"
publisher: "Wiley"
doi: "10.1002/rob.70369"
publication_year: 2026
summary: "针对复杂浅水环境中环境与声学干扰导致DVL测量异常、进而严重退化AUV导航性能的问题，本文提出一种基于上下文感知重建学习的鲁棒AUV导航策略。研究目标是实现DVL离群值检测，提升导航鲁棒性。主要内容包括构建基于深度自编码器架构的上下文感知重建网络CAR-Net，用于DVL异常测量识别，并将其嵌入AUV导航框架中以抑制异常量测对导航解算的影响。"
keywords:
  - "Doppler velocity log"
  - "detection"
  - "doppler"
score: 64.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7221604707"
  - name: "DOI"
    url: "https://doi.org/10.1002/rob.70369"
previewImage: "/daily/2026-10-15/assets/openalex--W7221604707/preview.svg"
---

## 核心内容

针对复杂浅水环境中环境与声学干扰导致DVL测量异常、进而严重退化AUV导航性能的问题，本文提出一种基于上下文感知重建学习的鲁棒AUV导航策略。研究目标是实现DVL离群值检测，提升导航鲁棒性。主要内容包括构建基于深度自编码器架构的上下文感知重建网络CAR-Net，用于DVL异常测量识别，并将其嵌入AUV导航框架中以抑制异常量测对导航解算的影响。

## 关键技术与数据

论文关键技术为上下文感知重建学习与深度自编码器，提出CAR-Net网络对DVL速度量测进行重建与残差判别，以实现离群值检测。方法利用时序上下文信息建模DVL量测的正常分布，通过重建误差识别异常。摘要未给出具体数据集、训练细节及对比算法，推测采用AUV实测或仿真DVL/惯导组合导航数据验证。

## 结果与结论

摘要未提供具体实验结果与性能指标。结论上，该研究创新性地将上下文感知重建学习引入DVL离群值检测，通过CAR-Net提升异常量测识别能力，从而增强复杂浅水环境下AUV导航鲁棒性。主要贡献在于提出鲁棒AUV导航策略及CAR-Net架构，为DVL异常抑制提供新思路。

## 来源链接

- OpenAlex：https://openalex.org/W7221604707
- DOI：https://doi.org/10.1002/rob.70369