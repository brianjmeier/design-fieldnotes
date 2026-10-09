# Exercise the component’s complete state model

A beautiful default state says little about slow, missing, or refused work. Build states from the resource lifecycle and give each a useful next step.

Expected evidence: Loading is distinct from empty; failures preserve context; retries cannot duplicate an operation; disabled controls explain what is missing.

```
Use your existing fixture or request-interception seam to produce:

loading   → stable geometry, clear pending feedback
empty     → reason for absence + useful first action
success   → result appears + feedback names the completed action
error     → speakable cause + retained input + recoverable next action
partial   → available content remains useful + missing data is named
long data → large counts, long names, translated labels, missing media

For each relevant state:
  capture the viewport and accessibility tree;
  perform the primary action using keyboard and pointer;
  record the actual result and recovery, not just a screenshot.

Network race: submit twice while pending. Observe one intended operation.
Do not claim that a disabled button alone proves backend idempotency.
```

A state inventory is evidence planning, not the skill. Choose the states that the component can actually enter.
