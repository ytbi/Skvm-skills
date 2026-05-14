from __future__ import annotations

import re
from pathlib import Path


def _read_md(workspace_path: str):
    path = Path(workspace_path) / "onboarding-redesign.md"
    if not path.exists():
        return None, "onboarding-redesign.md not found"
    return path.read_text(encoding="utf-8", errors="ignore"), None


def grade(transcript, workspace_path):
    text, err = _read_md(workspace_path)
    records = []

    exists = text is not None
    records.append({
        "id": "file_exists",
        "score": 1.0 if exists else 0.0,
        "weight": 0.10,
        "description": "onboarding-redesign.md exists.",
        "details": None if exists else err,
    })

    if not exists:
        for rid, weight, desc in [
            ("problem_analysis", 0.20, "Identifies multiple UX problems in the current flow."),
            ("flow_redesign", 0.20, "Proposes a redesigned step-by-step flow."),
            ("ux_principles", 0.15, "References UX principles such as cognitive load and progressive disclosure."),
            ("metrics", 0.15, "Includes measurable success metrics."),
            ("ab_test", 0.10, "Includes a specific A/B test proposal."),
            ("step_specificity", 0.10, "References the current onboarding steps concretely."),
        ]:
            records.append({"id": rid, "score": 0.0, "weight": weight, "description": desc, "details": "Markdown file missing."})
        return records

    lower = text.lower()
    issue_hits = len(re.findall(r"issue|problem|drop-off|friction", lower))
    analysis_score = 1.0 if issue_hits >= 3 else issue_hits / 3.0
    records.append({
        "id": "problem_analysis",
        "score": analysis_score,
        "weight": 0.20,
        "description": "Identifies multiple UX problems in the current flow.",
        "details": None if analysis_score == 1.0 else "Too few explicit problem markers.",
    })

    redesign_ok = "redesign" in lower and ("step 1" in lower or "step 2" in lower or "flow" in lower)
    records.append({
        "id": "flow_redesign",
        "score": 1.0 if redesign_ok else 0.0,
        "weight": 0.20,
        "description": "Proposes a redesigned step-by-step flow.",
        "details": None if redesign_ok else "Redesigned flow not clearly described.",
    })

    principle_terms = ["cognitive load", "user control", "progressive disclosure", "heuristic", "usability"]
    principle_hits = sum(1 for t in principle_terms if t in lower)
    principle_score = min(principle_hits / 3.0, 1.0)
    records.append({
        "id": "ux_principles",
        "score": principle_score,
        "weight": 0.15,
        "description": "References UX principles such as cognitive load and progressive disclosure.",
        "details": None if principle_score == 1.0 else "UX principle references are limited.",
    })

    metrics_ok = "completion rate" in lower or "time per step" in lower or "drop-off" in lower or "satisfaction" in lower
    records.append({
        "id": "metrics",
        "score": 1.0 if metrics_ok else 0.0,
        "weight": 0.15,
        "description": "Includes measurable success metrics.",
        "details": None if metrics_ok else "No clear metrics found.",
    })

    ab_ok = "a/b test" in lower or "ab test" in lower
    records.append({
        "id": "ab_test",
        "score": 1.0 if ab_ok else 0.0,
        "weight": 0.10,
        "description": "Includes a specific A/B test proposal.",
        "details": None if ab_ok else "A/B test proposal missing.",
    })

    step_hits = sum(1 for t in ["step 1", "step 2", "step 3", "step 4"] if t in lower)
    records.append({
        "id": "step_specificity",
        "score": step_hits / 4.0,
        "weight": 0.10,
        "description": "References the current onboarding steps concretely.",
        "details": None if step_hits == 4 else "Not all original steps are discussed.",
    })

    return records
