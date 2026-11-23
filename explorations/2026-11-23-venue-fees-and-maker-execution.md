# Assessment: venue fees and the maker-in, maker-out plan

Written 2026-11-23. Three questions were asked in conversation:

1. Does Kalshi charge fees on perpetuals?
2. Do other platforms offer perpetuals with lower fees?
3. If not, is the plan simply to enter and exit as a maker, resting at the best bid and offer?

How to read it:

- A source slug in brackets is a note in this repository. "Inference" marks a step that is this document's own and appears in no source.
- Each fee figure carries a "how verified" label. Only figures marked "primary source read" were checked against the venue's own document.
- This extends the "selective maker" reframing in `2026-11-22-assessment.md`; it does not repeat that document's recommendations.

## Short answers

1. Yes. Kalshi charges a percentage of notional on both the opening and the closing trade: 12 bp taker and 2 bp maker at the entry tier for an account cleared through a futures commission merchant.
2. Yes on the taker side, no on the maker side. Other venues' taker fees are roughly 2 to 5.5 bp against Kalshi's 12 bp, but their maker fees are about the same 1.5 to 2 bp. For a US resident the offshore venues are probably unavailable, which leaves Coinbase and Kraken (Bitnomial), neither fully costed here.
3. Maker-first is the right plan on Kalshi, but the 4 bp round trip it implies is a floor, not an expectation. Adverse selection on fills, missed winners, and taker exits on losing trades all add to it.

## Kalshi's fees

From the fee schedule filed with the CFTC on October 19, 2026, effective October 30 [kalshiex-2026-perpetuals-fee-schedule-amendment](../topics/06-kalshi-venue/notes/kalshiex-2026-perpetuals-fee-schedule-amendment.md). Crypto perpetuals, account cleared through a futures commission merchant:

| 30-day volume | Taker | Maker |
|---|---|---|
| $0 | 0.12% | 0.02% |
| $100K or more | 0.10% | 0.015% |
| $1M or more | 0.06% | 0.012% |
| $10M or more | 0.02% | 0% |
| $100M or more | 0.015% | 0% |
| $1B or more | 0.01% | 0% |

- The tier uses trailing 30-day volume across perpetuals and prediction markets, maker and taker combined, updated daily.
- Self-clearing members start at 0.04% taker and 0.02% maker.
- Funding is separate: it passes between longs and shorts, not to Kalshi, and was exactly zero in 401 of 517 SOL intervals since launch [kalshi-2026-solperp-public-market-data-snapshot](../topics/06-kalshi-venue/notes/kalshi-2026-solperp-public-market-data-snapshot.md).

Not confirmed:

- **The rate a retail account actually pays.** The filing says each futures commission merchant "remains free to set the commissions and fees it charges its own customers". The authoritative figure is the authenticated `GET /margin/fee_tiers` endpoint [kalshi-2026-perps-api-rest-websocket-fix](../topics/06-kalshi-venue/notes/kalshi-2026-perps-api-rest-websocket-fix.md).
- **The rebate for self-clearing members** (98% of taker fees and all maker fees through December 31, 2026). The fee note takes this from a companion filing, `rules10182634493.pdf`, which is not downloaded here; the 2026-11-22 assessment already flags it for checking.
- **Fee history.** The schedule was amended at least five times between August and October 2026, so a backtest needs dated fee regimes.
- **Help centre.** Kalshi's "Perps Fees Explained" article confirms fees on open and close, tiered by volume, and prints no rates [kalshi-2026-perps-help-center-funding-margin-liquidation](../topics/06-kalshi-venue/notes/kalshi-2026-perps-help-center-funding-margin-liquidation.md).

## Fees on other venues

Base tier, before volume or token discounts.

| Venue | Maker | Taker | How verified |
|---|---|---|---|
| Kalshi, account cleared through a futures commission merchant | 0.02% | 0.12% | Primary source read (CFTC filing) |
| Kraken Derivatives US, Bitnomial-listed perpetuals | $0.0113 per contract per side, flat | same | Primary source read [kraken-2026-us-futures-fees-bitnomial-perpetuals](../topics/06-kalshi-venue/notes/kraken-2026-us-futures-fees-bitnomial-perpetuals.md); contract unit not confirmed |
| Coinbase, US perp-style futures | not found | "as low as 0.02%" | One news report seen in a search summary; Coinbase's fee page refused the fetch |
| Hyperliquid | 0.015% | 0.045% | Comparison blogs seen in search summaries, not opened |
| Binance USDT-margined | 0.02% | 0.05% | Same |
| OKX | 0.02% | 0.05% | Same |
| Bybit | about 0.02% | about 0.055% | Same; one blog gives 0.01% and 0.06% |

