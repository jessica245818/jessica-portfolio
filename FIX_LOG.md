# Portfolio responsive and accessibility fix log

Live URL: https://jessica245818.github.io/jessica-portfolio/

Audit date: 20 August 2026

## Before and after

### 1. Color contrast

- Before: the gold eyebrow text used `#C58B4E`, which was too light for dependable small-text contrast on the near-white background.
- After: changed it to `#87521F`. Its measured contrast against `#F7F6F2` is 5.96:1, passing WCAG AA for normal text.

### 2. Keyboard accessibility

- Before: form inputs had a visible focus style, but links and the submit button did not.
- After: added a high-contrast `:focus-visible` outline to links and buttons, plus a keyboard-accessible “Skip to main content” link.

### 3. Mobile touch targets and navigation

- Before: navigation links were only as tall as their text and could be difficult to tap accurately.
- After: every navigation link is at least 44px high. The navigation wraps cleanly below 520px and keeps the logo separate from the link group.

### 4. Repository destination

- Before: “GitHub” opened the general profile instead of the repository for this portfolio.
- After: “Repository” now opens `github.com/jessica245818/jessica-portfolio` directly.

### 5. Motion preference

- Before: smooth scrolling was always enabled.
- After: visitors who request reduced motion receive normal, non-animated scrolling.

## Verification performed

- Phone-size browser audit: 390 × 844. No horizontal overflow; all links were at least 44px high; the submit button was 48px high; the two-column demo stacked into one column.
- Tablet audit: 768 × 1024. No horizontal overflow; the demo retained two balanced columns.
- Desktop audit: 1440 × 900. No horizontal overflow; layout remained centered and readable.
- Dynamic feature: test values of 2,500 impressions, position 8.4, and CTR 0.25% returned “Add to the human review queue” with score 1.232.
- Link checks: the portfolio, research paper, and exact repository all returned HTTP 200.
- Image check: this page currently contains no raster work captures, so there are no oversized or blurry images to compress.
- Contrast checks: primary text, muted text, headings, buttons, score text, and the revised eyebrow color all exceed 4.5:1 against their backgrounds.

## Final physical-phone check

The automated phone-size audit is complete, but the assignment specifically requires a real phone. Open the live URL on a phone, tap all three navigation links and both main buttons, run the demo once, and take one screenshot. If that check reveals a device-specific issue, add it below before submitting.

- Physical phone model: ____________________
- Browser: ____________________
- Result: ____________________
- Screenshot attached: yes / no
