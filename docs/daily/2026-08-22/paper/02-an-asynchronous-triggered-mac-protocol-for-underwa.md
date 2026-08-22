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
summary: "该论文针对水声网络中传统TDMA协议依赖严格时钟同步、开销大的问题，提出了一种异步触发的MAC协议。研究目标是设计一种无需全局同步、能适应水声信道长传播延迟和节点移动性的信道接入方案，以降低同步开销并提高网络吞吐量和能量效率。"
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

该论文针对水声网络中传统TDMA协议依赖严格时钟同步、开销大的问题，提出了一种异步触发的MAC协议。研究目标是设计一种无需全局同步、能适应水声信道长传播延迟和节点移动性的信道接入方案，以降低同步开销并提高网络吞吐量和能量效率。

## 关键技术与数据

协议设计基于异步触发机制，节点根据本地感知和预约信息动态安排发送时隙，替代固定同步时隙。关键技术包括分布式时隙竞争算法、冲突避免机制以及针对长延迟的握手协议优化。性能评估可能通过NS-3或OPNET等仿真平台，结合典型水声信道模型进行。

## 结果与结论

仿真结果表明，与标准TDMA协议相比，该协议显著降低了控制报文开销和同步能耗，在节点规模变化和移动场景下保持了较高的信道利用率和分组投递率。创新点在于完全去中心化的异步调度思想，为高动态水声网络提供了一种低开销、高可靠的MAC层解决方案。

## 来源链接

- arXiv：http://arxiv.org/abs/2608.10533v2
- PDF：http://arxiv.org/pdf/2608.10533v2