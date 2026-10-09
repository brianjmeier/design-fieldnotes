# Measure color in its actual role

Color supports meaning only when the foreground remains distinguishable from its actual composited background. Evaluate text, controls, focus, and semantic states separately.

Expected evidence: WCAG AA text contrast is at least 4.5:1, or 3:1 for qualifying large text. Relevant control boundaries and state indicators require 3:1 under the non-text criterion and its exceptions.

```
// Opaque sRGB hex colors only. Resolve opacity, gradients and overlays first.
function luminance(hex) {
  const rgb = hex.replace('#', '').match(/../g).map(x => parseInt(x, 16) / 255);
  const [r, g, b] = rgb.map(c => c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4);
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}
function contrast(a, b) {
  const [light, dark] = [luminance(a), luminance(b)].sort((a, b) => b - a);
  return (light + 0.05) / (dark + 0.05);
}
console.log(contrast('#606558', '#f6f5ef').toFixed(2));
// Run: node contrast.js
// Compare every actual text/state pair, including dark mode and disabled states.
// Use labels/icons as well as color to communicate success, error and selection.
```

Do not round a failing ratio into a pass. Large text is at least 18pt regular or 14pt bold; inactive controls have specific exceptions.

[W3C text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
[W3C non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)
