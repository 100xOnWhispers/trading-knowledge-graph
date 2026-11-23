# Topic 31: Reinforcement learning and evolutionary search on intraday crypto, second pass

Eighteen notes. This pass exists because topics [24](../24-reinforcement-learning/SYNTHESIS.md) and [25](../25-evolutionary-algorithms/SYNTHESIS.md) were written without web search. It adds the papers they could only name, journal work on evolutionary methods, training environments, head-to-head comparisons and data fidelity. It does not change their main conclusion. It sharpens it: on the evidence read, neither RL nor evolutionary search has a demonstrated edge over simple alternatives on intraday crypto, and the useful output of both literatures is method and test design.

Coverage note: the session's shared web-search budget ran out after eleven queries, so the journal sweep is partial. Sources after that point were reached by direct address. Gaps are listed at the end.

## What the literature agrees on

**Published RL agents do not survive a change of environment.** [FineFT](notes/qin-2025-fineft-ensemble-rl-crypto-futures.md) re-ran earlier agents on Binance futures at 5x leverage over a six-month test: MacroHFT (the positive result in topic 24) lost 75% on ETH and 50% on BNB; [EarnHFT](notes/qin-2023-earnhft-hierarchical-rl-crypto-hft.md) lost 69% on BNB; DQN lost 56% to 82% on all four assets. EarnHFT's own paper shows PPO and DQN losing on most pairs at a 0.02% fee. In the [FinRL contests](notes/wang-2025-finrl-contests-benchmarking-rl-agents.md), the winning teams on held-out second-level BTC data finished at +0.23% and -0.05% over about two and a half days.

**Seed dispersion is as large as the effect.** One configuration gave CAGR from -3% to +199% across five seeds on a one-year perp test ([lebiedz-2026](notes/lebiedz-2026-drl-execution-overlay-crypto-pair-trading.md)). The best method in a controlled benchmark ranked first in only about a quarter of seed-period runs ([sun-2023](notes/sun-2023-trademaster-rl-trading-platform-benchmark.md)). A five-seed offline-RL comparison had a standard deviation of 8 points of return in one setting ([yun-2024](notes/yun-2024-decision-transformer-offline-rl-trading.md)). Most crypto RL papers report one run.

**RL works best when confined.** The credible positive results restrict what the policy may do: timing and early exit inside fixed stops and limits ([lebiedz-2026](notes/lebiedz-2026-drl-execution-overlay-crypto-pair-trading.md)), a fallback to a conservative policy when recent states are unfamiliar ([qin-2025-fineft](notes/qin-2025-fineft-ensemble-rl-crypto-futures.md)), or scheduling a fixed sell order ([duflot-2025](notes/duflot-2025-rl-exec-impact-aware-liquidation-btc.md)).

**Offline and model-based RL do not solve the single-history problem.** Offline learners imitate a policy that was itself fitted to the one history ([yun-2024](notes/yun-2024-decision-transformer-offline-rl-trading.md)). A learned world model can only resample what it was fitted on ([wei-2019](notes/wei-2019-model-based-rl-limit-order-books.md)), and the best generative order-book model is still told apart from real data (ROC 0.83) and drifts as it is rolled forward ([nagy-2025](notes/nagy-2025-lob-bench-generative-order-book-benchmark.md)).

**Every simulator leaves something out, and which thing matters.** Replay has no reaction from other traders; agent-based simulation has reaction of unknown realism ([balch-2019](notes/balch-2019-market-replay-versus-interactive-simulation.md)). The standard open environments are spot-style with a proportional cost ([liu-2022](notes/liu-2022-finrl-meta-market-environments-benchmarks.md)). GPU simulators solve speed, not fidelity ([frey-2023](notes/frey-2023-jax-lob-gpu-limit-order-book-simulator.md)). Only FineFT's environment was confirmed to model margin, funding and liquidation (that paper also has notes in topics [03](../03-perp-pricing-funding/notes/qin-2025-fineft-ensemble-rl-futures-trading.md), 04 and 14, written from the funding and liquidation angles).

**Search must be compared with chance at equal budget.** Genetic programming beat random search given the same number of candidates in 3 of 9 markets, and where it beat random trading, random search usually did too ([chen-2007](notes/chen-2007-genetic-programming-versus-random-search-pretests.md)). Buy-and-hold is not an adequate null.

