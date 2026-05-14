# Common Component Patterns

## Button

```html
<button class="btn btn--primary" type="button">
  <span class="btn__label">Submit</span>
</button>

<button class="btn btn--secondary" type="button" disabled>
  <span class="btn__label">Saving...</span>
</button>
```

```css
.btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-4);
  border-radius: var(--border-radius);
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  border: 1px solid transparent;
  transition: background-color 0.15s, box-shadow 0.15s;
}
.btn:focus-visible { outline: 2px solid var(--color-primary); outline-offset: 2px; }
.btn[disabled] { opacity: 0.5; cursor: not-allowed; }
```

## Form Field

```html
<div class="field">
  <label class="field__label" for="email">Email address</label>
  <input class="field__input" id="email" type="email" required
         placeholder="you@example.com"
         aria-describedby="email-hint">
  <p class="field__hint" id="email-hint">We'll never share your email.</p>
  <p class="field__error" role="alert" hidden>Please enter a valid email.</p>
</div>
```

## Card

```html
<article class="card">
  <img class="card__image" src="..." alt="" loading="lazy">
  <div class="card__body">
    <h3 class="card__title">Card Title</h3>
    <p class="card__text">Supporting description.</p>
  </div>
  <div class="card__footer">
    <a class="card__link" href="#">Learn more</a>
  </div>
</article>
```

## Navigation

```html
<nav aria-label="Main navigation">
  <ul class="nav__list">
    <li><a class="nav__link nav__link--active" aria-current="page" href="/">Home</a></li>
    <li><a class="nav__link" href="/about">About</a></li>
    <li><a class="nav__link" href="/contact">Contact</a></li>
  </ul>
</nav>
```

## Modal/Dialog

```html
<dialog class="modal" id="confirm-modal">
  <div class="modal__content">
    <h2 class="modal__title">Confirm deletion</h2>
    <p>This action cannot be undone.</p>
    <div class="modal__actions">
      <button class="btn btn--secondary" onclick="this.closest('dialog').close()">Cancel</button>
      <button class="btn btn--danger" autofocus>Delete</button>
    </div>
  </div>
</dialog>
```
