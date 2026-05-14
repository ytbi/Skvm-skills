# Accessibility Checklist

## Semantic HTML

- [ ] Use `<nav>`, `<main>`, `<header>`, `<footer>`, `<section>`, `<article>` instead of generic `<div>`.
- [ ] One `<h1>` per page. Heading levels are semantic, not visual.
- [ ] Use `<button>` for actions, `<a>` for navigation — never use `<div>` or `<span>` as clickable elements.
- [ ] Form inputs have associated `<label>` elements (not placeholders alone).
- [ ] Use `<ul>` / `<ol>` for lists, not repeated `<div>`.
- [ ] Use `<table>` with `<th>` for tabular data, not for layout.

## Keyboard Navigation

- [ ] All interactive elements are reachable via Tab key.
- [ ] Tab order follows visual order (no positive `tabindex` values).
- [ ] Focus indicators are visible (never `outline: none` without replacement).
- [ ] Custom components (dropdown, modal, tabs) support arrow keys per WAI-ARIA patterns.
- [ ] Skip link present at page top for keyboard users.

## ARIA

- [ ] Use native HTML semantics first — ARIA is a supplement, not a replacement.
- [ ] `aria-label` on icon-only buttons and links.
- [ ] `aria-expanded` on expandable elements.
- [ ] `aria-current="page"` on current navigation link.
- [ ] `role="alert"` on dynamic error messages.
- [ ] `aria-live="polite"` on dynamically updating content.

## Color and Contrast

- [ ] Text contrast ≥ 4.5:1 (normal) / 3:1 (large).
- [ ] No information conveyed by color alone.
- [ ] Focus indicators have ≥ 3:1 contrast against adjacent colors.

## Forms

- [ ] Error messages are associated with inputs via `aria-describedby`.
- [ ] Required fields are indicated visually AND programmatically (`required` attribute).
- [ ] Autocomplete attributes on common fields (`email`, `tel`, `address`).

## Images and Media

- [ ] All `<img>` elements have descriptive `alt` text.
- [ ] Decorative images use `alt=""` (empty alt).
- [ ] Video and audio have captions or transcripts.

## Testing

- [ ] Test with keyboard only (no mouse).
- [ ] Test with browser zoom to 200%.
- [ ] Run axe DevTools or Lighthouse accessibility audit.
- [ ] Test with a screen reader (VoiceOver, NVDA, or JAWS).
