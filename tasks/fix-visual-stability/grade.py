from __future__ import annotations

import os
from pathlib import Path


def grade(transcript, workspace_path):
    root = Path(workspace_path)
    report_path = root / "visual-stability-report.md"
    records = []

    report_exists = report_path.exists()
    records.append({
        "id": "report_exists",
        "score": 1.0 if report_exists else 0.0,
        "weight": 0.15,
        "description": "visual-stability-report.md exists.",
        "details": None if report_exists else "visual-stability-report.md not found.",
    })

    report_text = ""
    if report_exists:
        report_text = report_path.read_text(encoding="utf-8", errors="ignore").lower()

    root_cause_terms = [
        "layout shift",
        "cls",
        "visual stability",
        "late-loading",
        "unstable",
        "reflow",
        "jank",
    ]
    root_hits = sum(1 for t in root_cause_terms if t in report_text)
    records.append({
        "id": "root_cause_reasoning",
        "score": min(root_hits / 3.0, 1.0),
        "weight": 0.20,
        "description": "The report identifies concrete visual stability root causes.",
        "details": None if root_hits >= 3 else "Too few concrete stability root-cause markers found in the report.",
    })

    changed_files_ok = "changed" in report_text or "modified" in report_text or "files" in report_text
    records.append({
        "id": "changed_files_documented",
        "score": 1.0 if changed_files_ok else 0.0,
        "weight": 0.15,
        "description": "The report states which files or components were changed.",
        "details": None if changed_files_ok else "The report does not clearly document changed files/components.",
    })

    constraint_terms = [
        "class names",
        "ids",
        "data-testid",
        "preserved",
        "not changed",
    ]
    constraint_hits = sum(1 for t in constraint_terms if t in report_text)
    records.append({
        "id": "constraint_discipline",
        "score": min(constraint_hits / 3.0, 1.0),
        "weight": 0.20,
        "description": "The report explicitly addresses preservation of constrained identifiers.",
        "details": None if constraint_hits >= 3 else "Constraint preservation is not clearly documented.",
    })

    exec_commands = 0
    read_like = 0
    write_like = 0
    for entry in transcript:
        if not isinstance(entry, dict):
            continue
        msg = entry.get("message") if entry.get("type") == "message" else None
        if not isinstance(msg, dict):
            continue
        content = msg.get("content", [])
        if not isinstance(content, list):
            continue
        for part in content:
            if not isinstance(part, dict):
                continue
            if part.get("type") == "toolCall":
                name = str(part.get("name", ""))
                if name == "execute_command":
                    exec_commands += 1
                if name == "read_file":
                    read_like += 1
                if name == "write_file":
                    write_like += 1

    workflow_score = 0.0
    if exec_commands > 0:
        workflow_score += 0.4
    if read_like > 0:
        workflow_score += 0.3
    if write_like > 0 or report_exists:
        workflow_score += 0.3
    records.append({
        "id": "repair_workflow_signal",
        "score": workflow_score,
        "weight": 0.15,
        "description": "The transcript shows a real inspect/edit workflow rather than a pure textual summary.",
        "details": None if workflow_score >= 0.7 else "The transcript does not strongly indicate a concrete inspect/edit workflow.",
    })

    app_exists = (root / "app").exists()
    records.append({
        "id": "app_target_presence",
        "score": 1.0 if app_exists else 0.0,
        "weight": 0.15,
        "description": "A target application directory is present for the repair task.",
        "details": None if app_exists else "The expected app/ directory is missing from the task workspace.",
    })

    return records
