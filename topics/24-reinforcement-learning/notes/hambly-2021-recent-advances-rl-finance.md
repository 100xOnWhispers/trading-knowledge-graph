---
title: "Recent Advances in Reinforcement Learning in Finance"
authors: "Hambly, Ben; Xu, Renyuan; Yang, Huining"
year: 2021
venue: "arXiv:2112.04553v4"
url: "https://arxiv.org/pdf/2112.04553"
pdf: "sources/24-reinforcement-learning/hambly-2021-recent-advances-rl-finance.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "24-reinforcement-learning"
asset_class: "multi"
horizon: "n/a"
tags: "survey, mdp, q-learning, policy-gradient, actor-critic, optimal-execution, market-making, risk-sensitive-rl, non-stationarity, offline-rl"
---

## Key insight
This 65-page survey is the standard map of RL in finance from the mathematical-finance side. It sets out the theory (Markov decision processes, value-based and policy-based methods, their deep versions, sample-complexity results) and then reviews applications by problem: optimal execution, portfolio optimization, option pricing and hedging, market making, smart order routing and robo-advising. Its framing is that RL trades model misspecification risk (the weakness of stochastic control) for overfitting and sample hunger, and that the productive direction is to embed the structure of the classical models into the learning problem.

## Method
Literature review. Section 2 covers MDPs, temporal-difference learning, Q-learning, SARSA, policy gradient, actor-critic, exploration, regularization and non-stationary RL. Section 3 covers deep value-based and policy-based algorithms. Section 4 takes each financial application in turn: it states the classical model (for execution, the Almgren-Chriss solution; for market making, the Avellaneda-Stoikov family), lists evaluation criteria and benchmarks, and catalogues RL papers by algorithm, state, action and reward. Section 5 lists open directions.

## Data and sample
No original data. The reference list has 271 entries, current to early 2023 (v4).

## Reported results
Findings read in the survey:
- Execution: the closed-form Almgren-Chriss schedule is pre-planned and ignores real-time market conditions; this is the stated motivation for RL. Q-learning and (double) DQN are the most used methods, followed by policy gradient, A2C and PPO. Standard benchmarks are TWAP, VWAP and submit-and-leave; standard criteria are P&L, implementation shortfall and Sharpe ratio, with the differential Sharpe ratio and Sortino ratio as variants.
- General RL algorithms "tend to overfit, using more information than is actually required for a particular application".
- Most RL algorithms need more samples than relevant history provides, and older data may not help because financial series are non-stationary; hence the interest in sample-efficient methods and in market simulators.
- Online parameter updates are impractical at high frequency; the plausible workflow is to collect data with a fixed exploration scheme during trading and update offline afterwards, which links to batch (offline) RL. The authors note these methods had not been tailored to finance.
- Exploration is costly in live markets and hard to justify institutionally.
- Risk-sensitive RL (utility-based, CVaR-constrained, dynamic risk measures) is identified as necessary and immature; several cited algorithms lack convergence or sample-complexity guarantees.
- The authors state they know of no financial study of transferring a trained RL strategy to a similar asset with fewer samples, and they pose cold start for newly issued assets with limited data as a separate open question.

## Signal construction
Not a signal. Use it as the reference for formulating each sub-problem: which state variables, action sets, rewards and benchmarks the literature has used for execution and market making, and which classical solution to compare an RL policy against.

## Relevance to SOL perpetuals at minutes to hours
The cold-start and transfer questions the survey flags as open are exactly this project's situation: a new contract on a new venue with little history, and abundant history on the same underlying elsewhere. The survey's advice implies a concrete design: learn the directional component on Binance or Bybit SOL perp data, and treat Kalshi-specific execution as a separate small problem with a classical baseline (TWAP or immediate crossing). The survey contains little on crypto, on perpetual funding, or on directional intraday trading as such; those are covered by other notes.

## Caveats
Coverage of empirical performance is descriptive: papers are catalogued by method, not audited for out-of-sample validity, costs or reproducibility, so the survey should not be read as evidence that the listed methods are profitable. Strongest on execution, market making and hedging; weakest on alpha generation. Literature cutoff early 2023.
