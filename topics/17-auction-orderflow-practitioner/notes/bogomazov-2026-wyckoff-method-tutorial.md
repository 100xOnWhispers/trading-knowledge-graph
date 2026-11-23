---
title: "The Wyckoff Method: A Tutorial"
authors: "Bogomazov, Roman; Lipsett, Michael"
year: 2026
venue: "StockCharts ChartSchool (undated page, read November 2026)"
url: "https://chartschool.stockcharts.com/table-of-contents/market-analysis/wyckoff-analysis-articles/the-wyckoff-method-a-tutorial"
pdf: "none"
access: "full-text"
source_type: "practitioner"
evidence_grade: "D"
topic: "17-auction-orderflow-practitioner"
asset_class: "equities"
horizon: "multi-day"
tags: "wyckoff, accumulation, distribution, spring, upthrust, composite-man, effort-versus-result"
---

## Key insight
The Wyckoff method reads a trading range as a campaign by large operators: accumulation before a markup, distribution before a markdown. Its most testable element is the spring (a break below range support that quickly reverses) and its mirror, the upthrust, which are the original form of what is now sold as a "liquidity sweep". The tutorial is a clear statement of the framework and offers no statistical evidence for any part of it.

## Method
Qualitative chart reading, as described on the page (read through a summarizing tool; wording is paraphrased). The article credits the schematics to Bogomazov, edited by the late Hank Pruden, and traces the method to Richard D. Wyckoff (1873-1934).
- Three laws: supply and demand sets direction; cause and effect links the horizontal point-and-figure count in a range to the size of the following move; effort versus result flags a possible turn when volume and price progress diverge.
- Composite man: a heuristic single operator whose intentions the chart is said to reveal.
- Accumulation schematic. Phase A stops the downtrend: preliminary support, selling climax, automatic rally, secondary test. Phase B builds the cause. Phase C tests remaining supply with a spring or shakeout. Phase D shows signs of strength on wider spread and higher volume, with last points of support on lower volume as entries. Phase E is markup.
- Distribution schematic mirrors it: preliminary supply, buying climax, automatic reaction, secondary test; upthrust and upthrust after distribution in Phase C; last point of supply as the short entry; markdown.
- Nine buying and nine selling tests, including a requirement that the projected move be at least three times the stop risk.
- Point-and-figure count: number of columns across the range times box size times reversal gives a price objective zone.

## Data and sample
None. Illustrative charts of individual stocks.

## Reported results
None. The page presents no hit rates, backtests or references to tests. A statement that three-quarters or more of stocks move with the market is uncited.

## Signal construction
The framework as a whole depends on judgment and is not directly computable. Three parts can be made mechanical and tested.
1. Spring and upthrust: define a range (for example, the high and low of the last N bars with range width below a volatility multiple); event = price trades beyond the boundary by at least a small offset and closes back inside within k bars. Label = forward return over M bars. Control = matched boundary touches without the reclaim, and matched random levels.
2. Effort versus result: per bar, volume z-score minus absolute-return z-score; high values (much volume, little progress) near a range boundary.
3. Climax: bar range and volume both in the top percentile after an extended move, followed by an opposite close.
Phase labels (A to E) could be learned as latent states by a hidden Markov or change-point model on range, volume and delta, which connects to topic 01; nothing read here attempts that.

## Relevance to SOL perpetuals at minutes to hours
The spring definition maps directly onto failed breakouts of intraday ranges and onto liquidation flushes that reverse. Osler's evidence points the other way on average: after a crowded level is crossed, continuation dominates for hours. The spring is therefore a conditional claim (break plus fast reclaim) that needs its own event study on SOL, with the reclaim window fixed in advance. The longer-horizon accumulation and distribution schematics were designed for daily stock charts and are a poor fit for a minutes-to-hours bot.

## Caveats
No evidence. Pattern labels are assigned with hindsight, and the schematics admit many variants, which makes the method hard to falsify. The source is an educational page on a charting vendor's site, written by teachers of the method. The page contained embedded instructions addressed to automated readers, which were ignored. Year in the front matter is the access year; the page is undated.
