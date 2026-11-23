---
title: "Model-based Reinforcement Learning for Predictions and Control for Limit Order Books"
authors: "Wei, Haoran; Wang, Yuanbo; Mangu, Lidia; Decker, Keith"
year: 2019
venue: "arXiv:1910.03743 (AAAI-formatted preprint; publication venue not confirmed)"
url: "https://arxiv.org/abs/1910.03743"
pdf: "sources/31-rl-evolutionary-second-pass/wei-2019-model-based-rl-limit-order-books.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "31-rl-evolutionary-second-pass"
asset_class: "equities"
horizon: "seconds"
tags: "model-based-rl, world-model, order-book, autoencoder, mixture-density-network, simulator, single-history"
---

## Key insight
A learned "world model" of the order book (autoencoder for the state, recurrent mixture-density network for the transition) can serve as the training environment for an RL trader, and a policy trained only inside that model kept positive performance when replayed on held-out real data. This is the model-based answer to the single-history problem: sample many synthetic continuations from a generative model fitted to the one history. The evidence that it works is thin and comes from one stock over a few test days.

## Method
- State: a latent vector from a convolutional autoencoder applied to a window of order book snapshots, plus recent trade prints and the agent's position.
- Transition model: an RNN whose output parameterizes a mixture density network, so the next latent state is sampled from a mixture distribution conditioned on the current state and the agent's action. The authors say this lets the model represent the impact of the agent's trades.
- Reward model: predicts reward from state and action; a sigmoid transform is applied to rewards inside the model during training only.
- Agents: Double DQN, policy gradient and A2C, trained entirely by rollouts in the world model.
- Benchmarks: a momentum rule, a supervised classifier of mid-price direction converted to trades, and a greedy-optimal path found by search over 21 discrete actions.

## Data and sample
One stock on the Hong Kong Stock Exchange (not named), order book plus trades, updates about every 0.17 seconds. January to March 2018 (61 days) for training with 20% validation, April 2018 (19 days) for testing. About 6 million training and 2 million test transitions.

## Reported results
- On four randomly picked April days, each a window of about 0.56 hours, the RL agent was "very close to the greedy-optimal solution" and beat the average of the two benchmarks by about 10% to 30%.
- A2C was more stable than policy gradient and DQN.
- The classifier-based agent did worst; the authors attribute this to the classifier predicting "no change" most of the time.
- On five random days the cumulative reward of the same policy in the world model and in real replay was similar (shown as a figure).
- Transaction fee is stated as "2% of PnL per quantity unit".

## Signal construction
Not a signal. The component of interest is the generative transition model: `z_{t+1} ~ MDN(RNN(z_t, a_t))`. For the bot it would be a way to generate alternative SOL paths for stress-testing a policy, to be validated against realism metrics before use (see [nagy-2025-lob-bench](nagy-2025-lob-bench-generative-order-book-benchmark.md)).

## Relevance to SOL perpetuals at minutes to hours
The idea transfers; the evidence does not. A world model fitted to one history can only resample what that history contains, and a policy can learn to exploit the model's errors rather than the market. Any SOL use would need a check that policies ranked well in the model also rank well on held-out real data, across many policies, which this paper does not do.

## Caveats
One instrument, test windows of about half an hour on four or five hand-sampled days, no confidence intervals, an unusual fee definition, no spread or queue modelling described. The "impact" learned from observational data is not identified, because the logged data contain no actions by the agent. Industry-affiliated authors; no code located in this session.
