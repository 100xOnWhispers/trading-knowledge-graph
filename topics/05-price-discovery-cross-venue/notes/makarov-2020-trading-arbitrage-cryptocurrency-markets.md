---
title: "Trading and arbitrage in cryptocurrency markets"
authors: "Makarov, Igor; Schoar, Antoinette"
year: 2020
venue: "Journal of Financial Economics"
url: "https://eprints.lse.ac.uk/100409/1/Makarov_Trading_and_arbitrage_in_cryptocurrency_markets.pdf"
pdf: "sources/05-price-discovery-cross-venue/makarov-2020-trading-arbitrage-cryptocurrency-markets.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "05-price-discovery-cross-venue"
asset_class: "crypto"
horizon: "hours"
tags: "arbitrage, cross-exchange, price-deviation, capital-controls, order-flow, common-factor, segmentation"
---

## Key insight
Bitcoin prices on different exchanges deviate by large, recurring amounts that persist for hours to weeks, and the deviations are far larger across countries than within a country, pointing to capital controls and stuck arbitrage capital rather than technology. Signed order flow has a strong common component across exchanges that drives the common price, while exchange-specific order flow explains exchange-specific deviations, which then mean-revert in relative terms.

## Method
Tick data are aggregated to volume-weighted prices. The authors build arbitrage indexes (ratio of maximum to minimum price across exchanges or regions), compute potential arbitrage profits from executed trades, and estimate country "bitcoin betas" by regressing a country's premium over the US on a buying-pressure measure (US log price minus its Hodrick-Prescott trend). For order flow, they follow Hasbrouck (1995) and Hasbrouck and Seppi (2001): factor analysis extracts a common component from signed volume and from returns across exchanges at 5-minute, hourly and daily frequencies, then returns are regressed on signed volume (Kyle lambda), separately for common and idiosyncratic parts.

## Data and sample
Kaiko tick data for 34 exchanges in 19 countries; bitcoin, ethereum and ripple; main sample January 1, 2017 to February 28, 2018.

## Reported results
- US-Korea daily average price ratio above 15% from December 2017 to early February 2018, reaching 40% on several days; Japan-US about 10%; US-Europe about 3%. Within-country deviations "typically do not exceed 1%, on average".
- Potential arbitrage profit: often above $75 million per day; at least $2 billion over December 2017 to February 2018.
- Crypto-to-crypto deviations are an order of magnitude smaller: when the US-Korea BTC/fiat gap exceeded 20%, the ETH/BTC gap averaged about 3%.
- Abstract: the common component of signed volume explains 80% of bitcoin returns. Text of the accepted version: about 50% of return variation at 5-minute and hourly levels and up to 85% at the daily level.
- Price impact: buying 10,000 bitcoins raises the price by about 4% at the daily level, mostly permanent; about nine basis points for a $1 million trade at a $10,000 bitcoin price.
- When an exchange's price is above (below) the average of others, its subsequent relative return is lower (higher).

## Signal construction
Two usable constructs. (1) Common order-flow factor: sum or first principal component of signed taker volume across the major SOL venues (Binance, Bybit, OKX, Coinbase, Hyperliquid) over 5-minute windows; this is the aggregate pressure that moves the common price. (2) Venue deviation: Kalshi mid minus a volume-weighted cross-venue reference; idiosyncratic Kalshi flow should explain it and it should mean-revert relative to the reference.

## Relevance to SOL perpetuals at minutes to hours
Kalshi is a US-only, fiat-collateralized, low-leverage venue: exactly the kind of partial segmentation the paper links to persistent deviations. Expect a Kalshi basis to offshore perps that is driven by local flow and closes slowly when arbitrage capital is constrained (margin, onboarding, no cross-margining with Binance). For direction, the common flow factor measured offshore is the relevant driver; the Kalshi-specific deviation is a relative-value signal.

## Caveats
Sample is the 2017-2018 bubble, spot only, before deep perp markets and before institutional market makers linked venues; magnitudes have fallen since. Potential profits ignore transfer times, fees and capital controls by construction. The 80% versus 50%/85% figures differ between abstract and text.
