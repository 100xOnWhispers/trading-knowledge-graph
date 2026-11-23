---
title: "Power and Bipower Variation with Stochastic Volatility and Jumps"
authors: "Barndorff-Nielsen, Ole E.; Shephard, Neil"
year: 2004
venue: "Journal of Financial Econometrics 2(1), 1-37 (read as Nuffield College working paper, May 2003 draft)"
url: "https://www.nuffield.ox.ac.uk/economics/papers/2003/w18/eric_may03.pdf"
pdf: "sources/14-volatility-forecasting/barndorff-nielsen-2004-power-bipower-variation-jumps.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "14-volatility-forecasting"
asset_class: "fx"
horizon: "daily"
tags: "bipower-variation, jumps, realized-variance, integrated-variance, jump-detection"
---

## Key insight
Realized variance converges to the whole quadratic variation, which mixes smooth (diffusive) variance and jumps. Realized bipower variation, built from products of adjacent absolute returns, converges to the diffusive part only when jumps are rare. The difference between the two is therefore an estimate of the jump contribution. The authors describe this as the first method to split quadratic variation into continuous and jump components.

## Method
With M intraday returns y_j in a day:

RV = sum of y_j squared, and BV = (pi/2) * sum over j of |y_{j-1}| * |y_j|.

The factor pi/2 is mu_1 to the power minus two, where mu_1 = E|N(0,1)| = sqrt(2/pi). Under stochastic volatility plus rare jumps, BV estimates integrated variance and RV minus BV estimates the sum of squared jumps. The intuition: a single large jump inflates one squared return in RV, but in BV it is multiplied by a neighbouring normal-sized return, so its weight vanishes as sampling gets finer. The paper gives theory, simulations and extensions to general power and multipower variation. The version read is the 2003 working paper, which gives proofs for special cases.

## Data and sample
Olsen DM/USD 5-minute returns (M = 288 per day) from 1 December 1986 to 30 November 1996.

## Reported results
- The diffusive component dominates daily realized variance: average RV is 0.528 and the average jump contribution is 0.0310, which the authors call quite modest.
- Estimated jump components show little serial dependence, while the bipower series is slightly more persistent than RV.
- Illustration: a day with a single large 5-minute move has high RV but much lower BV (flagged as a jump), whereas a day with a sustained one-hour run of same-sign returns has both high RV and high BV (not flagged).

## Signal construction
Not a directional signal by itself; it is a decomposition used as a feature and a filter. Compute both RV and BV on a rolling window (for example the last 60 one-minute returns), then:
- jump share J = max(RV - BV, 0) / RV;
- use BV (the persistent part) as the input to the volatility forecast, and treat J as a separate, less persistent feature;
- a high J in the latest window indicates that recent "volatility" was a discrete event, so sizing down as if volatility had regime-shifted may be an over-reaction.

## Relevance to SOL perpetuals at minutes to hours
Jumps are a much larger share of crypto price variation than of 1990s FX (see the Scaillet note), so the split matters more. Two things need care. First, the Hansen note shows that crypto volatility bursts in the first minute of each hour and at funding times, which breaks the assumption that adjacent returns are similar and can bias BV; deseasonalise first or avoid windows that straddle those minutes. Second, at 1-minute sampling on a thinner venue, zero returns push BV toward zero and overstate jumps.

## Caveats
Asymptotic theory under frictionless prices and rare (finite-activity) jumps. No microstructure-noise treatment in this paper. The empirical section is an illustration on one FX series, not a forecasting test.
