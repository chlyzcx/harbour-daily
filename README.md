# 水声工程每日精选

每日自动精选水声工程领域高质量学术论文，覆盖四大研究方向：

- **水声通信信道**
- **水声通信**
- **水声侦察**
- **海洋生物声学信号处理**

## 数据源

- [OpenAlex](https://openalex.org/) - 主数据源，覆盖 IEEE、Elsevier、Springer 等出版社
- [Semantic Scholar](https://www.semanticscholar.org/) - 补充摘要和引用信息
- [arXiv](https://arxiv.org/) - 预印本补充

## 本地开发

```bash
npm ci
npm run dev
```

## 构建

```bash
npm run build
```

## 自动化流程

1. **每日抓取**：GitHub Actions 每日 02:00 UTC（北京时间 10:00）自动运行
2. **智能筛选**：按期刊质量、时效性、研究方向匹配度评分
3. **自动发布**：生成 Markdown 后自动提交并部署到 GitHub Pages

## 项目结构

```
├── docs/                    # VitePress 站点
│   ├── .vitepress/         # 配置和主题
│   ├── daily/              # 每日论文（自动生成）
│   └── public/             # 静态资源
├── scripts/                # Python 抓取脚本
│   ├── config.py           # 关键词和期刊配置
│   ├── models.py           # 数据模型
│   ├── fetch_openalex.py   # OpenAlex 抓取
│   ├── fetch_arxiv.py      # arXiv 抓取
│   └── fetch_daily.py      # 主脚本
└── .github/workflows/      # 自动化工作流
```

## 配置

编辑 `scripts/config.py` 可调整：
- 研究方向关键词
- 期刊权重
- 每日精选数量
- 评分阈值
