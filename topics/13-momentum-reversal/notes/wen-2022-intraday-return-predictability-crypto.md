---
title: "Intraday return predictability in the cryptocurrency markets: Momentum, reversal, or both"
authors: "Wen, Zhuzhu; Bouri, Elie; Xu, Yahua; Zhao, Yang"
year: 2022
venue: "North American Journal of Economics and Finance 62, 101733"
url: "https://ideas.repec.org/a/eee/ecofin/v62y2022ics1062940822000833.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "13-momentum-reversal"
asset_class: "crypto"
horizon: "hours"
tags: "intraday-momentum, intraday-reversal, bitcoin, jumps, fomc, liquidity"
---

## Key insight
Per the abstract, Bitcoin and other major coins show both intraday momentum and intraday reversal, and which one dominates depends on conditions: large intraday jumps, FOMC announcement days, liquidity levels and the COVID-19 period all change the pattern. The authors present intraday reversal as a feature specific to crypto markets and attribute it to overreaction to non-fundamental information.

## Method
Only the abstract was read. It describes intraday return predictability tests on high-frequency data, conditioning on jumps, FOMC releases, liquidity and the COVID-19 outbreak, and a market-timing strategy built on the intraday predictors and compared with always-long and buy-and-hold benchmarks. The exact intervals used as predictors and targets were not confirmed.

## Data and sample
High-frequency Bitcoin prices from 3 March 2013 to 31 May 2020, with robustness on Ethereum, Litecoin and Ripple. Venue and bar size not confirmed.

## Reported results
From the abstract only:
- Both intraday momentum and reversal exist in Bitcoin.
- The predictive patterns change with large intraday price jumps, FOMC announcement releases, liquidity levels and the COVID-19 outbreak.
- The same predictability appears in Ethereum, Litecoin and Ripple.
- A timing strategy based on the intraday predictors has higher economic value than always-long and buy-and-hold benchmarks.
- Intraday momentum is linked to late-informed investors; intraday reversal is linked to overreaction to non-fundamental information and overconfidence.
No coefficients, R-squared values or cost assumptions were seen.

## Signal construction
Not confirmed in detail. The design implied by the abstract is the same family as Shen, Urquhart and Wang (2022): regress a late-session interval return on earlier-session interval returns, and let the coefficients differ by regime (jump day or not, FOMC day or not, high or low liquidity). A bot would implement this as an interaction model: forecast = b(regime) * earlier-interval return.

## Relevance to SOL perpetuals at minutes to hours
The value for the bot is the conditioning idea, not a specific number. It says the momentum-versus-reversal sign at intraday horizons is state-dependent, and it names the states to test on SOL: after a jump, on macro announcement days, and by liquidity. Together with Shen et al., it supports building the intraday trend signal as a regime-switched model instead of a fixed rule.

## Caveats
Abstract-only; magnitudes, costs and out-of-sample design are unknown. Sample ends May 2020, before the growth of perpetual volume on Binance, Bybit and Hyperliquid. The full text should be obtained before any parameter from this paper is used.
