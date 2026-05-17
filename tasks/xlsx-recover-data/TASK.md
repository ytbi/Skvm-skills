---
name: xlsx-recover-data
source: skillsbench
source_url: https://www.skillsbench.ai/tasks/xlsx-recover-data
category: spreadsheet
difficulty: medium
status: raw-import
skill: data-reconciliation
---

# xlsx-recover-data

Recover missing values in an Excel file `nasa_budget_incomplete.xlsx`.

## Task Description

Missing values are marked with `???`.

Analyze the relationships between sheets to determine the correct values and replace each `???` with the computed numeric value.

Save the repaired result as:

- `nasa_budget_recovered.xlsx`

## Why This Task Is Interesting For SkVM

- Structured binary artifact output
- Multiple sheets can encode implicit constraints
- Suitable for:
  - no-skill vs original
  - AOT compile
  - JIT optimize

## Migration Notes

When converting to a SkVM-native task later, likely outputs/checks include:

- file exists
- workbook parses
- recovered cells match expected values
- cross-sheet consistency holds
