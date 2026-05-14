# Responsive Design and Grid

## Breakpoints

Use these breakpoints consistently:

| Name | Min-width | Target |
|------|-----------|--------|
| mobile | 0 | Default (mobile-first) |
| tablet | 640px | Large phones, tablets |
| desktop | 1024px | Laptops, desktops |
| wide | 1280px | Large desktops |

```css
/* Mobile-first approach */
.grid { display: grid; gap: var(--space-4); grid-template-columns: 1fr; }

@media (min-width: 640px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 1024px) {
  .grid { grid-template-columns: repeat(3, 1fr); }
}
```

## Grid Patterns

| Columns | Container | Column Width | Gap |
|---------|-----------|-------------|-----|
| 1 | 100% | 1fr | — |
| 2 | 640px+ | 1fr 1fr | 16px |
| 3 | 1024px+ | 1fr 1fr 1fr | 24px |
| 12 | Any | repeat(12, 1fr) | 16px |

## Responsive Patterns

**Stack → Sidebar:**
```css
.page { display: flex; flex-direction: column; gap: var(--space-6); }
@media (min-width: 1024px) {
  .page { flex-direction: row; }
  .page__main { flex: 1; }
  .page__aside { width: 320px; flex-shrink: 0; }
}
```

**Image + Text:**
- Mobile: image full width above text
- Desktop: image beside text (50/50 or 40/60)

## Common Mistakes

- Hiding content on mobile (`display: none`) instead of reorganizing.
- Using em/rem for media queries — use px for breakpoints.
- Fixed-width containers that break on smaller viewports.
- Images without `max-width: 100%` causing horizontal scroll.
- Touch targets too small or too close together on mobile.
