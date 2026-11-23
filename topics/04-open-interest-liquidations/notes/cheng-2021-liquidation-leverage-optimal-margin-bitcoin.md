---
title: "Liquidation, Leverage and Optimal Margin in Bitcoin Futures Markets"
authors: "Cheng, Zhiyong; Deng, Jun; Wang, Tianyi; Yu, Mei"
year: 2021
venue: "arXiv preprint 2102.04591"
url: "https://arxiv.org/pdf/2102.04591"
pdf: "sources/04-open-interest-liquidations/cheng-2021-liquidation-leverage-optimal-margin-bitcoin.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "04-open-interest-liquidations"
asset_class: "crypto"
horizon: "hours"
tags: "liquidations, leverage, open-interest, bitmex, extreme-value-theory, margin"
---

## Key insight
On BitMEX in 2020, forced liquidations were a large and routine share of open interest: on an average day 3.51% of open interest was liquidated on the long side and 1.89% on the short side. Traders who were liquidated used roughly 60x leverage on both sides. Extreme value theory implies that a 1% maintenance margin is far too thin for bitcoin's tails and that long positions in inverse contracts need more margin than shorts.

## Method
Two parts. First, generalized extreme value (GEV) distributions are fitted to block maxima and minima of perpetual price changes at 5-minute to daily sampling, and the margin that keeps the margin-call probability at a target level is solved in closed form. Second, daily liquidation, volume and open interest data are combined into three descriptive measures:

- Speculation index: `SI = trading volume / open interest`.
- Liquidation percentage: daily long (short) liquidation divided by open interest.
- Implied minimum leverage of liquidated traders, assuming entry at the daily open and liquidation at the daily low (high): `L_long = -(1 + r_min) / r_min`, `L_short = (1 + r_max) / r_max`.

## Data and sample
BitMEX XBTUSD inverse perpetual. Daily volume, liquidations, open interest and OHLC collected manually from Coinalyze, 29 January 2020 to 3 February 2021 (372 days). Five-minute perpetual prices from the BitMEX API, 1 January 2017 to 6 February 2021 (431,346 observations).

## Reported results
- Average speculation index 3.75, against 0.15 for the S&P 500, 0.21 for the Nikkei and 0.45 for the DAX as cited from earlier work.
- Daily liquidations averaged about USD 20 million long and USD 10 million short; the largest long liquidation day was 12 March 2020 at USD 843 million, the largest short day 1 June 2020 at USD 132 million.
- Implied leverage of liquidated traders at least 58.13x long and 59.94x short.
- For a 1% daily margin-call probability the suggested margin is about 33% for longs (3x) and 20% for shorts (5x). At an 8-hour horizon and 0.1% probability, 46.98% for longs and 26.34% for shorts.
- The GEV tail parameter is positive at all frequencies (Frechet type) and larger at higher frequencies. A normal assumption understates required margin by at least half.

## Signal construction
Three inputs a bot can compute from public data: (1) `liq_long_usd / OI_usd` and `liq_short_usd / OI_usd` over a rolling window as a measure of how much leverage has just been cleared; (2) `volume / OI` as a turnover or speculation gauge; (3) the GEV margin formula as a sizing rule, giving the leverage at which the chance of liquidation over a holding period stays below a chosen tolerance. The paper does not test any of these as return predictors.

## Relevance to SOL perpetuals at minutes to hours
The liquidation-to-open-interest ratio is a natural normalization for cross-asset and cross-time comparison and should be recomputed for SOL on current venues. The margin analysis supports low leverage for a bot holding for hours: SOL is more volatile than BTC, so the BTC figures are a lower bound on required margin. Kalshi's low maximum leverage is closer to the paper's recommended levels than offshore venues are. The long-short asymmetry is specific to inverse (coin-margined) contracts and does not carry over to linear, dollar-margined perps.

## Caveats
One venue, one year that includes March 2020, and manually collected third-party data. The leverage estimate rests on a strong assumption about entry and liquidation timing. Exchange-reported liquidation data can be incomplete. No predictive test, and BitMEX's share of the market has fallen sharply since the sample.
