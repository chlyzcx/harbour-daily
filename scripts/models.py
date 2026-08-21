"""Data models for underwater acoustic daily papers."""

from dataclasses import dataclass, field
from datetime import date
from typing import Optional


@dataclass
class Source:
    name: str
    url: str


@dataclass
class Paper:
    candidate_id: str
    title: str
    authors: list[str]
    summary: str
    keywords: list[str]
    research_directions: list[str]
    score: float
    sources: list[Source]
    category: str = "Paper"
    journal: Optional[str] = None
    publisher: Optional[str] = None
    doi: Optional[str] = None
    publication_year: Optional[int] = None
    publication_date: Optional[date] = None
    preview_image: Optional[str] = None
    summary_zh: str = ""  # LLM-generated Chinese abstract; preferred over summary
    core_content: str = ""
    key_tech: str = ""
    results: str = ""
    # Additional fields for preview generation
    is_oa: bool = False  # Open access flag
    oa_url: Optional[str] = None  # Open access PDF URL

    def to_markdown(self, date_str: str, rank: int) -> str:
        """Convert paper to Markdown with front matter."""
        # Front matter requires a non-empty summary; fall back to a placeholder
        # when the source (e.g. CrossRef peer review reports) has no abstract.
        # The Chinese version is preferred for display; the title stays English.
        summary = self.summary_zh.strip() or self.summary.strip() \
            or "(No abstract was provided by the source for this item.)"
        # Keep the YAML double-quoted string valid
        summary_yaml = summary.replace("\\", "\\\\").replace('"', '\\"')
        lines = [
            "---",
            f'candidateId: "{self.candidate_id}"',
            f'category: "{self.category}"',
            f'date: "{date_str}"',
            f'rank: {rank}',
            f'title: "{self.title}"',
            "authors:",
        ]
        for author in self.authors:
            lines.append(f'  - "{author}"')
        if not self.authors:
            lines[-1] = "authors: []"

        lines.append("research_direction:")
        for direction in self.research_directions:
            lines.append(f'  - "{direction}"')
        if not self.research_directions:
            lines[-1] = "research_direction: []"

        if self.journal:
            lines.append(f'journal: "{self.journal}"')
        if self.publisher:
            lines.append(f'publisher: "{self.publisher}"')
        if self.doi:
            lines.append(f'doi: "{self.doi}"')
        if self.publication_year:
            lines.append(f'publication_year: {self.publication_year}')

        lines.append(f'summary: "{summary_yaml}"')

        lines.append("keywords:")
        for kw in self.keywords:
            lines.append(f'  - "{kw}"')
        if not self.keywords:
            lines[-1] = "keywords: []"

        lines.append(f"score: {self.score}")

        lines.append("sources:")
        for source in self.sources:
            lines.append(f'  - name: "{source.name}"')
            lines.append(f'    url: "{source.url}"')
        if not self.sources:
            lines[-1] = "sources: []"

        if self.preview_image:
            lines.append(f'previewImage: "{self.preview_image}"')

        lines.append("---")
        lines.append("")
        lines.append("## 核心内容")
        lines.append("")
        lines.append(self.core_content if self.core_content else summary)
        lines.append("")
        lines.append("## 关键技术与数据")
        lines.append("")
        lines.append(self.key_tech if self.key_tech else "（详细技术分析待补充）")
        lines.append("")
        lines.append("## 结果与结论")
        lines.append("")
        lines.append(self.results if self.results else "（实验结果与结论待补充）")
        lines.append("")
        lines.append("## 来源链接")
        lines.append("")
        for source in self.sources:
            lines.append(f"- {source.name}：{source.url}")

        return "\n".join(lines)


@dataclass
class DailySelection:
    date: str
    papers: list[Paper] = field(default_factory=list)

    def add_paper(self, paper: Paper) -> None:
        self.papers.append(paper)

    def sort_by_score(self) -> None:
        """Sort papers by score descending and assign ranks."""
        self.papers.sort(key=lambda p: p.score, reverse=True)
        for i, paper in enumerate(self.papers, start=1):
            paper.rank = i

    def to_manifest(self) -> dict:
        """Generate managed-manifest.json content."""
        return {
            "schema_version": 2,
            "cycle_id": f"daily-{self.date}",
            "display_date": self.date,
            "articles": [
                {
                    "candidate_id": p.candidate_id,
                    "category": p.category,
                    "rank": p.rank,
                    "path": f"docs/daily/{self.date}/{p.category.lower()}/{p.rank:02d}-{self._slugify(p.title)}.md"
                }
                for p in self.papers
            ],
            "assets": [
                {
                    "candidate_id": p.candidate_id,
                    "path": f"docs/public{p.preview_image}" if p.preview_image else ""
                }
                for p in self.papers
                if p.preview_image
            ]
        }

    @staticmethod
    def _slugify(title: str) -> str:
        """Generate URL-safe slug from title."""
        slug = title.lower()
        slug = "".join(c if c.isalnum() or c in " -" else "" for c in slug)
        slug = slug.replace(" ", "-")[:50]
        return slug
