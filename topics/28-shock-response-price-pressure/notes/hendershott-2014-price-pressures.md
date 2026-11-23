---
title: "Price pressures"
authors: "Hendershott, Terrence; Menkveld, Albert J."
year: 2014
venue: "Journal of Financial Economics 114, 405-423"
url: "https://faculty.haas.berkeley.edu/hender/Price_Pressures.pdf"
pdf: "sources/28-shock-response-price-pressure/hendershott-2014-price-pressures.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "28-shock-response-price-pressure"
asset_class: "equities"
horizon: "daily"
tags: "price-pressure, inventory, state-space, transitory-permanent, half-life, liquidity"
---

## Key insight
Price pressure is the gap between the traded price and the efficient price that arises because a risk-averse intermediary uses price to work off inventory. Using actual NYSE specialist inventories, the paper measures it directly: 0.49% on average, with a half-life of 0.92 days. The size and the decay time both rise steeply as stocks get smaller, and pressure measured this way differs across stocks far more than the bid-ask spread does.

## Method
A state-space model estimated by maximum likelihood with the Kalman filter:

`p(t) = m(t) + s(t)`, `m(t) = m(t-1) + drift + w(t)`

The permanent innovation `w` is related to surprise order flow (information); the transitory term `s` is related to the intermediary's inventory (pressure), `s(t) = alpha * I(t) + noise`. Inventory is idiosyncratic, since market-wide inventory can be hedged. A structural model of a single intermediary who trades off lost revenue from skewing prices against the risk of holding inventory reproduces the same state-space form and identifies risk aversion and investors' private-value dispersion.

## Data and sample
Balanced panel of 697 NYSE common stocks, daily, January 1994 to December 2005, sorted into size quintiles. Prices from CRSP and TAQ; end-of-day specialist positions from a proprietary NYSE data set.

## Reported results
- Average price pressure 49 basis points, half-life 0.92 days.
- Largest quintile: 17 basis points, half-life 0.54 days. Smallest quintile: 118 basis points, half-life 2.11 days.
- Marginal pressure: 0.02 basis points per USD 1,000 of idiosyncratic inventory for the largest stocks and 0.98 for the smallest. Effective half-spreads are 8.41 and 46.12 basis points. Small stocks are 49 times less liquid by marginal pressure and about 5 times by spread.
- Average permanent (efficient-price) daily volatility is 177 basis points.
- The implied social cost of price pressure is about 10% of the cost of immediacy.
- Scope record: horizon hours to days; conditioning variable intermediary inventory; sign negative (a long intermediary means price is below efficient and expected to rise); costs not a trading test.

## Signal construction
Not directly a signal, because dealer inventory is not observable in crypto. It gives the measurement template: fit `p = m + s` with `s` loading on a proxy for liquidity providers' inventory, and read the transitory component as the expected reversal. A workable proxy is cumulative signed taker flow over the last N minutes relative to depth (the mirror image of what makers were forced to absorb), or on Hyperliquid the liquidator vault's position, which is public. Output: an estimate of current pressure in basis points and its half-life, updated each bar.

## Relevance to SOL perpetuals at minutes to hours
The framework fits a liquidation burst closely: makers take on inventory in one direction at a discount and shed it over the following period. The paper shows that pressure can be several times the spread and that its half-life scales with illiquidity, which gives two testable quantities for SOL: the size of the transitory component after a burst and how fast it decays. The numbers themselves do not transfer. Crypto makers hedge across venues and instruments in seconds, so half-lives are likely minutes to hours, not a day. A thin venue such as Kalshi would sit at the slow, large-pressure end of the paper's cross-section.

## Caveats
One designated intermediary per stock in a market structure that no longer exists; modern liquidity supply is fragmented and inventory is unobserved. Daily closing data cannot see intraday dynamics. The decomposition is model-dependent: anything correlated with inventory and transitory in price is labelled pressure.
