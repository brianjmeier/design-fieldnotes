# Stress the layout with real content

Responsive design is a negotiation between content, priority, and available space. Use narrow widths and awkward data to reveal what the layout has been assuming.

Expected evidence: At 320, 768, and 1440 CSS pixels, primary actions remain usable; the document does not overflow horizontally. Intentionally scrolling tables need separate inspection.

```
import { test, expect } from '@playwright/test';

for (const width of [320, 768, 1440]) {
  test(`projects remain usable at ${width}px`, async ({ page }) => {
    await page.setViewportSize({ width, height: 900 });
    await page.goto('/projects?fixture=long-content');
    await expect(page.getByRole('button', { name: 'New project' })).toBeVisible();
    const geometry = await page.evaluate(() => ({
      content: document.documentElement.scrollWidth,
      viewport: document.documentElement.clientWidth,
    }));
    expect(geometry.content).toBeLessThanOrEqual(geometry.viewport);
    await page.screenshot({ path: `evidence/projects-${width}.png`, fullPage: true });
  });
}
// Fixture should include long names, large amounts, zero rows, and missing images.
// Also inspect at 200% zoom and the equivalent narrow reflow width.
```

No overflow is necessary but insufficient. Screenshots and task testing must confirm meaningful order and readable content.

[W3C reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
