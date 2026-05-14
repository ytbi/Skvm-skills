from __future__ import annotations

from pathlib import Path


def _load_html(workspace_path: str):
    path = Path(workspace_path) / "checkout.html"
    if not path.exists():
        return None, "checkout.html not found"
    return path.read_text(encoding="utf-8", errors="ignore"), None


def grade(transcript, workspace_path):
    html, err = _load_html(workspace_path)
    records = []

    exists = html is not None
    records.append({
        "id": "file_exists",
        "score": 1.0 if exists else 0.0,
        "weight": 0.08,
        "description": "checkout.html exists in the workspace.",
        "details": None if exists else err,
    })

    if not exists:
        records.extend([
            {"id": "step_indicator", "score": 0.0, "weight": 0.12, "description": "Includes a visible 3-step progress indicator.", "details": "HTML file missing."},
            {"id": "cart_review", "score": 0.0, "weight": 0.14, "description": "Includes cart items, quantity controls, and totals.", "details": "HTML file missing."},
            {"id": "empty_state", "score": 0.0, "weight": 0.08, "description": "Includes an empty cart state.", "details": "HTML file missing."},
            {"id": "shipping_form", "score": 0.0, "weight": 0.14, "description": "Includes all required shipping fields.", "details": "HTML file missing."},
            {"id": "validation_logic", "score": 0.0, "weight": 0.16, "description": "Contains validation hooks and blocking behavior for invalid input.", "details": "HTML file missing."},
            {"id": "payment_logic", "score": 0.0, "weight": 0.14, "description": "Includes card formatting, expiry formatting, CVV, and brand detection markers.", "details": "HTML file missing."},
            {"id": "success_modal", "score": 0.0, "weight": 0.14, "description": "Includes a success modal/overlay with completion messaging.", "details": "HTML file missing."},
        ])
        return records

    lower = html.lower()

    indicator_score = 1.0 if ("step" in lower and ("current" in lower or "completed" in lower)) else 0.0
    records.append({
        "id": "step_indicator",
        "score": indicator_score,
        "weight": 0.12,
        "description": "Includes a visible 3-step progress indicator.",
        "details": None if indicator_score == 1.0 else "Step indicator markers are incomplete.",
    })

    cart_ok = ("cart review" in lower) and ("quantity" in lower) and ("total" in lower) and ("+" in html and "-" in html)
    records.append({
        "id": "cart_review",
        "score": 1.0 if cart_ok else 0.0,
        "weight": 0.14,
        "description": "Includes cart items, quantity controls, and totals.",
        "details": None if cart_ok else "Cart step is missing quantity/totals behavior markers.",
    })

    empty_ok = "no data" in lower or "empty state" in lower or "continue shopping" in lower or "clear data" in lower or "empty cart" in lower
    records.append({
        "id": "empty_state",
        "score": 1.0 if empty_ok else 0.0,
        "weight": 0.08,
        "description": "Includes an empty cart state.",
        "details": None if empty_ok else "No empty-state markers found.",
    })

    shipping_fields = ["full name", "email", "address", "city", "zip", "country"]
    shipping_score = sum(1 for field in shipping_fields if field in lower) / len(shipping_fields)
    records.append({
        "id": "shipping_form",
        "score": shipping_score,
        "weight": 0.14,
        "description": "Includes all required shipping fields.",
        "details": None if shipping_score == 1.0 else "One or more shipping fields are missing.",
    })

    validation_ok = ("invalid" in lower or "error" in lower) and ("required" in lower or "pattern=" in lower or "disabled" in lower)
    nav_block_ok = "cannot advance" in lower or "next" in lower or "place order" in lower or "back" in lower
    validation_score = 0.0
    if validation_ok:
        validation_score += 0.5
    if nav_block_ok:
        validation_score += 0.5
    records.append({
        "id": "validation_logic",
        "score": validation_score,
        "weight": 0.16,
        "description": "Contains validation hooks and blocking behavior for invalid input.",
        "details": None if validation_score == 1.0 else "Validation or navigation blocking markers are incomplete.",
    })

    payment_terms = ["card number", "expiry", "cvv"]
    payment_score = sum(1 for t in payment_terms if t in lower) / len(payment_terms)
    if "visa" in lower or "mastercard" in lower or "amex" in lower:
        payment_score = min(1.0, payment_score + 0.25)
    records.append({
        "id": "payment_logic",
        "score": min(1.0, payment_score),
        "weight": 0.14,
        "description": "Includes card formatting, expiry formatting, CVV, and brand detection markers.",
        "details": None if payment_score >= 1.0 else "Payment field or brand-detection markers are incomplete.",
    })

    modal_ok = ("modal" in lower or "overlay" in lower) and ("order number" in lower or "checkmark" in lower or "continue shopping" in lower)
    records.append({
        "id": "success_modal",
        "score": 1.0 if modal_ok else 0.0,
        "weight": 0.14,
        "description": "Includes a success modal/overlay with completion messaging.",
        "details": None if modal_ok else "Success modal markers are incomplete.",
    })

    return records
