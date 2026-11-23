---
title: "Market Liquidity and Funding Liquidity"
authors: "Brunnermeier, Markus K.; Pedersen, Lasse Heje"
year: 2009
venue: "Review of Financial Studies (read here as NBER Working Paper 12939, February 2007)"
url: "https://www.nber.org/system/files/working_papers/w12939/w12939.pdf"
pdf: "sources/04-open-interest-liquidations/brunnermeier-2009-market-liquidity-funding-liquidity.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "04-open-interest-liquidations"
asset_class: "multi"
horizon: "n/a"
tags: "liquidity-spiral, margin-spiral, loss-spiral, leverage, funding-liquidity, theory"
---

## Key insight
Market liquidity (how easily an asset trades) and funding liquidity (how easily traders finance positions) feed each other. When leveraged liquidity providers lose capital or face higher margins, they cut positions, liquidity falls, prices move further, and margins and losses rise again. The result is that liquidity can be fragile: a small shock can cause a discontinuous drop in liquidity rather than a proportional one. This is the standard theoretical frame for every liquidation cascade discussed in this topic.

## Method
A multi-period equilibrium model in the spirit of Grossman and Miller (1988). Customers with offsetting demand shocks arrive sequentially, creating temporary order imbalances; speculators absorb them but must finance positions with collateralized borrowing from financiers who set margins by value-at-risk. Market illiquidity is defined as the gap between transaction price and fundamental value; funding illiquidity as the speculator's shadow cost of capital. Two feedback loops are derived:

- Margin spiral: if margins rise with illiquidity (because financiers cannot tell fundamental moves from liquidity moves and volatility is time-varying), a loss of speculator wealth lowers liquidity, which raises margins, which tightens the constraint further.
- Loss spiral: speculators with a large existing position lose on it when illiquidity rises, forcing further sales and further price moves.

The two spirals reinforce each other, so the total effect exceeds the sum of the parts.

## Data and sample
A theory paper. The only data shown in the part read is a chart of CME S&P 500 futures margin requirements from 1982 to 2006, which rose around the 1987 crash, the 1990 mini crash and the 1998 LTCM episode.

## Reported results
The model implies that market liquidity (i) can suddenly dry up, (ii) has commonality across securities, (iii) is related to volatility, (iv) is subject to flight to quality, and (v) comoves with the market. Stated testable predictions: a shock to speculator capital is a state variable for liquidity and risk premia; a capital reduction lowers liquidity more when capital is already low (a non-linear effect) and for high-margin securities; margins increase in illiquidity when fundamental value is hard to determine; speculator returns are negatively skewed. Proposition 3 gives conditions under which the equilibrium price cannot be continuous in the shocks ("fragility"), including a large initial speculator position.

## Signal construction
Not a signal. It is the conceptual model that tells a bot which state variables to watch: the stock of leveraged positions (open interest relative to depth), the capital of liquidity providers (order-book depth as a proxy), and whether the venue's margin or liquidation engine becomes more aggressive as volatility rises.

## Relevance to SOL perpetuals at minutes to hours
The loss spiral maps directly onto perp liquidations: forced, price-insensitive orders hit a book whose makers are simultaneously withdrawing. The non-linearity prediction matters most: the same sell flow should move SOL far more when depth is already thin and open interest is high. Crypto perps differ in that the "financier" is an automated liquidation engine with fixed maintenance margins, so the margin spiral operates through tiered margins, collateral haircuts and mark-price rules rather than discretionary margin calls. On a low-leverage venue such as Kalshi the local spiral should be weaker, but the price is set on offshore venues where it is strong.

## Caveats
A stylized model with no calibration to crypto and no horizon. It explains why cascades occur, not when. The published journal version was not opened in this session; the note reflects the NBER working paper text.
