---
title: "When do stop-loss rules stop losses?"
authors: "Kaminski, Kathryn M.; Lo, Andrew W."
year: 2014
venue: "Journal of Financial Markets, vol. 18, pp. 234-254"
url: "https://ideas.repec.org/a/eee/finmar/v18y2014icp234-254.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "27-execution-risk-management"
asset_class: "futures"
horizon: "daily"
tags: "stop-loss, risk-management, momentum, drawdown-control, serial-correlation"
---

## Key insight
The abstract establishes a framework for asking whether a stop-loss rule adds or subtracts value from a strategy's expected return and volatility, and reports that for a buy-and-hold index futures strategy, certain stop-loss policies raise expected return while substantially lowering volatility at longer sampling frequencies. The value of a stop is therefore an empirical property of the return process, not a free form of insurance.

## Method
From the abstract only. The authors propose "a simple analytical framework" to measure the value added or subtracted by stop-loss rules, defined as predetermined policies that reduce a portfolio's exposure after cumulative losses reach a threshold. The framework is applied to the expected return and volatility of an arbitrary portfolio strategy, and then tested empirically. The exact rule parameters, the re-entry condition and the analytical expressions were not read in this session.

## Data and sample
From the abstract: daily futures price data; stop-loss policies applied to a buy-and-hold strategy in index futures contracts. Contracts, period and sample size are not confirmed.

## Reported results
From the abstract only:
- "At longer sampling frequencies, certain stop-loss policies can increase expected return while substantially reducing volatility".
- The abstract describes this as consistent with the objectives of stop-losses in practice.

No magnitudes were read. The widely repeated summary of this paper, that stops cost return under a random walk and help when returns have momentum, is not stated in the abstract and is recorded here as not confirmed.

## Signal construction
Not a signal; a risk overlay. The generic form the abstract describes: track cumulative return over a rolling window; if it falls below a threshold, cut exposure; restore exposure under a re-entry rule. For a bot this means three parameters (window, loss threshold, re-entry condition) that should be justified by the measured serial correlation of the strategy's own returns, not chosen by backtest search. The Carr and Lopez de Prado note gives a simulation procedure for choosing such thresholds under an assumed process.

## Relevance to SOL perpetuals at minutes to hours
The question the paper poses is the right one for the bot: a stop helps only if losses predict further losses over the stop's horizon. At minutes to hours in crypto there are plausible reasons for both signs. Liquidation cascades (topic 04) create short bursts of continuation, which favours stops; intraday reversal after liquidity shocks (topic 13) favours holding. The abstract's finding concerns daily data and index futures at "longer sampling frequencies", which says nothing direct about intraday stops, where each stop-out also pays the spread and taker fee. This must be re-tested on the bot's own trade returns.

## Caveats
Abstract-only. The open-access copy in the MIT repository (handle 1721.1/114876) was located, but the download was rate-limited during this session, so no number or formula from the body is reported. Buy-and-hold index futures is a long-only, positive-drift setting; results for a two-sided intraday strategy may differ. Transaction costs of the stop itself are not mentioned in the abstract. A follow-up by Lo and Remorov on stop-losses with serial correlation, regime switching and transaction costs could not be opened.
