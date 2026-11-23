---
title: "FinRL Contests: Benchmarking Data-driven Financial Reinforcement Learning Agents"
authors: "Wang, Keyi; Holzer, Nikolaus; Xia, Ziyi; Cao, Yupeng; Gao, Jiechao; Walid, Anwar; Xiao, Kairong; Liu Yanglet, Xiao-Yang"
year: 2025
venue: "arXiv:2504.02281 (v4, July 2025; journal-formatted, venue not confirmed)"
url: "https://arxiv.org/abs/2504.02281"
pdf: "sources/31-rl-evolutionary-second-pass/wang-2025-finrl-contests-benchmarking-rl-agents.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "31-rl-evolutionary-second-pass"
asset_class: "multi"
horizon: "seconds"
tags: "reinforcement-learning, contest, benchmark, held-out-test, bitcoin, order-book, ensemble, gpu-environment"
---

## Key insight
Three years of open contests (2023 to 2025; 46, 21 and 85 teams) scored RL trading agents on data withheld from participants. On the second-level Bitcoin task the winning entries finished within a quarter of a percent of zero over a test window of about two and a half days; they "beat" Bitcoin only because Bitcoin fell 7% in that window. This is the closest thing in the literature to many independent teams being scored on the same held-out crypto data, and it shows no demonstrated edge.

## Method
- Tasks are Markov decision processes with gym-style environments. Starter kits include GPU-vectorized environments (PyTorch `vmap`, up to 2,048 parallel sub-environments) and ensemble baselines.
- Crypto task: one asset (BTC), second-level order book data; 101 formulaic alphas adapted to book data and compressed by an RNN into 8 features; DQN-family agents with discrete actions; ensembles by majority vote.
- Protocol: released data for training and validation, a withheld out-of-sample set for scoring, no retraining during evaluation.
- Organizers describe two standing problems: "policy instability" (sensitivity to seeds, hyperparameters and noise) and the lack of standard tasks and baselines.

## Data and sample
Crypto: BTC second-level book from 2021-04-07 11:32:42 to 2021-04-19 09:54:22. Contest split: train to 2021-04-17 00:38:02, test from then to 2021-04-19 09:54:22. Stock tasks use 30 Dow Jones or Nasdaq-100 names, daily or minute bars. Stock-task cost is 0.1% per trade; the cost used in the crypto task was not found in the parts read.

## Reported results
- Crypto contest winners: Fermion (2024) cumulative return 0.23%, Sharpe 0.0037, maximum drawdown -0.28%. Mt.Everest (2025) -0.05%, -0.0008, -1.23%. BTC price over the test: -7.35%, drawdown -17.02%.
- Organizers' own experiment on a 45-minute test slice: all three ensembles returned 0.66%, Double and Dueling DQN 0.48%, DQN 0.34%, a fixed-time exit rule -0.1%, BTC itself 0.74%. Ensembles of 3, 9 and 30 agents gave identical results; the authors say the agents' policies "may be converging" in the small action space.
- Stock contest 2023 (test 2023-10-25 to 2023-11-14 for the first period): winning teams had better drawdown but "poorer profitability compared with the Dow Jones Index".
- Two result tables carry notes that a team's Sharpe or Rachev ratio "was reported wrongly".
- A cited five-minute, ten-coin study had its best agent at -34.96% against -50.78% for a crypto index.

## Signal construction
Not a signal. Useful as (1) a public second-level BTC book dataset and vectorized environment for smoke-testing a pipeline, and (2) a template for a blind test: freeze the model, score once on data nobody on the project has looked at.

## Relevance to SOL perpetuals at minutes to hours
The contest design is the right one for the bot's own acceptance test. The contest evidence itself is too short to say anything about minutes-to-hours trading: two and a half days is one regime. No funding, shorting cost or liquidation appears in the environment description read.

## Caveats
Test windows of 45 minutes and about 2.4 days cannot separate skill from noise, and the contest Sharpe ratios (0.0037, -0.0008) are evidently not annualized. Winners are selected from many entrants on that same window, so even the 0.23% is upward-biased. Reported metrics include acknowledged errors. The organizers maintain the FinRL software that the contests promote. Author order in the front matter was reconstructed from a multi-column title page and may be imperfect.
