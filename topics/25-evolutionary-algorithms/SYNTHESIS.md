# Topic 25: Evolutionary algorithms and automated strategy discovery

Scope: genetic algorithms and genetic programming for trading rules, formulaic alpha mining (evolutionary, reinforcement-learning and LLM-driven), evolution strategies, multi-objective and quality-diversity search, and the overfitting controls specific to search. Fifteen notes. General reinforcement learning is topic 24 and general overfitting statistics are topic 26.

A note on coverage: the session's web-search budget was exhausted before this topic started, so sources were found from known addresses, from reference lists, and by browsing arXiv's monthly q-fin listings for 2023 to 2026. Gaps are listed at the end.

## What the literature agrees on

**Search finds in-sample structure easily, and most of it does not survive costs out of sample.** The founding study found rules that beat buy-and-hold on one test window and, by its own abstract, not on others ([allen-1999](notes/allen-1999-genetic-algorithms-technical-trading-rules.md)). At half-hour frequency in currencies, genetic programming found stable predictability worth over 100% a year before costs and nothing after realistic costs ([neely-2003 in topic 11](../11-intraday-seasonality-tradfi/notes/neely-2003-intraday-technical-trading-fx-genetic.md)). A 2026 benchmark of nine modern miners found that training IC "generally does not recover in testing" ([wang-2026](notes/wang-2026-factorbench-automated-factor-mining-benchmark.md)). A 2026 audit found that no LLM-discovered strategy could be distinguished from luck once every trial was counted ([gencay-2026](notes/gencay-2026-honest-evaluation-llm-strategy-discovery.md)).

**Turnover is where evolved rules die.** Left alone, search selects rules that trade often. Break-even one-way costs were 0.18% for daily equity rules ([allen-1999](notes/allen-1999-genetic-algorithms-technical-trading-rules.md)) and at most about one basis point for intraday currency rules trained without costs. A crypto post-mortem reports models that predicted 5 basis point moves against an 8 basis point round-trip fee ([chen-2025](notes/chen-2025-red-queen-deep-evolution-crypto-hft.md)).

**The same small set of protections recurs across thirty years.**
- Three windows: one drives the search, one chooses what to keep, one is opened once ([allen-1999](notes/allen-1999-genetic-algorithms-technical-trading-rules.md), [neely-1997](notes/neely-1997-genetic-programming-fx-technical-analysis.md)).
- Costs inside the fitness function, set above the real cost ([neely-1997](notes/neely-1997-genetic-programming-fx-technical-analysis.md)).
- Limits on complexity: node and depth caps, depth-by-depth construction ([zhang-2020](notes/zhang-2020-autoalpha-hierarchical-evolutionary-alpha-mining.md)), a cap on tunable constants ([kvasiuk-2026](notes/kvasiuk-2026-madevolve-llm-evolution-bitcoin-trading.md)).
- Stationary inputs, for example price divided by its moving average.
- A language that cannot express look-ahead ([huang-2026](notes/huang-2026-constrained-llm-agents-crypto-factors.md), [gencay-2026](notes/gencay-2026-honest-evaluation-llm-strategy-discovery.md)).

**Picking the single best candidate is unreliable; aggregating many is better.** The rule ranked first in the selection period was among the four worst of 100 out of sample, while a majority vote of all 100 was profitable in every currency ([neely-1997](notes/neely-1997-genetic-programming-fx-technical-analysis.md)). Genetic programming's test IC varied across random seeds by as much as its mean ([yu-2023](notes/yu-2023-alphagen-synergistic-formulaic-alphas-rl.md)). On index futures, generation 20 beat generation 100 out of sample ([yun-2025](notes/yun-2025-quantevolve-quality-diversity-strategy-evolution.md)).

**Populations collapse onto one idea unless diversity is enforced.** Plain genetic programming kept returning variants of `vwap/close` ([zhang-2020](notes/zhang-2020-autoalpha-hierarchical-evolutionary-alpha-mining.md)); three of five independent LLM searches produced nearly the same strategy ([gencay-2026](notes/gencay-2026-honest-evaluation-llm-strategy-discovery.md)); 500 "diverse" crypto agents ended in the same leveraged long ([chen-2025](notes/chen-2025-red-queen-deep-evolution-crypto-hft.md)). The remedies are similarity penalties, correlation cutoffs, parent-only replacement, islands, and behavior archives.

