---
candidateId: "openalex--W7204255488"
category: "Paper"
date: "2026-08-28"
rank: 10
title: "Weakly Supervised Seafloor Segmentation for Seagrass Habitat Mapping in Side-Scan Sonar Imagery"
authors:
  - "Hayat Rajani"
  - "Nuno Gracias"
  - "Rafael Garcia"
research_direction: []
journal: "arXiv (Cornell University)"
publisher: "Cornell University"
doi: "10.48550/arxiv.2608.24756"
publication_year: 2026
summary: "海草床是重要的蓝碳栖息地，绘制其分布范围是海岸管理和碳核算的前提。光学卫星传感器覆盖范围大，但无法到达深水或浑浊水域；侧扫声呐（SSS）则能以高分辨率在任意深度成像海底。然而SSS解译仍依赖密集的人工标注，耗时且昂贵。本文通过将弱监督语义分割框架适配到SSS底栖栖息地制图，解决该问题。"
keywords:
  - "classification"
score: 56.6
sources:
  - name: "OpenAlex"
    url: "https://openalex.org/W7204255488"
  - name: "DOI"
    url: "https://doi.org/10.48550/arxiv.2608.24756"
previewImage: "/daily/2026-08-28/assets/openalex--W7204255488/preview.png"
---

## 核心内容

海草床是重要的蓝碳栖息地，绘制其分布范围是海岸管理和碳核算的前提。光学卫星传感器覆盖范围大，但无法到达深水或浑浊水域；侧扫声呐（SSS）则能以高分辨率在任意深度成像海底。然而SSS解译仍依赖密集的人工标注，耗时且昂贵。本文通过将弱监督语义分割框架适配到SSS底栖栖息地制图，解决该问题。

## 关键技术与数据

方法采用弱监督语义分割框架，利用图像级标签或点标签等弱标注训练分割模型，减少对像素级密集标注的依赖。网络基于深度卷积架构，结合类别激活图（CAM）等技术生成伪标签并迭代优化。数据为SSS海草栖息地图像，标注形式为弱标签，用于训练与评估。

## 结果与结论

实验表明弱监督方法在SSS海草制图中取得了与全监督方法接近的分割精度，显著降低了标注成本。创新点在于将弱监督学习成功应用于SSS底栖栖息地制图，验证了其在减少人工标注负担的同时保持较高制图精度的可行性，为大规模海草监测提供了经济高效的解决方案。

## 来源链接

- OpenAlex：https://openalex.org/W7204255488
- DOI：https://doi.org/10.48550/arxiv.2608.24756