**Re-optimisation creates turnover.** Refitting every period and trading the newest rule gave the best gross and worst net return; requiring a supermajority of recent rules before changing position roughly doubled net return against a static rule ([martin-2019](notes/martin-2019-grammatical-evolution-ensembles-algorithmic-trading.md)).

**Volume data from unregulated venues was heavily contaminated.** Estimated wash trading above 70% of reported volume on unregulated exchanges in 2019, correlated with returns and volatility ([cong-2023](notes/cong-2023-crypto-wash-trading.md)). A second source asserts that most crypto papers of 2017 to 2019 used flawed data ([alexander-2020](notes/alexander-2020-critical-investigation-cryptocurrency-data.md), abstract only).

## Where it disagrees or is weak

- **RL execution against TWAP.** [duflot-2025](notes/duflot-2025-rl-exec-impact-aware-liquidation-btc.md) finds +2 to +23 basis points with tight intervals; topic 24's Ardaiz et al. find nothing. The first injects parametric impact into replay and tests one month; the second uses frictionless replay and many seeds. The sign depends on the simulator, and neither was checked against live fills.
- **RL against supervised forecast plus rule.** Still no clean test on intraday crypto. [ishikawa-2021](notes/ishikawa-2021-online-drl-forex-transaction-costs.md) is a tie at low cost and favours RL at higher cost, but the supervised baselines used a one-step target and were frozen while the RL agent learned online. [lebiedz-2026](notes/lebiedz-2026-drl-execution-overlay-crypto-pair-trading.md) compares RL with a rule, not with a supervised model, and reaches p of about 0.06. A 2026 preprint skimmed but not noted (Chistiakov and Yanovich, arXiv:2610.14750) reports a learned risk controller doing worse than a fixed one across 30 paired seeds on synthetic assets.
- **Does multi-objective evolution help?** [long-2026](notes/long-2026-multi-objective-genetic-programming-directional-changes.md) says yes with 110 series and 50 runs each, on daily long-only stock rules. Nothing comparable exists for intraday crypto, and that paper tuned three extra parameters per series.
- **How much wash trading?** The two estimation methods in [cong-2023](notes/cong-2023-crypto-wash-trading.md) give about 77% and about 16%. No source read measures it for perps or for any year after 2019.
- **Test lengths.** Nine days (EarnHFT), about 2.4 days (FinRL crypto contest), one month (RL-Exec), six months (FineFT), one year (Lebiedz). None spans more than one market regime.
- **Perp mechanics.** Only FineFT and a multi-agent LLM preprint skimmed but not noted (M3FT, arXiv:2611.10586; daily Binance perps with fees, funding, margin and a liquidation proxy, four seeds) put funding and liquidation inside the environment. Lebiedz et al. omit funding while holding at 10x.
- **Neuroevolution and grammatical evolution on crypto.** Nothing credible found. The only NEAT trading source opened was a 2014 class project on 40 minutes of FX data with no holdout (not noted). The grammatical-evolution evidence is one S&P 500 study with no buy-and-hold row.
- **Evolutionary against Bayesian search at equal budget.** Not found. A search-result summary of an IEEE conference paper (not opened) said Bayesian optimisation beat a genetic algorithm on 15-minute index rules.

## Candidate signals and methods

Nothing here is a ready signal. The table lists methods and controls.

