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
    score: int
    sources: list[Source]
    journal: Optional[str] = None
    publisher: Optional[str] = None
    doi: Optional[str] = None
    publication_year: Optional[int] = None
    publication_date: Optional[date] = None
    preview_image: Optional[str] = None
    category: str = "Paper"

    def to_markdown(self, date_str: str, rank: int) -> str:
        """Convert paper to Markdown with front matter."""
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

        lines.append("research_direction:")
        for direction in self.research_directions:
            lines.append(f'  - "{direction}"')

        if self.journal:
            lines.append(f'journal: "{self.journal}"')
        if self.publisher:
            lines.append(f'publisher: "{self.publisher}"')
        if self.doi:
            lines.append(f'doi: "{self.doi}"')
        if self.publication_year:
            lines.append(f'publication_year: {self.publication_year}')

        lines.append(f'summary: "{self.summary}"')

        lines.append("keywords:")
        for kw in self.keywords:
            lines.append(f'  - "{kw}"')

        lines.append(f"score: {self.score}")

        lines.append("sources:")
        for source in self.sources:
            lines.append(f'  - name: "{source.name}"')
            lines.append(f'    url: "{source.url}"')

        if self.preview_image:
            lines.append(f'previewImage: "{self.preview_image}"')

        lines.append("---")
        lines.append("")
        lines.append(f"# {self.title}")
        lines.append("")
        lines.append("## 摘要")
        lines.append("")
        lines.append(self.summary)
        lines.append("")
        lines.append("## 关键词")
        lines.append("")
        lines.append("、".join(self.keywords))
        lines.append("")
        lines.append("## 来源")
        lines.append("")
        for source in self.sources:
            lines.append(f"- [{source.name}]({source.url})")

        return "\n".join(lines)


@dataclass
class DailySelection:
    date: str
    papers: list[Paper] = field(default_factory=list)

    def add_paper(self, paper: Paper) -> None:
        self.papers.append(paper)

    def sort_by_score(self) -> None:
        self.papers.sort(key=lambda p: p.score, reverse=True)
