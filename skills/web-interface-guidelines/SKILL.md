---
name: web-interface-guidelines
description: Diagnose and fix UI instability issues in web applications while preserving existing identifiers, behaviors, and test hooks. Use for layout shift, flicker, unstable rendering, visual polish regressions, and frontend repair tasks in React/Next.js-style projects.
triggers:
  - fix visual stability
  - layout shift
  - cls
  - frontend repair
  - nextjs ui bug
  - flicker fix
origin:
  source: skillsbench
  source_url: https://www.skillsbench.ai/skills
---

# Web Interface Guidelines

Use this skill for frontend repair tasks where the challenge is to improve UI stability or usability **without destabilizing the application**.

This is not a redesign skill. It is a **careful repair** skill.

## Workflow

For all frontend repair tasks, follow this strict process: inspect the code, make concrete code edits, verify those edits, and only then report on the findings. This will ensure all modifications are effective and preserve the application’s integrity.

When fixing a web interface problem:

1. Inspect before editing
2. Identify the most likely root causes of instability
3. Prefer the smallest change that addresses the issue
4. Preserve existing selectors, hooks, and identifiers
5. Record what was changed and why

## Core Rules

### 1. Diagnose before editing

- Do not start by rewriting the page wholesale
- Identify whether the issue is caused by:
  - missing reserved dimensions
  - unstable mounts
  - conditional rendering jumps
  - asynchronous content shifts
  - layout recalculation after load

### 2. Preserve existing integration points

- Do not rename existing classes
- Do not rename existing ids
- Do not rename or remove `data-testid` attributes
- Treat these as hard constraints because tests and app logic may depend on them

### 3. Prefer minimal safe repair

- Fix the instability at the point of failure
- Avoid broad redesigns when a scoped layout or render fix is enough
- Do not replace established structure unless the task explicitly allows it

### 4. Keep functionality intact

- UI stability fixes must not break the actual user flow
- Visual cleanup is not a win if interactions, state, or tests regress

### 5. Report the repair honestly

- Provide a summary of the inspection including any identified issues.
- Clearly state which files/components were modified, and explicitly confirm that all protected identifiers (classes, ids, and `data-testid` values) were preserved. This verification step is crucial before finalizing the report.

- Explain what the root causes were
- State which files/components changed
- Explicitly state that protected identifiers were preserved

## Pre-Submit Checklist

Before final submission, verify:

- the issue analysis names plausible visual-stability causes
- code changes are targeted rather than destructive
- class names, ids, and `data-testid` values are preserved
- the report file exists and reflects the real modifications

## Common Failure Modes

- Treating the task like a full redesign
- Renaming selectors or test hooks
- Adding noisy changes unrelated to the stability issue
- Writing a report without actually making concrete code edits
