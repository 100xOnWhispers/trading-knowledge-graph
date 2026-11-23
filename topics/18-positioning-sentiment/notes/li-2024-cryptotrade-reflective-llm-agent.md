---
title: "A Reflective LLM-based Agent to Guide Zero-shot Cryptocurrency Trading (CryptoTrade)"
authors: "Li, Yuan; Luo, Bingqiao; Wang, Qian; Chen, Nuo; Liu, Xu; He, Bingsheng"
year: 2024
venue: "arXiv:2407.09546 (v2)"
url: "https://arxiv.org/pdf/2407.09546"
pdf: "sources/18-positioning-sentiment/li-2024-cryptotrade-reflective-llm-agent.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "18-positioning-sentiment"
asset_class: "crypto"
horizon: "daily"
tags: "llm-agent, news-sentiment, on-chain-statistics, reflection, sol, btc, eth, buy-and-hold-benchmark"
---

## Key insight
A multi-agent LLM trader that reads daily news summaries, on-chain statistics and technical indicators, and reflects on its recent trades, beats transformer time-series baselines but does not reliably beat buy-and-hold or simple moving-average rules on BTC, ETH or SOL. On SOL in a bull window it earned 99.84% against 176.72% for buy-and-hold. The abstract claims superior performance; the paper's own tables and limitations section are more modest. It is the clearest crypto-specific evidence that LLM news reading at a daily horizon is not yet a standalone edge.

## Method
Four LLM roles run once per day: a market analyst (price, on-chain transaction statistics, technical signals), a news analyst (summaries of articles gathered through the GNews API from outlets such as Bloomberg, Yahoo Finance and crypto.news, summarized with GPT-3.5-turbo), a trading agent that outputs an action in [-1, 1] (fraction of cash to buy or of holdings to sell), and a reflection agent that reviews recent prompts, actions and returns. A fee proportional to traded value is charged. No fine-tuning. Baselines: buy-and-hold, SMA, SLMA, MACD, Bollinger Bands, LSTM, Informer, AutoFormer, TimesNet, PatchTST.

## Data and sample
BTC, ETH and SOL daily data in 2023. Validation January to March 2023; test windows labelled bearish (12 April to 16 June), sideways (mid-June or July to late August) and bullish (1 October to 1 December). Each window is about two months.

## Reported results
- SOL total return, bull / sideways / bear: buy-and-hold 176.72 / -3.23 / -36.08; SLMA 169.98 / 6.22 / -8.11; SMA 119.37 / -0.62 / 1.04; CryptoTrade (GPT-4 row) 99.84 / -2.16 / -19.55; CryptoTrade (GPT-3.5-turbo) 102.45 / -13.05 / -24.08.
- The text says the agent is "comparable" to buy-and-hold and MACD, exceeds them by about 3% on ETH in the bull window, and "consistently surpasses more than half of the trading signals".
- Ablation on ETH bull window: full prompt 28.47% return (Sharpe 0.23); without news 19.69% (0.06); without reflection 17.14%; without on-chain statistics 12.70%; without technical signals 17.27%.
- A case study shows the agent buying ahead of Bitcoin ETF approval rumours.
- Limitations stated by the authors: small dataset, daily frequency only, and lack of fine-tuning as a likely reason for underperforming traditional signals.

## Signal construction
Inputs per day: price history, technical indicators, on-chain counts (transactions, active wallets, value transferred, gas), and summarized headlines. Pipeline: summarize news with a cheap LLM; ask one model for a market view, one for a news view; feed both plus a reflection on the last several trades to a trading prompt that returns a position change in [-1, 1]. Update daily in the paper; the authors list hourly or minute-level operation as future work.

## Relevance to SOL perpetuals at minutes to hours
SOL is in the sample, which is rare. The result argues against delegating the trading decision to an LLM and for using the LLM as a feature extractor: the news component added about 9 percentage points in one ablation window, while simple trend rules did as well or better overall. The agent is long-only spot, so it says nothing about shorting, funding or leverage.

## Caveats
Three two-month windows in a single year, so differences are statistically weak; no confidence intervals. The leakage argument in the paper refers to the GPT-3.5 cut-off of September 2021; whether the GPT-4 family models used had training data overlapping the 2023 test windows is not addressed in what was read. Model naming is inconsistent between text (GPT-4o) and tables (GPT-4). Window labels were chosen after the fact. Fee level not confirmed from the text read.
