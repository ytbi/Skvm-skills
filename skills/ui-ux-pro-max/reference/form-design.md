# Form Design Patterns

## Structure

- **One column** > multi-column (users scan vertically, not horizontally)
- **Labels above fields** > placeholder labels (placeholders disappear when typing)
- **Related fields grouped** with visual separation (section headers, spacing)
- **Optional fields marked explicitly**, not required fields (fewer visual distractions)

## Input Types

| Data | Input Type | Validation |
|------|-----------|------------|
| Email | `<input type="email">` | Must contain @ and domain |
| Password | `<input type="password">` | Show requirements before typing |
| Phone | `<input type="tel">` | Allow various formats; strip on backend |
| Date | `<input type="date">` or 3 dropdowns | Consider locale (MM/DD vs DD/MM) |
| Search | `<input type="search">` | Show results after 2+ characters |
| Number | `<input type="number">` | Show keyboard on mobile |

## Validation

- **Validate inline, not on submit**: Show errors when user leaves the field (on blur).
- **Error placement**: Below the field, not at top of form.
- **Error message format**: "Please enter a valid email address" (not "Invalid field").
- **Success indication**: Green checkmark or green border when field is valid.
- **Never clear fields on validation failure**: Preserve all user input.

## Button Placement

- **Primary action**: Left-aligned (F-pattern) or right-aligned (Z-pattern) — be consistent.
- **Secondary action**: Visually distinct (outline or text button), never side by side with primary without spacing.
- **Destructive action**: Red with warning text, requires confirmation.
- **Disabled state**: Use sparingly — explain why a button is disabled, or let users click and show error.

## Mobile Considerations

- Minimum touch target: 44×44px
- Autofocus on first field
- Appropriate keyboard type (email, numeric, etc.)
- No horizontal scroll
- Pinch-to-zoom should not be disabled