| Name | Inputs | Horizon | Evidence grade | Source notes |
|---|---|---|---|---|
| Perp environment specification: mark-to-market P&L, fee, book-walk slippage, funding at settlement, margin check, terminal liquidation | Bars or book snapshots, funding rate, venue margin rules | Minutes | B | [qin-2025-fineft](notes/qin-2025-fineft-ensemble-rl-crypto-futures.md) |
| Novelty gate: go conservative when recent states score low under density models fitted to validated regimes | Feature vectors of recent bars | Minutes to hours | B (single study) | [qin-2025-fineft](notes/qin-2025-fineft-ensemble-rl-crypto-futures.md) |
| Shielded learning: policy chooses timing only, inside deterministic stops, time limits and entry bounds | Rule signal, spread or z-score state, position status | Hours | B | [lebiedz-2026](notes/lebiedz-2026-drl-execution-overlay-crypto-pair-trading.md) |
| Hindsight-optimal Q as auxiliary training target | Replayed prices and costs under price-taker assumption | Seconds to minutes | B | [qin-2023-earnhft](notes/qin-2023-earnhft-hierarchical-rl-crypto-hft.md) |
| Paired execution test: same windows and costs, day as unit, Wilcoxon, multiplicity correction, bootstrap interval | Candidate and baseline fills per day | 30 to 120 minutes | B | [duflot-2025](notes/duflot-2025-rl-exec-impact-aware-liquidation-btc.md) |
| Multi-seed reporting: mean, worst seed, rank distribution, block bootstrap on the difference | At least five training seeds per configuration | n/a | B | [lebiedz-2026](notes/lebiedz-2026-drl-execution-overlay-crypto-pair-trading.md), [sun-2023](notes/sun-2023-trademaster-rl-trading-platform-benchmark.md) |
| Blind holdout scored once | A data segment nobody has examined | n/a | B | [wang-2025](notes/wang-2025-finrl-contests-benchmarking-rl-agents.md) |
| Equal-budget random search and exposure-matched random trading as nulls | Same rule grammar, same number of candidates; trade count and exposure share | Any | B | [chen-2007](notes/chen-2007-genetic-programming-versus-random-search-pretests.md) |
| Inertia ensemble across refits: switch only when a supermajority of the last `s` fitted models agrees | Outputs of recent model generations | Any; tested daily | A | [martin-2019](notes/martin-2019-grammatical-evolution-ensembles-algorithmic-trading.md) |
| Multi-objective evolution with post-hoc weighted selection from the front | Return, per-trade edge, risk | Any; tested daily | A (daily equities) | [long-2026](notes/long-2026-multi-objective-genetic-programming-directional-changes.md) |
| Directional-change event features | Price stream, threshold `theta` | Scale-free | C for intraday crypto | [long-2026](notes/long-2026-multi-objective-genetic-programming-directional-changes.md) |
| Cost-aware supervised label (forward move against trading cost) | Bars, cost estimate | Minutes | C | [ishikawa-2021](notes/ishikawa-2021-online-drl-forex-transaction-costs.md) |
| Simulator realism tests: distribution distances, discriminator score, response functions, drift with rollout | Real and generated data | Tick to minutes | B | [nagy-2025](notes/nagy-2025-lob-bench-generative-order-book-benchmark.md) |
| Replay validity bound: cap backtest order size relative to displayed depth | Book depth, order size | Seconds to minutes | C | [balch-2019](notes/balch-2019-market-replay-versus-interactive-simulation.md) |
| Venue data diagnostics: Benford fit, round-size share, tail exponent of trade size | Trade tape per venue and month | n/a | A | [cong-2023](notes/cong-2023-crypto-wash-trading.md) |

## Open questions worth testing on SOL perps

1. Run the Chen and Navet nulls on the project's own search: does any optimizer (genetic, Bayesian, LLM-driven) beat equal-budget random search out of sample on SOL five-minute bars with Kalshi costs?
2. RL against supervised, done fairly: same features, a multi-bar supervised target with a no-trade band, both refitted on the same schedule, at least ten seeds, block bootstrap on the difference.
3. Does a learned timing overlay inside fixed stops beat the underlying rule on SOL, and is the gain still there in the mean and the worst seed?
4. Add funding and Kalshi's margin rules to the environment. How much of a backtested edge at hours-scale holding is funding paid or received?
5. Does the inertia ensemble reduce turnover and raise net return when a SOL model is refitted daily or weekly? What are the best `s` and inertia factor, chosen on earlier data?
6. Does a novelty gate fitted on Binance SOL data fire sensibly on Kalshi data, or does the venue difference make every Kalshi state look unfamiliar?
7. Apply the wash-trade diagnostics to SOL perp trade tapes from Binance, Bybit, OKX and Hyperliquid by month. Do volume-based features lose predictive value when computed only from venues that pass?
8. At what order size relative to Kalshi touch depth do replayed and live fills diverge?
9. Can a bar-level generative model of SOL pass discriminator and drift tests well enough to be used for stress paths?
10. Do directional-change features add anything to clock-time features for SOL at thresholds matched to typical five-minute to one-hour moves?

