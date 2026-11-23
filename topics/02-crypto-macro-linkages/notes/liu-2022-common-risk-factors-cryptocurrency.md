---
title: "Common Risk Factors in Cryptocurrency"
authors: "Liu, Yukun; Tsyvinski, Aleh; Wu, Xi"
year: 2022
venue: "Journal of Finance 77(2), 1133-1177 (read here as NBER Working Paper 25882, May 2019)"
url: "https://www.nber.org/system/files/working_papers/w25882/w25882.pdf"
pdf: "sources/02-crypto-macro-linkages/liu-2022-common-risk-factors-cryptocurrency.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "02-crypto-macro-linkages"
asset_class: "crypto"
horizon: "multi-day"
tags: "factor-model, market-factor, size, momentum, cross-section"
---

## Key insight
Three crypto-native factors, the coin market return (CMKT), size (CSMB) and momentum (CMOM), account for the cross-section of expected cryptocurrency returns. Equity factor models (Fama-French three- and five-factor, Carhart) do not. Cross-sectional momentum is concentrated in large coins.

## Method
The authors take 25 price- and volume-based characteristics from the equity anomaly literature and build crypto counterparts. Each week coins are sorted into quintiles on a characteristic; the long-short return is quintile five minus quintile one. Nine of the 25 produce significant long-short returns. Time-series spanning regressions then test whether a one-factor (CMKT) or three-factor (CMKT, CSMB, CMOM) model leaves significant alpha.

## Data and sample
All coins on Coinmarketcap.com with market capitalization above one million dollars, 2014 through 2018, weekly returns. 1,707 coins in total; the number passing filters grows from 109 in 2014 to 1,583 in 2018. Mean (median) market capitalization 356.71 (8.17) million dollars.

## Reported results
- Size strategies (long small, short large) earn more than 3 percent per week: 3.4 percent sorting on market capitalization, 3.9 percent on end-of-week price, 4.1 percent on maximum price.
- Momentum long-short returns: 2.7 percent per week for one-week formation, 3.3 percent for two-week, 4.1 percent for three-week, 2.5 percent for four-week.
- Low-volume minus high-volume coins earn about 3.2 percent per week.
- The one-factor crypto CAPM fails: R-squared of the long-short strategies ranges from about zero to 6.8 percent, and alphas stay significant.
- Under the three-factor model none of the nine strategies retains a significant alpha.
- Momentum by size: 0.6 percent per week (insignificant) among below-median coins; 4.2 percent per week (significant) among above-median coins.
- Results are "virtually" unchanged when the short leg is replaced by shorting Bitcoin.

## Signal construction
For a single-instrument directional bot this is mostly context, but two pieces are computable:
1. CMKT: value-weighted return of the investable coin universe, updated at whatever frequency prices are sampled. It is the dominant common driver of SOL.
2. Cross-sectional momentum rank: SOL's one- to four-week return ranked against other large-cap coins. A high rank tilts long relative to the market; the paper's formation and holding periods are weekly.
A market-neutral version (long SOL, short BTC perpetual) isolates the momentum component; the paper finds shorting Bitcoin works about as well as shorting the low quintile.

## Relevance to SOL perpetuals at minutes to hours
SOL is a large coin, which is where the paper finds momentum to be strong. The factor structure says most of SOL's variance is the market factor, so BTC and ETH moves on the large venues are the first-order input for a SOL directional model, and SOL-specific signals should be built on residual returns. The horizon mismatch is large: factors are weekly, the bot trades minutes to hours. The weekly momentum state can serve as a slow bias or position-size modifier, not as an entry trigger. SOL did not exist in the sample.

## Caveats
Sample 2014 to 2018 only, dominated by the 2017 boom and bust. No transaction costs, and the small-coin legs are illiquid and often not shortable. Reported weekly returns of 3 to 4 percent are far above anything that would survive at scale. The Borri et al. (2026) review in this folder reports that size and momentum remain robust in later data and cites a specification-search study finding other factors are not.
