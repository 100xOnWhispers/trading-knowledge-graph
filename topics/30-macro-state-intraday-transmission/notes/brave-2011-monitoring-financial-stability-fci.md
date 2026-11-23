---
title: "Monitoring financial stability: A financial conditions index approach"
authors: "Brave, Scott; Butters, R. Andrew"
year: 2011
venue: "Economic Perspectives, Federal Reserve Bank of Chicago, 1Q/2011"
url: "https://www.chicagofed.org/-/media/publications/economic-perspectives/2011/1qtr2011-part2-brave-butters-pdf.pdf"
pdf: "sources/30-macro-state-intraday-transmission/brave-2011-monitoring-financial-stability-fci.pdf"
access: "full-text"
source_type: "documentation"
evidence_grade: "B"
topic: "30-macro-state-intraday-transmission"
asset_class: "multi"
horizon: "multi-day"
tags: "financial-conditions-index, nfci, dynamic-factor-model, mixed-frequency, state-variable, risk-liquidity-leverage, pre-2020"
---

## Key insight
This is the methodology article behind the Chicago Fed's financial conditions index. A single weekly index summarises 100 indicators of risk, liquidity and leverage drawn from money markets, debt and equity markets and the banking system, using a dynamic factor model that handles mixed frequencies and missing data. Positive values mean tighter-than-average conditions, measured in standard deviations. An adjusted version removes the part explained by current economic activity and inflation, isolating shocks that originate in finance.

## Method
Principal component analysis is the starting point; the index is then estimated as a large approximate dynamic factor model (Doz, Giannone and Reichlin) with the EM algorithm and the Kalman filter, which fills in unreleased or unavailable series and adds a time-series dimension to the averaging. Risk measures receive generally positive weights; liquidity and leverage measures generally negative weights. For the adjusted index, each indicator is first regressed on current and lagged measures of growth and inflation and the residuals are used. Evaluation: correspondence with known crises, and pseudo out-of-sample forecasts of nine real national-accounts variables at one, two, four and six quarters against an autoregressive baseline.

## Data and sample
100 financial indicators: 47 weekly, 29 monthly, 24 quarterly. Estimated on an unbalanced panel from the first week of 1971 through 2010; index reported from 1973. Forecast evaluation 1985:Q1 to 2010:Q2. No crypto.

## Reported results
- An index value of 1.0 means conditions tighter than average by one standard deviation.
- Peaks of the index line up with known crisis periods and turning points with well-known financial events.
- The adjusted index is much less persistent than the headline index.
- Adding the index residual to forecasting regressions that already include the Chicago Fed National Activity Index improves forecasts at every horizon and for every variable, by just under 1 percent to 22 percent in mean squared error; adding the adjusted index rarely helps unless its own dynamics are accounted for.

## Signal construction
Weekly state variable, published by the Chicago Fed (the publication schedule and current indicator list were not read in this session). Use: level above or below zero as a tight or loose flag, and the change over several weeks as the direction of conditions. Because it is weekly and model-smoothed, it suits a slow gate on leverage and holding period, not an intraday trigger. A bot wanting a daily counterpart should use a market-based risk index such as the one in the Chari et al. note.

## Relevance to SOL perpetuals at minutes to hours
Financial conditions indices are the most common regime labels in macro commentary on crypto, so the construction is worth knowing: the index is a broad, slow average dominated by credit and funding measures, it is revised as data arrive, and its headline value moves little from week to week. That makes it unlikely to add information at minutes to hours beyond what equity futures, credit and the dollar already show in real time. Its relation to crypto returns is not tested in any source read for this topic.

## Caveats
A 2011 methodology article; the index has been modified since and the details were not checked. The Kalman smoother revises history, so backtests using the latest vintage have look-ahead bias. Forecast evidence is for US real activity, not asset returns. Evidence grade reflects a central bank methodology paper without independent replication read here.
