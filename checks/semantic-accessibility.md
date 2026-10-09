# Check semantics, then inspect meaning

The accessibility tree should communicate the same action and structure as the pixels. Pair an automated scan with a direct reading of labels, order, and live feedback.

Expected evidence: No violations in the scanned state; labels describe actions and results are announced without unnecessary interruptions.

```
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('projects expose their meaning', async ({ page }) => {
  await page.goto('/projects');
  const result = await new AxeBuilder({ page }).analyze();
  expect(result.violations).toEqual([]);
  await expect(page.getByRole('heading', { level: 1, name: 'Projects' })).toBeVisible();
  await expect(page.getByRole('button', { name: 'New project' })).toBeVisible();
});
// Repeat the scan in open menus, dialogs, errors, and empty states.
// Inspect with a screen reader: heading structure, names, state, announcements.
```

Requires existing axe dependency. A zero-violation scan is not an accessibility conformance claim.

[Playwright accessibility testing](https://playwright.dev/docs/accessibility-testing)
