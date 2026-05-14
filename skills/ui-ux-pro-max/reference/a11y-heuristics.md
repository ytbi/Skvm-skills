# Accessibility Heuristics

## Perceivable

- [ ] All images have appropriate alt text (descriptive or `alt=""` for decorative)
- [ ] Color is never the sole means of conveying information
- [ ] Text contrast ≥ 4.5:1 (normal) / 3:1 (large text)
- [ ] Content can be zoomed to 200% without loss of functionality
- [ ] Captions provided for video/audio content

## Operable

- [ ] All functionality is available via keyboard
- [ ] Focus order follows visual order (no positive tabindex)
- [ ] Focus indicators are always visible (never `outline: none` without replacement)
- [ ] Touch targets ≥ 44×44px
- [ ] No content flashes more than 3 times per second

## Understandable

- [ ] Page language is declared (`<html lang="en">`)
- [ ] Navigation is consistent across pages
- [ ] Error messages are clear and suggest a fix
- [ ] Form inputs have associated `<label>` elements
- [ ] Autocomplete attributes on common fields (`email`, `tel`, `address`)

## Robust

- [ ] HTML is valid and semantic (W3C validator passes)
- [ ] ARIA landmarks used where HTML5 semantic elements are insufficient
- [ ] Custom components follow WAI-ARIA authoring practices
- [ ] Screen reader can navigate all content

## Quick Wins (High impact, low effort)

1. Add skip-to-content link at top of page
2. Ensure all form inputs have labels
3. Increase color contrast on low-contrast text
4. Add focus styles to all interactive elements
5. Add alt text to all images
6. Fix heading hierarchy (one h1, sequential h2-h6)
