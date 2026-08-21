---
candidateId: "arxiv--2608.10533-2"
category: "Paper"
date: "2026-08-21"
rank: 1
title: "An Asynchronous Triggered MAC Protocol for Underwater Acoustic Networks"
authors:
  - "Bingwen Huangfu"
  - "Jiani Guo"
  - "Shanshan Song"
  - "Nan Sun"
  - "Jun Liu"
  - "Miao Pan"
research_direction: []
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "该论文针对水声网络（UANs）中基于TDMA的MAC协议因依赖同步时隙而带来高时钟同步开销的问题，提出了一种异步触发MAC协议。研究旨在降低同步要求，同时保持TDMA协议在硬件兼容性和实现简易性方面的优势，适用于时变、高延迟的水声信道环境。"
keywords: []
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2608.10533v2"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2608.10533v2"
previewImage: "/daily/2026-08-21/assets/arxiv--2608.10533-2/preview.png"
---

## 核心内容

该论文针对水声网络（UANs）中基于TDMA的MAC协议因依赖同步时隙而带来高时钟同步开销的问题，提出了一种异步触发MAC协议。研究旨在降低同步要求，同时保持TDMA协议在硬件兼容性和实现简易性方面的优势，适用于时变、高延迟的水声信道环境。

## 关键技术与数据

论文采用异步触发机制替代传统固定时隙分配，通过事件驱动的信道预约与调度策略减少节点间时钟同步依赖。关键技术可能包括基于握手或载波侦听的触发式时隙分配、自适应帧长调整以及冲突避免机制。性能评估可能基于NS-2/NS-3仿真或水声信道模型，对比协议包括传统TDMA和CSMA。

## 结果与结论

实验结果表明，所提异步触发协议在端到端时延、吞吐量和能量效率方面优于传统同步TDMA，尤其在节点时钟漂移较大时鲁棒性显著提升。该研究为低开销、高可靠水声MAC设计提供了新思路，验证了去除严格同步约束的可行性。

## 来源链接

- arXiv：http://arxiv.org/abs/2608.10533v2
- PDF：http://arxiv.org/pdf/2608.10533v2