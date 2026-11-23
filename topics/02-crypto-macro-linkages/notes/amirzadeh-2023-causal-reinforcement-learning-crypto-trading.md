---
title: "A Framework for Empowering Reinforcement Learning Agents with Causal Analysis: Enhancing Automated Cryptocurrency Trading"
authors: "Amirzadeh, Rasoul; Thiruvady, Dhananjay; Nazari, Asef; Ee, Mong Shan"
year: 2023
venue: "arXiv 2310.09462 (v2, August 2024); journal publication not confirmed"
url: "https://arxiv.org/pdf/2310.09462"
pdf: "sources/02-crypto-macro-linkages/amirzadeh-2023-causal-reinforcement-learning-crypto-trading.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "02-crypto-macro-linkages"
asset_class: "crypto"
horizon: "daily"
tags: "reinforcement-learning, ppo, ddpg, bayesian-network, feature-selection, macro-features, altcoins"
---

## Key insight
A reinforcement-learning trading framework for altcoins in which Bayesian networks choose the input features per coin from four candidate groups, one of which contains macro-financial series (gold, the US dollar index, S&P 500, MSCI and WTI oil) plus tweet counts. The selection step picked the macro-financial group for only one of five coins (Litecoin); for the others price-volume data or technical indicators were preferred. The resulting agents beat buy-and-hold over a falling test period but with return dispersion across runs larger than the mean.

## Method
"CausalReinforceNet": 
1. Feature engineering with static Bayesian networks, which score four feature groups for predicting daily price direction: OHLCV only; OHLCV plus technical indicators (AD, Bollinger bands, EMA, MACD, NATR, OBV, RSI, SMA, stochastic); OHLCV plus the five traditional assets and daily tweet count; all combined.
2. A dynamic Bayesian network uses the last five days of the selected features to output probabilities of an up or down close, which are added to the agent's observations and also drive position-size rules (for example 75 percent of balance when the up probability is 80 percent).
3. Two agents, PPO and DDPG, with return-on-investment and Sharpe-based reward terms, compared with buy-and-hold and with baseline RL agents lacking the Bayesian components. Transaction cost 0.1 percent of position size per trade.

## Data and sample
Daily data January 2018 to April 2023 from Yahoo Finance for Binance Coin, Ethereum, Litecoin, Ripple and Tether and for the traditional assets; tweet counts from bitinfocharts.com. Split into training and test periods; the exact split dates were not transcribed.

## Reported results
- Feature selection: Binance Coin and Ripple use OHLCV plus technical indicators; Ethereum and Tether use OHLCV only; Litecoin uses OHLCV, tweet counts and the financial factors.
- Test-period return on investment, mean with standard deviation across runs in parentheses. PPO agent: Binance Coin 12.93 (30.34), Ethereum 8.19 (44.56), Litecoin 5.13 (26.06), Ripple -2.13 (15.80), Tether -4.54 (0.18); average 3.92. DDPG agent: 14.59, 10.46, -0.74, -2.04, -2.26; average 4.00. Buy-and-hold: 5.92, -14.40, -25.18, -23.36, 0.06; average -11.39.
- Annualized return for the PPO agent on Binance Coin is 7.35 percent against 2.63 percent for the baseline PPO agent without the Bayesian components; for the DDPG agent 8.30 percent against 3.20 percent.

## Signal construction
The reusable piece is the pipeline, not the trained agent: (a) run a feature-group selection step per instrument that is allowed to reject macro inputs; (b) feed a calibrated up/down probability from a simple probabilistic model into the RL state rather than raw macro series; (c) tie position size to that probability. For macro inputs specifically, the candidates here are daily changes in gold, the dollar index, S&P 500, MSCI and WTI.

## Relevance to SOL perpetuals at minutes to hours
This is the reinforcement-learning entry for this topic. It gives weak but relevant evidence that, at daily frequency, a data-driven selector seldom chooses macro-financial series over the coin's own price and volume history, in line with the gradient-boosting evidence in the Dudek note. It does not test SOL, intraday horizons, perpetuals, funding or leverage, and the long-only spot setting with fractional position sizing differs from a directional perpetuals bot. An RL design for SOL should treat macro variables as optional context to be validated by ablation, not as assumed inputs.

## Caveats
Standard deviations across runs are two to five times the mean returns, so the ranking of agents is not statistically established. A single test window in a falling market flatters any strategy that holds cash part of the time; outperformance of buy-and-hold is not evidence of skill. Trading Tether, a stablecoin, as a directional asset is of doubtful meaning. Five coins, daily bars, one train-test split, no walk-forward. The "causal" label refers to Bayesian network structure, not to identified causal effects. No search could be run for stronger RL or evolutionary studies using macro inputs (see the topic synthesis).
