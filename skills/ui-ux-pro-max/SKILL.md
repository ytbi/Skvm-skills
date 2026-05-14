---
name: ui-ux-pro-max
slug: ui-ux-pro-max
version: 1.0.0
homepage: https://skills.sh/nextlevelbuilder/ui-ux-pro-max-skill
description: "UI/UX design and user experience optimization. Design intuitive interfaces, improve user flows, create wireframes and prototypes, apply usability heuristics, and conduct UX audits. Use when (1) you need to design or evaluate a user interface; (2) the user wants to improve conversion, retention, or usability; (3) the work involves wireframes, mockups, user flows, or design systems; (4) you need to apply UX principles, accessibility, or design thinking; (5) the user explicitly installs or references the skill for the current task."
metadata: {"openclaw":{"emoji":"🎯","requires":{"bins":[]},"os":["linux","darwin","win32"]}}
---

## When to Use

Use this skill when the user needs to design, evaluate, or improve a user interface or user experience — from wireframes and prototypes to usability audits and design critiques.

Use it for user flow design, wireframing, visual hierarchy, conversion optimization, form UX, navigation patterns, onboarding design, error states, empty states, loading states, and accessibility compliance.

Prefer this skill over generic design help when the hard part is UX judgment: user mental models, task flows, information architecture, or usability trade-offs.

User asks about: designing a UI, improving UX, wireframes, user flow, usability, conversion, form design, onboarding, navigation, or design critique.

## Core Principle

Good UX is invisible. Every screen should guide the user to their goal without them having to think about it. If a user notices the design, the design failed.

## Before Designing

Before starting any design work:
1. **Who is the user?** — Primary persona, their goal, their context (mobile/desktop, time pressure, familiarity)
2. **What is the task?** — The single most important action on this screen
3. **What are the states?** — Loading, empty, error, success, edge cases
4. **What is the success metric?** — How will you know if this design works?

## Core Rules

### 1. One primary action per screen
- Every screen should have exactly one primary action (button, CTA). Everything else is secondary.
- If a screen has multiple equally important actions, it needs to be broken into multiple screens.

### 2. Reduce cognitive load
- Short-term memory holds ~4 items at once. Don't make users remember information across screens.
- Chunk information into groups of 3-5 items.
- Use recognition over recall: show options rather than requiring users to type from memory.

### 3. Error prevention over error handling
- Prevent errors through good defaults, constraints, and confirmation dialogs.
- When errors do happen: explain what happened in plain language, and tell the user exactly what to do next.
- Never show raw error codes or technical jargon to end users.

### 4. Consistency reduces learning
- Use the same patterns for the same purposes throughout the product.
- Follow platform conventions (iOS HIG, Material Design, or your own design system).
- Consistent placement of navigation, search, and actions builds user confidence.

### 5. Visibility of system status
- Every user action should have immediate, visible feedback.
- Loading states: skeleton screens > spinners > progress bars.
- Show estimated time for operations longer than 2 seconds.

### 6. Match between system and real world
- Speak the user's language: use their domain terminology, not technical jargon.
- Follow real-world conventions: shopping cart, trash can, folder — these metaphors work because users already understand them.

### 7. User control and freedom
- Every action should be reversible (undo, cancel, go back).
- Never force users through a linear flow when they might need to deviate.
- Provide clear exits for modal dialogs and overlays.

## The UX Audit Framework

When evaluating an existing design, follow this framework:

1. **Task analysis**: Can a new user complete the primary task in under 30 seconds?
2. **Heuristic evaluation**: Check against Nielsen's 10 usability heuristics
3. **Accessibility scan**: Check color contrast, keyboard navigation, screen reader support
4. **Consistency check**: Are patterns repeated consistently across screens?
5. **Error state review**: What happens when something goes wrong at each step?

## Common UX Anti-Patterns

- **Hamburger menu hiding primary navigation**: Often used as a lazy solution — consider tab bars or visible navigation instead.
- **Endless scrolling without context**: Show how many items exist and where the user is.
- **Confirm dialogs for every action**: Train users to ignore dialogs. Only confirm destructive, irreversible actions.
- **Forms that clear on error**: Users lose all typed input. Always preserve form data on validation failure.
- **Login walls before content**: Users leave. Show value first, ask for signup later.
- **Surprising behavior**: "Click here to read more" that opens a PDF download without warning.
- **Motion without purpose**: Animations that slow down the user without providing information.

## Design Deliverables

| Deliverable | Purpose | Format |
|-------------|---------|--------|
| User flow diagram | Steps user takes to complete a task | Markdown list or Mermaid diagram |
| Wireframe | Layout and structure without visual design | ASCII art, Markdown table, or HTML |
| Interactive prototype | Clickable flow to test usability | Describe states and transitions |
| UX audit report | Evaluation of existing design | Structured markdown with findings |
| Design critique | Feedback on a specific design | Organized by severity (critical/major/minor) |

## Related Reference Files

| Topic | File |
|-------|------|
| UX audit checklist | `reference/ux-audit.md` |
| User flow templates | `reference/user-flows.md` |
| Form design patterns | `reference/form-design.md` |
| Microcopy guidelines | `reference/microcopy.md` |
| Accessibility heuristics | `reference/a11y-heuristics.md` |

## Output Standards

1. **Lead with the user problem**, not the design solution.
2. **Describe user flows in terms of goals**, not UI elements.
3. **State assumptions explicitly**: "Assuming the user is returning, not first-time."
4. **Prioritize findings by impact**: Critical > Major > Minor > Cosmetic.
5. **Always include the "why" behind design decisions.**
