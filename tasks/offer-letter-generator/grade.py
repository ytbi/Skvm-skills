from __future__ import annotations

import json
import zipfile
from pathlib import Path


def _read_docx_xml(docx_path: Path):
    try:
        with zipfile.ZipFile(docx_path) as zf:
            names = set(zf.namelist())
            if "word/document.xml" not in names:
                return None, "word/document.xml missing from DOCX container"
            xml = zf.read("word/document.xml").decode("utf-8", errors="ignore")
            return xml, None
    except Exception as e:
        return None, f"DOCX open failed: {e}"


def grade(transcript, workspace_path):
    root = Path(workspace_path)
    docx_path = root / "offer_letter_filled.docx"
    report_path = root / "fill_report.json"
    records = []

    exists = docx_path.exists()
    records.append({
        "id": "docx_exists",
        "score": 1.0 if exists else 0.0,
        "weight": 0.15,
        "description": "The filled DOCX file exists.",
        "details": None if exists else "offer_letter_filled.docx not found.",
    })

    xml = None
    docx_valid = False
    docx_details = "offer_letter_filled.docx not found."
    if exists:
        xml, err = _read_docx_xml(docx_path)
        if err is None and xml is not None:
            docx_valid = True
            docx_details = None
        else:
            docx_details = err
    records.append({
        "id": "docx_valid",
        "score": 1.0 if docx_valid else 0.0,
        "weight": 0.20,
        "description": "The output document is a valid DOCX container with document XML.",
        "details": docx_details,
    })

    placeholder_score = 0.0
    placeholder_details = "Document XML unavailable."
    if xml is not None:
        unresolved = ("{{" in xml) or ("}}" in xml)
        placeholder_score = 1.0 if not unresolved else 0.0
        placeholder_details = None if not unresolved else "Template placeholders or control markers still remain in document XML."
    records.append({
        "id": "placeholders_resolved",
        "score": placeholder_score,
        "weight": 0.20,
        "description": "Template placeholders and control markers are removed from the final document.",
        "details": placeholder_details,
    })

    relocation_ok = 0.0
    relocation_details = "Document XML unavailable."
    if xml is not None:
        bad_markers = any(tok in xml for tok in ["IF_RELOCATION", "END_IF_RELOCATION"])
        relocation_ok = 1.0 if not bad_markers else 0.0
        relocation_details = None if relocation_ok == 1.0 else "Conditional relocation markers still remain in the output."
    records.append({
        "id": "conditional_blocks_handled",
        "score": relocation_ok,
        "weight": 0.15,
        "description": "Conditional relocation blocks were handled and control markers are gone.",
        "details": relocation_details,
    })

    report_ok = False
    report_details = "fill_report.json not found."
    if report_path.exists():
        try:
            report = json.loads(report_path.read_text())
            report_ok = (
                isinstance(report, dict)
                and isinstance(report.get("report"), dict)
                and report["report"].get("output_file") == "offer_letter_filled.docx"
                and report["report"].get("placeholders_resolved") is True
                and report["report"].get("conditional_blocks_handled") is True
                and report["report"].get("docx_valid") is True
            )
            report_details = None if report_ok else "fill_report.json does not match the required structure or values."
        except Exception as e:
            report_details = f"fill_report.json parse failed: {e}"
    records.append({
        "id": "fill_report",
        "score": 1.0 if report_ok else 0.0,
        "weight": 0.15,
        "description": "The fill report has the exact required shape and values.",
        "details": report_details,
    })

    workflow_score = 0.0
    if docx_valid:
        workflow_score += 0.5
    if report_ok:
        workflow_score += 0.5
    records.append({
        "id": "template_workflow",
        "score": workflow_score,
        "weight": 0.15,
        "description": "The agent followed a template-filling workflow and produced both the filled document and report.",
        "details": None if workflow_score == 1.0 else "One or more required artifacts for the template workflow are missing or invalid.",
    })

    return records
