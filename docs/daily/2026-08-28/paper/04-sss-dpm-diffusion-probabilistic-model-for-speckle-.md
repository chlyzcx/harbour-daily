---
candidateId: "s2--51526ac66110d9bb1d242e4801a52d5135df9258"
category: "Paper"
date: "2026-08-28"
rank: 4
title: "SSS-DPM: Diffusion Probabilistic Model for Speckle Noise Reduction in Side-Scan Sonar Images"
authors:
  - "Qi Wang"
  - "Bo He"
research_direction: []
journal: "IEEE Transactions on Geoscience and Remote Sensing"
publisher: "Semantic Scholar"
doi: "10.1109/TGRS.2026.3656240"
publication_year: 2026
summary: "搭载于自主水下航行器（AUV）的侧扫声呐（SSS）可实现高效精确的海底测绘与水下探测。然而SSS图像常受海底混响、环境干扰和自噪声影响，其中亚分辨率散射体产生的散斑噪声尤为显著。这种信号相关的乘性噪声不仅降低图像质量，还使特征提取复杂化。本文提出SSS-DPM，一种用于侧扫声呐图像散斑噪声抑制的扩散概率模型。"
keywords: []
score: 62.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.1109/TGRS.2026.3656240"
  - name: "Semantic Scholar"
    url: "https://www.semanticscholar.org/paper/51526ac66110d9bb1d242e4801a52d5135df9258"
previewImage: "/daily/2026-08-28/assets/s2--51526ac66110d9bb1d242e4801a52d5135df9258/preview.svg"
---

## 核心内容

搭载于自主水下航行器（AUV）的侧扫声呐（SSS）可实现高效精确的海底测绘与水下探测。然而SSS图像常受海底混响、环境干扰和自噪声影响，其中亚分辨率散射体产生的散斑噪声尤为显著。这种信号相关的乘性噪声不仅降低图像质量，还使特征提取复杂化。本文提出SSS-DPM，一种用于侧扫声呐图像散斑噪声抑制的扩散概率模型。

## 关键技术与数据

方法基于扩散概率模型（DPM），通过正向扩散过程将含噪图像逐步转化为高斯噪声，再学习逆向过程实现去噪。针对散斑噪声的乘性特性，模型在扩散过程中引入信号相关噪声建模。训练数据为实测SSS图像及仿真生成的含散斑图像对，用于学习噪声分布与图像先验。

## 结果与结论

实验表明SSS-DPM在散斑抑制和细节保持方面优于传统滤波器和深度学习方法，PSNR与SSIM指标均有提升。创新点在于将扩散模型成功应用于SSS图像乘性散斑去噪，利用生成式先验有效恢复海底细节，为声呐图像处理提供了新的生成式去噪范式。

## 来源链接

- DOI：https://doi.org/10.1109/TGRS.2026.3656240
- Semantic Scholar：https://www.semanticscholar.org/paper/51526ac66110d9bb1d242e4801a52d5135df9258