**Simple baselines are hard to beat.** A fitted autoregression did at least as well as genetic programming intraday (Neely and Weller). Alpha101 was competitive with every mined pool ([wang-2026](notes/wang-2026-factorbench-automated-factor-mining-benchmark.md)). A plain agent loop was not clearly worse than an evolutionary scaffold ([kvasiuk-2026](notes/kvasiuk-2026-madevolve-llm-evolution-bitcoin-trading.md)).

**Edges that are real decay.** The 1997 currency rules were re-run a decade later: three of six portfolios had turned negative ([neely-1997](notes/neely-1997-genetic-programming-fx-technical-analysis.md), [neely-2009 in topic 16](../16-oscillators-technical-rules/notes/neely-2009-adaptive-markets-foreign-exchange.md)).

## Where it disagrees or is weak

**Does a better search algorithm find better signals?** Each method paper says yes against its chosen baseline: AutoAlpha over `gplearn`, AlphaEvolve over a genetic algorithm, AlphaGen over `gplearn` again. The independent benchmark says there is no consistent ordering from genetic programming through reinforcement learning to LLM agents, and it measured AlphaGen's composite rank IC as negative on 2024 to 2025 data ([wang-2026](notes/wang-2026-factorbench-automated-factor-mining-benchmark.md)). I weight the benchmark more heavily because it did not design any of the methods.

**Are LLM-evolved strategies real?** [kvasiuk-2026](notes/kvasiuk-2026-madevolve-llm-evolution-bitcoin-trading.md) and [huang-2026](notes/huang-2026-constrained-llm-agents-crypto-factors.md) report gains that hold on later data. [gencay-2026](notes/gencay-2026-honest-evaluation-llm-strategy-discovery.md) certifies none. The difference is in the evaluation, not the search: the positive papers use a held-out period without deflating for trial count, and one relies on a fill model its authors call unrealistic.

**Correlation filters.** AutoAlpha and AlphaEvolve discard candidates correlated with accepted ones. AlphaGen shows a pool of mutually correlated formulas combining well and argues for scoring marginal contribution instead. Unresolved; it likely depends on how the signals are combined.

**Which objective.** Sharpe ratio, net PnL with an impact penalty, IC, and multi-objective fronts are all in use. MadEvolve avoids Sharpe because it rewards trading rarely; the multi-objective route ([deb-2002](notes/deb-2002-nsga-ii-multiobjective-genetic-algorithm.md)) has no rigorous trading evidence in what I read.

**Crypto and intraday evidence is thin.** The only minute-bar crypto studies here are a proof of concept on aggregated prices with generous fills ([kvasiuk-2026](notes/kvasiuk-2026-madevolve-llm-evolution-bitcoin-trading.md)) and a 4.5-hour failure report ([chen-2025](notes/chen-2025-red-queen-deep-evolution-crypto-hft.md)). Notes in other topics add a genetic algorithm that re-tunes a five-minute crypto strategy monthly ([tian-2025](../08-trade-flow-toxicity/notes/tian-2025-genetic-algorithm-crypto-strategy-optimization.md), graded C there), an artificial-market study of Bitcoin ([manahov-2021](../08-trade-flow-toxicity/notes/manahov-2021-efficiency-bitcoin-genetic-programming.md)) and evolved order-book rules in currencies that stopped working between 2003 and 2008 ([funie-2014](../07-order-book-imbalance/notes/funie-2014-genetic-programming-swarm-hft-rules.md)). No study combines perpetual futures, realistic fills, and trial accounting.

**Reported performance in the alpha-mining papers is not credible as stated.** Test Sharpe ratios of 3.4 ([zhang-2020](notes/zhang-2020-autoalpha-hierarchical-evolutionary-alpha-mining.md)) and 21 ([cui-2021](notes/cui-2021-alphaevolve-evolving-novel-alphas.md)) come from short windows with thin or no costs, and AlphaEvolve normalizes features with full-sample maxima.

**Neuroevolution has no trading evidence here.** Evolution strategies are well established as an optimizer ([salimans-2017](notes/salimans-2017-evolution-strategies-scalable-alternative-rl.md)) but need 3 to 10 times more data than gradient methods, and a market offers one history.

