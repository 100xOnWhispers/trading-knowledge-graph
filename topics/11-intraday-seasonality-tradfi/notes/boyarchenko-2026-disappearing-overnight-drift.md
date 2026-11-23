---
title: "The Disappearing Overnight Drift"
authors: "Boyarchenko, Nina; Larsen, Lars C.; Whelan, Paul"
year: 2026
venue: "Liberty Street Economics, Federal Reserve Bank of New York (1 July 2026)"
url: "https://libertystreeteconomics.newyorkfed.org/2026/07/the-disappearing-overnight-drift/"
pdf: "none"
access: "full-text"
source_type: "industry-research"
evidence_grade: "B"
topic: "11-intraday-seasonality-tradfi"
asset_class: "futures"
horizon: "hours"
tags: "overnight-drift, anomaly-decay, post-publication, order-imbalance, e-mini, liquidity-provision"
---

## Key insight
The authors of the overnight-drift paper report that the pattern is gone. The 02:00 to 03:00 ET window in E-mini S&P 500 futures, which earned about 3.7% a year from 1998 to 2020, has averaged close to zero from 2021 through 2025. Of the three inputs their inventory model says should drive the drift, only one changed: the dispersion of end-of-day order imbalance collapsed. The time-of-day pattern was a by-product of an imbalance state variable, and it went away when that state variable stopped moving.

## Method
Out-of-sample replication of the original charts on post-publication data, followed by an accounting exercise. Expected overnight return is modelled as (dollar order imbalance) x (return variance) / (risk-bearing capacity). Each input is compared between the original and new samples: the rolling 252-day standard deviation of end-of-day relative signed volume (15:15 to 16:15 ET), the VIX level, and the overnight share of volume. Next-day returns are sorted into four bins by closing signed volume in both periods. The post was read through a fetched text rendering; charts were not viewed directly.

## Data and sample
E-mini S&P 500 futures: 1998 to 2020 (5,691 trading days) versus January 2021 to December 2025 (1,245 trading days). The same flat pattern is stated for E-mini Nasdaq-100 and Dow futures.

## Reported results
- 1998 to 2020: the 02:00 to 03:00 window accounted for more than 60% of the contract's 5.9% annualized close-to-close return.
- 2021 to 2025: the window is flat.
- Standard deviation of end-of-day relative signed volume fell from 6.5% to 2.9%.
- VIX mean 20.4 versus 19.4 and median 18.6 versus 18.2: roughly unchanged.
- Overnight share of E-mini volume rose only from 15% to 16%.
- In 2007 to 2020, large negative closing imbalances were followed by positive overnight returns with a wide spread across bins; in 2021 to 2025 the spread is much narrower.
- The NightShares overnight ETFs launched in June 2022 and closed fourteen months later.
- Ongoing work suggests limit orders at the close have become smaller, consistent with algorithmic liquidity providers slicing flow more finely. The authors predict the drift would return if closing-imbalance dispersion widened again; this is untested.

## Signal construction
Not a signal by itself. It supplies a monitoring rule for any session-based reversal signal: track the rolling standard deviation of the conditioning imbalance variable. When dispersion compresses, expect the associated time-of-day drift to shrink and scale exposure down accordingly. Expected edge is proportional to imbalance x variance / liquidity-provider capacity, so all three should be logged.

## Relevance to SOL perpetuals at minutes to hours
Directly relevant as a warning and a design principle. A fixed-clock rule ("buy at hour X") discovered in backtests is fragile; the conditional relationship between prior-session signed flow and next-session returns is the object to estimate, and its strength should be re-estimated on a rolling basis. Crypto markets are less mature than E-mini futures, so imbalance dispersion may still be high, but the same compression is plausible as market makers professionalize.

## Caveats
A central-bank blog post, not a refereed paper; five years of post-sample data; explanations are partly from unpublished ongoing work. Publication-driven arbitrage is not separately tested. The decay coincides with other structural changes (retail options growth, zero-day options) that are not addressed.
