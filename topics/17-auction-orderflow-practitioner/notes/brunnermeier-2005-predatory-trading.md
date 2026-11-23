---
title: "Predatory Trading"
authors: "Brunnermeier, Markus K.; Pedersen, Lasse Heje"
year: 2005
venue: "Journal of Finance, 60(4), August 2005"
url: "https://www.princeton.edu/~markus/research/papers/predatory_trading.pdf"
pdf: "sources/17-auction-orderflow-practitioner/brunnermeier-2005-predatory-trading.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "17-auction-orderflow-practitioner"
asset_class: "multi"
horizon: "n/a"
tags: "predatory-trading, forced-liquidation, stop-hunt, price-overshooting, liquidity, theory"
---

## Key insight
When strategic traders know that another trader must liquidate (margin call, stop-loss, risk limit), it is optimal for them to trade in the same direction first and buy back afterwards. This produces price overshooting, makes the market least liquid when liquidity is most needed, and can even create the distress it exploits. The model gives the folklore of "stop hunts" a rigorous footing and states when hunting pays: an illiquid market, a large distressed position relative to others' capacity, and few predators.

## Method
A continuous-time equilibrium model, not an empirical study. A small number I of large strategic traders hold a risky asset, each with a position limit. Long-term investors supply a downward-sloping demand curve, so net selling by the strategic traders lowers the price. Traders can trade up to an aggregate intensity A without temporary impact cost. Some traders become distressed and must reduce their position to zero. The paper solves for the trading paths of distressed traders and predators and for the price path, then extends the model to endogenous distress, systemic spillovers, disclosure and valuation. I graded this B because it is peer-reviewed theory supported by anecdotes (LTCM 1998, the 1987 crash, Enron's trading book), not by statistical tests.

## Data and sample
None. Table I of the paper collects anecdotal evidence; numerical examples use three, nine and twenty-seven traders with one third in distress.

## Reported results
- With one predator, the predator sells as fast as it can alongside the distressed trader and then buys back; the price overshoots.
- With several predators, overshooting is strictly positive for any finite number of predators, decreases as their number grows, and tends to zero as the number goes to infinity (Proposition 3).
- The more traders are expected to be in distress, the higher the wealth needed to survive, so distress spreads (Proposition 4).
- Under certain conditions, paper value exceeds orderly liquidation value, which exceeds distressed liquidation value.
- Predation is profitable when the market is illiquid and the distressed position is large relative to the buying capacity of the other traders.

## Signal construction
Not a signal. It supplies the conditions under which a liquidation or stop cluster is likely to be attacked and overshot, which can be turned into features: (1) estimated forced-flow notional within x% of price (from liquidation estimates or stop-cluster proxies) divided by visible depth and recent volume; (2) concentration of that flow in few accounts, observable on Hyperliquid where positions are public; (3) a measure of how many large traders are active, as a proxy for the number of potential predators. The model predicts a three-stage path: pre-emptive move toward the cluster, overshoot through it, then partial reversal as predators buy back.

## Relevance to SOL perpetuals at minutes to hours
The model fits perps closely: liquidation prices are mechanical, partly inferable, and on some venues public. It predicts that a cascade's overshoot reverts once forced flow is exhausted, which is the logic of fading a liquidation flush, and that reversal is weaker when many traders compete to provide liquidity. Kalshi's low leverage implies smaller forced flows on Kalshi itself, so the relevant clusters are on Binance, Bybit, OKX and Hyperliquid. Whether overshoots on those venues are large enough to trade after costs is an empirical question for topic 04's liquidation data.

## Caveats
Theory with stylized assumptions (known distress, fixed capacity, no private fundamental information). It does not say how to tell a predatory overshoot from an informed move in real time. Evidence in the paper is anecdotal. Retail "stop hunt" narratives usually cannot be distinguished from ordinary volatility crossing a crowded level.