## Candidate signals and methods

Nothing in this topic is a ready signal. The table lists methods for a search and evaluation pipeline.

| Name | Inputs | Horizon | Evidence grade | Source notes |
|---|---|---|---|---|
| Three-window rule search (train / select / test) with net-of-cost fitness | Normalized price bars, funding as carry term | Any; tested daily | A | [allen-1999](notes/allen-1999-genetic-algorithms-technical-trading-rules.md), [neely-1997](notes/neely-1997-genetic-programming-fx-technical-analysis.md) |
| Majority vote or equal weight over many independent evolutions | Outputs of N search runs | Any; tested daily | A | [neely-1997](notes/neely-1997-genetic-programming-fx-technical-analysis.md) |
| Training cost set above live cost to suppress turnover | Fee and spread model | Any | B | [neely-1997](notes/neely-1997-genetic-programming-fx-technical-analysis.md) |
| Alpha101 operator grammar, rewritten for one instrument (rolling rank in place of cross-sectional rank) | OHLCV, VWAP, plus funding, open interest, basis | Bar-level, any size | C | [kakushadze-2016](notes/kakushadze-2016-101-formulaic-alphas.md) |
| Diversity-preserving genetic programming (depth-wise build, similarity penalty, warm start, parent-only replacement) | Operator grammar, forward-return target | Any; tested daily | C | [zhang-2020](notes/zhang-2020-autoalpha-hierarchical-evolutionary-alpha-mining.md) |
| Marginal-contribution fitness: score a candidate by the gain it adds to a regularized combination | Existing signal pool | Any; tested 20-day | B | [yu-2023](notes/yu-2023-alphagen-synergistic-formulaic-alphas-rl.md), [wang-2026](notes/wang-2026-factorbench-automated-factor-mining-benchmark.md) |
| Seeded search with pruning and fingerprint de-duplication | Hand-built seed signals | Any; tested daily | C | [cui-2021](notes/cui-2021-alphaevolve-evolving-novel-alphas.md) |
| Evolution strategies for policy or parameter vectors (mirrored sampling, rank shaping) | Any episode-level net performance measure | Any | B for the optimizer, none for trading | [salimans-2017](notes/salimans-2017-evolution-strategies-scalable-alternative-rl.md) |
| Multi-objective parameter search (return, drawdown, turnover; hard constraints) | Strategy parameters, backtester | Any | A for the algorithm, D for trading use | [deb-2002](notes/deb-2002-nsga-ii-multiobjective-genetic-algorithm.md), [freqtrade-2026](notes/freqtrade-2026-hyperopt-nsga3-strategy-optimization.md) |
| Behavior archive (one elite per turnover / holding-time / drawdown cell) with islands | Strategy code or rules | Daily and minute bars tested | C | [yun-2025](notes/yun-2025-quantevolve-quality-diversity-strategy-evolution.md), [kvasiuk-2026](notes/kvasiuk-2026-madevolve-llm-evolution-bitcoin-trading.md) |
| Evolving execution and sizing code with a cap on tunable constants | Forecast, minute bars, fill simulator | Minutes | C | [kvasiuk-2026](notes/kvasiuk-2026-madevolve-llm-evolution-bitcoin-trading.md) |
| Constrained formula language, gates fixed before search, append-only trace | Point-in-time features | Any; tested daily | C | [huang-2026](notes/huang-2026-constrained-llm-agents-crypto-factors.md) |
| Trial ledger with deflated acceptance threshold and a once-opened held-out window | Log of every backtest | Any | B | [gencay-2026](notes/gencay-2026-honest-evaluation-llm-strategy-discovery.md) |
| Residual test: keep a mined signal only if it predicts after regressing on simple known predictors | Lagged return, volatility, order-flow imbalance, funding, BTC return | Any | B | [wang-2026](notes/wang-2026-factorbench-automated-factor-mining-benchmark.md) |
| Pre-search fee check: expected move per signal against round-trip cost; break-even hit rate | Fee schedule, spread, forecast magnitude | Minutes | D | [chen-2025](notes/chen-2025-red-queen-deep-evolution-crypto-hft.md) |

## Open questions worth testing on SOL perps

