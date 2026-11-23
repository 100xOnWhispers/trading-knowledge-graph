# Perpetual futures pricing, funding rates and basis: synthesis

Sixteen notes: five on pricing theory, four on empirical carry, basis and funding-cycle behaviour, two exchange specifications, and five on forecasting, control and learning methods that use funding. Fourteen were read in full, one from its abstract page, one through a secondary article. Nothing here is specific to Kalshi; its contract rules belong to topic 06.

## What the literature agrees on

**The anchor is real but soft.** A perp never has to converge on any date. Shiller already said the link to the cash price "does not quite have the same force as a no-arbitrage condition" ([Shiller](notes/shiller-1993-perpetual-futures-hedonic-indices.md)). The modern theory makes this precise in two compatible ways: the perp price is the expected spot at a random time whose mean is one over the funding coefficient ([Ackerer et al.](notes/ackerer-2023-perpetual-futures-pricing.md)), and it is pinned by an arbitrage that pays off at an uncertain but bounded time, so with costs it is pinned only inside a band ([He et al.](notes/he-2022-fundamentals-perpetual-futures.md)).

**Fair funding on a linear perp is close to financing cost.** With no convexity in the payoff, the fair rate is the interest term ([Angeris et al.](notes/angeris-2022-primer-on-perpetuals.md)); the fair premium is a fraction of a basis point at realistic rates. Anything larger is the price of demand imbalance.

**Positive funding is mostly leveraged long demand meeting limited arbitrage capital.** Three independent papers reach this reading: carry fell when Binance cut maximum leverage ([Christin et al.](notes/christin-2022-crypto-carry-trade.md)); deviations rise after high trailing returns and shrink when margin rules free up arbitrage capital ([He et al.](notes/he-2022-fundamentals-perpetual-futures.md)); dated-futures carry is attributed to trend-chasing smaller investors and scarce arbitrage capital ([Schmeling et al.](notes/schmeling-2023-crypto-carry.md), abstract only).

**Funding is persistent, the basis change is close to noise.** Over one 8-hour window the funding component is serially correlated and known in advance, while the change in basis looks i.i.d. ([Christin et al.](notes/christin-2022-crypto-carry-trade.md)). A no-change forecast of the next funding print is hard to beat ([Inan](notes/inan-2026-predictability-funding-rates.md), secondary). On an hourly venue the half-life is a few hours ([Le](notes/le-2026-funding-aware-market-making-perp-dex.md)).

**The mispricing has decayed.** Absolute deviations fell about 22 points a year and are roughly 80% smaller after 2022 ([He et al.](notes/he-2022-fundamentals-perpetual-futures.md)); static carry Sharpe on BTC drops from above 11 in 2020 to 2022 ([Christin et al.](notes/christin-2022-crypto-carry-trade.md)) to 2.24 over 2020 to 2024.

**The funding clock shapes liquidity.** Volume, spreads and order-flow toxicity are U-shaped within the 8-hour cycle, more so when funding is large in either direction ([Ruan and Streltsov](notes/ruan-2024-perpetual-futures-market-quality.md)). The exchange formulas explain why: Binance weights late-interval premium samples more heavily ([Binance specification](notes/binance-2026-funding-rate-specification.md)).

**Perps track spot better than dated futures in stress,** and funding then pays the losing side ([Gornall et al.](notes/gornall-2025-perpetual-futures-basis-risk.md)).

## Where it disagrees or is weak

