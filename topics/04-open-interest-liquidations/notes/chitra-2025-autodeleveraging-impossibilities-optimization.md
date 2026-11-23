---
title: "Autodeleveraging: Impossibilities and Optimization"
authors: "Chitra, Tarun"
year: 2025
venue: "arXiv preprint 2512.01112 (v3, February 2026)"
url: "https://arxiv.org/pdf/2512.01112"
pdf: "sources/04-open-interest-liquidations/chitra-2025-autodeleveraging-impossibilities-optimization.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "04-open-interest-liquidations"
asset_class: "crypto"
horizon: "minutes"
tags: "auto-deleveraging, insurance-fund, october-2025, hyperliquid, mechanism-design, liquidations"
---

## Key insight
The first formal model of auto-deleveraging (ADL), the last-resort step in which a perp venue closes profitable positions to cover losses that liquidations and the insurance fund could not absorb. The paper proves a trilemma: no ADL rule can simultaneously preserve exchange solvency, exchange revenue and fairness to traders. Applied to Hyperliquid on 10 October 2025, it estimates that the production queue rule took more from winning traders than was needed to cover the shortfall.

## Method
A venue-agnostic model of trader equity, exchange shortfall, an insurance fund fed by fractions of fees, and ADL policies as haircuts on winners' positive PnL. Two canonical policies are compared: the queue used by most venues, which greedily closes positions ranked by a profit-times-leverage score (introduced by BitMEX, adopted by Binance in 2019 and by Hyperliquid), and wealth-pro-rata haircuts (variants used by Drift and Paradex). Axioms for fairness are stated and pro-rata is shown to be the unique rule satisfying them under smoothness conditions; queue rules can violate monotonicity. The empirical section reconstructs the Hyperliquid episode from public fills, using loser-side liquidation equity for deficits and a two-pass no-ADL counterfactual for wealth removed from winners.

## Data and sample
Hyperliquid's on-chain fill log for 10 October 2025: 34,983 ADL executions across 19,337 wallets and 162 tickers, grouped into waves separated by 5-second gaps. Binance account-level data are not public, so its comparison is indirect.

## Reported results
- ADL closed about USD 2.1 billion of positions in roughly 12 minutes; the introduction describes ADL being used over 40 times in a 10-minute period.
- Estimated aggregate loser deficit about USD 100.1 million; production overshoot relative to what was needed about USD 45.0 million in PnL terms, with a band of USD 45.0 to 51.7 million. A stylized wealth-space queue diagnostic corresponds to about USD 653.6 million of positions.
- The comparison "suggests" Binance over-used ADL far more than Hyperliquid.
- After the event Hyperliquid's open interest is described as nearly 50% lower while some competitors recovered to pre-event levels.
- Background facts cited: 2024 centralized perp volume near USD 58.5 trillion against USD 17.4 trillion spot; ADL first introduced by Huobi in 2015; earlier ADL episodes include March 2020 and 19 May 2021.
- Version 3 corrects an earlier draft that applied haircuts to total equity rather than to PnL; magnitudes were revised. A companion paper by Chitra and co-authors ("Autodeleveraging as Online Learning", arXiv 2602.15182, abstract read) reports the same overshoot of up to USD 51.7 million and an alternative algorithm that reduces it to USD 3 million.

## Signal construction
Not a signal. It defines a tail risk for the bot's own positions: in a cascade, a profitable, leveraged position on the winning side can be force-closed at the prior mark price. The ranking score is roughly unrealized profit ratio times leverage, so lower leverage and smaller unrealized gains per position reduce ADL priority. ADL activation on a major venue is also an observable state flag marking the peak of a cascade.

## Relevance to SOL perpetuals at minutes to hours
A short SOL position that is correctly placed ahead of a cascade may be closed early by ADL on venues using the queue rule, cutting the payoff exactly when the signal works best. Hedged books can be left naked. The bot should know the loss-allocation rules of every venue it trades or hedges on. Whether Kalshi uses ADL, a clearing-house default waterfall, or something else was not established from its API documentation and needs to be read from the rulebook.

## Caveats
Single author affiliated with a risk-modelling firm active in the sector. Reconstruction is from public data under partial observability, and the paper states that its magnitudes were revised between versions after public critique of how haircuts were defined. The Binance comparison is indirect because account-level data are not public. One event on one venue.
