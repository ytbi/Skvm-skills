from __future__ import annotations

import re
from pathlib import Path


def _load_html(workspace_path: str):
    path = Path(workspace_path) / "navbar.html"
    if not path.exists():
        return None, "navbar.html not found"
    return path.read_text(encoding="utf-8", errors="ignore"), None


def grade(transcript, workspace_path):
    html, err = _load_html(workspace_path)
    records = []

    exists = html is not None
    records.append({
        "id": "file_exists",
        "score": 1.0 if exists else 0.0,
        "weight": 0.10,
        "description": "navbar.html exists in the workspace.",
        "details": None if exists else err,
    })

    if not exists:
        records.extend([
            {"id": "doctype_present", "score": 0.0, "weight": 0.08, "description": "HTML document includes a DOCTYPE declaration.", "details": "HTML file missing."},
            {"id": "semantic_nav", "score": 0.0, "weight": 0.15, "description": "Uses nav, ul, and anchor semantics for navigation.", "details": "HTML file missing."},
            {"id": "required_links", "score": 0.0, "weight": 0.15, "description": "Contains the four required links and logo/nav content.", "details": "HTML file missing."},
            {"id": "responsive_mobile", "score": 0.0, "weight": 0.18, "description": "Includes a mobile breakpoint and hamburger/toggle behavior.", "details": "HTML file missing."},
            {"id": "sticky_and_states", "score": 0.0, "weight": 0.16, "description": "Implements sticky nav plus hover/active styles.", "details": "HTML file missing."},
            {"id": "design_tokens", "score": 0.0, "weight": 0.10, "description": "Uses CSS custom properties for styling tokens.", "details": "HTML file missing."},
            {"id": "focus_indicator", "score": 0.0, "weight": 0.08, "description": "Includes visible focus indicator styles.", "details": "HTML file missing."},
        ])
        return records

    lower = html.lower()

    doctype_ok = "<!doctype html" in lower
    records.append({
        "id": "doctype_present",
        "score": 1.0 if doctype_ok else 0.0,
        "weight": 0.08,
        "description": "HTML document includes a DOCTYPE declaration.",
        "details": None if doctype_ok else "Missing <!DOCTYPE html>.",
    })

    semantic_ok = "<nav" in lower and "<ul" in lower and lower.count("<a") >= 4
    records.append({
        "id": "semantic_nav",
        "score": 1.0 if semantic_ok else 0.0,
        "weight": 0.15,
        "description": "Uses nav, ul, and anchor semantics for navigation.",
        "details": None if semantic_ok else "Missing semantic nav structure.",
    })

    labels = ["home", "about", "services", "contact"]
    links_ok = all(label in lower for label in labels)
    records.append({
        "id": "required_links",
        "score": 1.0 if links_ok else 0.0,
        "weight": 0.15,
        "description": "Contains the four required links and logo/nav content.",
        "details": None if links_ok else "One or more required navigation labels are missing.",
    })

    media_ok = bool(re.search(r"@media\s*\(.*768px", html, re.IGNORECASE))
    hamburger_ok = any(token in lower for token in ["hamburger", "menu-toggle", "☰", "aria-label=\"menu\"", "aria-label='menu'"])
    responsive_score = 0.0
    details = []
    if media_ok:
        responsive_score += 0.5
    else:
        details.append("missing mobile media query")
    if hamburger_ok:
        responsive_score += 0.5
    else:
        details.append("missing hamburger/toggle marker")
    records.append({
        "id": "responsive_mobile",
        "score": responsive_score,
        "weight": 0.18,
        "description": "Includes a mobile breakpoint and hamburger/toggle behavior.",
        "details": None if responsive_score == 1.0 else ", ".join(details),
    })

    sticky_ok = bool(re.search(r"position\s*:\s*sticky", html, re.IGNORECASE))
    state_ok = ":hover" in lower and ("active" in lower or "aria-current" in lower)
    state_score = 0.0
    detail_parts = []
    if sticky_ok:
        state_score += 0.5
    else:
        detail_parts.append("missing sticky positioning")
    if state_ok:
        state_score += 0.5
    else:
        detail_parts.append("missing hover/active state styling")
    records.append({
        "id": "sticky_and_states",
        "score": state_score,
        "weight": 0.16,
        "description": "Implements sticky nav plus hover/active styles.",
        "details": None if state_score == 1.0 else ", ".join(detail_parts),
    })

    tokens_ok = "--" in html and "var(" in html
    records.append({
        "id": "design_tokens",
        "score": 1.0 if tokens_ok else 0.0,
        "weight": 0.10,
        "description": "Uses CSS custom properties for styling tokens.",
        "details": None if tokens_ok else "Missing CSS custom properties.",
    })

    focus_ok = ":focus" in lower or ":focus-visible" in lower or "outline:" in lower
    records.append({
        "id": "focus_indicator",
        "score": 1.0 if focus_ok else 0.0,
        "weight": 0.08,
        "description": "Includes visible focus indicator styles.",
        "details": None if focus_ok else "No clear focus indicator styling found.",
    })

    return records
