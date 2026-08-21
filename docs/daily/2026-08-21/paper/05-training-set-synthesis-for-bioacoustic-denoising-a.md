---
candidateId: "arxiv--2608.10054-1"
category: "Paper"
date: "2026-08-21"
rank: 5
title: "Training Set Synthesis for Bioacoustic Denoising: A Case Study With Mice"
authors:
  - "Reyhaneh Abbasi"
  - "Peter Balazs"
  - "Vincent Lostanlen"
  - "Clara Hollomey"
  - "Dustin J. Penn"
  - "Sarah M. Zala"
  - "Nicki Holighaus"
research_direction: []
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "该论文针对生物声学信号（以小鼠发声为例）去噪中干净训练数据稀缺的问题，提出了一种训练集合成方法。研究背景是野外或实验室记录常混有环境噪声，弱发声信号被掩盖，而U-Net等监督去噪模型需要大量干净-带噪配对数据。目标是开发一种数据合成策略，使深度去噪模型能有效处理真实生物声学噪声。"
keywords:
  - "classification"
  - "neural network"
  - "tracking"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2608.10054v1"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2608.10054v1"
previewImage: "/daily/2026-08-21/assets/arxiv--2608.10054-1/preview.png"
---

## 核心内容

该论文针对生物声学信号（以小鼠发声为例）去噪中干净训练数据稀缺的问题，提出了一种训练集合成方法。研究背景是野外或实验室记录常混有环境噪声，弱发声信号被掩盖，而U-Net等监督去噪模型需要大量干净-带噪配对数据。目标是开发一种数据合成策略，使深度去噪模型能有效处理真实生物声学噪声。

## 关键技术与数据

关键技术包括训练集合成流程，将干净的小鼠发声片段与多种实测或模拟噪声（如笼内噪声、通风噪声）按不同信噪比混合，生成配对训练数据；采用U-Net架构进行监督去噪，预测时频掩码或直接估计干净频谱。数据方面使用公开的小鼠声学数据库，并人工标注干净发声段。

## 结果与结论

实验结果显示，基于合成数据训练的U-Net模型在真实带噪录音上的去噪效果显著，提高了发声检测和分类的准确率，且优于传统谱减法或维纳滤波。合成训练策略有效缓解了数据稀缺问题。创新点在于将语音增强中的训练集合成思路迁移到生物声学领域，验证了跨域数据增强的可行性。

## 来源链接

- arXiv：http://arxiv.org/abs/2608.10054v1
- PDF：http://arxiv.org/pdf/2608.10054v1