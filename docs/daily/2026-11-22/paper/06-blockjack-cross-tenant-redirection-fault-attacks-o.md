---
candidateId: "openalex--W7237104004"
category: "Paper"
date: "2026-11-22"
rank: 6
title: "BlockJack: Cross-Tenant Redirection Fault Attacks on Paged KV Cache Address Translation in LLM Serving"
authors:
  - "Qifan Wang"
  - "Jeremy Boy"
  - "Jonas Sander"
  - "Yansong Gao"
  - "Hongsheng Hu"
  - "Ye Dong"
  - "Thomas Eisenbarth"
  - "David Oswald"
research_direction: []
journal: "arXiv (Cornell University)"
publisher: "Cornell University"
doi: "10.48550/arxiv.2611.25945"
publication_year: 2026
summary: "该论文研究大语言模型（LLM）服务框架中分页KV缓存地址转换的跨租户重定向故障攻击问题。vLLM等分页服务框架通过块表将请求的逻辑KV块映射到物理KV块，形成软件管理的地址转换层，类似操作系统页表。论文提出BlockJack攻击，利用故障注入手段篡改块表映射，实现跨租户的KV缓存重定向。"
keywords: []
score: 56.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7237104004"
  - name: "DOI"
    url: "https://doi.org/10.48550/arxiv.2611.25945"
previewImage: "/daily/2026-11-22/assets/openalex--W7237104004/preview.png"
---

## 核心内容

该论文研究大语言模型（LLM）服务框架中分页KV缓存地址转换的跨租户重定向故障攻击问题。vLLM等分页服务框架通过块表将请求的逻辑KV块映射到物理KV块，形成软件管理的地址转换层，类似操作系统页表。论文提出BlockJack攻击，利用故障注入手段篡改块表映射，实现跨租户的KV缓存重定向。

## 关键技术与数据

关键技术涉及LLM推理服务中的分页KV缓存管理机制与块表地址转换层，借鉴Rowhammer等针对操作系统页表的故障攻击思路，将其迁移至LLM服务框架的软件管理地址转换层。攻击方法通过故障注入破坏块表项，使不同租户请求的物理KV块映射发生重定向，实验对象为基于vLLM等分页服务框架的LLM推理系统。

## 结果与结论

论文揭示了分页KV缓存地址转换层存在跨租户重定向故障攻击面，BlockJack攻击可破坏租户间KV缓存隔离，导致推理状态混淆与信息泄露风险。该研究创新性地将硬件故障攻击范式引入LLM服务框架的软件地址转换层，指出分页KV缓存管理机制的安全隐患，为LLM服务系统的隔离与安全防护设计提出了新的挑战。

## 来源链接

- OpenAlex：https://openalex.org/W7237104004
- DOI：https://doi.org/10.48550/arxiv.2611.25945