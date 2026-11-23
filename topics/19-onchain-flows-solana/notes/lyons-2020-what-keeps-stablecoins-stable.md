---
title: "What Keeps Stablecoins Stable?"
authors: "Lyons, Richard K.; Viswanath-Natraj, Ganesh"
year: 2020
venue: "NBER Working Paper 27136"
url: "https://www.nber.org/system/files/working_papers/w27136/w27136.pdf"
pdf: "sources/19-onchain-flows-solana/lyons-2020-what-keeps-stablecoins-stable.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "19-onchain-flows-solana"
asset_class: "crypto"
horizon: "daily"
tags: "stablecoin, tether, issuance, peg, arbitrage, order-flow, safe-haven, null-result"
---

## Key insight
Stablecoin issuance behaves like demand-driven peg arbitrage, not like central-bank intervention, and aggregate Tether flows from the Treasury to the secondary market have no systematic effect on Bitcoin or Ethereum prices at a daily horizon. Stablecoin premiums rise when Bitcoin volatility rises, which marks stablecoins as the safe haven inside crypto. This is the main counterweight to the reading of [griffin-2020](griffin-2020-is-bitcoin-really-untethered.md) that issuance pushes prices.

## Method
- Classify every Tether transaction on Omni and Ethereum as grant, revoke or simple send, and build net flows from the Tether Treasury to the secondary market (exchanges).
- Local projections (Jorda 2005) of the change in the Tether/USD price on Treasury-to-exchange flow, with four lags of flow and price changes: `P(t+h) - P(t-1) = a + b_h * Flow(t) + lags + u`.
- The same specification with the Bitcoin (and Ethereum) price as the outcome, adding controls for daily changes in hash rate and unique addresses.
- Regressions of the daily Tether/USD price change on signed order flow in the Tether/USD pair and on a 10-day rolling standard deviation of BTC/USDT.
- A pseudo natural experiment: Tether's April 2019 launch on Ethereum, which widened access to the Treasury.

## Data and sample
Tether on-chain transactions from Omni Explorer and Etherscan; trades and order books from Coinapi for Bitfinex, Bittrex, Kraken and Binance. April 2017 to March 2020. Daily for flow regressions, minute prices for arbitrage spreads, hourly for the March 2020 case study.

## Reported results
- No significant effect of Tether secondary-market flows on Bitcoin or Ethereum prices. The authors add that this does not rule out manipulation in specific episodes.
- Arbitrage flows stabilise the peg: after April 2019 a one-standard-deviation flow shock (about USD 30 million a day) moves the Tether price 5 to 10 basis points toward parity.
- After the Ethereum launch, average arbitrage trade size fell from USD 7.0 million to 4.0 million, average spreads from 69 to 27 basis points, and the half-life of peg deviations from 6 days to 3.
- Order flow moves the Tether price: roughly 1 percent per USD 40 million of net buying.
- Higher Bitcoin volatility raises the Tether premium; premiums exceeded 100 basis points in March 2020 and averaged about 5 cents in the January 2018 crash.

## Signal construction
Two usable features, neither a directional return signal by itself:
1. Stablecoin premium: `(USDT/USD mid) - 1` from Kraken or Coinbase, updated each minute. A rising premium is a real-time stress and flight-to-stablecoin gauge.
2. Treasury-to-exchange net flow: sum of mints and Treasury transfers to exchange addresses minus redemptions, per hour or day. The paper says to expect no stand-alone daily price effect.

## Relevance to SOL perpetuals at minutes to hours
The null result is the main takeaway: do not expect a daily "USDT printed, therefore buy" rule to work unconditionally. The premium gauge transfers directly as a risk-state input, since a stablecoin premium during a SOL sell-off signals forced de-risking across the market. The daily frequency is too coarse to reject effects that last under an hour, which is where [saggu-2022](saggu-2022-intraday-bitcoin-tether-minting-burning.md) finds them.

## Caveats
Sample ends March 2020, before USDC grew, before Tron became the main USDT chain and before regulated issuance. Local projections with lag controls do not fully identify causality. Peg deviations are now far smaller, so the premium may carry less information.
