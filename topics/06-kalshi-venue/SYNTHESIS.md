# Topic 06 synthesis: Kalshi perpetuals, contract rules, API and regulated US perps

Compiled 2026-11-22 from primary sources: CFTC filings, the Federal Register, Kalshi's help center and API documentation, and Kalshi's public market-data API. There is almost no academic or independent research on this venue yet, so most notes are documentation and the empirical content is a one-day snapshot computed in this session.

## What the literature agrees on

**Contract identity.** The SOL perp (API ticker `KXSOLPERP`, rulebook name SOLPERP) is a linear, USD-settled, cash-settled perpetual future listed by KalshiEX LLC, a designated contract market, and cleared by Kalshi Klear LLC. It was self-certified on June 1 and 2, 2026 and has funding history from June 3, 2026. The tradable unit is 0.1 SOL with a $0.0001 tick per unit ($0.001 per SOL), whole units only. It trades 24/7 except a maintenance window on Thursdays around 3:00 to 5:00 AM ET. See [the CFTC filing](notes/kalshiex-2026-solperp-contract-terms-cftc-filing.md) and [the API snapshot](notes/kalshi-2026-solperp-public-market-data-snapshot.md).

**Reference index.** CME CF Solana-Dollar Real Time Index (SOLUSD_RTI), built each second from the order books of Coinbase, Kraken, Gemini, LMAX Digital and Bitstamp. No offshore venue is a constituent.

**Funding schedule and limits.** All four starting facts for funding are confirmed by the filing, the help center and the API:

| Starting fact | Status | Evidence |
|---|---|---|
| Funding at 12:00 AM, 8:00 AM, 4:00 PM ET | Confirmed | Filing; help center; API history shows 04/12/20 UTC in summer and 05/13/21 UTC after the clock change |
| Rates under 0.01% set to zero | Confirmed | Filing deadband; API `funding_deadband` 0.0001; smallest non-zero historical rate was 1.01 bp |
| Cap of 2% per period | Confirmed | Filing clamp; API `funding_cap` 0.02; largest observed magnitude 8.5 bp |
| SOL maximum leverage about 3.5x | Partly confirmed | API on 2026-11-22: long 3.59x and short 3.09x at $1,000 notional, lower at size; headline estimate 3.09x |

**Funding is usually zero.** 401 of 517 SOL funding intervals since launch were exactly zero, and the mean was about 0.15 bp per 8 hours. The premium only registers when the index falls outside the $1,000 impact bid and ask.

**Regulatory basis.** The CFTC approved the BTC perp as a futures contract on May 29, 2026 and extended the reasoning to similar perps on digital commodities with deep, continuous spot markets ([order](notes/cftc-2026-btcperp-approval-order-perpetual-futures.md)). A same-day [policy statement](notes/cftc-2026-policy-statement-listing-perpetual-contracts.md) routes other asset classes through prior review. SOL is covered only by Kalshi's self-certification.

**Account structure.** Retail users trade through Kalshi Prime, a futures commission merchant; institutions can be self-clearing members. Margin is isolated in the app and portfolio-based through the API. Margin comes from a scenario-based model recalibrated over time, so leverage is an output, not a fixed tier.

**Competing US SOL perps exist and share a design family.** [Coinbase Derivatives](notes/coinbase-2025-nano-solana-perp-style-futures-filing.md) (August 2025, five-year "perp style", hourly funding), [Bitnomial](notes/bitnomial-2026-solana-deci-perpetual-futures-filing.md) (May and September 2026) and [OG.com Markets / Nadex](notes/nadex-2026-solana-perpetual-futures-ogcom-filing.md) (October 2026). Kalshi, Bitnomial and OG.com all use an impact-price premium with linearly increasing weights over 8 hours.

## Where it disagrees or is weak

**How the funding average is computed.** Three Kalshi sources give three descriptions.

| Source | Description |
|---|---|
| CFTC filing | Per-second premium, weight proportional to position in the interval; "not a time-weighted average price" |
| Help center | "TWAP of 1-minute candlestick premiums over the 480 candles" |
| API reference | "time-weighted average of the premium index" over bars of "one second or longer, depending on the market" |

The filing is the binding text. The difference matters: under linear weights the last two hours carry about 44% of the rate. The correct rule can be settled empirically by recomputing settled rates from stored premium data.

**Contract size.** The June 2 filing states a Trading Unit of 1,000 SOL; the June 1 filing and the API say 0.1 SOL. They reconcile through the filing's minimum unit of 1/10,000 contract, but position-accountability arithmetic depends on which unit is meant.

**Leverage and liquidation distance.** The help center shows a generic 1x to 6x table with liquidation after an adverse move of roughly 1/leverage. The API reports SOL leverage near 3.1x to 3.6x, an initial-margin multiplier of 1.3 over maintenance, and separate liquidation-queue and liquidation thresholds. Whether the published leverage estimate is based on initial or maintenance margin is not confirmed, so the true liquidation distance for a SOL position is unknown without authenticated endpoints. A search-result summary said Kalshi's own learn page listed 2.6x for SOL at some date; that page refused automated requests and could not be opened, so the figure is unverified.

