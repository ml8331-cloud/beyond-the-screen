# Beyond the Screen

An independent Audience Growth & Content Strategy portfolio case for a FOX Entertainment Summer 2027 internship application. Not an official FOX project.

## What is inside

- `index.html`, `styles.css`, `app.js`: complete buildless, responsive portfolio website. Works offline, including its data explorer. No accounts, analytics, external libraries or API keys.
- `downloads/Beyond-the-Screen.pdf`: eight-page English executive strategy deck.
- `downloads/Beyond-the-Screen.pptx`: editable eight-slide presentation, including native charts and speaker notes with sources.
- `data/`: observed YouTube records, 53 weekly Google Trends rows, source register, derived metrics and experiment planning table.
- `METHODOLOGY.md`: extraction method, limitations, formulas and proposed experiment.
- `analysis.py`: reproducible standard-library analysis of the supplied CSVs.
- `PUBLISHING.md`: GitHub Pages deployment and application-use guidance.

## Project brief

Question: how can The Masked Singer and The Floor invite casual clip viewers to take a qualified next step toward an episode?

Evidence: five public YouTube examples plus one excluded unlisted example, and a jointly normalized US Google Trends search-term comparison for 2025. Direct YouTube watch-page metrics supersede older web-search snapshots. This is a small exploratory study. The Floor query has a material ambiguity problem, disclosed throughout. No internal audience, retention, revenue or conversion metrics were available.

Recommendation: test clue-first creative for The Masked Singer and category-first play for The Floor. The case includes a measurement plan and 30-day pilot. Campaign lift remains unmeasured.

Prepared with AI assistance for research, analysis and artifact production. Review source links and the methodology before presenting this as part of an application. Never claim to have run the proposed tests.

## Reproduce

Run `python3 analysis.py` from this folder. It reads the included CSVs and prints descriptive statistics and the assumed experiment sample size. The website uses the same observed values embedded in `app.js` so opening `index.html` directly works without a server. The two CSVs remain the canonical delivered observations. Update both before refreshing the website.

No publication or GitHub repository creation has been performed.
