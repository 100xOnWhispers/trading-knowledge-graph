---
title: "Exploring the Predictability of Cryptocurrencies via Bayesian Hidden Markov Models"
authors: "Koki, Constandina; Leonardos, Stefanos; Piliouras, Georgios"
year: 2020
venue: "arXiv preprint arXiv:2011.03741v2 (stat.AP)"
url: "https://arxiv.org/pdf/2011.03741"
pdf: "sources/01-macro-regime-detection/koki-2020-predictability-cryptocurrencies-bayesian-hmm.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "01-macro-regime-detection"
asset_class: "crypto"
horizon: "daily"
tags: "hidden-markov-model, non-homogeneous-transitions, bayesian, bitcoin, ether, ripple, density-forecast, covariates"
---

## Key insight
For Bitcoin, Ether and Ripple daily returns, every hidden Markov specification tried gave better one-step-ahead density forecasts than single-regime benchmarks (random walk, AR(5), a regression with all predictors), and a four-state model whose transition probabilities depend on covariates was best overall. The states are not persistent: they alternate frequently. So the models improve the forecast distribution, mostly by tracking volatility, without producing long tradable regimes.

## Method
Eight hidden Markov specifications with 2 to 5 states are compared. In the non-homogeneous model (NHHM) the predictors enter both the state-conditional mean and the transition probabilities through a multinomial logit, `p_ij(t) = exp(x_t * beta_ij) / sum_l exp(x_t * beta_il)`. Estimation is Bayesian MCMC: forward-backward sampling of states, Gibbs steps for regression coefficients, Pólya-Gamma augmentation for the logit coefficients, and a reversible-jump variable-selection step over predictors. Forecast evaluation uses the Continuous Rank Probability Score (CRPS) and mean squared error over L = 30 one-step-ahead predictive densities, with parameter estimates held fixed.

## Data and sample
Daily percentage log returns: BTC from 1/2014 to 11/2019, ETH from 9/2015, XRP from 1/2015. Twelve predictors, including fiat exchange rates, S&P 500 returns, the VIX, the US 10-year Treasury yield, commodity prices, and hash rate (BTC and ETH only). Sources: investing.com, Yahoo Finance, quandl.com, etherscan.io.

## Reported results
- Bitcoin average CRPS over the 30 forecast points: four-state NHHM 1.78, two-state Markov-switching random walk 1.85, random walk 1.98, AR(5) 1.95, all-predictor regression 1.92.
- The four-state NHHM is best on average for all three coins.
- Bitcoin states: state 1, the most frequent, is a bear regime (negative returns, high volatility); states 2 and 3 are bull regimes (positive returns, low volatility) differing in kurtosis; state 4 is calm (returns near zero).
- For Ether, alternation is mostly between a high-volatility state and a low-volatility state.
- States for all three coins "are not persistent, but they present frequent alternations".
- Only the Treasury yield and the VIX have predictive power for all three series.

## Signal construction
A bot version: features `x_t` (lagged VIX, yields, hash-rate change, own lags); a small HMM whose transition matrix is a softmax of `x_t`; output the one-step-ahead state probabilities and the implied predictive mean and variance. The practical use is the predictive variance and tail probability for sizing, not the predictive mean.

## Relevance to SOL perpetuals at minutes to hours
Supports two design choices: use more than two states for crypto, and let observable covariates drive transition probabilities instead of assuming a fixed transition matrix. The specific covariates are daily macro series that do not update intraday (and belong to topic 02); intraday analogues would be funding rate, open-interest change, BTC realised volatility and order-flow imbalance. SOL is not in the sample and the period ends in 2019, before perpetuals dominated crypto volume.

## Caveats
The out-of-sample test is 30 daily forecasts with parameters fixed, which is far too short to establish anything about trading value. The CRPS differences among HMM variants are small. Full MCMC estimation is likely too slow for intraday refitting (my assessment; the paper reports no timings that I saw). No costs, no strategy. The version read is the December 2020 preprint; a journal version was not confirmed.
