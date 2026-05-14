---
name: frontend-design
description: Frontend UI and page design for responsive web interfaces. Use for landing pages, dashboards, forms, navigation, card layouts, responsive redesigns, accessibility cleanup, and design-system-aligned component work.
triggers:
  - design frontend
  - build ui
  - responsive page
  - landing page
  - dashboard ui
  - form ux
  - design system
  - accessibility review
  - frontend layout
  - ui component
---

# Frontend Design

Design and implement frontend interfaces that are visually coherent, responsive, and accessible. This skill is for tasks where layout, component structure, hierarchy, spacing, color, or usability matter as much as the code itself.

Use this skill when the output is expected to be:

- a page or screen layout
- a reusable UI component
- a responsive redesign
- a form or navigation flow
- a small design-system-consistent frontend feature

## Workflow

When solving a frontend-design task:

1. Identify the primary user goal on the screen
2. Extract the content hierarchy before choosing layout
3. Choose the simplest layout pattern that fits the content
4. Apply a consistent spacing, typography, and color system
5. Ensure responsive behavior and accessible interactions
6. Validate empty, error, and loading states before finishing

Do not start from arbitrary CSS. Start from hierarchy, layout pattern, and interaction requirements.

## Output Priorities

In order of priority:

1. Correct user flow
2. Clear visual hierarchy
3. Responsive layout behavior
4. Accessibility and interaction quality
5. Aesthetic polish

If there is a tradeoff, prefer structure and usability over visual decoration.

## Core Rules

### 1. Start from hierarchy, not decoration

- Decide what the primary action is before styling anything.
- Make the most important action or information the most visually prominent.
- Group related elements with spacing and alignment before adding borders or background blocks.

### 2. Use a real spacing system

- Use a consistent spacing scale instead of ad hoc margins.
- Prefer layout gap systems over scattered child margins.
- Use larger spacing to separate sections than to separate items inside a section.

See `reference/layout-spacing.md`.

### 3. Make layout explicit

- Pick one layout pattern deliberately: stack, split, grid, sidebar, or dashboard.
- Do not mix multiple layout systems without a clear reason.
- Avoid dense multi-column layouts on mobile unless the task explicitly requires them.

See `reference/responsive-grid.md`.

### 4. Typography must carry hierarchy

- Heading levels should reflect information structure, not just visual size.
- Body text must remain readable without zoom.
- Avoid more than a handful of font sizes on the same screen.

See `reference/typography-color.md`.

### 5. Components should be composable

- One component should have one clear responsibility.
- Name components by role, not location.
- Prefer composition over giant all-in-one components.

See `reference/component-patterns.md`.

### 6. Accessibility is a default constraint

- Interactive elements must remain keyboard reachable.
- Focus states must be visible.
- Contrast and hit-target size are hard constraints, not optional cleanup.

See `reference/accessibility.md`.

### 7. Design all important states

Every important view should account for at least:

- normal state
- loading state
- empty state
- error state

If the task asks for a data UI and you only design the happy path, the job is incomplete.

## Frontend Design Checklist

Before final submission, verify:

- the page has one clear primary action or focal point
- spacing is consistent across the screen
- the layout still works on narrow screens
- text hierarchy is obvious without color alone
- buttons, inputs, and links are visibly interactive
- there is at least one meaningful empty/error/loading strategy where relevant
- semantics are correct (`button`, `form`, `nav`, `main`, `section`, etc.)

## Common Failure Modes

- Starting from a visual gimmick instead of user goal
- Overusing nested containers and wrappers
- Making desktop layout first and collapsing it badly on mobile
- Using arbitrary spacing values that destroy rhythm
- Treating accessibility as a post-process instead of a design constraint
- Creating components that look different but solve the same role
- Designing only the success path

## Code Expectations

When implementation is requested:

- use semantic HTML
- keep layout primitives simple and explicit
- prefer CSS variables or shared tokens for spacing/color/typography
- include responsive behavior
- include interactive states
- avoid unnecessary complexity in CSS architecture

The design should feel intentional, but maintainability matters more than flashy visuals.
