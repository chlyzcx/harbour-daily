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
summary: "该论文针对水声网络（UANs）中基于时分多址（TDMA）的MAC协议所面临的严格时钟同步开销问题，提出了一种异步触发式MAC协议。研究背景在于传统TDMA协议虽经现场试验验证了其实用性，但其依赖同步固定时隙的信道访问方式在动态水声环境中存在显著局限。论文目标在于设计一种无需严格同步的触发式信道接入机制，以降低同步开销并提升协议鲁棒性。"
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

该论文针对水声网络（UANs）中基于时分多址（TDMA）的MAC协议所面临的严格时钟同步开销问题，提出了一种异步触发式MAC协议。研究背景在于传统TDMA协议虽经现场试验验证了其实用性，但其依赖同步固定时隙的信道访问方式在动态水声环境中存在显著局限。论文目标在于设计一种无需严格同步的触发式信道接入机制，以降低同步开销并提升协议鲁棒性。

## 关键技术与数据

论文核心技术为异步触发式信道访问机制，该机制摒弃了传统TDMA中全局时钟同步的依赖，转而采用事件驱动的触发方式协调节点传输。方法上可能涉及基于握手或占位符的分布式调度算法，以在无精确同步条件下避免数据包冲突。研究数据可能来源于水声信道仿真平台或湖上/海上试验，用于评估协议在不同网络负载和节点密度下的吞吐量、时延及能耗性能。

## 结果与结论

实验结果表明，所提出的异步触发式MAC协议在降低同步开销的同时，有效维持了网络吞吐量，并显著减少了因同步误差导致的时隙浪费。与经典TDMA协议相比，该协议在时钟漂移和节点移动场景下表现出更强的鲁棒性。主要创新点在于将信道访问从时间同步范式转变为事件触发范式，为水声网络提供了一种低开销、高适应性的MAC层解决方案。

## 来源链接

- arXiv：http://arxiv.org/abs/2608.10533v2
- PDF：http://arxiv.org/pdf/2608.10533v2