1. **Does evolved structure beat a linear baseline?** Run genetic programming on 5-minute and 15-minute SOL bars and compare, out of sample and net of costs, with an autoregression plus a no-trade band. In currencies the linear model matched or beat the evolved rules.
2. **How much does inflating the training cost help?** Train at 1x, 2x and 3x the live Kalshi cost and compare out-of-sample net return and turnover.
3. **Vote or pick?** Compare the majority vote of 50 to 100 independent runs with the single best-on-validation rule.
4. **How many independent trials does one run contain?** Cluster the return streams of all candidates evaluated in a run. The 2026 audit literature reports 100 nominal trials shrinking to 6 to 8 effective ones; the answer sets the deflation threshold.
5. **Do evolved signals survive residualization?** Regress each on order-flow imbalance, funding, basis, lagged SOL return and lagged BTC return, and test the residual.
6. **Is execution logic a safer target than forecasting?** Hold a simple forecaster fixed and evolve only entry, exit and sizing rules, with a fill model calibrated to Kalshi's book rather than to bar ranges.
7. **Where does validation performance peak?** Record out-of-sample performance by generation to see whether early stopping near the validation peak beats running to convergence.
8. **Does a behavior archive give real diversification?** Check whether elites from different turnover and holding-time cells hold different positions at the same time, or collapse to one bet.
9. **How fast do evolved rules decay?** Measure net performance by week since selection, and test whether periodic re-evolution on a rolling window beats a frozen rule set after accounting for the extra trials.
10. **Cross-venue fitness.** Evolve on Binance and Hyperliquid inputs but score with Kalshi prices, fees and 8-hour funding; quantify how much apparent edge is lost to the venue gap and to timestamp alignment.

## Reading order

1. [neely-1997](notes/neely-1997-genetic-programming-fx-technical-analysis.md): the cleanest classic; method, ensemble result and later decay in one place.
2. [allen-1999](notes/allen-1999-genetic-algorithms-technical-trading-rules.md): origin of the three-window design.
3. [neely-2003 in topic 11](../11-intraday-seasonality-tradfi/notes/neely-2003-intraday-technical-trading-fx-genetic.md): what happens at intraday frequency after costs.
4. [gencay-2026](notes/gencay-2026-honest-evaluation-llm-strategy-discovery.md): trial accounting and why deflation and leakage control are separate.
5. [wang-2026](notes/wang-2026-factorbench-automated-factor-mining-benchmark.md): independent comparison of modern miners.
6. [kvasiuk-2026](notes/kvasiuk-2026-madevolve-llm-evolution-bitcoin-trading.md): the nearest thing to the target use case, with its limits.
7. [chen-2025](notes/chen-2025-red-queen-deep-evolution-crypto-hft.md): failure modes on crypto perpetuals.
8. [kakushadze-2016](notes/kakushadze-2016-101-formulaic-alphas.md), then [zhang-2020](notes/zhang-2020-autoalpha-hierarchical-evolutionary-alpha-mining.md), [yu-2023](notes/yu-2023-alphagen-synergistic-formulaic-alphas-rl.md), [cui-2021](notes/cui-2021-alphaevolve-evolving-novel-alphas.md): the formulaic-alpha line.
9. [yun-2025](notes/yun-2025-quantevolve-quality-diversity-strategy-evolution.md) and [huang-2026](notes/huang-2026-constrained-llm-agents-crypto-factors.md): quality-diversity archives and constrained LLM search.
10. [deb-2002](notes/deb-2002-nsga-ii-multiobjective-genetic-algorithm.md), [salimans-2017](notes/salimans-2017-evolution-strategies-scalable-alternative-rl.md), [freqtrade-2026](notes/freqtrade-2026-hyperopt-nsga3-strategy-optimization.md): optimizer references and practitioner tooling.

## Not covered

- Grammatical evolution in finance (Brabazon and O'Neill): no open copy located.
- NEAT and other neuroevolution applied to trading: no credible source found.
- Rigorous multi-objective (NSGA-II) studies on crypto strategies: none found.
- Opened but not written up: Alpha-GPT (arXiv 2308.00016), an LLM-guided MCTS factor miner (arXiv 2505.11122), AlphaForge (arXiv 2406.18394), warm-start genetic programming (arXiv 2412.00896), MAP-Elites (arXiv 1504.04909), and the in-loop deflation follow-up (arXiv 2611.14539).
