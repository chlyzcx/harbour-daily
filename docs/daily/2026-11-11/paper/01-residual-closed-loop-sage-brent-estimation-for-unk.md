---
candidateId: "arxiv--2611.13699-1"
category: "Paper"
date: "2026-11-11"
rank: 1
title: "Residual-Closed-Loop SAGE-Brent Estimation for Unknown-Order Wideband Underwater Acoustic Channels"
authors:
  - "Wenxu Bi"
  - "Peng Chen"
  - "Wei Wang"
research_direction: []
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "该论文针对宽带水声信道估计中网格失配导致的结构化残留问题展开研究。强路径消除后的残留会产生虚假相关峰或掩盖弱到达路径，使连续参数误差转化为路径数误差。论文提出RC-SAGE-Brent残差闭环估计器，旨在联合精化连续时延-尺度参数并校正未知阶数的路径集合，从而提升宽带水声信道估计的精度与鲁棒性。"
keywords:
  - "channel estimation"
  - "detection"
  - "sparse"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2611.13699v1"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2611.13699v1"
previewImage: "/daily/2026-11-11/assets/arxiv--2611.13699-1/preview.png"
---

## 核心内容

该论文针对宽带水声信道估计中网格失配导致的结构化残留问题展开研究。强路径消除后的残留会产生虚假相关峰或掩盖弱到达路径，使连续参数误差转化为路径数误差。论文提出RC-SAGE-Brent残差闭环估计器，旨在联合精化连续时延-尺度参数并校正未知阶数的路径集合，从而提升宽带水声信道估计的精度与鲁棒性。

## 关键技术与数据

采用残差闭环反馈架构，在每个反馈周期内使用模糊约束交替Brent搜索抑制强路径干扰；结合SAGE（空间交替广义期望最大化）算法进行参数迭代优化，实现时延-尺度连续参数与路径阶数的联合估计。通过闭环残差反馈机制动态修正路径集合，解决网格失配引起的路径数误判问题。

## 结果与结论

该方法有效抑制了结构化残留引起的虚假相关峰，改善了弱路径检测能力，降低了连续参数误差向路径数误差的转化率。RC-SAGE-Brent在未知阶数宽带水声信道条件下实现了更准确的路径集合估计与参数精化，为复杂水声环境下的信道建模提供了有效手段。

## 来源链接

- arXiv：http://arxiv.org/abs/2611.13699v1
- PDF：http://arxiv.org/pdf/2611.13699v1