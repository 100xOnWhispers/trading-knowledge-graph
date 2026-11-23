---
title: "The impact of macroeconomic news on Bitcoin returns"
authors: "Corbet, Shaen; Larkin, Charles; Lucey, Brian M.; Meegan, Andrew; Yarovaya, Larisa"
year: 2020
venue: "European Journal of Finance 26(14), 1396-1416 (read here as the accepted preprint dated 4 August 2020)"
url: "https://doras.dcu.ie/25037/1/B27___SC_CL_BL_AM_LY__SUBMITTED_The_impact_of_macroeconomic_news_on_Bitcoin_returns%5B1%5D.pdf"
pdf: "sources/02-crypto-macro-linkages/corbet-2020-macroeconomic-news-bitcoin-returns.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "02-crypto-macro-linkages"
asset_class: "crypto"
horizon: "daily"
tags: "macro-news, news-sentiment, unemployment, durable-goods, cpi, gdp, daily-event-study"
---

## Key insight
Over 2010 to 2019, the tone of newspaper coverage following US unemployment and durable goods releases is related to same-day Bitcoin returns with the opposite sign to equities: more positive coverage goes with lower Bitcoin returns. Coverage of GDP and CPI releases shows no significant relation. The paper reads this as early evidence that Bitcoin was beginning to interact with macro news, but as a contrarian or safe-haven-like asset rather than a risk asset.

## Method
For each release, headlines from the day of and the day after the announcement are collected from LexisNexis and classified as positive or negative. A News Index is built as the percentage of positive stories minus the percentage of negative stories, plus 100. Bitcoin's close-to-close return on the announcement day is regressed on the News Index (or the positive and negative percentages separately), a standardized surprise S = (actual minus consensus) / standard deviation, and day-of-week dummies. A second specification interacts the surprise with low, medium and high business-cycle states defined from industrial production growth. The authors deliberately use daily rather than intraday returns.

## Data and sample
CoinDesk Bitcoin Price Index, daily closes, 19 July 2010 to 30 September 2019. 3,831 headlines on four releases: GDP, unemployment, CPI and durable goods.

## Reported results
- Surprise-only regression: of the four releases only GDP surprises are significant.
- With business-cycle interactions: GDP has a significant positive coefficient and unemployment a significant negative one; durable goods and CPI are insignificant.
- News Index: the unemployment coefficient is -0.048 and significant. Splitting by tone, the positive-percentage coefficient is -0.091 and the negative-percentage coefficient is 0.070.
- The durable goods News Index coefficient is -0.018 and significant, with the same sign pattern.
- GDP and CPI News Index coefficients are not significant at 5 percent.
- Results are almost unchanged when the surprise is added as a control.
- Daily return standard deviation of Bitcoin in the sample is 4.9 percent; daily moves above 50 percent occur.

## Signal construction
As specified this is a same-day relation, not a forecast: the news tone and the return are measured over overlapping periods. A live analogue would score headlines in the minutes after a release (positive or negative tone about the labor market or orders) and use the net tone as a contextual feature alongside the numeric surprise. The paper gives no evidence on whether tone leads price within the day.

## Relevance to SOL perpetuals at minutes to hours
Limited direct use. Its value for this repository is historical and cautionary: in the pre-2020 sample the sign of Bitcoin's response to good real-economy news was negative or absent, the reverse of the risk-asset behavior documented after 2021 (see the Copestake and Kroner notes). Any rule that hard-codes "good data is bullish for crypto" or the reverse is regime-dependent. The payrolls sign flip around 2020 reported second-hand in the Kroner note is consistent with this. Nothing here is tested on SOL or intraday.

## Caveats
Daily close-to-close returns cannot isolate the announcement from other news in a 24-hour market. Headline sentiment is measured on the day of and the day after the release, so reverse causality (price moves shaping coverage) is possible; the authors discuss it but cannot rule it out. The sample is dominated by Bitcoin's early, thinly traded years. No out-of-sample test, no trading costs. Coefficient units depend on the index scaling and were not converted to basis points.
