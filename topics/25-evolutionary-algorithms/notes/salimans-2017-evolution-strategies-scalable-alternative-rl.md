---
title: "Evolution Strategies as a Scalable Alternative to Reinforcement Learning"
authors: "Salimans, Tim; Ho, Jonathan; Chen, Xi; Sidor, Szymon; Sutskever, Ilya"
year: 2017
venue: "arXiv preprint 1703.03864v2 (OpenAI)"
url: "https://arxiv.org/pdf/1703.03864"
pdf: "sources/25-evolutionary-algorithms/salimans-2017-evolution-strategies-scalable-alternative-rl.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "25-evolutionary-algorithms"
asset_class: "multi"
horizon: "n/a"
tags: "evolution-strategies, neuroevolution, black-box-optimization, policy-search, parallelism, fitness-shaping"
---

## Key insight
A neural-network policy can be trained by perturbing its weights with Gaussian noise, scoring each perturbed copy on whole episodes, and moving the weights toward the perturbations that scored well. No gradients through the policy, no value function and no reward discounting are needed. The method matched standard deep reinforcement learning on Atari and MuJoCo benchmarks while parallelizing almost linearly across more than a thousand CPU cores. There is no finance in the paper; it is the reference for neuroevolution of trading agents.

## Method
With policy weights theta, noise scale sigma, learning rate alpha and n workers:

1. Each worker draws epsilon_i ~ N(0, I) and evaluates the return F_i of the policy with weights theta + sigma * epsilon_i over a full episode.
2. Update theta <- theta + alpha * (1 / (n * sigma)) * sum_i F_i * epsilon_i.

This is a randomized finite-difference estimate of the gradient of a Gaussian-smoothed objective, so the objective itself may be discontinuous. Practical details that the authors found necessary: antithetic (mirrored) sampling, evaluating both +epsilon and -epsilon; fitness shaping by replacing returns with their ranks, which removes the influence of outlier episodes; weight decay; a fixed sigma; and virtual batch normalization of the policy, without which the method "proved brittle". Workers share random seeds and exchange only scalar returns, which is why communication cost stays negligible.

## Data and sample
Simulated control (MuJoCo) and Atari 2600 games. No market data.

## Reported results
- 3D humanoid walking solved in under 10 minutes with 1,440 workers.
- Atari: about one hour per game on 720 CPUs; better than published one-day A3C results on 23 games and worse on 28.
- Data efficiency: matching A3C took between 3x and 10x as much data; matching TRPO on MuJoCo took no more than 10x. Computation per sample is roughly 3x lower because there is no backpropagation.
- Stated advantages: invariance to action frequency, tolerance of delayed rewards and very long horizons, and more varied exploration than policy gradients.

## Signal construction
Not a signal. It is an optimizer for a trading policy or for any non-differentiable objective. In a trading setting F_i would be a net-of-cost performance measure of the perturbed policy over a sampled block of history, and rank shaping would stop one lucky block from dominating the update.

## Relevance to SOL perpetuals at minutes to hours
Three properties fit the problem: the objective can be Sharpe, drawdown-penalized return or any other episode-level statistic that has no usable gradient; rewards that arrive only when a position closes are handled naturally; and the action frequency does not need tuning. The cost is 3x to 10x more data than gradient methods in simulators that can generate unlimited fresh episodes. A market offers one fixed history, so every extra evaluation is a re-use of the same sample and adds to overfitting rather than to learning. No test on market data appears in this paper, and I found none of comparable quality for crypto.

## Caveats
Benchmarks are deterministic or near-deterministic simulators with high signal-to-noise fitness; trading fitness is dominated by noise. Results depend on reparameterization tricks. Reinforcement-learning methods for trading are covered in topic 24.