## Reading order

1. [qin-2025-fineft](notes/qin-2025-fineft-ensemble-rl-crypto-futures.md): the perp environment, and the table showing earlier agents failing.
2. [lebiedz-2026](notes/lebiedz-2026-drl-execution-overlay-crypto-pair-trading.md): RL against a rule on perp data with seeds and a bootstrap.
3. [chen-2007](notes/chen-2007-genetic-programming-versus-random-search-pretests.md): the nulls every search should face.
4. [martin-2019](notes/martin-2019-grammatical-evolution-ensembles-algorithmic-trading.md): the cost of periodic re-optimisation and a fix.
5. [wang-2025](notes/wang-2025-finrl-contests-benchmarking-rl-agents.md): what held-out contest scoring shows.
6. [cong-2023](notes/cong-2023-crypto-wash-trading.md): why volume inputs need auditing.
7. [duflot-2025](notes/duflot-2025-rl-exec-impact-aware-liquidation-btc.md): execution result and test protocol.
8. [balch-2019](notes/balch-2019-market-replay-versus-interactive-simulation.md), then [nagy-2025](notes/nagy-2025-lob-bench-generative-order-book-benchmark.md) and [frey-2023](notes/frey-2023-jax-lob-gpu-limit-order-book-simulator.md): what simulators can and cannot tell you.
9. [qin-2023-earnhft](notes/qin-2023-earnhft-hierarchical-rl-crypto-hft.md): second-level crypto RL and the hindsight teacher.
10. [long-2026](notes/long-2026-multi-objective-genetic-programming-directional-changes.md): multi-objective genetic programming with adequate replication.
11. [ishikawa-2021](notes/ishikawa-2021-online-drl-forex-transaction-costs.md), [yun-2024](notes/yun-2024-decision-transformer-offline-rl-trading.md), [wei-2019](notes/wei-2019-model-based-rl-limit-order-books.md): weaker evidence on supervised baselines, offline RL and world models.
12. [sun-2023](notes/sun-2023-trademaster-rl-trading-platform-benchmark.md), [liu-2022](notes/liu-2022-finrl-meta-market-environments-benchmarks.md): platforms and their limits.
13. [alexander-2020](notes/alexander-2020-critical-investigation-cryptocurrency-data.md): abstract only.

## Not covered

Opened or skimmed without a note (abstract or first pages only): DeepScalper (arXiv:2201.09058; Chinese index and bond futures, not crypto), ABIDES-Gym (arXiv:2110.14771), JaxMARL-HFT (arXiv:2511.02136), M3FT (arXiv:2611.10586), Goluza et al. on intraday futures RL (arXiv:2406.08013), Wang and Klabjan on crypto RL ensembles (arXiv:2309.00626), Pricope's review (arXiv:2106.00123), Theate and Ernst (arXiv:2004.06627), Ning, Lin and Jaimungal (arXiv:1812.06600), a daily Bitcoin genetic-algorithm factor preprint (arXiv:2411.03035), warm-start genetic programming on Chinese stocks (arXiv:2412.00896), and the Gencay follow-up on in-loop deflation (arXiv:2611.14539; it belongs to topic 26, and its abstract reports that a hundred nominal trials collapsed to 6 to 8 effectively independent return streams).

Not reached: Ammann et al. on survivorship in crypto universes (SSRN blocked); full text of Alexander and Dakos; Ding et al. (2025) on genetic programming for crypto volatility (repository and publisher blocked; the record seen describes daily volatility models with a climate-policy input, of limited relevance); Brabazon and O'Neill's grammatical-evolution work; Deng et al. (2017); Moody and Saffell (2001); Kolm and Ritter; Sun, Wang and An's survey; ABIDES-MARL; MAP-Elites, Alpha-GPT, AlphaForge and LLM-guided MCTS factor mining; Omole and Enke (2024), Danilo et al. (2026), Mahayana et al. (2022) and the TU Delft thesis; any systematic search of Expert Systems with Applications, Swarm and Evolutionary Computation, GECCO, CIFEr or ICAIF proceedings.
