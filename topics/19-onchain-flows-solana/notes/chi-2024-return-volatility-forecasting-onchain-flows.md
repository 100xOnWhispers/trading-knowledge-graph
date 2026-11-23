---
title: "Return and Volatility Forecasting Using On-Chain Flows in Cryptocurrency Markets"
authors: "Chi, Yeguang; Chu, Qionghua (Ruihua); Hao, Wenyan"
year: 2024
venue: "arXiv preprint arXiv:2411.06327 (version read dated June 2025)"
url: "https://arxiv.org/pdf/2411.06327"
pdf: "sources/19-onchain-flows-solana/chi-2024-return-volatility-forecasting-onchain-flows.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "19-onchain-flows-solana"
asset_class: "crypto"
horizon: "hours"
tags: "exchange-inflows, exchange-outflows, net-flow, stablecoin, usdt, intraday, return-prediction, volatility"
---

## Key insight
The closest published test of the standard practitioner claim at this repository's horizon. At 1 to 6 hours, USDT net inflows to exchanges predict higher BTC and ETH returns (1 and 2 hours only), ETH net inflows predict lower ETH returns at every interval, and BTC net inflows mostly do not predict BTC returns. Coin inflows also predict lower subsequent volatility. Inflows carry information; outflows do not.

## Method
Predictive OLS at intervals of 1, 2, 3, 4 and 6 hours:
- Single-variable: `R(t+1) = b0 + b1 * NetInflow(t) + e`
- Double-variable: adds the current-period return as a control.
- The same pair of regressions with volatility as the dependent variable and current volatility as the control.
Net inflow is inflows from wallets to exchanges minus outflows from exchanges to wallets, in USD millions. The authors state that in-sample and out-of-sample tests were run. Case studies and option strategies (selling ETH calls after extreme ETH inflows) are added.

## Data and sample
On-chain exchange flows for BTC, ETH and USDT aggregated across a long list of exchanges (including Binance, Bitfinex, Bybit, Coinbase, Deribit and others). 16 December 2017 to 20 January 2023 for the regressions; option tests use 2021 to May 2022. The name of the flow data vendor was not found in the text read.

## Reported results
- USDT net inflow: positive for BTC and ETH returns at 1 and 2 hours; not significant at 3, 4 or 6 hours. Stated magnitude: USD 100 million of USDT net inflow predicts 0.11 percent ETH return and 0.065 percent BTC return over the next hour.
- ETH net inflow: negative for ETH returns at all five intervals.
- BTC net inflow: no predictive power for BTC returns except a positive coefficient at 4 hours.
- Net outflows show no consistent relationship with returns. The authors' explanation is that withdrawals have many motives (custody, cold storage) while deposits mostly precede selling.
- Volatility: ETH and BTC net inflows are negatively related to subsequent volatility; USDT net inflow is negatively related to volatility at 6 hours.

## Signal construction
- Inputs: hourly exchange inflow and outflow for the asset and for USDT (and USDC), from a vendor that labels exchange addresses.
- Features: `usdt_netflow_1h` (expected sign positive, 1 to 2 hour life) and `asset_netflow_1h` (expected sign negative).
- Normalise by a trailing mean and standard deviation, since raw USD flow scales with price and market size.
- Refresh hourly. Treat inflow and outflow as separate features; the paper finds only inflows informative.

## Relevance to SOL perpetuals at minutes to hours
Direct in horizon and in design. SOL was not tested. The ETH-versus-BTC difference warns that the sign and strength are asset-specific, so SOL needs its own estimate. Solana's fast finality means a deposit can be sold within seconds to minutes, so an hourly bar may be too slow; the same regressions should be run at 5 and 15 minutes. Staking and liquid-staking flows will contaminate naive SOL exchange-flow measures.

## Caveats
Some stated magnitudes are implausible as written (for example, USD 1 million of ETH net inflow predicting a 1.70 percent fall in the next hour, or USD 1 million of BTC inflow predicting 0.99 percent over 4 hours), which points to a units or scaling problem; trust the signs more than the sizes, as the authors themselves suggest. Out-of-sample design is asserted but thinly described. No trading costs on the directional signal. Exchange address labelling by vendors is revised after the fact, which creates look-ahead risk in any backtest. Not peer-reviewed.
