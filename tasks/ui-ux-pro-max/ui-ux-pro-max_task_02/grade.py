from __future__ import annotations

import re
from pathlib import Path


def _read_md(workspace_path: str):
    path = Path(workspace_path) / "checkout-flow.md"
    if not path.exists():
        return None, "checkout-flow.md not found"
    return path.read_text(encoding="utf-8", errors="ignore"), None


def grade(transcript, workspace_path):
    text, err = _read_md(workspace_path)
    records = []

    exists = text is not None
    records.append({
        "id": "file_exists",
        "score": 1.0 if exists else 0.0,
        "weight": 0.10,
        "description": "checkout-flow.md exists.",
        "details": None if exists else err,
    })

    if not exists:
        for rid, weight, desc in [
            ("step_coverage", 0.20, "All four flow steps are covered."),
            ("layout_goals", 0.16, "Each step includes screen layout and user goals."),
            ("states", 0.16, "Each step includes state coverage."),
            ("microcopy", 0.14, "Microcopy is present for the flow."),
            ("accessibility", 0.12, "Accessibility considerations are present."),
            ("summary_and_optimizations", 0.12, "Step count and optimization suggestions are included."),
        ]:
            records.append({"id": rid, "score": 0.0, "weight": weight, "description": desc, "details": "Markdown file missing."})
        return records

    lower = text.lower()
    steps = ["cart review", "checkout", "payment", "confirmation"]
    step_score = sum(1 for s in steps if s in lower) / len(steps)
    records.append({
        "id": "step_coverage",
        "score": step_score,
        "weight": 0.20,
        "description": "All four flow steps are covered.",
        "details": None if step_score == 1.0 else "One or more required steps are missing.",
    })

    layout_hits = lower.count("screen layout")
    goal_hits = lower.count("user goals")
    layout_goal_score = min(min(layout_hits, goal_hits) / 4.0, 1.0)
    records.append({
        "id": "layout_goals",
        "score": layout_goal_score,
        "weight": 0.16,
        "description": "Each step includes screen layout and user goals.",
        "details": None if layout_goal_score == 1.0 else "Some steps are missing layout or user-goal sections.",
    })

    state_markers = ["default", "loading", "error", "empty", "success"]
    state_hits = sum(1 for s in state_markers if s in lower)
    state_score = min(state_hits / 5.0, 1.0)
    records.append({
        "id": "states",
        "score": state_score,
        "weight": 0.16,
        "description": "The flow includes meaningful state coverage.",
        "details": None if state_score == 1.0 else "State coverage appears incomplete.",
    })

    microcopy_ok = "microcopy" in lower and ("button" in lower or "error message" in lower or "confirmation" in lower)
    records.append({
        "id": "microcopy",
        "score": 1.0 if microcopy_ok else 0.0,
        "weight": 0.14,
        "description": "Microcopy is present for the flow.",
        "details": None if microcopy_ok else "Microcopy section not clearly present.",
    })

    accessibility_score = 1.0 if "accessibility" in lower else 0.0
    records.append({
        "id": "accessibility",
        "score": accessibility_score,
        "weight": 0.12,
        "description": "Accessibility considerations are present.",
        "details": None if accessibility_score == 1.0 else "Accessibility considerations not found.",
    })

    summary_ok = ("total step count" in lower or "step count" in lower) and ("optimization suggestions" in lower or "reduce friction" in lower)
    records.append({
        "id": "summary_and_optimizations",
        "score": 1.0 if summary_ok else 0.0,
        "weight": 0.12,
        "description": "Step count and optimization suggestions are included.",
        "details": None if summary_ok else "Step count or optimization suggestions missing.",
    })

    return records
