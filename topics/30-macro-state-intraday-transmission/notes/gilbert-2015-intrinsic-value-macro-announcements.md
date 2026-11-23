---
title: "Is the Intrinsic Value of Macroeconomic News Announcements Related to their Asset Price Impact?"
authors: "Gilbert, Thomas; Scotti, Chiara; Strasser, Georg; Vega, Clara"
year: 2015
venue: "Finance and Economics Discussion Series 2015-046, Federal Reserve Board (the version read; the published version is usually cited as Journal of Monetary Economics, 2017)"
url: "https://www.federalreserve.gov/econresdata/feds/2015/files/2015046pap.pdf"
pdf: "sources/30-macro-state-intraday-transmission/gilbert-2015-intrinsic-value-macro-announcements.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "30-macro-state-intraday-transmission"
asset_class: "futures"
horizon: "daily"
tags: "announcement, event-ranking, timeliness, nowcasting, treasury-futures, revision-noise, pre-2020"
---

## Key insight
Why do some releases move markets and others not? The authors measure each release's intrinsic value as its weight in a nowcast of GDP growth, inflation and the federal funds target at the moment it comes out, and find that differences in this value explain a meaningful share of the cross-section of price impact. Of the three ingredients (relation to fundamentals, timing, revision noise), timing matters most: a release that arrives early in the data cycle moves prices more than a later, more accurate one.

## Method
A nowcasting framework assigns each of 36 US announcements a weight for predicting three primitives. Tardiness is the percent loss in a release's nowcasting weight caused by its delay relative to the most timely announcement, which accounts for what earlier releases already revealed; revision noise is the percent loss in weight caused by its future revisions; relation to fundamentals is its nowcasting importance independent of revisions and release time. Price impact is the slope from regressing the daily Treasury futures log price change on the standardised surprise (actual minus Bloomberg median forecast, divided by its sample standard deviation). Daily returns are used on purpose, to capture the pre-release drift documented by Kurov et al.; the authors report similar conclusions with five-minute impacts. Cross-sectional regressions relate impact to intrinsic value and its components.

## Data and sample
36 US macroeconomic announcements; Table 2 of the paper reports responses for four assets, with the analysis focused on US Treasury bond futures; 1998 to 2013. Pre-2020; bonds only; no crypto.

## Reported results
- Intrinsic value explains between 8 and 22 percent of the variation in price impact across announcements, consistently across the three primitives.
- Tardiness is the most important single characteristic; relation to fundamentals is less important; revision noise is insignificant.
- The tardiness measure explains impact better than the simple reporting lag used in earlier work.
- The link is imperfect: nonfarm payrolls have the largest impact on Treasury prices without being the announcement with the highest intrinsic value. The authors suggest a coordination role for payrolls.
- Final GDP is closely related to fundamentals but has little impact because it arrives late.

## Signal construction
Not a signal. It is a principled way to weight an event calendar: rank releases by (a) how early they report on a given month or quarter and (b) their historical price-impact coefficient, and concentrate attention on the first release in each information category (payrolls for labour, ISM for activity, CPI before PCE for prices, advance before final GDP). Releases that restate known information can be dropped from the gate.

## Relevance to SOL perpetuals at minutes to hours
A crypto bot cannot estimate reliable betas for 36 releases on a few years of data. This paper justifies a short list on structural grounds and explains why late releases can be ignored even when they are economically important. Combined with the attention result in the Kroner note, the practical gate is: early releases in the category the market currently cares about. The specific ranking must still be checked against crypto responses post-2021.

## Caveats
Impact is measured on Treasury futures, and the ranking for risk assets may differ. The 8 to 22 percent explained share leaves most cross-sectional variation unexplained. Sample ends in 2013, before the 2021 to 2023 shift in which CPI became the dominant release.
