---
title: "QuantEvolve: Automating Quantitative Strategy Discovery through Multi-Agent Evolutionary Framework"
authors: "Yun, Junhyeog; Lee, Hyoun Jun; Jeon, Insu"
year: 2025
venue: "arXiv preprint 2510.18569v1 (Qraft Technologies)"
url: "https://arxiv.org/pdf/2510.18569"
pdf: "sources/25-evolutionary-algorithms/yun-2025-quantevolve-quality-diversity-strategy-evolution.pdf"
access: "full-text"
source_type: "industry-research"
evidence_grade: "C"
topic: "25-evolutionary-algorithms"
asset_class: "multi"
horizon: "daily"
tags: "quality-diversity, map-elites, island-model, llm-agents, strategy-code-evolution, futures, early-stopping"
---

## Key insight
QuantEvolve applies quality-diversity search to whole trading strategies written as code. LLM agents propose and implement mutations, and a MAP-Elites style grid keeps the best strategy for each combination of behavioral attributes instead of one global winner. Its most useful finding is negative: on index futures, the strategy from generation 20 was the best out of sample, and 80 further generations added complexity that generalized worse.

## Method
- Feature map: a grid whose axes are strategy category (momentum, mean reversion, and so on), trading frequency, maximum drawdown, Sharpe ratio, Sortino ratio and total return, each cut into bins. Each cell stores the single best strategy with that profile. A new strategy replaces the occupant only if it scores higher.
- Islands: one sub-population per seed category plus a buy-and-hold seed. Islands evolve separately and periodically send their top 10% to neighbors.
- Variation: a research agent reads a parent and "cousin" strategies sampled from the map and writes a hypothesis; a coding team implements and backtests it; an evaluation team records what worked and failed. Insights are curated every 50 generations and fed into later prompts.
- Fitness: Score = Sharpe ratio + information ratio + maximum drawdown (drawdown enters as a negative number), equal weights.
- Selection for reporting: evolve on the training period, choose the strategy with the best validation score, report on the test period.

## Data and sample
Daily OHLCV. Equities: AAPL, NVDA, AMZN, GOOGL, MSFT, TSLA; training August 2015 to July 2020, validation to July 2022, test August 2022 to July 2025. Futures: ES and NQ; training 2018 to July 2021, validation to July 2022, test August 2022 to January 2024. Costs: $0.0075 per share with a $1 minimum, plus slippage quadratic in the share of volume traded.

## Reported results
- Equities, test period (Sharpe, maximum drawdown, information ratio, cumulative return): market-cap portfolio 0.99, -33%, n/a, 99%; equal weight 1.07, -36%, 0.80, 129%; MACD 1.10, -39%, 0.75, 171%; generation 0 0.99, -35%, 0.03, 100%; generation 150 1.52, -32%, 0.69, 256%.
- Futures, test period: buy-and-hold ES Sharpe 0.66 (+14.4%), NQ 0.97 (+31.3%); generation 0 -1.21 (-25.4%); generation 10 -0.41 (-7.1%); generation 20 1.03 (+37.4%).
- The authors state that evolution continued to generation 100 on futures but generation 20 "achieved superior out-of-sample performance" and later generations "degraded generalization".

## Signal construction
Not a signal. As a search design: describe each candidate by behavior (turnover, drawdown, holding time, strategy family), keep an archive with one elite per behavior cell, sample parents from across the archive, and migrate between sub-populations.

## Relevance to SOL perpetuals at minutes to hours
The archive is the useful part. A grid over turnover, average holding time and drawdown yields a portfolio of structurally different candidates, and low-turnover cells can be preferred for a venue with wide spreads. The paper itself notes the map can take futures-specific axes such as roll cost; funding paid is the perp equivalent. The futures result argues for stopping rules based on validation performance, not generation count.

## Caveats
Eight instruments, all large US technology stocks or US index futures, in a test period dominated by a rising market; the equity result is hard to separate from beta, and its information ratio (0.69) is below the equal-weight baseline's (0.80). The statement that generation 20 beat later generations out of sample implies the test set was inspected for more than one generation, which is itself selection. I found no count of total strategies evaluated and no multiple-testing adjustment. Daily bars only. The authors work at Qraft Technologies, a commercial firm.