**Liquidation mechanics.** The help center says the clearinghouse places market orders. The API overview says system exit orders are IOC limit orders that can fail to fill, and that liquidations bypass the book price band.

**Fees.** The [October 2026 schedule](notes/kalshiex-2026-perpetuals-fee-schedule-amendment.md) charges FCM-cleared crypto trades 12 bp taker and 2 bp maker at the entry tier, against 4 bp and 2 bp for self-clearing members, who also receive a 98% taker rebate through December 31, 2026. What Kalshi Prime passes to a retail customer is not confirmed, and the schedule has changed several times since launch. The only confirmed fee for a competing US perp is [Kraken's flat $0.0113 per contract per side](notes/kraken-2026-us-futures-fees-bitnomial-perpetuals.md) on Bitnomial-listed perpetuals, with no maker and taker split; the contract unit behind it is not confirmed, so it cannot yet be compared in basis points. A cross-venue fee comparison and what it means for a passive-only plan is in `explorations/2026-11-23-venue-fees-and-maker-execution.md`.

**"First perpetual futures in America."** Kalshi's claim conflicts with the CFTC filing index, which shows Coinbase "perp style" futures certified in mid-2025 and Bitnomial perpetual futures certified in January and May 2026.

**Liquidity evidence is thin.** The only quantitative evidence on spreads, depth and tracking is a single day pulled in this session. Volume is 12 to 37 times open interest per day depending on the contract, during active rebate and liquidity-provider programmes, so volume is a poor proxy for depth. The [one independent article](notes/shander-2026-kalshi-perps-leverage-funding-liquidation.md) is a retail explainer.

**Interest on collateral.** Two help articles give 3.25% and 3.50% APY.

## Candidate signals and methods

| Name | Inputs | Horizon | Evidence grade | Source notes |
|---|---|---|---|---|
| Live funding replication | L2 book ($1,000 impact prices), SOLUSD_RTI per second, linear weights | hours | B (rule), untested as signal | [filing](notes/kalshiex-2026-solperp-contract-terms-cftc-filing.md), [API](notes/kalshi-2026-perps-api-rest-websocket-fix.md) |
| Kalshi premium index state (zero, positive, negative) | `/funding_rates/premium_index` or own computation | minutes | C | [snapshot](notes/kalshi-2026-solperp-public-market-data-snapshot.md) |
| Book-to-index basis | book mid, `reference_price` from `ticker` | minutes | C | [snapshot](notes/kalshi-2026-solperp-public-market-data-snapshot.md) |
| Cross-venue US premium panel | premium and funding on Kalshi, OG.com, Bitnomial, Coinbase | minutes to hours | D (hypothesis) | [Nadex](notes/nadex-2026-solana-perpetual-futures-ogcom-filing.md), [Bitnomial](notes/bitnomial-2026-solana-deci-perpetual-futures-filing.md), [Coinbase](notes/coinbase-2025-nano-solana-perp-style-futures-filing.md) |
| Staggered funding-boundary seasonality | venue funding clocks (ET, CT, UTC) | hours | D (hypothesis) | same three notes |
| Settlement-window effects | 60-second VWAP windows at 12:00 PM and 4:00 PM ET and at funding times | minutes | D (hypothesis) | [filing](notes/kalshiex-2026-solperp-contract-terms-cftc-filing.md) |
| Event-contract implied probability | Kalshi 15-minute and hourly crypto binaries | minutes to hours | D | [event contracts](notes/kalshi-2026-crypto-event-contracts-cf-benchmarks.md) |
| Fee-tier-aware cost model | fee schedule, own 30-day volume, spread, depth | n/a | B | [fees](notes/kalshiex-2026-perpetuals-fee-schedule-amendment.md) |
| Side-asymmetric sizing | `long_leverage_estimates`, `short_leverage_estimates` | n/a | C | [snapshot](notes/kalshi-2026-solperp-public-market-data-snapshot.md), [Shander](notes/shander-2026-kalshi-perps-leverage-funding-liquidation.md) |

### Implications for machine learning, reinforcement learning and evolutionary search

No source found applies these methods to Kalshi perps; the following are design constraints the venue imposes on them.

- **Environment definition.** Action space: whole contracts of 0.1 SOL at a $0.0001 tick; limit, IOC, FOK and post-only orders; reduce-only only with IOC or FOK; bracket and trailing exits that fire as limit orders. Hard constraints: leverage about 3x and different for longs and shorts; no closing a position while a resting order exists on it in the app flow; no trading on Thursday mornings.
- **Reward and cost.** Fees dominate. A tier-0 FCM taker round trip is about 24 bp plus a 4.5 bp spread, against one-minute volatility near 8 bp. Reward functions should charge fees by the tier the agent's own turnover earns, treat funding as a deadband step function evaluated three times a day, and credit collateral interest. A direction-only objective will learn to overtrade; the choice between resting and crossing should be part of the policy.
- **Data budget.** One-minute bars with bid and ask and trades with taker side go back to June 2026, about 248,000 minutes. That is small for deep models and smaller still for walk-forward validation. Pretraining on Binance, Bybit, OKX, Hyperliquid and Coinbase data and fine-tuning or calibrating on Kalshi is the realistic route. Per-second premium data is not retained and must be recorded from now on.
- **Non-stationarity.** Fee schedules, rebate programmes, leverage calibrations and the number of competing venues all changed within five months. Evolutionary or hyperparameter search over this history will fit regime artefacts unless each regime is held out in turn.
- **Simulation.** A demo exchange exists and mirrors the API, which can serve as a paper-trading loop. Its liquidity is unlikely to resemble production, so fill models should be fitted to production book and trade data.
- **Latency and limits.** The Basic tier allows about 20 order writes per second and 200 WebSocket connections, enough for minute-scale inference.

## Open questions worth testing on SOL perps

1. Which funding average does Kalshi actually apply? Record per-second premium for several weeks and regress settled rates on the linear-weight and equal-weight versions.
2. Does Kalshi lag Binance, Hyperliquid or Coinbase at sub-minute resolution? The one-minute lag correlation in the snapshot was about zero, but that says nothing about seconds.
3. What is the true liquidation distance for long and for short SOL positions at $1,000 and $100,000 notional? Requires authenticated `GET /margin/risk`.
4. How do spread and depth behave around the Thursday maintenance window, the 12:00 PM and 4:00 PM ET settlements, and the three funding times?
5. Does the sign of the late-window premium index predict short-horizon returns once the 12 bp taker fee is charged, or only at maker cost?
6. Is there measurable flow at the staggered funding boundaries of Bitnomial (Central time) and OG.com (UTC) that shows up on Kalshi?
7. Do Kalshi 15-minute and hourly crypto binaries exist for SOL, and do their prices lead or lag the perp?
8. How much of Kalshi volume is rebate-driven, and what happens to spreads when the self-clearing-member rebate expires on December 31, 2026?
9. What fee does Kalshi Prime actually charge a retail API account, and at what turnover does tier 2 become reachable?
10. How large is the weekend and overnight basis to offshore perps when US spot books thin out?

## Reading order

1. [SOLPERP CFTC filing](notes/kalshiex-2026-solperp-contract-terms-cftc-filing.md): the binding contract terms and funding formula.
2. [Public market-data snapshot](notes/kalshi-2026-solperp-public-market-data-snapshot.md): live parameters, spreads, funding history, data depth.
3. [Perps fee schedule](notes/kalshiex-2026-perpetuals-fee-schedule-amendment.md): the cost hurdle that shapes every strategy.
4. [Perps API documentation](notes/kalshi-2026-perps-api-rest-websocket-fix.md): what the bot can observe and do.
5. [Help center collection](notes/kalshi-2026-perps-help-center-funding-margin-liquidation.md): account mechanics, and where retail documentation diverges from the rules.
6. [CFTC BTCPERP order](notes/cftc-2026-btcperp-approval-order-perpetual-futures.md) and [policy statement](notes/cftc-2026-policy-statement-listing-perpetual-contracts.md): regulatory footing and its limits.
7. [OG.com / Nadex SOL perp](notes/nadex-2026-solana-perpetual-futures-ogcom-filing.md), [Bitnomial SOL perp](notes/bitnomial-2026-solana-deci-perpetual-futures-filing.md), [Coinbase SOL perp-style](notes/coinbase-2025-nano-solana-perp-style-futures-filing.md): the competing regulated venues. [Kraken's US futures fee page](notes/kraken-2026-us-futures-fees-bitnomial-perpetuals.md) gives the one confirmed fee among them.
8. [Crypto event contracts](notes/kalshi-2026-crypto-event-contracts-cf-benchmarks.md): a possible same-venue information source.
9. [Shander (2026)](notes/shander-2026-kalshi-perps-leverage-funding-liquidation.md): a dated third-party cross-check.

**Neighbouring material opened but not given a note.** Allium's documentation lists six third-party Kalshi perps tables (trades, one-minute candles, market snapshots, order-book snapshots, funding estimates, settled funding) at `docs.allium.so/historical-data/perpetuals/kalshi`; coverage dates were not stated. A Bloomberg report of June 16, 2026, read only to its paywall, said Kalshi perps traded more than $5.5 billion in two weeks across 11 crypto contracts. Polymarket's perps documentation states that orders are not permitted from the United States, so it is not a regulated US competitor. Kalshi block-trade minimums for crypto perps are $100,000 for SOL (CFTC rule filing of July 1, 2026). General perp pricing theory belongs to topic 03.
