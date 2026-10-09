# Make focus follow the interaction

A pointer screenshot cannot reveal where keyboard users are stranded. Follow focus into a dialog, through its controls, and back to the invoking action.

Expected evidence: The dialog receives focus, Escape dismisses it, focus returns to its trigger, and every action has a visible keyboard focus indicator.

```
import { test, expect } from '@playwright/test';

test('dialog returns focus to its trigger', async ({ page }) => {
  await page.goto('/projects');
  const trigger = page.getByRole('button', { name: 'New project', exact: true });
  await trigger.focus();
  await page.keyboard.press('Enter');
  await expect(page.getByRole('dialog')).toBeVisible();
  await expect(page.getByLabel('Project name')).toBeFocused();
  await page.keyboard.press('Escape');
  await expect(page.getByRole('dialog')).not.toBeVisible();
  await expect(trigger).toBeFocused();
});
// Manually Tab through the entire flow and inspect the visible focus ring.
// Confirm no trap, no off-screen focused control, and no hover-only actions.
```

A dialog may intentionally focus a heading instead of its first field; adapt the expectation to the content and documented focus decision.

[W3C dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)