Reading the table:

- **Kalshi is an outlier only on the taker side.** Its maker fee matches the offshore venues. A strategy that rests on both legs gives up little by trading on Kalshi; one that crosses the spread pays two to three times more than elsewhere.
- **Kraken's flat fee cannot be converted to basis points yet.** $0.01 of the $0.0113 is a fixed NFA charge per contract. If the charged unit is 0.1 SOL the fee is 11.3 bp per side at a SOL price of $100 and 5.65 bp at $200; if it is 1,000 SOL the fee is negligible. The Bitnomial filing gives both sizes [bitnomial-2026-solana-deci-perpetual-futures-filing](../topics/06-kalshi-venue/notes/bitnomial-2026-solana-deci-perpetual-futures-filing.md). The order form's estimated-fee field would settle it.
- **A flat fee removes the maker advantage.** On Kraken a resting order saves no fee, so the reason to rest there is the spread alone.
- **Fees are not the whole cost.** Spread, depth and leverage on Bitnomial and Coinbase are not in the repository. Hyperliquid funding settles hourly and Binance every eight hours, so funding needs normalising before any comparison.

### Access from the United States

Not verified in this repository, and the repository does not record where the account holder resides. From general knowledge: Binance, OKX and Bybit do not offer their international perpetuals to US residents, and Hyperliquid's terms exclude US persons. The search confirmed only Bybit. If the account is US-based, the realistic alternatives to Kalshi are the other CFTC-regulated venues: Coinbase Derivatives, Bitnomial (through Kraken or another broker) and OG.com Markets [coinbase-2025-nano-solana-perp-style-futures-filing](../topics/06-kalshi-venue/notes/coinbase-2025-nano-solana-perp-style-futures-filing.md), [nadex-2026-solana-perpetual-futures-ogcom-filing](../topics/06-kalshi-venue/notes/nadex-2026-solana-perpetual-futures-ogcom-filing.md). The offshore venues remain useful as signal inputs whatever the access position.

## Maker in, maker out at the best bid and offer

The mechanics work: Kalshi's API supports post-only orders, and two maker legs cost 4 bp in fees against 24 bp for two taker legs. The fee is the smallest part of the real cost.

**1. Fills arrive when the trade is wrong.** In a live experiment with minimum-size orders on the Binance BTC perpetual, resting orders at the touch filled mostly when the next five seconds went against them and rarely when the price went their way. Markouts ran from -0.3 bp to -1.2 bp depending on queue state, and a naive two-sided quoter lost almost 60% in under four days even with a rebate [albers-2025-market-makers-dilemma-fill-probability](../topics/27-execution-risk-management/notes/albers-2025-market-makers-dilemma-fill-probability.md). That experiment is market making on BTC at Binance, not directional trading on SOL at Kalshi; the mechanism transfers, the magnitudes need measuring.

**2. The missed trades are the winners.** A long signal resting on the bid fills when the price falls to it and misses when the price runs away. The same paper finds imbalance-following maker strategies fail on fill probability for this reason. A replay backtest cannot show the effect, because simulated passive fills are unreliable.

**3. Maker-out fails when the exit matters most.** Inference. A resting exit fills when the trade has worked. When the position moves against the bot, the exit order sits unfilled while the price leaves, and the bot must chase or cross and pay 12 bp plus half the spread. Two Kalshi details bear on this: bracket and trailing exits fire as limit orders according to the topic 06 synthesis of the API documentation, and the help centre says a position cannot be closed while a resting order sits on it, so the bot must cancel before exiting. Whether a triggered exit pays the taker fee is not confirmed.

**4. The competition at the touch pays less.** Self-clearing members pay 4 bp taker and 2 bp maker before the rebate noted above. Inference: those firms watch the larger venues, and because Kalshi follows them, their quotes move first and a slower resting order is the stale one that gets hit.

