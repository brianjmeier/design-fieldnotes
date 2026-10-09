# Follow the primary task to its result

A clear interface earns its hierarchy by helping someone finish a job. Test the outcome, including the recoverable failure, rather than the presence of decorative components.

Expected evidence: A named action produces its intended result; a refusal preserves input and explains the next useful step.

```
import { test, expect } from '@playwright/test';

test('a person can create and find a project', async ({ page }) => {
  await page.goto('/projects');
  await page.getByRole('button', { name: 'New project', exact: true }).click();
  await page.getByLabel('Project name').fill('October launch');
  await page.getByRole('button', { name: 'Create project', exact: true }).click();
  await expect(page.getByRole('heading', { name: 'October launch' })).toBeVisible();
  await expect(page.getByRole('status')).toContainText('Project created');
});

// Add a refused-server-response case using your actual API route.
// Assert the name is retained, the error names the cause, and retry works.
// Run in the existing project: ./node_modules/.bin/playwright test primary-task.spec.ts
```

Example labels and routes must match your product. This verifies a workflow; it does not establish visual quality.

[Playwright assertions](https://playwright.dev/docs/test-assertions)
