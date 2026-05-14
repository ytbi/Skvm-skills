# Layout and Spacing Systems

## Spacing Scale

Use a consistent 4px base spacing scale:

| Token | Pixels | Rem | Usage |
|-------|--------|-----|-------|
| space-1 | 4px | 0.25 | Icons, badges |
| space-2 | 8px | 0.5 | Tight padding, gap between related controls |
| space-3 | 12px | 0.75 | Button padding, card inner padding |
| space-4 | 16px | 1 | Default spacing, section padding |
| space-5 | 24px | 1.5 | Section margins, card gaps |
| space-6 | 32px | 2 | Page section spacing |
| space-7 | 48px | 3 | Major section separation |
| space-8 | 64px | 4 | Page-level margins |

## Layout Patterns

| Pattern | Use Case | Technique |
|---------|----------|-----------|
| Stack | Single column, vertical flow | `display: flex; flex-direction: column; gap` |
| Inline | Horizontal row of items | `display: flex; gap; align-items: center` |
| Grid | 2D layout, equal cells | `display: grid; grid-template-columns` |
| Sidebar | Main + aside | `display: grid; grid-template-columns: 1fr 300px` |
| Centered | Max-width container | `max-width: 1200px; margin: 0 auto` |

## CSS Custom Properties

```css
:root {
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 24px;
  --space-6: 32px;
  --space-7: 48px;
  --space-8: 64px;
  --max-width: 1200px;
  --border-radius: 8px;
}
```

## Common Anti-Patterns

- Mixing px, rem, and em for spacing — use one unit consistently (prefer rem).
- 1px gaps between layout elements — use gap properties, not margins on children.
- Fixed heights on containers — text can grow, containers should flex.
