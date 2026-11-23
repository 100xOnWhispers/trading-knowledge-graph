---
title: "Pinning in the S&P 500 futures"
authors: "Golez, Benjamin; Jackwerth, Jens Carsten"
year: 2012
venue: "Journal of Financial Economics 106(3), 566-585"
url: "https://kops.uni-konstanz.de/server/api/core/bitstreams/b9492112-cab3-4217-a7d0-d2c4f5ba7825/content"
pdf: "sources/20-options-derived-signals/golez-2012-pinning-sp500-futures.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "20-options-derived-signals"
asset_class: "futures"
horizon: "daily"
tags: "pinning, option-expiration, delta-hedging, sp500-futures, strike-clustering, market-makers, anti-pinning"
---

## Key insight
Option expiry can pull a large, liquid futures contract toward a strike, but the direction of the effect depends on who holds the options. S&P 500 futures finish near the at-the-money strike more often on days when options on those futures expire (pinning), and less often near the relevant strike when cash-settled European index options expire (anti-pinning). Both follow from delta-hedging trades, so the sign is set by dealer positioning and contract design, not by a universal "price goes to the strike" rule.

## Method
Logistic regressions with fixed effects in the style of Ni, Pearson and Poteshman (2005), over a window of ten days either side of each expiry. The dependent variable equals one if the futures settlement price is within $0.375 of the nearest strike (strikes are $5 apart, so 15% is expected by chance); $0.25 and $0.50 bands are robustness checks. Separate variables for pinning from above and from below. Mechanisms tested with option volume, open interest, early exercise and futures volume: (a) time decay of dealers' delta hedges (Avellaneda and Lipkin, 2003), which predicts anti-pinning when dealers are short options; (b) customers reselling in-the-money options before expiry; (c) early exercise of American futures options; (d) manipulation. Economic size is bounded with the Ni et al. method.

## Data and sample
First-to-maturity S&P 500 futures and options on them, serial (non-quarterly) expirations, November 1992 to November 2009 (136 expirations); a shorter sample from October 1998 (89 expirations). SPX index options for the cross-market tests.

## Reported results
- Futures finish within the band on 22.47% of expirations in the 1998 to 2009 sample against 15% expected. In the full sample, 14.71% of expirations pin from below the strike and 6.62% from above.
- Symmetric pinning is significant against surrounding days (p = 0.01 full sample, p = 0.03 short sample). Pinning from below is strong; pinning from above is absent (p = 0.99). The authors attribute the asymmetry to dealers holding larger short put than short call positions.
- The price shift is at least 11.00 basis points from Thursday to expiration Friday, at least $115 million of notional per expiration; about $59 million of it occurs in the last 30 minutes of trading. In the later sample the figures are $240 million and $105 million.
- Hedge time decay alone produces anti-pinning; customer reselling and early exercise outweigh it. Futures volume adds nothing once hedging variables are included, which argues against manipulation.
- On SPX option expirations the futures are pushed away from the cost-of-carry-adjusted strike.

## Signal construction
For an expiry at time T with strikes K_i: compute distance of the underlying from the nearest high-open-interest strike in units of expected remaining volatility, `d = (S - K) / (S * sigma * sqrt(T - t))`, for the last hours before expiry. A pinning hypothesis predicts mean reversion of `d` toward zero when dealers are net long gamma at K; an anti-pinning hypothesis predicts repulsion when they are net short. The sign must come from a position estimate ([amberdata-2026-gamma-exposure-gex-documentation](amberdata-2026-gamma-exposure-gex-documentation.md)).

## Relevance to SOL perpetuals at minutes to hours
Deribit options are European and cash-settled against a 30-minute average of the index before 08:00 UTC ([almeida-2024-risk-premia-bitcoin-market](almeida-2024-risk-premia-bitcoin-market.md) describes the settlement). On this paper's evidence that design removes the reselling and early-exercise channels that created pinning, leaving only the hedge-decay channel, whose sign depends on dealer gamma. "Max pain" claims for crypto expiries therefore have no direct support here. The effect size, 11 basis points in the most liquid equity future, sets a realistic upper bound on what to expect for BTC, and SOL option open interest is far too small for any such effect.

## Caveats
Equity index futures with American physically delivered options; one expiry a month, so 136 events. The effect is a shift in the distribution of the settlement price, not a tradable return net of costs. Sample ends in 2009, before weekly and daily expiries. The transfer to crypto is this note's reasoning, not a tested result.
