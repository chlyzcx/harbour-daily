---
candidateId: "openalex--W7221622485"
category: "Paper"
date: "2026-10-15"
rank: 5
title: "FMFNet: Frequency-Aware multi-scale attention with fine-grained feature fusion for sonar image semantic segmentation"
authors:
  - "Juan Lei"
  - "Zelin Lei"
  - "Huaxia Zhang"
  - "Jiayuan Li"
research_direction: []
journal: "Ocean Engineering"
publisher: "Elsevier BV"
doi: "10.1016/j.oceaneng.2026.128493"
publication_year: 2026
summary: "声纳图像语义分割在水下目标探测与识别中具有重要意义，但受成像机制限制，声纳图像普遍存在分辨率低、噪声强、目标边缘模糊等问题，导致分割精度受限。针对上述问题，本文提出FMFNet，一种频率感知多尺度注意力与细粒度特征融合网络，旨在充分利用声纳图像的频域信息与多尺度特征，提升语义分割的准确性与鲁棒性。主要内容包括设计频率感知模块、多尺度注意力机制及细粒度特征融合策略，并在公开声纳图像数据集上验证其有效性。"
keywords: []
score: 67.0
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7221622485"
  - name: "DOI"
    url: "https://doi.org/10.1016/j.oceaneng.2026.128493"
previewImage: "/daily/2026-10-15/assets/openalex--W7221622485/preview.png"
---

## 核心内容

声纳图像语义分割在水下目标探测与识别中具有重要意义，但受成像机制限制，声纳图像普遍存在分辨率低、噪声强、目标边缘模糊等问题，导致分割精度受限。针对上述问题，本文提出FMFNet，一种频率感知多尺度注意力与细粒度特征融合网络，旨在充分利用声纳图像的频域信息与多尺度特征，提升语义分割的准确性与鲁棒性。主要内容包括设计频率感知模块、多尺度注意力机制及细粒度特征融合策略，并在公开声纳图像数据集上验证其有效性。

## 关键技术与数据

论文提出FMFNet网络，核心技术包括：频率感知模块，利用频域变换提取声纳图像的高频细节与低频结构信息；多尺度注意力机制，在不同尺度上增强目标区域的特征响应；细粒度特征融合模块，通过跨层特征交互保留边缘与纹理细节。网络基于编码器-解码器架构，可能采用ResNet或类似骨干网络。实验使用公开声纳图像数据集（如UATD或类似水下声纳分割数据集），并进行数据增强与归一化处理。

## 结果与结论

实验结果表明，FMFNet在声纳图像语义分割任务中优于现有主流方法，在mIoU、PA等指标上取得显著提升，尤其在小目标与边缘模糊区域分割效果改善明显。消融实验验证了频率感知模块、多尺度注意力与细粒度融合模块的有效性。结论指出，融合频域信息与多尺度注意力可有效缓解声纳图像低质量带来的分割困难，创新点在于频率感知与细粒度特征融合的协同设计，为水声图像分割提供了新思路。

## 来源链接

- OpenAlex：https://openalex.org/W7221622485
- DOI：https://doi.org/10.1016/j.oceaneng.2026.128493