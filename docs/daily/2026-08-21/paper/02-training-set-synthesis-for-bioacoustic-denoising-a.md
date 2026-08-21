---
candidateId: "arxiv--2608.10054-1"
category: "Paper"
date: "2026-08-21"
rank: 2
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
summary: "Bioacoustic recordings are often degraded by ambient noise, which complicates the analysis of weak or noise-overlapped vocalizations. Convolutional neural networks, particularly U-Net architectures, have shown a strong denoising performance in speech and music processing. However, their direct application to bioacoustic signals is limited by the scarcity of clean training data. To address this issue, we propose a training set synthesis approach and develop a supervised denoising model that predi..."
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

Bioacoustic recordings are often degraded by ambient noise, which complicates the analysis of weak or noise-overlapped vocalizations. Convolutional neural networks, particularly U-Net architectures, have shown a strong denoising performance in speech and music processing. However, their direct application to bioacoustic signals is limited by the scarcity of clean training data. To address this issue, we propose a training set synthesis approach and develop a supervised denoising model that predi...

## 关键技术与数据

提出一种训练集合成方法用于生物声学降噪，以小鼠超声声为例，通过模拟真实环境噪声与干净叫声混合生成配对训练数据，构建基于U-Net的监督降噪模型，预测干净频谱掩码，解决真实生物声学数据缺乏干净标签的问题。

## 结果与结论

合成训练策略有效提升模型在真实噪声环境下的降噪性能，优于直接使用通用语音降噪模型，验证了数据合成方法在生物声学信号处理中的可行性，为弱信号提取与噪声抑制提供了可复现的解决方案。

## 来源链接

- arXiv：http://arxiv.org/abs/2608.10054v1
- PDF：http://arxiv.org/pdf/2608.10054v1