- **Which benchmark price.** Ackerer et al. say the first He et al. formula was wrong; He et al. reply that ignoring the clamp misplaces the benchmark by about 55 annualised points and halves strategy Sharpe. For a bot the practical point is that the "zero" of the premium depends on the clamp and on the interest rate assumed.
- **Is the premium a risk gauge or just a cost?** Volatility enters He et al.'s regressions with the wrong sign for a risk-constraint story; Gornall et al. model constrained market makers; Ruan and Streltsov read funding-time flow as informed. These are not reconciled.
- **Does funding predict returns?** This is the weakest area. None of the sources read tests funding or premium as a predictor of the perp's own return at minutes to hours. The evidence is indirect: carry predicts crashes at slow horizons (Schmeling et al., horizon not confirmed); funding and same-coin spot returns are weakly correlated contemporaneously (0.08 to 0.23 in He et al.); hourly funding and price changes are uncorrelated on Hyperliquid (Le). A funding gate barely changed a tuned trend strategy ([Deng](notes/deng-2025-autoquant-execution-constrained-tuning.md)). An older arXiv note claiming Granger causality between BitMEX funding and price (Nimmagadda and Sasanka, 2019) was skimmed and judged too thin to note.
- **Signed price behaviour around settlement timestamps** is not reported anywhere read. Only volume, spread and toxicity are.
- **Hourly versus 8-hour venues.** There is theory (averaging-window bound in [Kim and Park](notes/kim-2025-designing-funding-rates.md)) and specification ([Hyperliquid](notes/hyperliquid-2026-funding-rate-specification.md)), but no empirical comparison was accessible. Two MDPI papers by Zhivkov (2026) on funding across 26 centralised and decentralised venues appear to address this and report spread peaks about two hours after settlement, but the publisher blocked access and they are not noted.
- **SOL.** Only Le (Hyperliquid funding dynamics) and Deng (4-hour backtests) include SOL. Everything else is BTC-centred.
- **Learning methods.** RL work includes funding in the reward ([Borrageiro et al.](notes/borrageiro-2022-recurrent-reinforcement-learning-crypto-agent.md)) or as a countdown feature ([Qin et al.](notes/qin-2025-fineft-ensemble-rl-futures-trading.md)) but never ablates it. For evolutionary methods the only funding-aware evidence found is Deng's small benchmark, where genetic and differential-evolution search over rule parameters overfit as readily as Bayesian search. No genetic-programming or neuroevolution study using funding or basis inputs was found. A multi-agent RL plus language-model system for perps (M3FT, arXiv 2611.10586) uses funding and premium as daily features; it was skimmed and left to the machine-learning topic.

## Candidate signals and methods

| Name | Inputs | Horizon | Evidence grade | Source notes |
|---|---|---|---|---|
| Clamp-adjusted premium deviation (rho) and cost band | Perp mid, index, interest rate, venue clamp and fee tier | hours | B | [he-2022](notes/he-2022-fundamentals-perpetual-futures.md), [ackerer-2023](notes/ackerer-2023-perpetual-futures-pricing.md) |
| Cross-coin average premium as leveraged-demand gauge | rho for BTC, ETH, SOL and others | hours to daily | B | [he-2022](notes/he-2022-fundamentals-perpetual-futures.md) |
| Funding in excess of the 0.01% default (long crowding, known holding cost) | Predicted and realised funding | hours | B | [christin-2022](notes/christin-2022-crypto-carry-trade.md), [binance-2026](notes/binance-2026-funding-rate-specification.md) |
| Dated-futures carry as crash-risk regime flag | CME or quarterly futures, spot | multi-day | B (abstract only) | [schmeling-2023](notes/schmeling-2023-crypto-carry.md) |
| Trailing return predicts wider premium | 120-day (and shorter, untested) spot return | daily | B | [he-2022](notes/he-2022-fundamentals-perpetual-futures.md) |
| State-dependent impact: order flow moves the premium about three times more when it is already stretched | Perp taker imbalance, premium tercile | hours | B | [he-2022](notes/he-2022-fundamentals-perpetual-futures.md) |
| Funding-clock features (minutes to settlement, hour-either-side flag, times absolute funding) | Venue schedule, predicted funding | minutes | B for liquidity effects, untested for direction | [ruan-2024](notes/ruan-2024-perpetual-futures-market-quality.md), [qin-2025](notes/qin-2025-fineft-ensemble-rl-futures-trading.md) |
| Reconstructed running predicted funding and distance to clamp edge | 5-second premium samples, venue weights | minutes to hours | C | [binance-2026](notes/binance-2026-funding-rate-specification.md), [hyperliquid-2026](notes/hyperliquid-2026-funding-rate-specification.md) |
| OU forecast of funding with jump flag | Hourly or 8-hour funding history | hours | C | [le-2026](notes/le-2026-funding-aware-market-making-perp-dex.md), [inan-2026](notes/inan-2026-predictability-funding-rates.md) |
| Hourly-venue funding (times 8) minus 8-hour-venue predicted funding | Hyperliquid and Binance SOL funding | hours | C (untested as a signal) | [hyperliquid-2026](notes/hyperliquid-2026-funding-rate-specification.md), [kim-2025](notes/kim-2025-designing-funding-rates.md) |
| Post-shock overshoot and funding cushion | Hourly spot return, premium, time since shock | hours | B | [gornall-2025](notes/gornall-2025-perpetual-futures-basis-risk.md) |
| Funding-inclusive reward for RL or evolutionary search | Position, price change, costs, funding | minutes | B | [borrageiro-2022](notes/borrageiro-2022-recurrent-reinforcement-learning-crypto-agent.md) |
| Strict funding alignment and cost-stress screening of tuned parameters | Timestamped funding, fee and funding multipliers | method | C | [deng-2025](notes/deng-2025-autoquant-execution-constrained-tuning.md) |

