---
title: "The price impact of order book events"
authors: "Cont, Rama; Kukanov, Arseniy; Stoikov, Sasha"
year: 2014
venue: "Journal of Financial Econometrics (read as arXiv:1011.6402v3, March 2011)"
url: "https://arxiv.org/pdf/1011.6402"
pdf: "sources/07-order-book-imbalance/cont-2014-price-impact-order-book-events.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "07-order-book-imbalance"
asset_class: "equities"
horizon: "seconds"
tags: "order-flow-imbalance, ofi, price-impact, depth, top-of-book, foundational"
---

## Key insight
Over short intervals, mid-price changes are explained mainly by order flow imbalance (OFI): the net of limit orders, cancellations and market orders at the best bid and ask. The relation is linear, and its slope is inversely proportional to market depth. OFI explains price changes far better than signed trade volume, and the familiar square-root law of volume is argued to be an aggregation artifact of this linear relation. The result is contemporaneous, not predictive.

## Method
For each update n of the best quotes, the event contribution is

`e_n = 1{Pb_n >= Pb_{n-1}} qb_n - 1{Pb_n <= Pb_{n-1}} qb_{n-1} - 1{Pa_n <= Pa_{n-1}} qa_n + 1{Pa_n >= Pa_{n-1}} qa_{n-1}`

and `OFI_k` is the sum of `e_n` over interval k. A market sell and a bid cancellation of the same size are treated as equivalent. The model is `dP_k = beta * OFI_k + eps_k` (price change in ticks), estimated by OLS in half-hour windows, with `beta_i = c / AD_i^lambda`, where AD is average depth at the best quotes. A stylized book with constant depth D per level gives `dP = OFI / (2D)`.

## Data and sample
NYSE TAQ consolidated quotes and trades for 50 randomly chosen S&P 500 stocks, April 2010. Base interval 10 seconds; robustness checks from 10 quote updates up to 10 minutes on a subsample.

## Reported results
- Average R2 of the OFI regression is 65%; beta is almost always significant and the intercept mostly insignificant.
- Excluding price-changing events from OFI (to test for tautology), R2 falls but stays in the 35% to 60% range.
- A quadratic term raises average R2 only from 65% to 68%.
- Trade imbalance alone gives an average R2 of 32%; it becomes insignificant once OFI is included.
- The depth exponent lambda is close to 1; the hypothesis lambda = 1 cannot be rejected for 35 of 50 stocks.
- Quote updates outnumber trades roughly 40 to 1 in the data.
- Fit generally improves as the interval lengthens within the tested range.

## Signal construction
Inputs: best bid/ask price and size on every book update (L1 stream). Compute `e_n` per update, sum over a window (for example 1 s, 10 s, 1 min), and normalize by average top-of-book depth over a trailing window: `nOFI = OFI / AD`. Re-estimate beta on a rolling window (the paper uses 30 minutes) because depth and impact are strongly seasonal. Use as a state variable describing current pressure, and as the building block for the multi-level and cross-asset variants in the companion notes.

## Relevance to SOL perpetuals at minutes to hours
The construction transfers directly to Binance, Bybit, OKX and Hyperliquid SOL perp feeds. The inverse-depth scaling matters for a thin venue such as Kalshi: the same net flow moves price more there, so a cross-venue signal should be normalized by the depth of the venue where it is measured. What does not transfer automatically is any forecasting claim. This paper shows that OFI explains the price move in the same interval; whether lagged OFI predicts the next 1 to 60 minutes of SOL returns must be tested separately (see the Cont, Cucuringu and Zhang note).

## Caveats
One month of 2010 US equity data with timestamps rounded to the second. Contemporaneous regression, so high R2 is partly mechanical. No trading strategy or cost analysis. Crypto books differ in tick size, cancellation rates, and the presence of spoofed depth away from the touch.
