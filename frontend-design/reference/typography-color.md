# Typography and Color

## Typography Scale

Use a modular scale (1.25 ratio) for consistent typography:

| Level | Size | Weight | Line Height | Usage |
|-------|------|--------|-------------|-------|
| h1 | 2.5rem (40px) | 700 | 1.2 | Page title (once per page) |
| h2 | 2rem (32px) | 700 | 1.25 | Section headings |
| h3 | 1.5rem (24px) | 600 | 1.3 | Card titles, subsection |
| h4 | 1.25rem (20px) | 600 | 1.35 | Group headings |
| body | 1rem (16px) | 400 | 1.5 | Default body text |
| small | 0.875rem (14px) | 400 | 1.5 | Captions, metadata |
| label | 0.875rem (14px) | 500 | 1 | Form labels |

## Color Palette Template

```css
:root {
  /* Primary brand */
  --color-primary: #2563eb;
  --color-primary-hover: #1d4ed8;
  --color-primary-light: #dbeafe;
  --color-primary-dark: #1e40af;

  /* Neutrals */
  --color-bg: #ffffff;
  --color-bg-secondary: #f8fafc;
  --color-text: #0f172a;
  --color-text-secondary: #64748b;
  --color-border: #e2e8f0;

  /* Semantic */
  --color-success: #22c55e;
  --color-warning: #f59e0b;
  --color-danger: #ef4444;
  --color-info: #3b82f6;
}
```

## Color Usage Rules

- Primary: buttons, links, active states, branded elements.
- Neutral: backgrounds, borders, body text, secondary text.
- Semantic colors: reserved for status indicators — never use decoratively.
- Hover states: darken primary by one shade, never change hue.

## Accessibility

- Minimum contrast ratio: 4.5:1 for normal text, 3:1 for large text (≥18px bold or ≥24px).
- Test with: WebAIM Contrast Checker or browser devtools.
- Never use color alone to indicate state — pair with icon, text, or pattern.

## Font Stack Recommendations

```css
/* System font stack (fastest, no external requests) */
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
  'Helvetica Neue', Arial, sans-serif;

/* Reading-optimized */
font-family: Georgia, 'Times New Roman', serif;
```
