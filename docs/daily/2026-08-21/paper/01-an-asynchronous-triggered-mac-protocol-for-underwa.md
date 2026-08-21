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
summary: "该论文针对水声网络（UANs）中基于时分多址（TDMA）的MAC协议所面临的严格时钟同步开销问题，提出了一种异步触发式MAC协议。传统TDMA方案采用同步固定长度时隙组织信道接入，虽硬件兼容性好且易于实现，但同步开销巨大。该研究旨在设计无需严格时间同步的MAC机制，以提升水声网络的实用性和效率。"
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

该论文针对水声网络（UANs）中基于时分多址（TDMA）的MAC协议所面临的严格时钟同步开销问题，提出了一种异步触发式MAC协议。传统TDMA方案采用同步固定长度时隙组织信道接入，虽硬件兼容性好且易于实现，但同步开销巨大。该研究旨在设计无需严格时间同步的MAC机制，以提升水声网络的实用性和效率。

## 关键技术与数据

论文采用异步触发机制替代传统同步时隙分配，通过事件驱动的方式实现信道接入，避免了节点间频繁的时钟同步协商。关键技术包括基于触发条件的分布式时隙竞争策略、冲突避免机制以及针对水声信道长传播延迟的适配设计。研究可能涉及网络仿真平台，对比了所提协议与标准TDMA在吞吐量、端到端延迟和同步能耗等方面的性能。

## 结果与结论

实验结果表明，所提出的异步触发MAC协议在保持TDMA硬件兼容性优势的同时，显著降低了对时钟同步精度的依赖，减少了因同步维护带来的控制开销和能量消耗。在网络负载变化时，该协议展现出优于传统TDMA的适应性和信道利用率。创新点在于将信道访问从时间同步约束中解放出来，为水声网络提供了一种更鲁棒且易于部署的MAC层解决方案。

## 来源链接

- arXiv：http://arxiv.org/abs/2608.10533v2
- PDF：http://arxiv.org/pdf/2608.10533v2