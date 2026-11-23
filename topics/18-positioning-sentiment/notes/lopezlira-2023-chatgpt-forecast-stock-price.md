---
title: "Can ChatGPT Forecast Stock Price Movements? Return Predictability and Large Language Models"
authors: "Lopez-Lira, Alejandro; Tang, Yuehua"
year: 2023
venue: "arXiv:2304.07619 (v6, October 2025; first version April 2023)"
url: "https://arxiv.org/pdf/2304.07619"
pdf: "sources/18-positioning-sentiment/lopezlira-2023-chatgpt-forecast-stock-price.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "18-positioning-sentiment"
asset_class: "equities"
horizon: "daily"
tags: "llm-news-sentiment, chatgpt, headline-scoring, post-cutoff-test, alpha-decay, transaction-costs"
---

## Key insight
An off-the-shelf LLM, asked a single yes/no/unknown question about a headline, classifies the market's initial reaction with roughly 90% portfolio-day accuracy and also predicts one to two days of subsequent drift. Predictive ability rises with model size. The edge is small per trade, vanishes at 20 basis points round-trip, and decays year by year as LLM use spreads. This is the reference design for LLM-scored news, and its decay path is the main warning.

## Method
Each headline is sent to the model with a fixed prompt at temperature 0: act as a financial expert, answer YES if good news, NO if bad, UNKNOWN if uncertain for the named company's stock price in the short term, then give one sentence of explanation. Answers map to +1, -1 and 0, averaged per stock per day. The score is compared with (a) the initial reaction (not tradable) and (b) the drift after the first tradable price. Long-short portfolios buy positive-score and sell negative-score stocks, rebalanced daily at opening and closing auctions. Twelve models are compared, from GPT-1 to GPT-4. The sample begins after the model's knowledge cut-off (September 2021 for the GPT-4 version used) to avoid look-ahead. A theoretical model with capacity-constrained information processing and limits to arbitrage frames the results.

## Data and sample
Headlines for 4,123 US common stocks from major news media and newswires, October 2021 to May 2024. Daily open and close prices.

## Reported results
- Hit rate for the direction of the initial reaction: 93.3% for overnight headlines and 88.8% for intraday headlines (daily portfolio level).
- Drift strategy on overnight news: 34 bps per day before costs.
- Annualized Sharpe of the next-day drift strategy: 2.97 for GPT-4, 1.66 for GPT-3.5, 1.26 for DistilBART-MNLI, negative for most small models.
- Costs: at 5 bps round-trip the cumulative return is still over 300% for the sample; at 10 bps above 100%; at 20 bps the strategy is unprofitable.
- Decay: annualized Sharpe of the overnight-news strategy falls from 6.54 in 2021Q4 to 3.68 in 2022, 2.33 in 2023 and 1.22 in January to May 2024.
- Underreaction is strongest for small stocks and negative news. Topics such as earnings and partnership announcements are priced efficiently; insider transactions and conference presentations show drift.
- Embedding-based supervised models trained on rolling six-month windows perform worse than the prompt approach.

## Signal construction
Inputs: timestamped headlines mapped to the asset. For each headline call an LLM with the fixed prompt, map YES/NO/UNKNOWN to +1/-1/0, average over the interval. Enter in the direction of the score at the first tradable price after publication; hold one interval. Parameters: model, prompt, aggregation window, holding period. Use only models whose training cut-off precedes the backtest period.

## Relevance to SOL perpetuals at minutes to hours
The prompt design and the post-cutoff discipline transfer directly. The economics may not: the equity drift lives in small, hard-to-arbitrage stocks over a day, whereas SOL is a liquid 24-hour asset where headline reactions complete in seconds to minutes. A crypto version needs a tick-level timestamp study of how fast SOL perps absorb scored headlines, and should expect the initial reaction to be untradable for a slow bot. Crypto-specific evidence is in the CryptoTrade note in this folder.

## Caveats
Equities only. Auction execution assumption has no crypto analogue. Returns are concentrated where costs and impact are highest. The decay evidence implies that results from 2021 to 2023 overstate what is available now. Working paper version read; journal status not confirmed.
