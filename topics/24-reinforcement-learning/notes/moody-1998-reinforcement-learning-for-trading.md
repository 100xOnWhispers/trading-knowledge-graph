---
title: "Reinforcement Learning for Trading"
authors: "Moody, John; Saffell, Matthew"
year: 1998
venue: "Advances in Neural Information Processing Systems 11 (NIPS 1998)"
url: "https://proceedings.neurips.cc/paper_files/paper/1998/file/4e6cd95227cb0c280e99a195be5f6615-Paper.pdf"
pdf: "sources/24-reinforcement-learning/moody-1998-reinforcement-learning-for-trading.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "24-reinforcement-learning"
asset_class: "equities"
horizon: "multi-day"
tags: "direct-reinforcement, recurrent-rl, differential-sharpe-ratio, q-learning, transaction-costs, reward-design, policy-gradient"
---

## Key insight
This is the founding statement of "direct reinforcement" for trading: train the position-taking function itself by gradient ascent on a financial objective (profit, Sharpe ratio), instead of learning a value function or a price forecast. Because transaction costs make today's reward depend on yesterday's position, the trader must be recurrent, with its previous position as an input. The paper also introduces the differential Sharpe ratio, an incremental risk-adjusted reward that can be computed online. On the authors' test, the direct method beat Q-learning and traded less.

## Method
Position `F_t` in {-1, 0, 1} is a function of learned parameters, the information set and the previous position `F_{t-1}`. Per-period return with cost rate `delta` (additive form): `R_t = mu * [ r_f + F_{t-1} (r_t - r_f) - delta * |F_t - F_{t-1}| ]`.

Differential Sharpe ratio: keep exponential moving estimates of the first and second moments of returns, `A_t = A_{t-1} + eta (R_t - A_{t-1})` and `B_t = B_{t-1} + eta (R_t^2 - B_{t-1})`, expand the Sharpe ratio to first order in `eta`, and use the first-order term as the reward. Equation (4) of the paper did not survive text extraction from the scanned PDF; the form reproduced in Borrageiro et al. (2022), which cites this work, is `D_t = (B_{t-1} dA_t - 0.5 A_{t-1} dB_t) / (B_{t-1} - A_{t-1}^2)^{3/2}`.

Recurrent reinforcement learning (RRL) updates parameters online with `dU_t/dtheta = dU_t/dR_t * (dR_t/dF_t * dF_t/dtheta + dR_t/dF_{t-1} * dF_{t-1}/dtheta)`, computed by real-time recurrent learning. The comparison system ("Qtrader") uses Q-learning with a two-layer network of 30 tanh units; the RRL networks are linear with weight decay 0.01.

## Data and sample
Monthly S&P 500 total return index and 3-month Treasury bills, January 1950 to December 1994, from Citibase. 84 input series (financial and macroeconomic, macro lagged one month). Test period 1970 to 1994, retrained each year on a rolling 20-year window (10 years to fit, 10 years to validate early stopping for RRL). Transaction cost 0.5%.

## Reported results
- Annualized Sharpe ratios over the 25-year test: buy and hold 0.34, Qtrader voting ensemble 0.63, RRL voting ensemble 0.83.
- Ensembles of 30 RRL trials and 10 Qtrader trials with different random initial parameters; both reported as significantly better than buy and hold.
- Qtrader traded much more frequently than RRL and performed worse; the authors state that Q-learning "can suffer from the curse of dimensionality and is more difficult to use".
- Input sensitivities drift over time (yield curve slope in the 1970s, long-rate trends in the 1980s, short-rate trends in the early 1990s), which the authors read as non-stationarity.

## Signal construction
Not a signal. It is a training recipe: (1) feed the previous position into the policy, (2) put the cost term `delta * |F_t - F_{t-1}|` inside the reward, (3) use the differential Sharpe ratio as a per-step reward when a risk-adjusted objective is wanted, (4) retrain on a rolling window, (5) trade the majority vote of an ensemble of differently initialized learners.

## Relevance to SOL perpetuals at minutes to hours
The formulation transfers directly: for a perp, add a funding term `-kappa_t * F_t` to the return (as Borrageiro et al. do) and replace the fixed cost with the observed half-spread plus fees. The differential Sharpe ratio needs one decay parameter `eta`, which sets the effective look-back and should be re-chosen for 1 to 5 minute bars. The empirical result itself (monthly equity index timing with macro inputs) does not transfer.

## Caveats
One instrument, monthly data, 300 test months, a single cost assumption. Results depend on 84 hand-picked inputs. The Q-learning baseline is a 1990s implementation; the ranking of direct versus value-based methods is not settled by this test (Zhang, Zohren and Roberts find DQN ahead on futures). The longer journal version (Moody and Saffell, 2001, IEEE Transactions on Neural Networks) was not opened in this session.
