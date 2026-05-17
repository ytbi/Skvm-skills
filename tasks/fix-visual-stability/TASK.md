---
name: fix-visual-stability
source: skillsbench
source_url: https://www.skillsbench.ai/tasks/fix-visual-stability
category: web-performance
difficulty: hard
status: raw-import
skill: web-interface-guidelines
---

# fix-visual-stability

Fix visual instability issues in a Next.js e-commerce application.

## Task Description

There is a Next.js app at:

- `/app`

Users experience visual instability issues including layout shifts and generally poor UX.

Your job is to assess the root cause of the user experience issues using React/Next.js best practices and fix the implementation accordingly.

## Rules

- Do not break existing functionality
- Do not change existing class names
- Do not change existing ids
- Do not change existing `data-testid` values, because tests rely on them

## Why This Task Is Interesting For SkVM

- Real frontend engineering behavior
- Requires diagnosis + minimal safe edits
- Skill quality can strongly affect whether the agent:
  - over-edits
  - breaks identifiers
  - chases the wrong cause

## Migration Notes

When converting to a SkVM-native task later, likely checks include:

- required files still build
- targeted visual-stability regressions are reduced
- protected identifiers are unchanged
- final output preserves application behavior
