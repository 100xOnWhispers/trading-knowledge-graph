---
title: "Modelling microstructure noise with mutually exciting point processes"
authors: "Bacry, Emmanuel; Delattre, Sylvain; Hoffmann, Marc; Muzy, Jean-Francois"
year: 2013
venue: "Quantitative Finance 13, 65-77 (arXiv:1101.3422 version of January 2011 read)"
url: "https://arxiv.org/abs/1101.3422"
pdf: "sources/21-cross-asset-lead-lag/bacry-2013-microstructure-noise-mutually-exciting-point-processes.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "21-cross-asset-lead-lag"
asset_class: "futures"
horizon: "seconds"
tags: "hawkes, point-process, epps-effect, lead-lag, signature-plot, cross-excitation, methodology"
---

## Key insight
A tick-level price model built from mutually exciting (Hawkes) point processes reproduces two facts that any high-frequency cross-asset analysis must respect: realized variance explodes at fine sampling (the signature plot) and cross-asset correlation collapses toward zero at fine sampling (the Epps effect). Both come out in closed form, and lead-lag appears as an asymmetry in the cross-excitation kernels between the two assets.

## Method
One asset: X(t) = N1(t) - N2(t), where N1 and N2 count upward and downward price jumps. Intensities are lambda1(t) = mu + integral of phi(t-s) dN2(s) and symmetrically for lambda2, so an up-move raises the chance of a down-move. With an exponential kernel phi(t) = alpha * exp(-beta * t) this generates microscopic mean reversion while the price diffuses at large scales.

Two assets: a four-dimensional Hawkes process (up and down jumps of each asset) with a kernel matrix that contains the within-asset mean-reversion terms plus cross terms: an up-jump of asset 1 excites up-jumps of asset 2 and the reverse. The paper derives the covariance matrix C(tau) of increments at scale tau, hence the correlation rho(tau) = C12(tau) / C11(tau) as a function of scale. For lead-lag it defines

Delta(tau) = C12(tau, tau) - C21(tau, tau),

the difference between the correlation of asset 1's past increment with asset 2's next increment and the reverse. Delta is zero when the kernel matrix is symmetric and non-zero when one asset excites the other more strongly than the reverse; a closed form in the kernel parameters is given. The authors state that a dedicated study of lead-lag in this framework is left to a later paper. Parameters are estimated by regression on the empirical signature plot and correlation curve.

## Data and sample
Simulations, and Eurex Euro-Bund and Euro-Bobl futures trade data from QuantHouse; fits are shown for individual days (for example 11 March 2009, December 2009 contract).

## Reported results
- Theoretical signature plots and Epps curves match the simulated and the Bund/Bobl empirical curves "in several situations"; correlation between Bund and Bobl increments rises from near zero at the finest scale toward its diffusive limit as tau grows.
- The exponential-kernel choice is described as somewhat arbitrary.
- A later review by Bacry, Mastromatteo and Muzy (arXiv:1502.04592, opened in this session) restates that the signature plot, lead-lag behaviour and the Epps effect are all expressed through the Hawkes kernel matrix.

## Signal construction
Not a signal. It is a modelling framework and a warning. Use: (1) pick sampling intervals for cross-asset features above the scale where the Epps effect has faded, read off the empirical rho(tau) curve for BTC/SOL or ES/BTC; (2) as an alternative lead-lag estimator, fit a multivariate Hawkes model to up and down mid-price jumps of leader and target and compare the integrated cross-kernels in each direction (the branching ratio from leader to target versus target to leader); the kernel decay rate gives the time scale of the lead.

## Relevance to SOL perpetuals at minutes to hours
Raw correlation between BTC and SOL returns measured at one second will look low and lagged correlations will look relatively large purely because of asynchronous price updating on a thin venue. The Hawkes view separates this mechanical effect from a genuine directional excitation. For a slow venue such as a new Kalshi perp the Epps scale could be tens of seconds or more, and it should be measured before any lead-lag feature is trusted.

## Caveats
Interest-rate futures in 2009, a handful of days, no out-of-sample test and no trading application. Lead-lag is defined but not studied empirically here. Exponential kernels miss the slow-decaying dependence found in later Hawkes work.
