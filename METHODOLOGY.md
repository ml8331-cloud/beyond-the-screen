# Beyond the Screen: research and methods

Independent portfolio study prepared for a FOX Entertainment Summer 2027 internship application. Not affiliated with, commissioned by, or endorsed by FOX. Research access date: October 19, 2026. Historical data windows differ by source and are stated separately. No internal FOX data, paid campaign records, interviews or user research were available. AI assisted public-source research, analysis, writing and artifact production. The applicant should review the work and be able to explain it before submission.

## Research question

How could two FOX entertainment franchises turn casual clip discovery into qualified episode-page visits? This study combines a descriptive public-data audit with creative hypotheses and a proposed experiment. It does not claim measured audience growth.

## Google Trends: 53 weekly observations

Source: [saved query](https://trends.google.com/trends/explore?date=2025-01-01%202025-12-31&geo=US&q=The%20Masked%20Singer,The%20Floor%20FOX).

- Search terms: `The Masked Singer` and `The Floor FOX`, entered together. These are search terms, not Google Topic entities and not exact-phrase searches.
- Geography: United States. Search type: Web Search. Category: All categories. Requested period: January 1–December 31, 2025.
- Extraction: visible accessible chart table in the Google Trends browser interface, transcribed to `data/trends_weekly.csv`. This is a table transcription, not a native downloaded Google CSV. There are 53 displayed weekly bins, labeled December 29, 2024 through December 28, 2025. Boundary bins intersect the requested period. Do not relabel them as 53 complete calendar-2025 weeks.
- Both series share the request's normalized scale. Index 100 marks the highest relative search-interest point in this comparison, not 100 searches. A 0 may reflect insufficient data or rounding. Trends samples searches, so future pulls may differ.
- Result: The Masked Singer peaks at 100 in the bin starting May 4, 2025. The Floor FOX peaks at 4 in the bin starting February 9, 2025. No causal event attribution is established.
- Critical validity issue: the visible rising queries for The Floor FOX included `fox news live`, `99 to beat` and `fox news`. This is evidence of query ambiguity. Its low series must not be treated as a measure of the show's relative audience, share of voice, or market opportunity. The Masked Singer term can also include international franchise interest.
- Before budget allocation, validate the correct television-series Topic for each show where available, inspect related queries, and run a sensitivity analysis against disambiguated terms in the same request. No validated topic comparison is claimed in this version.
- The visible Trends average cards showed 31 and 1. We calculate means from the transcribed weekly values (30.642 and 1.509) separately and do not substitute either for Google’s displayed averages. Differences in UI aggregation/rounding are unresolved. The deck avoids an average comparison.

Official methodology: [Google Trends FAQ](https://support.google.com/trends/answer/4365533?hl=en), [export and citation guidance](https://support.google.com/trends/answer/4365538?hl=en). Data source: Google Trends (https://www.google.com/trends).

## YouTube: five public videos and one excluded record

The sample is a convenience audit of discoverable, accessible uploads from the official show channel and FOX-linked channel Reality Club (@RealityClubFox). It is not a random sample, a complete channel census, or a fixed-period sample. Discovery used web search and links in video recommendations. A third-party article supplied two embedded official links, which we then verified on YouTube itself.

For each URL we opened the watch page and expanded the description to read exact views and the publication date. We recorded displayed likes and precision. The Masked Singer reveal compilation displayed 2.1K likes, so 2,100 is an approximate translation, not an exact count. Counts can change after the observation. All video URLs, dates, channel names, status and values appear in `data/youtube_observations.csv`.

`NVCRybSLd9s` was labeled Unlisted. Its 1,254 views and 5 likes remain in the audit table but are excluded from the public-video chart and all public-sample summaries. Its restricted discoverability would distort a comparison.

We use the direct browser observations in preference to search-engine snapshots: for example, the reveal compilation's search result showed 159,504 views, while its expanded watch page showed 186,068. We retain the latter. We do not calculate growth from this difference because the search snapshot's measurement time is unknown.

Derived `like_per_1000_views = displayed_likes / views * 1000`. This is a descriptive like-to-view ratio, not an engagement rate based on unique users and not a conversion rate. It is approximate when likes are rounded. We do not use it to rank formats. Views count plays and are not unique people. Missing impressions, retention, paid distribution, country mix and comparable exposure periods prevent causal or demographic conclusions. No daily view velocity is inferred from lifetime views.

## Strategy logic and experiment

The public examples establish the existence of clue packages, reveals, trailers and trivia compilations. They do not prove that one format creates more growth. Proposed mechanisms:

1. The Masked Singer: an unresolved clue invites a prediction while preserving the reveal. Test clue-first against performance-first edits.
2. The Floor: a recognizable category lets people play immediately. Test challenge-first against host-introduction edits.

For each show separately, use a randomized platform experiment with equal allocation, the same episode source, audience, clip duration, CTA, budget and flight. Create matched variants from two episodes per show and block randomization by episode. If the platform cannot randomize, report matched-post comparisons as observational and make no causal lift claim. Do not infer audience overlap between the shows.

Primary measure: deduplicated qualified episode-page sessions (at least 10 seconds on an owned destination) per 1,000 served impressions. Use consented first-party tracking with stable campaign and variant IDs. Fix the attribution window to 24 hours after the tagged click. Attribute each session once. YouTube alone cannot provide the owned-destination qualification event. If permission or instrumentation is unavailable, fall back to platform-reported clicks as a clearly different diagnostic metric and report qualified visits as unavailable.

Diagnostics: click-through rate, clip completion and qualified visits per click. Guardrails: spoiler complaints per 1,000 comments, negative feedback per 1,000 impressions and cost per qualified visit. Human-review spoiler complaints using a fixed coding guide. Audience claims require separately consented platform analytics.

Pre-register the primary metric, sample size, duration and exclusions. Report a 97.5% confidence interval per show for the primary effect, applying Bonferroni adjustment to the two show tests. An illustrative baseline of 1.0% and treatment rate of 1.2% imply about 52,000 independent impressions per arm per show (80% power, two-sided alpha 0.025). These are assumptions, not observed FOX rates or a forecast. The independent Bernoulli approximation ignores repeated exposure and clustering, which may increase the required sample. Recalculate before launch using real baselines and design effects.

Planning formula: n = [z(1-alpha/2) * sqrt(2*pbar*(1-pbar)) + z(power) * sqrt(p1*(1-p1)+p2*(1-p2))]^2 / (p2-p1)^2. See `analysis.py` for calculations from the delivered CSVs using Python's standard library.

Suggested decision rule (proposal): scale only if the adjusted confidence interval for qualified-visit lift excludes zero in the positive direction and guardrails meet prespecified tolerances. Set those tolerances with the team before launch. Otherwise report inconclusive or no improvement. At day 30, an underpowered result remains inconclusive. No invented lift, ROI, budget, or streaming conversion appears in this study.

## Evidence labels

- OBSERVED: values read from public interfaces, with the collection date.
- DERIVED: arithmetic based on observed values, with a formula.
- ASSUMPTION: a planning input without empirical validation here.
- PROPOSAL: a creative or operational recommendation, not a research finding.

## Rights and authorship

The site uses original typography and data charts, without downloaded FOX photos, video footage or logos. Program titles remain trademarks of their owners. Links point to original sources. Proposed video concepts require appropriate footage, music and image rights before actual production. Do not state that FOX commissioned this project or that its recommendations have delivered results. The applicant should describe their own contribution and AI assistance honestly.
