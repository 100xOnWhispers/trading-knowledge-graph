---
title: "Deep Reinforcement Learning that Matters"
authors: "Henderson, Peter; Islam, Riashat; Bachman, Philip; Pineau, Joelle; Precup, Doina; Meger, David"
year: 2017
venue: "arXiv:1709.06560v3 (AAAI 2018)"
url: "https://arxiv.org/pdf/1709.06560"
pdf: "sources/24-reinforcement-learning/henderson-2017-deep-reinforcement-learning-that-matters.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "24-reinforcement-learning"
asset_class: "multi"
horizon: "n/a"
tags: "reproducibility, random-seeds, hyperparameters, significance-testing, policy-gradient, evaluation-methodology"
---

## Key insight
Deep RL results are far less stable than their learning curves suggest. With identical code and hyperparameters, two groups of five random seeds can produce statistically different performance; network architecture, activation function, reward scale and the choice of codebase each change results by amounts comparable to the gaps between published algorithms. Any trading claim of the form "algorithm X beat algorithm Y in one backtest" inherits this problem, with a far noisier environment than the physics simulators studied here.

## Method
Controlled experiments on policy-gradient methods for continuous control (TRPO, DDPG, PPO, ACKTR) in OpenAI Gym MuJoCo tasks such as HalfCheetah, Hopper and Walker2d. One factor is varied at a time: hyperparameters, network structure and activations, reward scaling, random seeds and number of trials, environment, and codebase. The authors then apply significance measures to algorithm comparisons: two-sample t-test, Kolmogorov-Smirnov test, and bootstrap confidence intervals with power analysis.

## Data and sample
Simulated robotics benchmarks, not markets. Most experiments use five trials per configuration with a fixed set of seeds; the seed experiment uses ten.

## Reported results
- Seed experiment: ten TRPO runs on HalfCheetah with the same hyperparameters, split into two sets of five. The two averaged learning curves differ, with a two-sample t-test of t = -9.09, p = 0.0016. Variation from seeds alone is "enough to create statistically different distributions".
- The authors note that published work often reports the top N trials or averages fewer than five.
- Example of a non-significant "win": ACKTR versus DDPG on Walker2d, t = 1.03, p = 0.334, bootstrapped percent difference 44.47% with a 95% interval of -80.62% to 111.72%.
- Reward scaling, network architecture and different implementations of the same algorithm each shift results materially.
- Recommendations: run many seeds, report all hyperparameters and implementation details, match baseline implementations to their original reported performance, and apply significance tests before claiming improvement.

## Signal construction
Not a signal. It sets the evaluation protocol for any RL component of the bot:
1. Train every configuration with many seeds (the paper gives no fixed number; power analysis on the observed variance decides).
2. Report the distribution of out-of-sample results across seeds, never the best run.
3. Compare two configurations with a bootstrap interval on the difference.
4. Treat reward scale and normalization as hyperparameters that can decide the outcome.

## Relevance to SOL perpetuals at minutes to hours
Transfers completely as methodology. In trading, seed variance is compounded by a low signal-to-noise environment and short test windows, so the bar is higher than in this paper. Borrageiro et al. (information ratio 0.22 to 1.76 across 250 random initializations of the same crypto agent) and Ardaiz et al. (11 of 100 execution agents collapsing to never trading) show the same effect in crypto. A practical rule for this project: an RL policy change is accepted only if the improvement survives across seeds and across walk-forward windows.

## Caveats
No financial data. Benchmarks are deterministic simulators, which understates the variance a trading agent faces. Covers policy-gradient methods only. Published 2017 to 2018; libraries have since stabilized, but the seed-variance finding has been repeated in later work.
