# Jessica George — portfolio

A static GitHub Pages portfolio with one dynamic feature: a client-side content-opportunity baseline demo based on my FlyRank capstone.

Live site: https://jessica245818.github.io/jessica-portfolio/

## Files

- `index.html` contains the page structure, styling, interactive form, scoring rule, and plain-words backend explanation.
- `.nojekyll` tells GitHub Pages to publish the files directly without Jekyll processing.

## Feature data flow

The visitor enters impressions, average position, and CTR. Browser JavaScript validates the values, applies the documented Week-4 baseline, and displays a human-review recommendation. No backend, database, tracking, or data submission is used.

## Baseline rule

Eligible pages have at least 300 impressions, average position from 1 to 20, and CTR below 0.50 percentage points. The score is:

`log(1 + impressions) × (0.50 − CTR) × ((21 − position) / 20)`

The feature is decision support, not a prediction of guaranteed impact.
