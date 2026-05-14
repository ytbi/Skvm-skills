from __future__ import annotations

from pathlib import Path


def _read_html(workspace_path: str):
    path = Path(workspace_path) / "task-app.html"
    if not path.exists():
        return None, "task-app.html not found"
    return path.read_text(encoding="utf-8", errors="ignore"), None


def grade(transcript, workspace_path):
    html, err = _read_html(workspace_path)
    records = []

    exists = html is not None
    records.append({
        "id": "file_exists",
        "score": 1.0 if exists else 0.0,
        "weight": 0.08,
        "description": "task-app.html exists.",
        "details": None if exists else err,
    })

    if not exists:
        for rid, weight, desc in [
            ("screen_coverage", 0.16, "Includes task list, new task form, and task detail screens."),
            ("states", 0.18, "Includes loading, error, empty, success, and confirmation states."),
            ("task_controls", 0.14, "Includes completion toggle and form actions."),
            ("form_fields", 0.12, "Includes required new-task form fields."),
            ("filter_tabs", 0.12, "Includes all/active/completed filtering."),
            ("success_and_delete", 0.10, "Includes success toast and delete confirmation."),
            ("design_tokens", 0.10, "Uses modern styling markers such as CSS custom properties and accent color."),
        ]:
            records.append({"id": rid, "score": 0.0, "weight": weight, "description": desc, "details": "HTML file missing."})
        return records

    lower = html.lower()

    screen_hits = sum(1 for t in ["today's tasks", "new task", "task detail"] if t in lower)
    records.append({
        "id": "screen_coverage",
        "score": screen_hits / 3.0,
        "weight": 0.16,
        "description": "Includes task list, new task form, and task detail screens.",
        "details": None if screen_hits == 3 else "One or more core screens are missing.",
    })

    state_hits = sum(1 for t in ["loading", "error", "all caught up", "task created", "confirmation"] if t in lower)
    records.append({
        "id": "states",
        "score": min(state_hits / 5.0, 1.0),
        "weight": 0.18,
        "description": "Includes loading, error, empty, success, and confirmation states.",
        "details": None if state_hits >= 5 else "Not all required states are visible in the markup.",
    })

    controls_ok = ("complete" in lower or "checkbox" in lower) and ("save" in lower) and ("cancel" in lower)
    records.append({
        "id": "task_controls",
        "score": 1.0 if controls_ok else 0.0,
        "weight": 0.14,
        "description": "Includes completion toggle and form actions.",
        "details": None if controls_ok else "Completion or form action controls are incomplete.",
    })

    fields = ["title", "description", "due date", "priority"]
    field_score = sum(1 for f in fields if f in lower) / len(fields)
    records.append({
        "id": "form_fields",
        "score": field_score,
        "weight": 0.12,
        "description": "Includes required new-task form fields.",
        "details": None if field_score == 1.0 else "One or more required form fields are missing.",
    })

    filter_hits = sum(1 for t in ["all", "active", "completed"] if t in lower)
    records.append({
        "id": "filter_tabs",
        "score": filter_hits / 3.0,
        "weight": 0.12,
        "description": "Includes all/active/completed filtering.",
        "details": None if filter_hits == 3 else "Filter controls are incomplete.",
    })

    modal_ok = ("task created" in lower or "toast" in lower) and ("delete" in lower and "confirm" in lower or "dialog" in lower)
    records.append({
        "id": "success_and_delete",
        "score": 1.0 if modal_ok else 0.0,
        "weight": 0.10,
        "description": "Includes success toast and delete confirmation.",
        "details": None if modal_ok else "Success feedback or delete confirmation markers are missing.",
    })

    design_ok = ("#6366f1" in lower or "--" in html) and ("transition" in lower)
    records.append({
        "id": "design_tokens",
        "score": 1.0 if design_ok else 0.0,
        "weight": 0.10,
        "description": "Uses modern styling markers such as CSS custom properties and accent color.",
        "details": None if design_ok else "Design token or transition markers are missing.",
    })

    return records
