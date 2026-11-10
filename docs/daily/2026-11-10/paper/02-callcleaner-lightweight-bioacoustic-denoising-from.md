---
candidateId: "arxiv--2611.11491-1"
category: "Paper"
date: "2026-11-10"
rank: 2
title: "CallCleaner: Lightweight Bioacoustic Denoising from an Audio Foundation Model"
authors:
  - "Michael Xie"
  - "Gašper Beguš"
  - "Morris Alper"
research_direction: []
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "该论文针对动物声学研究中野外录音背景噪声污染严重、干净训练数据稀缺及动物发声多样性大的问题，提出轻量级生物声学降噪方法CallCleaner。研究目标是借助音频基础模型实现无需干净配对数据的降噪，提升动物发声录音质量以支撑后续声学分析。"
keywords:
  - "detection"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2611.11491v1"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2611.11491v1"
previewImage: "/daily/2026-11-10/assets/arxiv--2611.11491-1/preview.png"
---

## 核心内容

该论文针对动物声学研究中野外录音背景噪声污染严重、干净训练数据稀缺及动物发声多样性大的问题，提出轻量级生物声学降噪方法CallCleaner。研究目标是借助音频基础模型实现无需干净配对数据的降噪，提升动物发声录音质量以支撑后续声学分析。

## 关键技术与数据

方法基于音频基础模型构建轻量级降噪器，规避对干净训练数据的依赖；对比对象包括传统谱门限（尤其无VAD时残留噪声明显）和面向生物声学的无检测器神经网络降噪器。涉及动物发声野外录音数据。

## 结果与结论

研究表明所提方法在噪声去除效果上优于传统谱门限和无检测器神经降噪器，且模型轻量。创新点在于利用音频基础模型解决生物声学降噪中干净数据稀缺与发声多样性难题，为野外动物声学监测提供实用降噪工具。

## 来源链接

- arXiv：http://arxiv.org/abs/2611.11491v1
- PDF：http://arxiv.org/pdf/2611.11491v1