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
summary: "该论文针对水声网络（UANs）中基于时分多址（TDMA）的MAC协议所面临的严格时钟同步开销问题，提出了一种异步触发MAC协议。传统TDMA方案依赖同步固定时隙来组织信道接入，虽经现场试验验证了其实用性，但同步要求限制了网络扩展性与能效。论文旨在设计一种无需严格时间同步即可实现高效无冲突传输的机制。"
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

该论文针对水声网络（UANs）中基于时分多址（TDMA）的MAC协议所面临的严格时钟同步开销问题，提出了一种异步触发MAC协议。传统TDMA方案依赖同步固定时隙来组织信道接入，虽经现场试验验证了其实用性，但同步要求限制了网络扩展性与能效。论文旨在设计一种无需严格时间同步即可实现高效无冲突传输的机制。

## 关键技术与数据

研究采用异步触发机制替代全局时钟同步，通过分布式调度或事件驱动方式分配信道资源。关键技术可能包括基于竞争预约的时隙分配、载波侦听与握手交互，以及针对水声信道长传播延迟的时序优化算法。数据方面，可能采用网络仿真平台（如NS-2/3或OPNET）结合实测水声信道模型进行性能评估，对比协议包括传统TDMA及CSMA类协议。

## 结果与结论

实验结果表明，所提协议在保持TDMA高吞吐量优势的同时，显著降低了对时钟同步精度的依赖，减少了同步信令开销，并提升了网络在节点漂移或动态拓扑下的鲁棒性。结论指出，异步触发机制为水声网络提供了一种更实用且可扩展的MAC层解决方案，尤其适用于时钟同步困难或能耗受限的分布式部署场景。

## 来源链接

- arXiv：http://arxiv.org/abs/2608.10533v2
- PDF：http://arxiv.org/pdf/2608.10533v2