## Open questions worth testing on SOL perps

1. Does the SOL premium or predicted funding on Binance, Bybit or Hyperliquid predict the SOL perp return over the next 5 minutes to 8 hours, after controlling for trailing return? Test level, change and extremes separately, and long and short sides separately.
2. Is there a signed drift in the hour before settlement against the side that will pay, and a reversal after? Does it scale with absolute predicted funding? Compare 8-hour timestamps on Binance with hourly ones on Hyperliquid.
3. Does Hyperliquid's hourly SOL funding lead the 8-hour averaged print on Binance and, later, on Kalshi? At what lag does the information run out, given a half-life near 2.3 hours?
4. How large and how persistent is the Kalshi SOL premium to its index compared with offshore venues? The leverage mechanism in Christin et al. predicts smaller funding under low leverage; thin arbitrage capital on a new venue predicts wider, slower-closing gaps. Which dominates?
5. Does the three-to-one state dependence of order-flow impact hold for SOL, and at 5-minute instead of 8-hour aggregation?
6. After a volatility-scaled spot shock, how far does the SOL perp overshoot and how quickly does it close, on a deep venue and on Kalshi?
7. In an RL or evolutionary set-up, does adding predicted funding, premium and minutes-to-settlement improve out-of-sample results over price and volume features alone? Run the ablation the published papers skip, under Deng-style strict alignment.
8. Is the cross-coin average premium a better crowding state than SOL's own premium for conditioning momentum or reversal signals from other topics?

## Reading order

1. [He et al.](notes/he-2022-fundamentals-perpetual-futures.md): theory, measurement and the main empirical facts in one place.
2. [Binance specification](notes/binance-2026-funding-rate-specification.md) then [Hyperliquid specification](notes/hyperliquid-2026-funding-rate-specification.md): what is actually computed, 8-hour versus hourly.
3. [Christin et al.](notes/christin-2022-crypto-carry-trade.md): funding as the price of leverage; the funding versus basis split.
4. [Ruan and Streltsov](notes/ruan-2024-perpetual-futures-market-quality.md): the funding-cycle clock.
5. [Gornall et al.](notes/gornall-2025-perpetual-futures-basis-risk.md): behaviour in stress.
6. [Schmeling et al.](notes/schmeling-2023-crypto-carry.md): slow carry and crash risk (read the full paper).
7. [Le](notes/le-2026-funding-aware-market-making-perp-dex.md) and [Inan](notes/inan-2026-predictability-funding-rates.md): funding dynamics and forecasting.
8. [Borrageiro et al.](notes/borrageiro-2022-recurrent-reinforcement-learning-crypto-agent.md), [Qin et al.](notes/qin-2025-fineft-ensemble-rl-futures-trading.md), [Deng](notes/deng-2025-autoquant-execution-constrained-tuning.md): how learning and search methods should handle funding.
9. [Ackerer et al.](notes/ackerer-2023-perpetual-futures-pricing.md), [Angeris et al.](notes/angeris-2022-primer-on-perpetuals.md), [Kim and Park](notes/kim-2025-designing-funding-rates.md), [Shiller](notes/shiller-1993-perpetual-futures-hedonic-indices.md): pricing theory and origins, for reference.

Neighbouring work not noted here: Alexander, Choi, Park and Sohn (2020) on BitMEX price discovery (topic 05); Soska et al. (2021) on BitMEX traders and liquidations (topic 04, downloaded and skimmed, little on funding); De Blasis and Webb (2022) on perp liquidity seasonality and Dai et al. (2025) on clamp-based no-arbitrage bounds (both seen only as citations).
