# Portfolio hardening log

Live site: https://jessica245818.github.io/jessica-portfolio/

Hardening date: 20 August 2026

## Where I tried to break it

| Test | What happened | Triage | Action |
|---|---|---|---|
| Submit with an empty required field | Native browser validation blocks the click, but the JavaScript previously converted a bypassed empty value to zero. | Fix now | Added an explicit empty-string check before number conversion. Empty or non-numeric values cannot produce a score. |
| Enter letters into number fields | Number inputs reject text in normal use; the scoring code also rejects non-finite values. | Fixed / defended | Kept numeric input types and added explicit JavaScript validation. |
| Enter negative impressions | The HTML minimum blocks submission. | Fixed / defended | Kept `min="0"`; no score is produced through the normal form. |
| Enter a position above 100 or CTR above 100 | HTML maximum constraints block submission. | Fixed / defended | Kept the range constraints and required fields. |
| Submit twice quickly | The same deterministic result is rendered twice; no duplicate request or record is created because there is no server submission. | No break | No change required. |
| Use the eligible example | 2,500 impressions, position 8.4, CTR 0.25% returns review action and score 1.232. | Pass | No change required. |
| Use a non-eligible example | 100 impressions, position 35, CTR 1.2% returns no baseline action and lists the failed thresholds. | Pass | No change required. |
| Test phone, tablet, and desktop widths | No horizontal overflow at 390px, 768px, or 1440px. The form stacks on phone width. | Pass | Earlier mobile fixes retained. |
| Click portfolio, research paper, and repository URLs | All three destinations returned HTTP 200. | Pass | Repository link already points to the exact project. |
| Test without a backend | The feature continues to work because it is intentionally client-side. Refresh clears all entered values. | Known limitation | No persistence is intentional for privacy and free hosting. |

## SEO and social sharing added

- Specific page title and meta description
- Canonical URL
- Open Graph title, description, URL, image, dimensions, and image description
- Twitter large-image card metadata
- 1200 × 630 compressed social preview image (about 32 KB)
- Search-engine `robots.txt`
- XML sitemap
- Person structured data using Schema.org JSON-LD

## Findability and speed

- A web search for the exact site and for “Jessica George jessica245818 portfolio” did not yet return this new portfolio. Search engines need time to discover and index new GitHub Pages sites. This is a **known limitation**, not evidence that the page is broken.
- The page now exposes a canonical URL, crawl permission, and sitemap to support indexing.
- Google PageSpeed Insights' public API returned a temporary rate-limit response during the check. As a fallback measurement, a fresh command-line request to the live page recorded approximately 0.264 seconds to first byte and 0.267 seconds total for the HTML response.
- The HTML is about 12 KB and the only image is the approximately 32 KB social preview, which is not rendered in the visible page. The page has no web-font, framework, analytics, database, or API dependency.

## Fix-now items completed

1. Explicit empty-input validation added.
2. Search description and title made specific to search data and machine learning.
3. Canonical, crawler, sitemap, social-preview, and structured-data metadata added.
4. Social preview compressed and kept outside the visible page load.

## Known limitations

- The site is not yet visible in search results; indexing timing is controlled by search engines.
- The scoring demo is a transparent baseline, not a production model and not proof that a content change will cause an improvement.
- Values are not stored. Refreshing resets the demo.
- No automated cross-browser service was used; Safari/Chrome on a real second device should still be included in the human review.
- The page does not yet have analytics, so usage and failures are not measured over time.

## Hardening-review request

Send this log and the live URL to a mentor or peer with this message:

> Please harden-review my portfolio rather than reviewing its visual taste. Try empty, extreme, and repeated inputs; open every link; check it on a different browser or phone; and inspect the “known limitations” list. Tell me which item is a must-fix before launch and which can remain documented. Please do not use private or client data in the demo.

## Reviewer response

This section must contain a real mentor or peer response before the checkpoint is submitted.

- Reviewer: ____________________
- Browser/device: ____________________
- Must-fix feedback: ____________________
- Nice-to-have feedback: ____________________
- Change made in response: ____________________
