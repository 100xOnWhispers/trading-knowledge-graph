---
title: "Anomalous price impact and the critical nature of liquidity in financial markets"
authors: "Toth, B.; Lemperiere, Y.; Deremble, C.; de Lataillade, J.; Kockelkoren, J.; Bouchaud, J.-P."
year: 2011
venue: "Physical Review X 1, 021006 (read as arXiv:1105.1694v3)"
url: "https://arxiv.org/pdf/1105.1694"
pdf: "sources/09-liquidity-price-impact/toth-2011-anomalous-impact-critical-liquidity.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "09-liquidity-price-impact"
asset_class: "futures"
horizon: "hours"
tags: "square-root-law, metaorder, latent-liquidity, price-impact, order-book"
---

## Key insight
The average price move caused by a metaorder of size Q follows a square-root law, not a linear one. The paper explains this with a "latent order book": because prices diffuse, the true supply and demand near the current price is swept away, so liquidity is V-shaped and vanishes at the current price. Small orders therefore have disproportionately large impact, and large orders must be split.

## Method
The law is

Delta(Q) = Y * sigma * sqrt(Q / V)

with sigma the daily volatility, V the daily traded volume and Y a constant of order one. The theory is a reaction-diffusion equation for latent buy and sell intentions, whose stationary solution is linear in distance from the price. The authors test it with a numerical order-flow model ("epsilon-intelligence") in which sign autocorrelation decays with exponent gamma, and with their own execution data.

## Data and sample
Proprietary Capital Fund Management metaorders on futures markets, June 2007 to December 2010, nearly 500,000 trades. Impact is measured as the average execution shortfall, plotted as Delta/sigma against Q/V.

## Reported results
- Impact exponent delta = 0.5 for small-tick contracts and delta = 0.6 for large-tick contracts.
- The paper cites earlier estimates of delta between 0.4 and 0.7, including delta about 0.6 from Almgren et al. on US stocks.
- The volume at the best quotes is typically about 1,000 times smaller than daily turnover.
- The width of the linear liquidity region is of the order of the daily volatility (about 2% for stocks and futures in their estimate).
- In the simulated market, the impact exponent stays near 0.5 for a range of gamma and participation rates, and becomes linear when the latent book's memory is erased.

## Signal construction
Not a direction signal. It gives a cost and state model:
1. Expected impact of your own order: cost = Y * sigma_daily * sqrt(Q / V_daily), with sigma and V measured over the trailing 24 hours on the venue you trade. Start with Y between 0.5 and 1 and calibrate.
2. Liquidity state variable: L = V_daily / sigma_daily^2 (the quantity that sets how much volume moves the price by one volatility unit). A falling L means the same flow moves price more.
3. Flow-to-move conversion: given net aggressive flow Q_net over a window, the implied move is about sigma * sqrt(|Q_net| / V), which can be compared with the realized move to flag over- or under-reaction.

## Relevance to SOL perpetuals at minutes to hours
The law has since been confirmed on Bitcoin spot (Donier and Bonart 2015) and tested on Hyperliquid perpetuals (Barone and Lillo 2026, who find exponents below one half). On Kalshi, V is small, so the law predicts that even modest orders cost a meaningful fraction of daily volatility. Use it to size orders, and to estimate how much externally observed flow on Binance should move SOL. The constant Y and the exponent must be re-fitted per venue.

## Caveats
One firm's proprietary flow, which is not a random sample of trades. The law describes averages over many metaorders; any single order is dominated by noise. It is expected to break down for very small orders (linear regime) and for orders that are a large share of daily volume. The latent book cannot be observed directly.
