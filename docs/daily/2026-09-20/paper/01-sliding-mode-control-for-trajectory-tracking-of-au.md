---
candidateId: "crossref--10.1177-09596518261477964"
category: "Paper"
date: "2026-09-20"
rank: 1
title: "Sliding mode control for trajectory tracking of autonomous underwater vehicles via predefined time disturbance observer"
authors:
  - "Yong Yu"
  - "Zhankui Song"
  - "Wudeng Wang"
research_direction: []
journal: "Proceedings of the Institution of Mechanical Engineers, Part I: Journal of Systems and Control Engineering"
publisher: "SAGE Publications"
doi: "10.1177/09596518261477964"
publication_year: 2026
summary: "本文针对自主水下航行器（AUV）在集总扰动（模型不确定性与未知时变外部扰动）下的轨迹跟踪控制问题，研究了具有预设性能约束的控制方法。目标是实现AUV在复杂海洋环境中的高精度轨迹跟踪，并保证闭环系统在预设时间内收敛。主要内容包括建立实用的预设时间Lyapunov判据以刻画闭环收敛特性，并设计连续预设时间扰动观测器，在预设时间内估计集总扰动，进而构建滑模跟踪控制器。"
keywords:
  - "time-varying"
  - "tracking"
score: 55.0
sources:
  - name: "DOI"
    url: "https://doi.org/10.1177/09596518261477964"
previewImage: "/daily/2026-09-20/assets/crossref--10.1177-09596518261477964/preview.svg"
---

## 核心内容

本文针对自主水下航行器（AUV）在集总扰动（模型不确定性与未知时变外部扰动）下的轨迹跟踪控制问题，研究了具有预设性能约束的控制方法。目标是实现AUV在复杂海洋环境中的高精度轨迹跟踪，并保证闭环系统在预设时间内收敛。主要内容包括建立实用的预设时间Lyapunov判据以刻画闭环收敛特性，并设计连续预设时间扰动观测器，在预设时间内估计集总扰动，进而构建滑模跟踪控制器。

## 关键技术与数据

关键技术包括：预设时间Lyapunov稳定性理论、滑模控制（SMC）、预设时间扰动观测器（PTDO）、预设性能函数（PPF）约束。方法上采用连续扰动观测器对集总扰动进行前馈补偿，结合滑模面设计实现鲁棒跟踪。数据方面，摘要未提及具体数据集，通常通过数值仿真在典型AUV模型（如REMUS、ODIN等）上验证，对比PID、传统SMC等方法，评估跟踪误差、收敛时间与抗扰性能。

## 结果与结论

结果表明，所提方法可在预设时间内实现扰动估计与轨迹跟踪，闭环信号一致最终有界，跟踪误差满足预设性能约束。相比传统方法，收敛时间可预先设定且不依赖初始条件，抖振得到抑制。创新点在于将预设时间收敛与扰动观测器结合用于AUV轨迹跟踪，提升了鲁棒性与工程可调性。结论是该控制策略适用于强扰动、高精度要求的AUV作业场景。

## 来源链接

- DOI：https://doi.org/10.1177/09596518261477964