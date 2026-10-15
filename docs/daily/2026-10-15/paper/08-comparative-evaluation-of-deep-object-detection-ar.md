---
candidateId: "openalex--W7221599064"
category: "Paper"
date: "2026-10-15"
rank: 8
title: "Comparative Evaluation of Deep Object Detection Architectures for Automatic Target Recognition in Real-World AUV-Acquired Side-Scan Sonar Imagery"
authors:
  - "Daniel Powarzyński"
  - "Norbert Sigiel"
  - "Aleksander Cirocki"
  - "Mateusz Toporek"
research_direction: []
journal: "Sensors"
publisher: "Multidisciplinary Digital Publishing Institute"
doi: "10.3390/s26206486"
publication_year: 2026
summary: "针对水声目标探测中侧扫声呐（SSS）图像人工判读效率低的问题，该论文面向AUV实测侧扫声呐图像，开展自动目标识别（ATR）研究。研究背景源于水雷对抗、未爆弹药调查、航行障碍评估及海底基础设施巡检等任务对可靠水下目标检测的迫切需求。论文旨在系统比较多种深度目标检测架构在真实AUV采集SSS图像上的性能，以评估其用于ATR任务的适用性与鲁棒性，为后续自动化判读提供依据。"
keywords:
  - "detection"
score: 56.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7221599064"
  - name: "DOI"
    url: "https://doi.org/10.3390/s26206486"
previewImage: "/daily/2026-10-15/assets/openalex--W7221599064/preview.svg"
---

## 核心内容

针对水声目标探测中侧扫声呐（SSS）图像人工判读效率低的问题，该论文面向AUV实测侧扫声呐图像，开展自动目标识别（ATR）研究。研究背景源于水雷对抗、未爆弹药调查、航行障碍评估及海底基础设施巡检等任务对可靠水下目标检测的迫切需求。论文旨在系统比较多种深度目标检测架构在真实AUV采集SSS图像上的性能，以评估其用于ATR任务的适用性与鲁棒性，为后续自动化判读提供依据。

## 关键技术与数据

论文采用深度学习目标检测方法，对比多种主流架构（如Faster R-CNN、SSD、YOLO系列等）在侧扫声呐图像上的检测性能。数据来源于真实AUV搭载侧扫声呐采集的实测图像，包含多种海底目标与复杂背景。关键技术涉及声呐图像预处理、数据增强、迁移学习及模型训练与推理优化，并针对SSS图像低信噪比、目标尺度差异大、纹理模糊等特点进行适配。评价指标包括检测精度、召回率及推理速度等。

## 结果与结论

实验结果表明，不同深度检测架构在真实SSS图像上的性能存在显著差异，部分单阶段检测器在推理速度上占优，而两阶段检测器在复杂背景下精度更高。论文总结了各架构在AUV侧扫声呐ATR任务中的优缺点，指出需在精度与实时性之间权衡。创新点在于基于真实AUV实测数据开展系统性对比评估，为水声工程中ATR模型选型提供实证参考，并指出未来需进一步优化小目标检测与跨域泛化能力。

## 来源链接

- OpenAlex：https://openalex.org/W7221599064
- DOI：https://doi.org/10.3390/s26206486