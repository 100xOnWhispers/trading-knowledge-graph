---
title: "Implied ETF Carry Rates and the Limits of Arbitrage in Segmented Bitcoin Markets"
authors: "Mallory, Mindy L."
year: 2026
venue: "arXiv preprint 2605.29309"
url: "https://arxiv.org/abs/2605.29309"
pdf: "sources/20-options-derived-signals/mallory-2026-implied-etf-carry-cme-bitcoin.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "20-options-derived-signals"
asset_class: "crypto"
horizon: "daily"
tags: "cme-futures-basis, ibit-options, put-call-parity, carry, limits-to-arbitrage, cross-margining, etf"
---

## Key insight
The carry priced into CME bitcoin futures is on average about 2.6 percentage points a year higher than the carry implied by put-call parity in options on the largest spot bitcoin ETF (IBIT), and the gap swings between roughly -5 and +10 points. Two regulated US venues therefore price the same forward differently, which the author attributes to collateral and margin systems that do not net a hedged position across the futures and securities sides. The CME basis is partly a price of balance-sheet friction, not a clean measure of bullish demand.

## Method
- ETF-implied forward from matched call and put mid-quotes: `F = K + exp(r * tau) * (C - P)`.
- Converted to bitcoin units by dividing by bitcoin per ETF share from the issuer's daily holdings file.
- ETF carry = annualised premium of that forward over the ETF close, plus the 0.25% expense ratio.
- CME carry = annualised premium of the matched CME futures close over BRRNY, the New York close variant of the CME CF Bitcoin Reference Rate.
- Wedge = CME carry minus ETF carry.

Filters: 14 to 90 days to expiry, absolute moneyness under 5%, spread under 10% of mid, open interest of at least 100 contracts on both legs. One near-the-money strike is kept per date in each of two maturity buckets (targets of 22 and 45 days). American exercise is handled by sample selection, not by a model.

## Data and sample
IBIT option quotes (OptionMetrics), issuer holdings files, SOFR, CME bitcoin futures (Barchart), BRRNY. 386 date-bucket observations (193 in each bucket). The calendar dates of the sample are not stated in the text read.

## Reported results
- Wedge: mean 2.58%, median 2.52%, standard deviation 4.72%, 5th percentile -4.77%, 95th percentile 10.42%, in annual percentage points.
- 14 to 30 day bucket: mean 2.22%, standard deviation 5.53%. 31 to 60 day bucket: mean 2.94%, standard deviation 3.71%.
- The 61 to 90 day bucket is dropped as too thin.

The paper also records contract facts: standard CME bitcoin futures final-settle to the 4 p.m. London reference rate (BRR), Bitcoin Friday futures to BRRNY, and daily settlement uses a volume-weighted price of trades between 2:59 and 3:00 p.m. Central Time.

## Signal construction
Daily features, all from public or low-cost data:
- `cme_carry = (F_cme / spot_ref)^(365 / days) - 1` for the front and second contracts.
- `etf_carry` from near-the-money IBIT put-call parity as above.
- `wedge = cme_carry - etf_carry`, and its change.
Hypothesis for testing, not a result of the paper: a rising wedge indicates leveraged long demand concentrating in futures, or dealer balance sheet becoming scarce, and both are states in which funding-driven liquidations are more likely. Compare with offshore perpetual funding from topic 03.

## Relevance to SOL perpetuals at minutes to hours
Indirect. This is a daily, bitcoin-only quantity that describes the regulated US leg of crypto leverage, which is also where a Kalshi perpetual sits. It is useful as a slow state variable alongside funding and basis measures, and as a caution that CME basis levels cannot be compared one-for-one with offshore funding rates. Nothing in the paper tests return or volatility prediction, and nothing covers SOL futures or SOL ETF options.

## Caveats
A five-page preprint with summary statistics only: no tests, no time-series analysis, and an undisclosed sample window that cannot be long given when ETF options began trading. The wedge includes early-exercise premia, quote noise from a single strike, and timing mismatch between option quotes and the futures close. The author discloses use of AI tools in preparing the manuscript. CME weekend gaps and trading-hours effects are not addressed.
