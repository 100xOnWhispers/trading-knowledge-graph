---
title: "Cryptocurrency as an Investable Asset Class: Coming of Age"
authors: "Borri, Nicola; Liu, Yukun; Tsyvinski, Aleh; Wu, Xi"
year: 2026
venue: "arXiv 2510.14435 (v4, March 2026); prepared for Annual Review of Financial Economics, Vol. 18"
url: "https://arxiv.org/pdf/2510.14435"
pdf: "sources/02-crypto-macro-linkages/borri-2026-cryptocurrency-investable-asset-class.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "02-crypto-macro-linkages"
asset_class: "crypto"
horizon: "multi-day"
tags: "review, equity-correlation, regime-shift-2020, factor-model, inflation-expectations"
---

## Key insight
A review by the authors of the foundational crypto asset-pricing papers that re-estimates their results on data through September 2025. The headline for this topic: the pre-2020 finding that crypto is uncorrelated with traditional assets no longer holds. The correlation of the coin market with global equities rose from 1 percent before 2020 to 39 percent after. A small set of crypto factors (size, momentum, value) still spans the cross-section.

## Method
The paper organizes the literature into seven stylized facts and re-computes the main statistics on an updated dataset: summary statistics and cross-asset correlations by sub-period (pre- and post-2020), quintile sorts and factor spanning tests, jump statistics from tick data, carry and cross-exchange arbitrage returns.

## Data and sample
CoinGecko daily data aggregated to weekly returns, 2014 to September 2025. 18,622 listed coins plus 29,230 delisted coins to avoid survivorship bias; after filters, 16,468 coins and about 9.5 million records. Stablecoins and wrapped tokens excluded; coins under one million dollars of market capitalization excluded at formation. Bloomberg series for MSCI World, global high-yield and government bonds, commodities, gold, DXY, 10-year nominal and real yields. Binance Bitcoin perpetual prices and funding at 8-hour frequency, August 2020 to May 2025, for the carry strategy. Kraken tick data for jumps, 2015 to March 2025.

## Reported results
- Weekly crypto returns average above 1 percent with volatility about ten times that of global equities; weekly Sharpe ratios are similar to equities.
- Crypto drawdowns and volatility are smaller after 2020 than before; the reverse holds for equities.
- Coin-market correlation with global equities: 1 percent pre-2020, 39 percent post-2020. With the S&P 500: 2 percent pre-2020, 37 percent post-2020.
- Post-2020 the coin market is also significantly correlated with commodities (27 percent), high-yield bonds (24 percent), global government bonds (13 percent) and gold (18 percent), and with changes in 10-year breakeven inflation (31 percent). Correlation with US government bonds stays insignificant.
- The authors state that the literature "has yet to reach a consensus on the cause" of the shift, listing monetary policy, retail trading and financialization as candidates.
- Size (CSIZE) and two-week momentum (CMOM) remain significant; the paper cites a study of 20,736 research designs finding size and momentum robust and other factors not.
- A Black-Litterman illustration implies allocations of about 3.1 percent (retail) and 5.5 percent (institutional), which the authors call back-of-the-envelope.

## Signal construction
Not a signal. It is the up-to-date reference for the factor structure and for the size of the equity link. One derived quantity is useful as a regime feature: the rolling correlation between the crypto market return and an equity index (weekly returns in the paper), which tells the bot how much weight equity-index moves deserve as an input at a given time.

## Relevance to SOL perpetuals at minutes to hours
It justifies treating equity-index futures and breakeven-inflation or rates moves as inputs for a SOL directional model in the current regime, and it warns that this link is a post-2020 feature whose cause is not settled and which could weaken. All correlations are weekly; intraday co-movement, lead-lag and behavior outside US cash hours are not addressed (topic 21 covers lead-lag). SOL-specific betas are not reported in the parts read.

## Caveats
Review article by authors assessing their own earlier findings. The pre/post-2020 split is a single break chosen after the fact. CoinGecko prices are stamped at 00:00 UTC while traditional assets close at different times, which the authors flag; weekly aggregation mitigates but does not remove the mismatch. Correlations are unconditional averages over a period that includes both the 2022 tightening and the ETF era.
