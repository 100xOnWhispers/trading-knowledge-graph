---
title: "Trading volume and liquidity provision in cryptocurrency markets"
authors: "Bianchi, Daniele; Babiak, Mykola; Dickerson, Alexander"
year: 2022
venue: "Sveriges Riksbank Working Paper Series No. 413"
url: "https://www.riksbank.se/globalassets/media/rapporter/working-papers/2022/no.-413-trading-volume-and-liquidity-provision-in-cryptocurreny-markets.pdf"
pdf: "sources/13-momentum-reversal/bianchi-2022-trading-volume-liquidity-provision-crypto.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "13-momentum-reversal"
asset_class: "crypto"
horizon: "daily"
tags: "short-term-reversal, volume, liquidity-provision, adverse-selection, crypto"
---

## Key insight
Short-term reversal in crypto is the return to providing liquidity, and it is concentrated in pairs with abnormally low trading volume and in small, volatile, illiquid coins. After high-volume moves, and in large liquid coins, reversal profits are close to zero or negative. The interaction of lagged return and volume, not lagged return alone, carries the predictive information, consistent with models where high volume signals informed trading that continues and low volume signals liquidity trading that reverts.

## Method
Daily cross-sectional reversal strategies (buy recent losers, sell recent winners) double-sorted on de-trended trading volume, with equal and value weighting. Risk adjustment against a crypto market factor and long-short liquidity, volatility, momentum and size portfolios. Predictive regressions of conditional reversal returns on liquidity-supply proxies (idiosyncratic volatility, aggregate bid-ask spread, the Treasury-Eurodollar spread). Panel and Fama-MacBeth regressions with a lagged-return times volume interaction. The introduction and summary of findings were read closely; later tables were not read line by line.

## Data and sample
A moderately large cross-section of cryptocurrency pairs against the US dollar, 1 March 2017 to 1 March 2022, daily, with prices and volume aggregated across multiple centralised exchanges.

## Reported results
- Equal-weighted reversal conditional on low volume: 1.26% average daily return (p = 0.001), against 0.54% (p = 0.002) conditional on high volume.
- Value-weighted reversal: 0.65% a day (p = 0.002) in low-volume pairs against -0.19% (p = 0.251) in high-volume pairs.
- Results are reported as robust to the de-trending window and to linear transaction costs, and not explained by market, liquidity, volatility, momentum or size factors.
- For larger, more liquid, less volatile assets, reversal returns are close to zero and not statistically significant.
- Reversal returns are predictable by liquidity-supply proxies, more so when volume is below trend.

## Signal construction
Inputs: return over the last bar and volume relative to its own trend (for example log volume minus a rolling mean). Signal = -(lagged return) * indicator(volume below trend); optionally +(lagged return) when volume is far above trend. Parameters: bar size, volume de-trending window, thresholds. The paper uses daily bars across many coins; a single-asset intraday version is an adaptation.

## Relevance to SOL perpetuals at minutes to hours
Gives the conditioning variable that decides between fading and following a move: a SOL move on low relative volume is more likely to revert, a move on high volume is more likely to persist. This agrees with the volume-time adjustment in Avellaneda and Lee (2010) and with the high-volume intraday momentum in Shen et al. (2022). The value-weighted result is the sobering part: for large liquid coins, unconditional reversal earns nothing at daily frequency, so a SOL mean-reversion signal must be conditional. Volume should be measured on the large venues, not on Kalshi alone.

## Caveats
Working paper. Daily equal-weighted reversal returns above 1% a day are dominated by small illiquid pairs where bid-ask bounce and untradeable prices inflate paper profits. Evidence is cross-sectional; time-series transfer to one asset at intraday frequency is untested here. Sample ends March 2022.
