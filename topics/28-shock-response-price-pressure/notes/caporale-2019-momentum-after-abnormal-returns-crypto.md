---
title: "Momentum Effects in the Cryptocurrency Market After One-Day Abnormal Returns"
authors: "Caporale, Guglielmo Maria; Plastun, Alex"
year: 2019
venue: "CESifo Working Paper No. 7917 (October 2019)"
url: "https://www.ifo.de/DocDL/cesifo1_wp7917.pdf"
pdf: "sources/28-shock-response-price-pressure/caporale-2019-momentum-after-abnormal-returns-crypto.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "28-shock-response-price-pressure"
asset_class: "crypto"
horizon: "hours"
tags: "overreaction, intraday-momentum, continuation, abnormal-returns, hourly, no-costs"
---

## Key insight
On days that end up as abnormal-return days, hourly returns keep moving in the direction of the shock until the day closes, and in most cases the drift carries into the first hours of the next day. The paper reads this as intraday momentum after large moves, the opposite of the reversal found by De Nicola on Bitstamp data. The evidence is weaker than it looks because the entry hour is chosen with hindsight and no costs are charged.

## Method
Daily return is `Close / Open - 1`. A positive (negative) overreaction day has a return above (below) the mean plus (minus) `k` standard deviations, with `k = 2` for BTC and `k = 1.5` for ETH and LTC, chosen to give enough events. Hourly returns on overreaction days are compared with normal days by t-test, and cumulative abnormal hourly returns are plotted to find the hour at which the overreaction typically becomes detectable ("timing of overreaction"). Strategy 1 opens a position in the direction of the move once that hour is reached and closes at the end of the day. Strategy 2 opens in the same direction at the start of the next day (or opposite where a contrarian pattern was found) and closes at an asset-specific hour. Trades are compared with random trading by t-test.

## Data and sample
BTCUSD, ETHUSD and LTCUSD, daily and hourly, from CoinMarketCap, Gemini and Bitstamp. The abstract gives 1 January 2017 to 1 September 2019 for the tests; the data section gives 1 January 2015 as the start.

## Reported results
- Hourly returns on overreaction days differ significantly from normal days for all three assets and both signs.
- Typical detection hour: 18:00 (BTC), 13:00 (LTC), 12:00 (ETH) for positive days; 16:00, 14:00 and 13:00 for negative days.
- Strategy 1 (same day, with the move), no costs: BTC positive 49 trades, 86% winners, 2.92% per trade; LTC 38 trades, 97%, 8.19%; ETH 58 trades, 78%, 8.75%. Negative days: BTC 46 trades, 91%, 4.40%; LTC 39, 85%, 4.38%; ETH 57, 75%, 5.87%. All differ from random.
- Strategy 2 (next day): smaller, 1.1% to 4.0% per trade, 37% to 67% winners, and not different from random in three of six cases. The next day is contrarian for BTC after positive shocks and for ETH after negative shocks, and momentum otherwise.
- Scope record: horizon the remaining hours of the shock day and the first 10 to 21 hours of the next; conditioning variable daily open-to-close return beyond 1.5 to 2 standard deviations; sign continuation on the same day, mixed the next day; costs not charged.

## Signal construction
As published the rule is not implementable, because whether today is an overreaction day is known only at the close, and the entry hour was estimated from the same days it is applied to. A clean version: at each hour, compute the return since the daily open (or over a rolling 12-hour window) relative to a trailing distribution of same-length returns; if it exceeds a threshold, record the return over the next 1 to 12 hours. That is a testable intraday momentum-after-shock feature. Thresholds and windows must be fixed before looking at outcomes.

## Relevance to SOL perpetuals at minutes to hours
The claim matters because it contradicts the reversal evidence at a similar horizon. The two can both hold: this paper conditions on a slow move that accumulates over many hours of a calendar day, while De Nicola conditions on a single sharp one- or two-hour bar. Slow, sustained moves continuing and sharp spikes reversing is exactly the information versus price-pressure split the theory predicts. That hypothesis is not tested in either paper and is worth testing directly on SOL, with the speed of the move as the conditioning variable.

## Caveats
Selection bias: conditioning on the day ending as an extreme day guarantees that prices moved in that direction during the day, so Strategy 1's win rates are inflated by construction. No costs. Calendar-day boundaries are arbitrary in a 24-hour market. Small event counts (38 to 58 per case). Sample dates are stated inconsistently.
