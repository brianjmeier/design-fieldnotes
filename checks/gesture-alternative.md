# Give gestures a discoverable alternative

Swiping and dragging can reduce effort for fluent users, while hiding the action from everyone else. Preserve the same operation through an ordinary visible control.

Expected evidence: The same action is available without a complex path gesture or drag. Targets meet the applicable size criterion; common 44px comfort targets are a design choice, not WCAG AA’s blanket minimum.

```
import { test, expect } from '@playwright/test';

test('archive is available without swiping', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('/messages');
  const row = page.getByRole('listitem').filter({ hasText: 'October launch' });
  await row.getByRole('button', { name: 'More actions' }).click();
  await page.getByRole('menuitem', { name: 'Archive', exact: true }).click();
  await expect(page.getByRole('status')).toContainText('Archived');
  await page.getByRole('button', { name: 'Undo', exact: true }).click();
  await expect(row).toBeVisible();
});
// On a real touch device: test scroll vs swipe intent, cancellation and reversal.
// Measure hit areas, not icon glyphs. WCAG 2.2 AA target size is 24x24 CSS px
// with specified spacing and other exceptions; 44x44 is the enhanced criterion.
```

A desktop emulated viewport is not touch-device verification. Irreversible actions need an appropriate recovery or confirmation decision.

[W3C pointer gestures](https://www.w3.org/WAI/WCAG22/Understanding/pointer-gestures.html)
[W3C target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
