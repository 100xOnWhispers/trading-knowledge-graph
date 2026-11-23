---
title: "Multi-Level Order-Flow Imbalance in a Limit Order Book"
authors: "Xu, Ke; Gould, Martin D.; Howison, Sam D."
year: 2019
venue: "arXiv:1907.06230v2"
url: "https://arxiv.org/pdf/1907.06230"
pdf: "sources/07-order-book-imbalance/xu-2019-multi-level-order-flow-imbalance.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "07-order-book-imbalance"
asset_class: "equities"
horizon: "seconds"
tags: "multi-level-ofi, mlofi, ridge-regression, tick-size, depth, price-formation"
---

## Key insight
Net order flow at price levels behind the best quotes carries information about contemporaneous mid-price changes that best-level OFI misses. The earlier conclusion that deeper levels add little came from using OLS on highly correlated regressors; with Ridge regression every level out to the tenth is significant, and out-of-sample fit improves with each added level. The gain is much larger for large-tick stocks.

## Method
MLOFI is an M-dimensional vector whose m-th component is the net order flow (additions minus removals, with the Cont et al. treatment of price changes) at the m-th best bid and ask levels over a window. The model is a linear regression of the contemporaneous mid-price change on the MLOFI vector, fitted separately in intraday windows by OLS and by Ridge, with in-sample and out-of-sample R2 and RMSE compared for M = 1 to 10.

## Data and sample
Nasdaq (LOBSTER) data for six liquid stocks over 2016: ORCL, CSCO and MU (large-tick) and AMZN, TSLA and NFLX (small-tick). Base window 10 seconds within half-hour estimation blocks, giving 2,772 regression fits per stock; robustness to windows of 5 to 40 seconds and blocks of 30 to 60 minutes.

## Reported results
- Order flows at different levels are strongly correlated, which makes OLS coefficients unstable and individually weak; OLS shows signs of over-fitting for some stocks.
- With Ridge, coefficients for levels deep in the book are strongly significant.
- Including deeper levels improves out-of-sample RMSE by about 65% to 75% for large-tick stocks and about 15% to 30% for small-tick stocks.
- Adjusted R2 at M = 10 is about 0.65 for OLS and about 0.6 for Ridge (as stated in the paper's summary of its tables).
- For large-tick stocks results are similar across window lengths; for small-tick stocks R2 rises slightly with longer windows.

## Signal construction
Inputs: L2 book updates for the top M levels. For each level m, accumulate signed size changes on bid and ask with the price-change rules of OFI, over the chosen window. Use the vector as regressors in a regularized (Ridge) linear model, or collapse it to one number (see the integrated OFI in the Cont, Cucuringu and Zhang note). Never use plain OLS on the raw vector: collinearity across levels is severe.

## Relevance to SOL perpetuals at minutes to hours
Most crypto venues publish 5 to 20 levels cheaply, so MLOFI is easy to compute for SOL on Binance, Bybit, OKX and Hyperliquid. The tick-size finding matters for mapping: the benefit of depth should be re-estimated per venue because relative tick size differs across them. Because the result is contemporaneous, the practical use is a cleaner measure of current pressure and a better input to a forecasting model, not a forecast in itself. Deeper crypto levels are also where spoofed liquidity concentrates (see the Fabre and Challet note), so deep-level weights fitted on equities should not be assumed.

## Caveats
Six stocks, one year, working paper. Contemporaneous fit only; no forecasting or trading test. Depth far from the touch may be less genuine in crypto than on Nasdaq.
