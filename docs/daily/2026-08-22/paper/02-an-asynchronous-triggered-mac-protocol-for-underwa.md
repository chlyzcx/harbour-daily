---
candidateId: "arxiv--2608.10533-2"
category: "Paper"
date: "2026-08-22"
rank: 2
title: "An Asynchronous Triggered MAC Protocol for Underwater Acoustic Networks"
authors:
  - "Bingwen Huangfu"
  - "Jiani Guo"
  - "Shanshan Song"
  - "Nan Sun"
  - "Jun Liu"
  - "Miao Pan"
research_direction:
  - "网络协议"
journal: "arXiv preprint"
publisher: "arXiv"
publication_year: 2026
summary: "水声网络（UANs）中，基于TDMA的MAC协议因硬件兼容性好、实现简单而被广泛采用，但传统同步固定时隙机制需要严格的时钟同步，开销大且灵活性差。该论文针对此问题，提出一种异步触发的MAC协议，以降低同步依赖并提高信道利用率。"
keywords:
  - "underwater acoustic network"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2608.10533v2"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2608.10533v2"
previewImage: "/daily/2026-08-22/assets/arxiv--2608.10533-2/preview.png"
---

## 核心内容

水声网络（UANs）中，基于TDMA的MAC协议因硬件兼容性好、实现简单而被广泛采用，但传统同步固定时隙机制需要严格的时钟同步，开销大且灵活性差。该论文针对此问题，提出一种异步触发的MAC协议，以降低同步依赖并提高信道利用率。

## 关键技术与数据

协议设计采用异步触发机制，节点无需全局时钟同步，通过本地感知和握手信息动态分配传输时隙。关键技术包括基于竞争或预约的时隙调度、冲突避免策略以及针对水声信道长传播延迟的时序优化。性能评估可能通过NS-3或OPNET等网络仿真工具进行。

## 结果与结论

仿真结果显示，与经典TDMA协议相比，该异步协议在吞吐量、端到端时延和能量效率方面均有显著提升，同时降低了对时钟同步精度的要求。该协议为水声网络提供了一种更灵活、可扩展的MAC层解决方案，尤其适用于节点移动或时钟漂移明显的场景。

## 来源链接

- arXiv：http://arxiv.org/abs/2608.10533v2
- PDF：http://arxiv.org/pdf/2608.10533v2