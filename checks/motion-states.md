# Verify motion and its quiet equivalent

Animation should explain state, location, or causality. Its reduced-motion version must communicate the same result without relying on travel or repeated movement.

Expected evidence: The result is understandable with reduced motion, repeated actions do not overlap, and exits do not strand focus or leave invisible hit targets.

```
import { test, expect } from '@playwright/test';

test('navigation remains clear with reduced motion', async ({ page }) => {
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.goto('/projects');
  await page.getByRole('button', { name: 'Open navigation' }).click();
  await expect(page.getByRole('navigation', { name: 'Primary' })).toBeVisible();
  await page.getByRole('link', { name: 'Settings', exact: true }).click();
  await expect(page.getByRole('heading', { name: 'Settings', exact: true })).toBeVisible();
});

/* In CSS, target the component rather than erasing every transition globally:
@media (prefers-reduced-motion: reduce) {
  .drawer { transition: none; }
  .decorative-loop { animation: none; }
}
*/
```

State assertions do not assess motion quality. Inspect normal motion, interruptions, rapid reversal, and reduced motion directly.

[MDN reduced motion](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion)
