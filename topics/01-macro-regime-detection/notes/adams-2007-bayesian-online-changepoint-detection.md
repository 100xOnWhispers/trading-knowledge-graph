---
title: "Bayesian Online Changepoint Detection"
authors: "Adams, Ryan Prescott; MacKay, David J. C."
year: 2007
venue: "arXiv preprint arXiv:0710.3742 (stat.ML)"
url: "https://arxiv.org/pdf/0710.3742"
pdf: "sources/01-macro-regime-detection/adams-2007-bayesian-online-changepoint-detection.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "01-macro-regime-detection"
asset_class: "multi"
horizon: "n/a"
tags: "changepoint-detection, bocpd, run-length, online-inference, hazard-function, bayesian"
---

## Key insight
An exact online algorithm for the question "how long ago did the data-generating parameters last change?". At each new observation it updates a probability distribution over the current run length (time since the last changepoint) by a simple message-passing recursion, using only past data. Unlike a Markov-switching model it does not assume regimes recur: parameters after a changepoint are independent of those before.

## Method
Let `r_t` be the run length at time t. With each new datum `x_t`, for every possible run length:

- growth: `P(r_t = r_{t-1}+1, x_{1:t}) = P(r_{t-1}, x_{1:t-1}) * pi_t(r) * (1 - H(r_{t-1}))`
- changepoint: `P(r_t = 0, x_{1:t}) = sum over r_{t-1} of P(r_{t-1}, x_{1:t-1}) * pi_t(r) * H(r_{t-1})`

where `pi_t(r)` is the predictive probability of `x_t` given the data in the current run and `H` is the hazard function. Normalising gives `P(r_t | x_{1:t})`. With a geometric prior on segment length of timescale lambda, the hazard is constant at `1/lambda`. Conjugate exponential-family likelihoods make the predictive a matter of updating sufficient statistics per run length. Cost per step is linear in the number of points seen; discarding run lengths with tail mass below a threshold such as 1e-4 gives average cost on the order of the expected run length.

## Data and sample
Three demonstrations: 4,050 nuclear magnetic response measurements from a well log (changing Gaussian mean); daily Dow Jones Industrial Average returns from 3 July 1972 to 30 June 1975 (zero-mean Gaussian with changing variance, gamma prior on precision with a = 1, b = 1e-4, lambda = 250); and coal-mining disaster intervals (Poisson rate, lambda = 1000).

## Reported results
Results are shown as figures, not as detection statistics. In the well-log data, drops of the run length to zero line up with abrupt changes in the mean. In the Dow Jones data the run-length posterior is plotted against three marked events (the Watergate convictions of 30 January 1973, the start of the OPEC embargo on 19 October 1973, and Nixon's resignation on 9 August 1974); the paper does not quantify how closely detected changes align with them. No accuracy, delay or false-alarm numbers are reported, and there is no trading test.

## Signal construction
Inputs: a stream of bar returns (or any feature such as realised variance or signed order flow). Parameters: hazard `1/lambda`, the conjugate prior, a pruning threshold. Per bar: compute predictives for all live run lengths, apply the two update rules, normalise. Outputs usable by a bot:
- `P(r_t < k)`: probability that a change happened within the last k bars, a "regime just changed" flag.
- The run-length-weighted predictive mean and variance, an adaptive estimate that forgets pre-change data automatically.
- Expected run length, as an input feature to another model (see [wood-2022](wood-2022-slow-momentum-fast-reversion-changepoint.md), which feeds changepoint outputs to a neural network).

## Relevance to SOL perpetuals at minutes to hours
Well matched to the problem: online, no look-ahead by construction, cheap, and it does not need regimes to repeat. What needs work is the observation model. A Gaussian with unknown variance will fire on every fat-tailed bar and on the daily volatility cycle, so returns should be deseasonalised and a Student-t predictive (which the Normal-Gamma conjugate model gives) used. The hazard rate directly sets how jumpy the detector is and must be tuned on SOL data with costs included.

## Caveats
A methods paper with illustrative examples only. The constant-hazard and independent-segment assumptions are both false for markets, where volatility regimes recur. The detector reports a change only after enough post-change data have arrived, and the paper does not quantify that delay.
