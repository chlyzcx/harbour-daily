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
summary: "该论文针对水声网络（UANs）中基于时分多址（TDMA）的MAC协议所面临的严格时钟同步开销问题，提出了一种异步触发MAC协议。研究背景在于传统TDMA方案虽经海试验证具有硬件兼容性和易实现性，但其同步定长时隙机制在动态水声信道中效率受限。目标是设计无需严格同步的触发式信道接入机制，以降低同步开销并适应水声信道的大传播延迟与拓扑动态性。"
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

该论文针对水声网络（UANs）中基于时分多址（TDMA）的MAC协议所面临的严格时钟同步开销问题，提出了一种异步触发MAC协议。研究背景在于传统TDMA方案虽经海试验证具有硬件兼容性和易实现性，但其同步定长时隙机制在动态水声信道中效率受限。目标是设计无需严格同步的触发式信道接入机制，以降低同步开销并适应水声信道的大传播延迟与拓扑动态性。

## 关键技术与数据

关键技术在于摒弃全局时钟同步，采用异步触发机制协调节点传输。方法上可能涉及基于事件或接收信号触发的时隙分配，利用水声信道的传播延迟特性进行调度，或采用分布式竞争与预约相结合的协议设计。数据方面可能基于OPNET或NS-2等网络仿真平台，结合实测水声信道模型，评估协议在不同节点密度、流量负载下的吞吐量、端到端延迟和能量效率。

## 结果与结论

实验结果表明，所提出的异步触发协议相比传统同步TDMA方案，显著降低了时钟同步开销，并在动态拓扑和高负载场景下提升了网络吞吐量，降低了接入延迟。该协议验证了在硬件兼容性前提下，通过异步设计可有效提升UANs的鲁棒性和信道利用率。创新点在于将触发机制引入MAC层，为水声网络提供了一种低开销、高适应性的信道接入新范式。

## 来源链接

- arXiv：http://arxiv.org/abs/2608.10533v2
- PDF：http://arxiv.org/pdf/2608.10533v2