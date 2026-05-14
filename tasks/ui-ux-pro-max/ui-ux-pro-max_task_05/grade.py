from __future__ import annotations

import re
from pathlib import Path


def _read(path: Path):
    if not path.exists():
        return None, f"{path.name} not found"
    return path.read_text(encoding="utf-8", errors="ignore"), None


def grade(transcript, workspace_path):
    root = Path(workspace_path)
    review, err1 = _read(root / "ux-review.md")
    proposal, err2 = _read(root / "redesign-proposal.md")
    nav, err3 = _read(root / "navigation-redesign.html")

    records = []

    files_present = [review is not None, proposal is not None, nav is not None]
    records.append({
        "id": "files_exist",
        "score": sum(1 for x in files_present if x) / 3.0,
        "weight": 0.12,
        "description": "All three required output files exist.",
        "details": None if all(files_present) else "; ".join(e for e in [err1, err2, err3] if e),
    })

    if review is None or proposal is None or nav is None:
        for rid, weight, desc in [
            ("review_issue_count", 0.18, "UX review contains at least 8 issues."),
            ("review_structure", 0.15, "UX review includes severity, heuristic, affected users, and business impact."),
            ("proposal_structure", 0.17, "Redesign proposal includes before/after comparison and priority/effort ordering."),
            ("nav_grouping", 0.14, "Navigation prototype groups items into a limited number of logical sections."),
            ("nav_features", 0.12, "Navigation prototype includes collapsible groups, active state, and icons."),
            ("nav_bottom_section", 0.12, "Navigation prototype includes user area plus settings/help at the bottom."),
        ]:
            records.append({"id": rid, "score": 0.0, "weight": weight, "description": desc, "details": "One or more required files are missing."})
        return records

    review_lower = review.lower()
    proposal_lower = proposal.lower()
    nav_lower = nav.lower()

    issue_count = len(re.findall(r"critical|major|minor", review_lower))
    records.append({
        "id": "review_issue_count",
        "score": min(issue_count / 8.0, 1.0),
        "weight": 0.18,
        "description": "UX review contains at least 8 issues.",
        "details": None if issue_count >= 8 else f"Detected only {issue_count} severity markers.",
    })

    structure_score = 0.0
    for token in ["severity", "heuristic", "affected users", "impact on business metrics"]:
        if token in review_lower:
            structure_score += 0.25
    records.append({
        "id": "review_structure",
        "score": structure_score,
        "weight": 0.15,
        "description": "UX review includes severity, heuristic, affected users, and business impact.",
        "details": None if structure_score == 1.0 else "Review structure is incomplete.",
    })

    proposal_ok = ("before" in proposal_lower and "after" in proposal_lower and "|" in proposal and "p1" in proposal_lower and "p2" in proposal_lower and "p3" in proposal_lower)
    records.append({
        "id": "proposal_structure",
        "score": 1.0 if proposal_ok else 0.0,
        "weight": 0.17,
        "description": "Redesign proposal includes before/after comparison and priority/effort ordering.",
        "details": None if proposal_ok else "Before/after comparison or priority ordering missing.",
    })

    groups = ["analytics", "commerce", "customers", "content", "settings", "reports", "operations", "support"]
    group_hits = sum(1 for g in groups if g in nav_lower)
    records.append({
        "id": "nav_grouping",
        "score": min(group_hits / 4.0, 1.0),
        "weight": 0.14,
        "description": "Navigation prototype groups items into a limited number of logical sections.",
        "details": None if group_hits >= 4 else "Too few clear grouped navigation labels detected.",
    })

    feature_score = 0.0
    if "active" in nav_lower or "aria-current" in nav_lower:
        feature_score += 1/3
    if "collapse" in nav_lower or "expand" in nav_lower or "accordion" in nav_lower:
        feature_score += 1/3
    if any(icon in nav for icon in ["📊", "🛒", "👥", "📦", "⚙", "❓"]):
        feature_score += 1/3
    records.append({
        "id": "nav_features",
        "score": feature_score,
        "weight": 0.12,
        "description": "Navigation prototype includes collapsible groups, active state, and icons.",
        "details": None if feature_score == 1.0 else "Navigation features are incomplete.",
    })

    bottom_ok = ("settings" in nav_lower and "help" in nav_lower) and ("avatar" in nav_lower or "user" in nav_lower or "profile" in nav_lower)
    records.append({
        "id": "nav_bottom_section",
        "score": 1.0 if bottom_ok else 0.0,
        "weight": 0.12,
        "description": "Navigation prototype includes user area plus settings/help at the bottom.",
        "details": None if bottom_ok else "Bottom user/settings/help section not clearly present.",
    })

    return records
