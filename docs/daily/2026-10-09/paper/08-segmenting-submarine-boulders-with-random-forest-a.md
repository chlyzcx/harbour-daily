---
candidateId: "openalex--W7220854926"
category: "Paper"
date: "2026-10-09"
rank: 8
title: "Segmenting submarine boulders with Random Forest and nnU-Net: from bathymetric rasters to survey-scale size distributions"
authors:
  - "Aïcha Naumann"
  - "Robert Haase"
  - "Peter Feldens"
  - "Svenja Papenmeier"
research_direction: []
doi: "10.31223/x5tj8d"
publication_year: 2026
summary: "波罗的海南部以软底为主，地质成因硬基质是生物多样性热点，但MBES数据中巨砾的像素级分割方法缺乏，制约了对巨砾场生态理解。本文开发并评估两种分割方法，目标是从测深栅格中分割海底巨砾并获取调查尺度粒径分布。研究旨在推动波罗的海巨砾场生态研究，提供开源像素级分割方案。"
keywords:
  - "classification"
  - "deep learning"
  - "detection"
  - "machine learning"
  - "sparse"
score: 56.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7220854926"
  - name: "DOI"
    url: "https://doi.org/10.31223/x5tj8d"
previewImage: "/daily/2026-10-09/assets/openalex--W7220854926/preview.png"
---

## 核心内容

波罗的海南部以软底为主，地质成因硬基质是生物多样性热点，但MBES数据中巨砾的像素级分割方法缺乏，制约了对巨砾场生态理解。本文开发并评估两种分割方法，目标是从测深栅格中分割海底巨砾并获取调查尺度粒径分布。研究旨在推动波罗的海巨砾场生态研究，提供开源像素级分割方案。

## 关键技术与数据

关键技术包括随机森林分类（APOC-25）与nnU-Net深度学习分割、多波束测深（MBES）栅格数据处理、粒径分布统计。方法上分别训练经典机器学习与深度学习模型进行巨砾像素级分割，并基于分割结果提取调查尺度粒径分布。数据采用波罗的海南部MBES测深栅格，涵盖软底与硬基质区域，用于模型训练与评估。

## 结果与结论

实验表明，nnU-Net与APOC-25均能有效分割海底巨砾，深度学习模型在复杂边界与不同尺度上表现更优，随机森林方法计算效率更高。基于分割结果可获取调查尺度粒径分布，支持巨砾场生态研究。创新点在于首次系统比较深度学习与经典机器学习在MBES巨砾分割中的性能，提供开源像素级方案，推动波罗的海硬基质生态研究。

## 来源链接

- OpenAlex：https://openalex.org/W7220854926
- DOI：https://doi.org/10.31223/x5tj8d