**5. Queue position is cheap to take.** Inference from the contract terms: the tick is $0.001 per SOL [kalshiex-2026-solperp-contract-terms-cftc-filing](../topics/06-kalshi-venue/notes/kalshiex-2026-solperp-contract-terms-cftc-filing.md), a small fraction of the roughly 4.5 bp median spread in the one-day snapshot, so any participant can step in front of an order resting exactly at the touch for almost nothing. Not measured.

### What the round trip is likely to cost

Inference, using the cost convention of the break-even table in the [topic 27 synthesis](../topics/27-execution-risk-management/SYNTHESIS.md): a maker leg costs 2 bp, a taker leg costs 12 bp plus 2.25 bp of half-spread, at the entry tier. If the entry is always passive and a share `q` of exits is passive:

`round trip = 2 + 2q + 14.25(1 - q) bp, plus the markout on passive fills`

| Share of exits that rest (q) | Fees and spread (bp) | With 2 bp adverse selection (bp) |
|---|---|---|
| 1.0 | 4.0 | 6.0 |
| 0.8 | 6.5 | 8.5 |
| 0.7 | 7.7 | 9.7 |
| 0.5 | 10.1 | 12.1 |
| 0.0 | 16.3 | 18.3 |

The 2 bp adverse-selection figure is the placeholder the topic 27 table uses, not a measurement. That table puts the break-even holding period for two maker legs with 2 bp of adverse selection between about 37 minutes and 5.5 hours depending on forecast strength, and for two taker legs between about 14 hours and 5 days. Its own caveat applies: it omits the cost of trades missed when the passive order does not fill.

Volume helps on the taker legs only slowly: $1M of 30-day volume halves the taker fee to 6 bp, and $10M makes maker free and taker 2 bp. Maker volume counts toward the tier.

### What to measure before building on it

These repeat questions 1 and 2 of the topic 27 synthesis and entry 9 of [SIGNALS.md](../synthesis/SIGNALS.md), sharpened for this plan.

1. **Fill rate and markout.** Place minimum-size post-only orders at the Kalshi touch and record whether each fills and the mid 5 seconds, 1 minute and 5 minutes after. This single measurement decides whether the 10 bp fee gap per leg survives adverse selection.
2. **Cancel on reference move.** Repeat with a rule that cancels when the Binance or Coinbase mid moves, and measure how much of the adverse selection it removes and how much fill rate it costs.
3. **Exit mix.** In live or paper trading, record `q`, the share of exits that fill passively, separately for winning and losing trades. The table above shows how sensitive the cost is to it.
4. **Queue behaviour.** Record how often an order at the touch is stepped in front of before it fills, to test point 5.
5. **Triggered exits.** Confirm on a small position whether bracket and trailing exits are charged the maker or the taker fee.

Kill condition, from SIGNALS.md entry 9: passive entry is not viable if the measured markout plus the value of missed trades exceeds the fee gap.

## Open items

- The fee tier Kalshi Prime applies to this account (`GET /margin/fee_tiers`).
- The self-clearing rebate filing, `rules10182634493.pdf`, not downloaded.
- Coinbase's US perp-style fee schedule. The August 2026 CFTC fee filing (`rules08032613651.pdf`) appeared in search results and was not opened.
- The contract unit behind Kraken's per-contract fee for Bitnomial SOL perpetuals.
- Offshore fees from each venue's own fee page, if those venues are ever considered for execution.
- US access terms for each venue.

## Sources outside the repository

Opened:

- Kraken, "US Futures Fees": https://support.kraken.com/articles/us-futures-fees

Seen only as search-result summaries, not opened:

- CryptoSlate on Coinbase's US perpetuals: https://cryptoslate.com/coinbase-starts-cftc-regulated-perpetuals-for-us-traders-offering-10x-leverage-and-0-02-fees/
- Coinperps, Hyperliquid and Binance fees: https://www.coinperps.com/learn/hyperliquid-vs-binance-fees
- Datawallet, futures exchange comparison: https://www.datawallet.com/crypto/best-crypto-derivatives-platforms
- OKX, futures fees compared: https://www.okx.com/it/learn/crypto-futures-fees-compared
- dev.to, exchange fee comparison: https://dev.to/nyxance/crypto-exchange-fee-comparison-2026-what-traders-actually-pay-2ojp

Refused the fetch:

- Coinbase help, derivatives fees: https://help.coinbase.com/en/coinbase/derivatives/derivatives-fees
