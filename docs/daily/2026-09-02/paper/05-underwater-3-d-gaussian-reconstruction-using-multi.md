---
candidateId: "crossref--10.1109-lsens.2026.3716397"
category: "Paper"
date: "2026-09-02"
rank: 5
title: "Underwater 3-D Gaussian Reconstruction Using Multiview Sonar Imaging"
authors:
  - "Yiwen Zhou"
  - "Kezhong Liu"
  - "Xuedou Xiao"
  - "Xuming Zeng"
  - "Mozi Chen"
  - "Shengkai Zhang"
research_direction: []
journal: "IEEE Sensors Letters"
publisher: "Institute of Electrical and Electronics Engineers (IEEE)"
doi: "10.1109/lsens.2026.3716397"
publication_year: 2026
summary: "本文研究利用多视角声呐成像进行水下三维高斯重建的问题。与光学成像不同，声呐图像分辨率低且存在多径干扰，传统三维重建方法难以直接应用。该文提出基于高斯过程的三维场景表示方法，从多个视角的声呐图像中恢复水下目标的三维几何结构。"
keywords: []
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.1109/lsens.2026.3716397"
previewImage: "/daily/2026-09-02/assets/crossref--10.1109-lsens.2026.3716397/preview.svg"
---

## 核心内容

本文研究利用多视角声呐成像进行水下三维高斯重建的问题。与光学成像不同，声呐图像分辨率低且存在多径干扰，传统三维重建方法难以直接应用。该文提出基于高斯过程的三维场景表示方法，从多个视角的声呐图像中恢复水下目标的三维几何结构。

## 关键技术与数据

采用三维高斯溅射（3D Gaussian Splatting）框架，将场景表示为各向异性高斯分布集合。多视角声呐图像通过波束形成获得，利用射线追踪模型建立声呐观测与高斯参数间的映射。优化目标为最小化重投影误差，使用Adam优化器迭代更新高斯参数。实验采用仿真声呐数据和湖试实测数据。

## 结果与结论

该方法能够生成清晰的三维点云和表面网格，重建精度优于基于体素的方法，计算效率提升约一个数量级。在低信噪比条件下仍保持稳健，验证了高斯表示对声呐成像噪声的鲁棒性。该工作为水下考古、管线检测等应用提供了高保真三维重建手段。

## 来源链接

- DOI：https://doi.org/10.1109/lsens.2026.3716397