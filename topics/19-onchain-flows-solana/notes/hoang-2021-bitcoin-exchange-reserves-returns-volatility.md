---
title: "Effects of Bitcoin Exchange Reserves on Bitcoin Returns and Volatility"
authors: "Hoang, Lai T.; Baur, Dirk G."
year: 2021
venue: "SSRN working paper 3902504 (read via a Quantpedia summary dated 9 November 2021)"
url: "https://quantpedia.com/bitcoin-returns-and-volatility-predicted-by-bitcoin-exchange-reserves/"
pdf: "none"
access: "secondary"
source_type: "working-paper"
evidence_grade: "B"
topic: "19-onchain-flows-solana"
asset_class: "crypto"
horizon: "daily"
tags: "exchange-reserves, exchange-balances, exchange-inflows, cryptoquant, bitcoin, volatility, panic-selling"
---

## Key insight
The reference daily study behind the "coins moving onto exchanges are bearish" rule. Changes in aggregate Bitcoin exchange reserves are negatively related to same-day and future Bitcoin returns, and the size of reserve changes is positively related to volatility. Causality runs both ways: a large price drop is followed by a rise in reserves the next day, which the summary describes as panic selling.

## Method
Read only through a third-party summary (Quantpedia); the SSRN page was not accessible. As described there, the authors regress Bitcoin returns and volatility on daily changes in exchange reserves at several horizons, separate increases from decreases, add controls (market capitalisation, liquidity, economic policy uncertainty, stock volatility), and also run the reverse regression of reserve changes on lagged returns and volatility. Exact specifications, coefficients and standard errors were not seen. The year of the working paper is not confirmed.

## Data and sample
Daily exchange reserve data from CryptoQuant covering 20 exchanges, 1,979 trading days from 1 January 2016 to 1 June 2021. Reserves averaged about 12 percent of circulating supply. Exchanges sent and received about 100,000 BTC per day on average. Coinbase held about 25 percent of total reserves at the end of the sample. (The summary states reserve levels in "billion BTC", which cannot be right; millions is presumably meant. Not confirmed.)

## Reported results
As reported by the summary:
- Daily reserve changes are negatively related to contemporaneous and future returns, significant at all horizons examined.
- Both increases and decreases matter for short-term returns; only decreases are associated with positive long-term returns.
- The absolute reserve change is positively related to volatility, and increases in reserves affect volatility more than decreases.
- Reverse direction: a large fall in returns is followed by a reserve increase the next day; the effect fades at longer lags.
- When volatility is extreme (above the 95th or below the 5th percentile) investors are less likely to move coins to exchanges.
No effect sizes were given in the summary.

## Signal construction
- Input: aggregate exchange reserve for the asset from a labelled-address vendor, sampled daily or hourly.
- Features: `d_reserve` scaled by circulating supply or by trailing mean absolute change; separate positive and negative parts; `abs(d_reserve)` as a volatility input.
- Expected signs: reserve increase negative for returns and positive for volatility.
- Because lagged returns drive reserve changes, include lagged returns as controls or the feature will proxy for short-term reversal or momentum.

## Relevance to SOL perpetuals at minutes to hours
This is the daily result that [chi-2024](chi-2024-return-volatility-forecasting-onchain-flows.md) takes to hourly data, where it holds for ETH but not clearly for BTC. For SOL it suggests a slow bias feature and a volatility input. The reverse-causality finding matters most at short horizons: after a sharp SOL drop, expect exchange inflows to rise whether or not they predict anything further. Exchange-reserve series for SOL are complicated by exchange-operated staking and liquid-staking tokens.

## Caveats
Secondary access: every statement here is the summariser's reading, not checked against the paper. Sample ends June 2021, before spot ETFs moved a large share of holdings to custodians, which changes what "exchange reserve" means. Daily in-sample regressions with no trading test in what was read. Exchange wallet labels are vendor estimates and are revised.
