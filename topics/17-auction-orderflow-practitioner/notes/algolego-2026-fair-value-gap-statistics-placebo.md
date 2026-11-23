---
title: "Fair Value Gap (FVG) Statistics with Placebo Control"
authors: "algolego (TradingView account, Algolego Studio)"
year: 2026
venue: "TradingView open-source script description (posted 12 August; year inferred from the data window)"
url: "https://www.tradingview.com/script/Kbq3WncE-Fair-Value-Gap-FVG-Statistics-with-Placebo-Control/"
pdf: "none"
access: "full-text"
source_type: "practitioner"
evidence_grade: "C"
topic: "17-auction-orderflow-practitioner"
asset_class: "multi"
horizon: "minutes"
tags: "fair-value-gap, ict, placebo-control, triple-barrier, hit-rate-baseline, negative-result"
---

## Key insight
When returns to a fair value gap are scored against size-matched placebo zones placed where no gap formed, the gap shows no measurable edge: the pooled difference in hit rate is about zero, with a confidence interval of roughly plus or minus one percentage point. The script's wider lesson is that a raw hit rate measured against 50% can look significant in either direction purely because the baseline for "price returns to a zone, then hits a symmetric target before a stop" is not 50%.

## Method
As described on the page (read through a summarizing tool; wording is paraphrased). A gap becomes active on the bar after its three-bar pattern closes, and every confirmed zone is kept in the sample. Entry is recorded at the close of the bar that touches the zone, not at the zone edge. Take-profit and stop are symmetric, sized in ATR or zone-height units, with a time limit; bars that touch both barriers count as losses; unresolved zones are excluded. For each real zone, one or more placebo zones with the same height, direction and distance from price are anchored at bars with no gap and scored by the same rules. Headline statistic: real hit rate minus placebo hit rate, with a z-score. The author cites Aronson's evidence-based technical analysis and the triple-barrier method of López de Prado as the origin of the design.

## Data and sample
Crypto, currencies and equity index futures; 5-minute, 30-minute and 1-hour charts; two non-overlapping periods, with published settings ending 1 August 2026 and a 30-minute table covering 1 January 2025 to 1 August 2026; three barrier sizes and two time limits. Fourteen measurements in all. The number of gap events and the exact symbols were not visible in the text retrieved (result tables did not render).

## Reported results
- Raw hit rates of 49.5% (crypto) and 51.4% (currencies), a 1.9 point spread; the spread between their placebo baselines is 2.7 points, so the apparent market difference comes from the baseline.
- Illustration: a 54% raw hit rate is significant against 50% (p about 0.003) but not against its placebo; a 48.4% rate (z = -2.25 against 50%) is likewise a baseline artifact.
- Largest of the fourteen real-minus-placebo estimates: 1.49 standard errors from zero.
- Pooled estimate: -0.04 percentage points, 95% interval about -1.2 to +1.1.
- None of the fourteen reaches conventional significance.

## Signal construction
Not a signal; a test harness worth copying. For any zone or level family: (1) define the event causally; (2) score with a triple barrier entered at the close of the touching bar; (3) draw K placebo zones per event matched on size, side and distance; (4) report real minus placebo with a pooled confidence interval; (5) repeat across instruments and periods. As a model input, the gap flag can still be supplied to a learner, but the result implies it should carry no weight once recent return and volatility are present.

## Relevance to SOL perpetuals at minutes to hours
Directly relevant: crypto at 5 to 60 minute bars is in the sample, and the finding is that the best-known ICT construct adds nothing over a matched random zone. The placebo design is the right guard for any reinforcement-learning or evolutionary search over level definitions, where the risk of fitting baseline artifacts is high. It should be the default evaluation for every level-based feature tested on SOL.

## Caveats
A TradingView script description by a pseudonymous author; not peer-reviewed, and the author says so. Event counts and tables were not visible to me. Placebos cannot match the fact that real gaps form after strong moves, so directional splits are unreliable in trends (the author notes this). Costs are excluded. One gap definition and one entry rule; conditional variants (gap plus sweep plus session) are untested. Year not shown on the page.
