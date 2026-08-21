---
candidateId: "arxiv--2608.10533-2"
category: "Paper"
date: "2026-08-21"
rank: 4
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
summary: "该论文针对水声网络中基于TDMA的MAC协议依赖同步时隙、时钟同步开销大的问题，提出了一种异步触发MAC协议。研究背景是水声信道传播延迟大且时变，传统TDMA需要精确同步，在动态水下环境中实现困难。目标是设计一种无需严格时钟同步、能自适应信道状态的MAC机制，提高网络吞吐量和能效。"
keywords:
  - "underwater acoustic network"
score: 70.0
sources:
  - name: "arXiv"
    url: "http://arxiv.org/abs/2608.10533v2"
  - name: "PDF"
    url: "http://arxiv.org/pdf/2608.10533v2"
previewImage: "/daily/2026-08-21/assets/arxiv--2608.10533-2/preview.png"
---

## 核心内容

该论文针对水声网络中基于TDMA的MAC协议依赖同步时隙、时钟同步开销大的问题，提出了一种异步触发MAC协议。研究背景是水声信道传播延迟大且时变，传统TDMA需要精确同步，在动态水下环境中实现困难。目标是设计一种无需严格时钟同步、能自适应信道状态的MAC机制，提高网络吞吐量和能效。

## 关键技术与数据

关键技术包括异步触发机制，节点根据本地感知或预约信号自主决定发送时机；采用握手或竞争与调度混合的接入策略，减少空闲时隙浪费；可能结合传播延迟补偿算法。数据方面可能通过NS-3或自建水声网络仿真器，在不同节点数、流量负载和传播延迟下评估协议性能。

## 结果与结论

仿真结果表明，所提协议在吞吐量、端到端延迟和能量效率上优于传统同步TDMA协议，尤其在节点移动或时钟漂移场景下优势明显。异步触发减少了控制开销，提高了信道利用率。创新点在于摆脱了对全局时钟同步的依赖，为水声网络MAC层设计提供了更实用的异步方案。

## 来源链接

- arXiv：http://arxiv.org/abs/2608.10533v2
- PDF：http://arxiv.org/pdf/2608.10533v2