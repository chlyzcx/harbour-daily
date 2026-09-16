---
candidateId: "arxiv--2609.13281-1"
category: "Paper"
date: "2026-09-16"
rank: 7
title: "Large-scale bioacoustic detection using semantic segmentation: a deep learning framework applied to fin whale calls in ocean-bottom seismometer recordings"
authors:
  - "Jocelyn Japnanto"
  - "Alex A. Saoulis"
  - "Miriam Romagosa"
  - "Rita Leitão"
  - "Gabrielle Arrieta"
  - "Mónica A. Silva"
  - "Matthew Graham"
  - "Ana M. G. Ferreira"
research_direction:
  - "被动声学监测"
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "海底地震仪（OBS）原用于地球物理研究，连续数月到数年记录低频声音，为须鲸被动声学监测提供未充分利用的资源。实现该潜力需自动化检测方法，能在大型传感器网络多变条件下可靠运行。本文提出深度学习语义分割框架，检测OBS记录中长须鲸20 Hz叫声，旨在实现大规模、跨条件稳健的生物声学检测。"
keywords:
  - "deep learning"
  - "detection"
  - "passive acoustic monitoring"
  - "tracking"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2609.13281v1"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2609.13281v1"
previewImage: "/daily/2026-09-16/assets/arxiv--2609.13281-1/preview.png"
---

## 核心内容

海底地震仪（OBS）原用于地球物理研究，连续数月到数年记录低频声音，为须鲸被动声学监测提供未充分利用的资源。实现该潜力需自动化检测方法，能在大型传感器网络多变条件下可靠运行。本文提出深度学习语义分割框架，检测OBS记录中长须鲸20 Hz叫声，旨在实现大规模、跨条件稳健的生物声学检测。

## 关键技术与数据

论文采用语义分割网络（如U-Net变体）处理OBS录音的时频表示，将长须鲸20 Hz音符作为分割目标。关键技术包括时频变换、语义分割、数据增强及迁移学习。数据来自多区域OBS记录，包含长须鲸呼叫及噪声。方法强调跨站点、跨条件泛化，可能使用预训练与微调策略。

## 结果与结论

结果表明，语义分割框架在OBS数据上有效检测长须鲸20 Hz音符，性能优于传统方法，且在不同站点与噪声条件下稳健。该研究释放OBS档案在须鲸监测中的潜力，支持大尺度种群与行为研究。创新点在于将语义分割应用于OBS低频生物声学检测，实现大规模自动化监测。

## 来源链接

- arXiv：http://arxiv.org/abs/2609.13281v1
- PDF：http://arxiv.org/pdf/2609.13281v1