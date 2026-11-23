---
title: "Multi-level deep Q-networks for Bitcoin trading strategies"
authors: "Sattarov, Otabek; Choi, Jaeyoung"
year: 2024
venue: "Scientific Reports 14:771"
url: "https://www.nature.com/articles/s41598-024-51408-w.pdf"
pdf: "sources/18-positioning-sentiment/sattarov-2024-multi-level-dqn-bitcoin-sentiment.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "18-positioning-sentiment"
asset_class: "crypto"
horizon: "hours"
tags: "reinforcement-learning, dqn, twitter-sentiment, vader, reward-shaping, hourly, bitcoin"
---

## Key insight
A stacked reinforcement-learning design, in which two small DQNs first turn (a) price history and (b) price plus Twitter sentiment into a trade recommendation and a predicted price change, and a third DQN trades on those two outputs, reports up to a 29.93% return and a Sharpe ratio up to 2.74 on hourly Bitcoin (from two different parameter settings). The evidence is weak: the test set is 30 days. The paper is useful mainly as a worked example of how sentiment can enter an RL state and how reward shaping drives trade frequency.

## Method
Three DQNs:
1. Trade-DQN: state is the hourly Bitcoin price; actions are buy, hold, sell; reward is realized profit on sell, with a penalty of -1 after 20 consecutive holds.
2. Predictive-DQN: state is `[price_t, sentiment_t]`, where sentiment is a VADER compound score of Bitcoin tweets; output is a predicted percentage price change in [-100, 100].
3. Main-DQN: state is the pair `[x1, x2]` of the Trade-DQN recommendation and the Predictive-DQN predicted change; actions are buy, hold, sell.
The Main-DQN reward combines realized profit net of transaction fees, a penalty when a risk measure exceeds a threshold alpha (30%, 55% or 80%), and a penalty tied to an active-trading threshold omega (up to 8, 16 or 24 trades per day). A "classic" variant feeds raw data without the two preprocessing DQNs. Comparisons are made against two reward functions from earlier papers and against results reported by other studies.

## Data and sample
Hourly Bitcoin closing prices, 1 October 2014 to 1 March 2019 (stated source offers free historical data; name not confirmed here). Over seven million Bitcoin tweets collected through the Twitter streaming API, 1 April 2014 to 14 November 2018, scored with VADER. Training: 1 October 2014 to 14 October 2018. Test: the following 30 days (720 hours).

## Reported results
- Risk threshold 55%, up to 16 trades per day: ROI 29.9% for the proposed method against 23.5% for the classic variant, with Sharpe 2.39.
- Risk threshold 30%: proposed ROI 14.6% against classic 12.8%; maximum Sharpe 2.74 for the proposed method against 2.63 for classic.
- The abstract's "29.93% and Sharpe above 2.7" therefore pairs the best ROI and the best Sharpe from two different settings.
- In the comparison with other published models the authors rank first on Sharpe and second on ROI (another study is cited at 57.5% ROI); those studies used different data and periods.
- Risk threshold 80%: proposed 28.1% against classic 24.1%; Sharpe 1.88 against 1.58. Higher permitted risk did not yield higher profit.
- The Predictive-DQN is reported to reach 86.13% accuracy on its prediction task.
- The authors list as limitations: reliance on Twitter alone, a reward that "may overlook" transaction costs, slippage, liquidity and price impact, and Bitcoin-only scope.

## Signal construction
Inputs: hourly price, hourly mean sentiment score of asset-related posts. Train a price-only policy and a price-plus-sentiment predictor separately; feed their two outputs as a compact two-dimensional state to a final policy with actions buy, hold, sell. Reward = realized profit minus fees, minus a drawdown-style risk penalty, minus an inactivity or over-activity penalty. Parameters: risk threshold, trade-count threshold, discount factor. Hourly decision frequency.

## Relevance to SOL perpetuals at minutes to hours
The hourly decision interval matches the target horizon, and the two-stage structure (compress sentiment into a predicted move before the policy sees it) is a sensible way to keep an RL state small. Nothing about performance transfers. A perp version would need short actions, funding in the reward, realistic taker fees and slippage, and walk-forward testing over many months. Rewarding trade count is a design choice that manufactures turnover and should not be copied without a cost model.

## Caveats
One 30-day test window (mid-October to mid-November 2018); a Sharpe ratio from 720 hourly points in a single market state is not informative. No walk-forward, no multiple seeds reported in the text read, no buy-and-hold comparison located. The sentiment contribution is not isolated by ablation: "classic" versus "proposed" changes the whole preprocessing stack. Treatment of costs is inconsistent between the reward description and the limitations section. See the topic 16 note on Gort et al. (2022) for why single-split RL backtests overstate performance.
