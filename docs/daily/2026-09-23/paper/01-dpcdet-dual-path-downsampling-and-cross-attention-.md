---
candidateId: "openalex--W7213896152"
category: "Paper"
date: "2026-09-23"
rank: 1
title: "DPCDet: Dual-path downsampling and cross-attention enhanced detector for forward sonar image"
authors:
  - "Jie Li"
  - "Ziqi Xia"
  - "Chunyan Zhang"
  - "Guangming Xie"
  - "Jianlei Zhang"
research_direction:
  - "水声成像"
journal: "Ocean Engineering"
publisher: "Elsevier BV"
doi: "10.1016/j.oceaneng.2026.128255"
publication_year: 2026
summary: "前视声呐是水下感知的重要手段，但其图像存在分辨率低、纹理弱、信噪比低等问题，对通用检测模型构成挑战。现有检测网络通过连续下采样丢失细节，削弱了有限的语义线索；基于残差的跨层融合缺乏对跨阶段特征重要性的动态建模；声呐噪声还会降低图像质量并影响检测精度。本文提出DPCDet检测器，旨在提升前视声呐图像的目标检测性能。"
keywords:
  - "detection"
  - "forward-looking sonar"
score: 78.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7213896152"
  - name: "DOI"
    url: "https://doi.org/10.1016/j.oceaneng.2026.128255"
previewImage: "/daily/2026-09-23/assets/openalex--W7213896152/preview.png"
---

## 核心内容

前视声呐是水下感知的重要手段，但其图像存在分辨率低、纹理弱、信噪比低等问题，对通用检测模型构成挑战。现有检测网络通过连续下采样丢失细节，削弱了有限的语义线索；基于残差的跨层融合缺乏对跨阶段特征重要性的动态建模；声呐噪声还会降低图像质量并影响检测精度。本文提出DPCDet检测器，旨在提升前视声呐图像的目标检测性能。

## 关键技术与数据

提出双路径下采样（Dual-path Downsampling）模块与交叉注意力（Cross-attention）增强机制。双路径下采样旨在缓解连续下采样导致的细节丢失问题，交叉注意力用于动态建模跨阶段特征的重要性。针对声呐噪声问题，网络设计中融入噪声鲁棒性考量。具体数据集信息摘要中未完整给出，推测使用前视声呐实测或仿真图像数据集进行验证。

## 结果与结论

摘要信息不完整，未能获取具体性能指标。从方法设计来看，创新点在于：1）双路径下采样结构保留更多空间细节；2）交叉注意力实现跨阶段特征的动态融合，替代传统残差融合的静态方式；3）对声呐噪声的鲁棒性设计。预期在低信噪比前视声呐图像检测任务上取得优于通用检测器的性能。

## 来源链接

- OpenAlex：https://openalex.org/W7213896152
- DOI：https://doi.org/10.1016/j.oceaneng.2026.128255