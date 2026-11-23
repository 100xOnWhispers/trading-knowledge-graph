---
title: "KalshiEX LLC - Exchange Fee Schedule (Perpetual Futures Contracts) Update"
authors: "KalshiEX LLC (signed Ross, Rhianna)"
year: 2026
venue: "CFTC rule filing (Regulation 40.6(a) self-certification), dated October 19, 2026"
url: "https://www.cftc.gov/filings/orgrules/rules10182634487.pdf"
pdf: "sources/06-kalshi-venue/kalshiex-2026-perpetuals-fee-schedule-amendment.pdf"
access: "full-text"
source_type: "documentation"
evidence_grade: "B"
topic: "06-kalshi-venue"
asset_class: "crypto"
horizon: "n/a"
tags: "kalshi, fees, maker-taker, fcm, self-clearing-member, rebate-program, transaction-costs"
---

## Key insight
Kalshi runs two perps fee schedules. Self-clearing members pay 4 bp taker and 2 bp maker at the entry tier; customers who clear through a futures commission merchant, which is how most retail users trade, are charged 12 bp taker and 2 bp maker on crypto perps. A separate programme rebates almost all fees to self-clearing members through 2026, so the cost a retail bot faces is several times that of the professional firms it trades against.

## Method
Fee schedule in an 8-page rule filing, with redline and clean exhibits. Two companion filings were also opened: the Temporary Perpetual Fee Rebate Program update of the same date (`rules10182634493.pdf`) and the FCM Perpetuals Fee Rebate Program of October 15, 2026 (`rules10152634001.pdf`).

## Data and sample
Schedule effective on or after October 30, 2026. Tiers depend on trailing 30-day volume in perps plus prediction markets, counting maker and taker volume, updated daily.

## Reported results
Crypto perpetuals, taker / maker, as a percentage of notional:

| Tier | 30-day volume | Self-clearing member | FCM-cleared |
|---|---|---|---|
| 0 | $0 | 0.0400% / 0.0200% | 0.1200% / 0.0200% |
| 1 | >= $100K | 0.0300% / 0.0150% | 0.1000% / 0.0150% |
| 2 | >= $1M | 0.0250% / 0.0120% | 0.0600% / 0.0120% |
| 3 | >= $10M | 0.0200% / 0.0000% | 0.0200% / 0.0000% |
| 4 | >= $100M | 0.0150% / 0.0000% | 0.0150% / 0.0000% |
| 5 | >= $1,000M | 0.0100% / 0.0000% | 0.0100% / 0.0000% |

- Other asset classes use multipliers of the base rate: metals and indices 0.06x, energy 0.2x, foreign exchange 0.14x.
- Fees are charged on notional at the time of trade.
- The filing notes that each FCM "remains free to set the commissions and fees it charges its own customers".
- Temporary rebate programme (self-clearing members only): 98% of net taker fees and 100% of net maker fees are rebated monthly, until the earlier of December 31, 2026 or termination. Incentives are capped so that net fees per trade never become negative.
- FCM rebate programme: pays the FCM, not the customer, a monthly share of exchange fees, through December 31, 2027; the calculation is in a confidential appendix.

## Signal construction
Not a signal. This is the transaction-cost input. For an FCM-cleared account at tier 0, a taker round trip costs 24 bp plus the spread; a maker round trip costs 4 bp. Tier 2 ($1M of 30-day volume) halves the taker fee to 6 bp. A backtest or reinforcement-learning reward must apply the tier that the strategy's own turnover would earn, which makes cost path-dependent.

## Relevance to SOL perpetuals at minutes to hours
Decisive. Using the one-day statistics in the market-data note (one-minute volatility 8.3 bp, spread 4.5 bp), a tier-0 taker round trip of roughly 28 bp exceeds three minutes of typical movement and is close to half of a naive one-hour standard deviation of about 64 bp (my scaling, assuming independent minutes). Signals at the minutes horizon will not clear that hurdle with market orders; passive entry, longer holding periods, or reaching tier 2 or 3 are prerequisites. This also argues for a learning objective that chooses between resting and crossing, not only direction.

## Caveats
The CFTC filing index lists perps fee-schedule filings dated August 4, September 2, September 22, October 15 and October 18, 2026, plus general fee-schedule filings in June and July that were not opened, so any backtest must use dated fee regimes. Launch-period fees are not confirmed; a search-result summary of launch coverage, not opened, said they were zero. The fee Kalshi Prime actually passes to a retail customer is not confirmed here; an FCM may add commission or discount. The live fee for an account should be read from the authenticated `GET /margin/fee_tiers` endpoint. Rebate terms for self-clearing members expire at year end and may change the competitive landscape.
