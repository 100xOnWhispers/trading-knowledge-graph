---
title: "Evaporating Liquidity"
authors: "Nagel, Stefan"
year: 2012
venue: "NBER Working Paper 17653 (December 2011), the version read; published in the Review of Financial Studies, 2012 (journal version not opened)"
url: "https://www.nber.org/system/files/working_papers/w17653/w17653.pdf"
pdf: "sources/28-shock-response-price-pressure/nagel-2012-evaporating-liquidity.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "28-shock-response-price-pressure"
asset_class: "equities"
horizon: "multi-day"
tags: "reversal, liquidity-provision, vix, time-varying-expected-return, stress, conditioning-variable"
---

## Key insight
The return to a short-term reversal strategy is the price of liquidity provision, and that price is not constant. It rises sharply and predictably with the VIX. In stress, liquidity suppliers withdraw, so prices overshoot more and the subsequent reversal is larger. Reversal is therefore strongest exactly when volatility is highest and capital is scarce.

## Method
Each day, form a portfolio that weights stocks in proportion to the negative of their market-adjusted return on each of the previous five days (five sub-strategies averaged), scaled to USD 1 long and USD 1 short. Compute returns from transaction prices and, separately, from quote midpoints to remove bid-ask bounce. Hedge conditional market exposure. Run predictive regressions of the strategy's daily return on VIX (normalized to daily volatility by dividing by the square root of 250) measured at the end of day t-5, with controls for decimalization and the lagged four-week market return. An industry-portfolio version tests whether the effect is more than single-stock microstructure.

## Data and sample
US stocks from CRSP (quote-midpoint results use Nasdaq stocks only), daily, January 1998 to December 2010.

## Reported results
- Mean return per day: 0.30% with transaction prices, 0.18% with quote midpoints, 0.02% for industry portfolios. About half of the transaction-price return is bid-ask bounce.
- Annualized Sharpe ratios before costs: 8.44, 4.50 and 0.56.
- VIX coefficient 0.22 (standard error 0.02) for transaction-price returns: one point of normalized VIX (about 16 points of annualized VIX) adds 0.22 percentage points of expected daily return; adjusted R-squared 0.07 daily. For quote-midpoint returns the coefficient is 0.16 (0.02).
- Monthly averages: adjusted R-squared 56% (transaction prices), 25% (midpoints), 7% (industry).
- Industry reversal is unprofitable on average but earns about 0.20% per day at the VIX levels of late 2008.
- Reversal returns were near 1% per day in the 1998 and 2000-2001 episodes, below 0.2% by 2007, then rose above the 1998 level in the financial crisis.
- The predictable component lasts far longer than a day.
- Scope record: horizon one to five days; conditioning variable VIX; sign positive (more stress, more reversal); costs not charged, and the author notes Sharpe ratios would be much less extreme after costs.

## Signal construction
Use implied or realized volatility as a multiplier on the expected size of reversal, not as a direction signal. For a SOL bot: expected post-shock reversal = base coefficient times a stress scalar built from a volatility index (Deribit DVOL for BTC or ETH, or short-window realized volatility of SOL), lagged so it is known before the shock. Refit the slope periodically. The paper's second lesson is to measure everything on mid or mark prices, otherwise half the apparent edge is bounce.

## Relevance to SOL perpetuals at minutes to hours
The mechanism should transfer: crypto market makers are capital-constrained and pull quotes in stress, as the October 2025 studies in topic 04 show for spreads and depth. That predicts larger overshoot and larger reversal after shocks in high-volatility states, and near-zero reversal edge in calm ones. What does not transfer is the horizon (daily cross-sectional portfolios versus one instrument intraday) and the diversification: a single-asset bot has no cross-section to net out market moves, so a liquidity-provision trade on SOL carries full directional risk during the very periods when the expected reward is highest.

## Caveats
Gross of costs. Cross-sectional and daily. The Khandani and Lo quant-crisis episode of August 2007, cited in the paper, shows reversal strategies can lose badly for days when liquidity suppliers themselves are forced to delever. Sample ends in 2010.
