---
title: "Weekend Crypto Volatility and Monday Market Risk"
authors: "Ebadollahyvahed, Pedram; Umeorah, Nneka"
year: 2026
venue: "arXiv preprint 2610.35702"
url: "https://arxiv.org/abs/2610.35702"
pdf: "sources/21-cross-asset-lead-lag/ebadollahyvahed-2026-weekend-crypto-volatility-monday-risk.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "21-cross-asset-lead-lag"
asset_class: "multi"
horizon: "multi-day"
tags: "volatility-spillover, weekend, crypto-to-equity, har, structural-break, connectedness, machine-learning, calendar"
---

## Key insight
Because crypto trades through the weekend while traditional markets are closed, the direction of information flow can be identified by the calendar. Weekend crypto variance predicts Monday variance in the S&P 500, gold and a Treasury ETF, but only from about late 2023; before that the effect is absent. A standard Diebold-Yilmaz connectedness analysis on the same assets does not show the change, so pooled connectedness indices can miss spillovers that are concentrated in particular time windows.

## Method
Daily Garman-Klass range-based variance for each asset. Weekend crypto variance is the sum of Saturday and Sunday variances; the common factor W is the equally weighted average of the logged weekend variances of the three coins. Monday log variance of each traditional asset is regressed on its HAR terms (daily, weekly, monthly lags) plus W, with and without Friday crypto variance as a control; Newey-West errors. Further steps: sub-period and rolling two-year estimates; an Andrews-type endogenous break search with 15% trimming; decomposition of each coin's weekend variance into the common factor and a coin-specific residual; expanding-window out-of-sample forecasts scored by QLIKE with Diebold-Mariano tests; comparison of HAR with tree-based models and an LSTM; interactions with spot ETF flows and with the VIX regime; a Diebold-Yilmaz connectedness benchmark.

## Data and sample
Bitcoin, Ether, XRP; S&P 500 index, COMEX gold futures, iShares 7-10 Year Treasury ETF (IEF). Daily OHLC, November 2017 to June 2026.

## Reported results
- Mean of the nine pairwise weekend coefficients: about zero and slightly negative before 2020; weak in 2022-2023 (two of nine positive and significant at 5%); 0.35 after January 2024 with all nine positive and significant.
- Post-2024, a one-standard-deviation rise in W is associated with about 28% higher fitted Monday variance for the S&P 500, 54% for gold and 27% for the Treasury ETF.
- Adding W to HAR lowers out-of-sample QLIKE loss by 11-22%, with statistical support varying by market.
- Friday crypto variance alone has little predictive content. The common factor predicts; coin-specific residuals do not.
- The estimated break is in late 2023. ETF-flow interactions are insignificant for the S&P 500 and gold and negative for the Treasury ETF, so the mechanism is unresolved.
- Estimated separately by weekday, the weekend-factor coefficient is largest on Monday in all three markets (versus Tuesday and Wednesday); for the S&P 500 it is larger in the high-VIX regime.
- Tuned machine-learning models "do not consistently outperform the HAR benchmark".
- The rolling Diebold-Yilmaz index shows no comparable change around 2023-24.
- The authors cite Mourey et al. (2025) for the return analogue: weekend crypto returns predicting Monday equity returns, with a break dated to the 2022 LUNA collapse (not opened here).

## Signal construction
Weekly feature for volatility and sizing: W = mean over BTC, ETH (and SOL) of log(Saturday variance + Sunday variance), standardized on a trailing window. Inputs to the bot: (a) forecast of Monday equity-session volatility, which feeds expected crypto volatility through the equity beta at the US open; (b) a flag for elevated Sunday-evening futures reopen risk. The same construction generalizes to any window when one market is closed: crypto variance during the US overnight as a predictor of variance at the US cash open.

## Relevance to SOL perpetuals at minutes to hours
Indirect but useful. It shows the crypto-to-traditional direction is now live, so the lead between equities and crypto is not one-way; over the weekend crypto is the only price-discovery venue for macro news and Monday's equity open can feed back into SOL. It also gives a concrete example of unstable cross-asset structure: a relation that did not exist before late 2023. The methodological point matters for this topic: test spillovers by session and calendar window, since pooled measures dilute them.

## Caveats
Preprint, one month old at the time of reading. Daily range-based variances, volatility not direction. About 116 post-break Mondays. Nine pairs share three highly correlated coins, so the count of significant pairs overstates independent evidence. A break found by search invites data-snooping concerns even with Andrews critical values. SOL is not in the sample.
