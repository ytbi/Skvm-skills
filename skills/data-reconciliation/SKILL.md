---
name: data-reconciliation
description: Recover missing or inconsistent values in structured tabular data while preserving the original file format and validating cross-sheet consistency. Use for spreadsheet repair, numeric reconciliation, totals recovery, and structured data correction.
triggers:
  - recover spreadsheet values
  - repair xlsx
  - fill missing values
  - reconcile tabular data
  - recover corrupted workbook
  - spreadsheet consistency check
origin:
  source: skillsbench
  source_url: https://www.skillsbench.ai/skills
---

# Data Reconciliation

Recover missing or inconsistent values in structured spreadsheet-style data by reasoning from the surrounding rows, columns, totals, and cross-sheet relationships.

This skill is not for vague guesswork. It is for deterministic or near-deterministic recovery tasks where the missing values can be inferred from the data already present.

## Workflow

When repairing structured tabular data:

1. Inventory the workbook structure first
2. Identify every missing or suspicious cell
3. Infer recovery constraints from:
   - row totals
   - column totals
   - formulas
   - cross-sheet references
   - repeated patterns
4. Fill only the missing values that can be justified by the observed constraints
5. Preserve the original workbook structure and all unaffected cells
6. **Generate a valid `.xlsx` file**: Ensure that the output file structure conforms to the `.xlsx` specification and can be opened as a valid Excel workbook. This involves creating a real workbook, not just a text file with an `.xlsx` extension.
7. **Validate the repaired workbook before submission**: Before final submission, confirm:
   - every placeholder / missing token has been replaced
   - repaired values are numeric where numeric values are expected
   - the workbook still opens successfully
   - cross-sheet totals and consistency checks still hold
   - the validation/report artifact matches the actual repaired workbook

When repairing structured tabular data:

1. Inventory the workbook structure first
2. Identify every missing or suspicious cell
3. Infer recovery constraints from:
   - row totals
   - column totals
   - formulas
   - cross-sheet references
   - repeated patterns
4. Fill only the missing values that can be justified by the observed constraints
5. Preserve the original workbook structure and all unaffected cells
6. Validate the repaired workbook before submission

## Core Rules

### 1. Preserve the artifact format

- If the input is `.xlsx`, the output must remain `.xlsx`
- Do not replace the workbook with CSV, JSON, or markdown summaries
- Do not flatten multi-sheet structure into a text report
- Ensure the output is a valid and parsable `.xlsx` workbook that can be opened in Excel, with appropriate handling of file metadata ensuring compliance with `.xlsx` standards.

### 1. Preserve the artifact format

- If the input is `.xlsx`, the output must remain `.xlsx`
- Do not replace the workbook with CSV, JSON, or markdown summaries
- Do not flatten multi-sheet structure into a text report

### 2. Recover from constraints, not intuition

- Prefer arithmetic consistency over semantic guessing
- Use totals, deltas, ratios, and mirrored rows before using narrative assumptions
- If multiple sheets encode the same number indirectly, they should agree after repair

### 3. Change only what is required

- Keep all existing sheet names, unaffected cells, and layout structure
- Do not rewrite large parts of the workbook when only a few cells are missing
- Do not invent extra sheets or metadata unless explicitly requested

### 4. Validate before final submission

Before final submission, confirm:

- every placeholder / missing token has been replaced
- repaired values are numeric where numeric values are expected
- the workbook still opens successfully
- cross-sheet totals and consistency checks still hold
- the validation/report artifact matches the actual repaired workbook

## Common Failure Modes

- Replacing the workbook with the wrong file type
- Filling placeholders with prose instead of numbers
- Fixing one sheet while breaking another sheet's totals
- Writing a recovery report that claims success without checking the workbook
- Modifying non-missing cells unnecessarily

## Output Discipline

If the task requests both a repaired workbook and a machine-readable validation report, always:

1. repair the workbook first
2. validate the workbook
3. then write the report so it reflects the actual result
