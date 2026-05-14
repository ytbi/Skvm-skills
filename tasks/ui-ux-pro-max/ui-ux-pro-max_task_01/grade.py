from __future__ import annotations

import re
from pathlib import Path


def _read_md(workspace_path: str):
    path = Path(workspace_path) / "ux-audit.md"
    if not path.exists():
        return None, "ux-audit.md not found"
    return path.read_text(encoding="utf-8", errors="ignore"), None


def grade(transcript, workspace_path):
    text, err = _read_md(workspace_path)
    records = []

    exists = text is not None
    records.append({
        "id": "file_exists",
        "score": 1.0 if exists else 0.0,
        "weight": 0.10,
        "description": "ux-audit.md exists.",
        "details": None if exists else err,
    })

    if not exists:
        for rid, weight, desc in [
            ("title_and_sections", 0.15, "Document has the required title and top-level sections."),
            ("issue_count", 0.20, "At least 6 issues are documented."),
            ("issue_structure", 0.20, "Each issue includes severity, heuristic, description, impact, and recommendation."),
            ("heuristic_coverage", 0.15, "The audit references UX heuristics meaningfully."),
            ("summary_counts", 0.10, "The summary includes total issue counts by severity."),
            ("top_priorities", 0.10, "The summary includes top 3 immediate priorities."),
        ]:
            records.append({
                "id": rid,
                "score": 0.0,
                "weight": weight,
                "description": desc,
                "details": "Markdown file missing.",
            })
        return records

    lower = text.lower()

    title_ok = "# ux audit: signup page" in lower
    sections_ok = "## issues found" in lower and "## summary" in lower
    records.append({
        "id": "title_and_sections",
        "score": 1.0 if title_ok and sections_ok else 0.0,
        "weight": 0.15,
        "description": "Document has the required title and top-level sections.",
        "details": None if title_ok and sections_ok else "Missing required title or Issues/Summary section.",
    })

    issue_count = len(re.findall(r"^###\s+issue\s+\d+", text, re.IGNORECASE | re.MULTILINE))
    issue_score = min(issue_count / 6.0, 1.0)
    records.append({
        "id": "issue_count",
        "score": issue_score,
        "weight": 0.20,
        "description": "At least 6 issues are documented.",
        "details": None if issue_count >= 6 else f"Found {issue_count} issue headings; expected at least 6.",
    })

    severity_count = lower.count("**severity**")
    heuristic_count = lower.count("**heuristic violated**")
    description_count = lower.count("**description**")
    impact_count = lower.count("**impact**")
    recommendation_count = lower.count("**recommendation**")
    structured = min(severity_count, heuristic_count, description_count, impact_count, recommendation_count)
    structure_score = min(structured / 6.0, 1.0)
    records.append({
        "id": "issue_structure",
        "score": structure_score,
        "weight": 0.20,
        "description": "Each issue includes severity, heuristic, description, impact, and recommendation.",
        "details": None if structure_score == 1.0 else "Not all issue blocks include the required fields.",
    })

    heuristic_terms = [
        "visibility of system status",
        "match with real world",
        "user control and freedom",
        "consistency and standards",
        "error prevention",
        "recognition over recall",
        "flexibility and efficiency",
        "aesthetic and minimalist design",
        "help users recognize, diagnose, and recover from errors",
        "help and documentation",
    ]
    hits = sum(1 for h in heuristic_terms if h in lower)
    heuristic_score = min(hits / 3.0, 1.0)
    records.append({
        "id": "heuristic_coverage",
        "score": heuristic_score,
        "weight": 0.15,
        "description": "The audit references UX heuristics meaningfully.",
        "details": None if heuristic_score == 1.0 else "Few explicit heuristic references detected.",
    })

    summary_ok = (
        "total issues:" in lower and
        "critical:" in lower and
        "major:" in lower and
        "minor:" in lower and
        "cosmetic:" in lower
    )
    records.append({
        "id": "summary_counts",
        "score": 1.0 if summary_ok else 0.0,
        "weight": 0.10,
        "description": "The summary includes total issue counts by severity.",
        "details": None if summary_ok else "Summary count block is incomplete.",
    })

    priorities_ok = bool(re.search(r"top 3 priorities.*1\..*2\..*3\.", lower, re.DOTALL))
    records.append({
        "id": "top_priorities",
        "score": 1.0 if priorities_ok else 0.0,
        "weight": 0.10,
        "description": "The summary includes top 3 immediate priorities.",
        "details": None if priorities_ok else "Top 3 priority list not found.",
    })

    return records
