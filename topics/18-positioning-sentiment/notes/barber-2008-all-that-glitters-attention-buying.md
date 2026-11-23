---
title: "All that Glitters: The Effect of Attention and News on the Buying Behavior of Individual and Institutional Investors"
authors: "Barber, Brad M.; Odean, Terrance"
year: 2008
venue: "Review of Financial Studies (author manuscript, marked forthcoming)"
url: "https://faculty.haas.berkeley.edu/odean/papers/attention/all%20that%20glitters.pdf"
pdf: "sources/18-positioning-sentiment/barber-2008-all-that-glitters-attention-buying.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "A"
topic: "18-positioning-sentiment"
asset_class: "equities"
horizon: "daily"
tags: "attention-driven-buying, retail-investors, buy-sell-imbalance, abnormal-volume, extreme-returns, news"
---

## Key insight
Individual investors are net buyers of whatever grabs their attention: stocks in the news, stocks with abnormal volume, and stocks with extreme one-day returns in either direction. The asymmetry arises because buying requires searching thousands of candidates while selling is limited to what one already owns (few individuals short). Institutions do not show the pattern. This is the behavioural foundation for treating attention as a predictor of retail order flow direction.

## Method
Stocks are sorted each day into deciles (the top decile split into two vingtiles) by three attention proxies: abnormal trading volume (day-t volume divided by its mean over the prior 252 trading days), the previous day's return, and whether the firm appeared in the news. For each investor group and partition the buy-sell imbalance is computed:

`BSI = (buys - sells) / (buys + sells)`

by number of trades and by value, then averaged over days. Sorting on the previous day's return avoids reverse causality from the investors' own trades. A simple theoretical model of attention-constrained buying is provided.

## Data and sample
Trading records from a large discount brokerage (78,000 households, January 1991 to December 1996, of which 66,465 held common stocks), a small discount brokerage, a large full-service retail brokerage, and institutional money managers via the Plexus Group. US common stocks.

## Reported results
- Abnormal volume sort, large discount brokerage, by number of trades: buy-sell imbalance is -18.15% in the lowest volume decile and +29.5% in the highest vingtile. By value: -16.28% and +17.67%. Imbalance rises nearly monotonically with volume.
- Previous-day return sort: imbalance is 29.4% for the vingtile with the worst returns, falls to 1.8% in the eighth decile, and rises to 24% for the best-return vingtile. Retail buys both big losers and big winners.
- Only 0.29% of positions in the large discount brokerage data are short (0.78% by value), which is why selling does not respond to attention.
- The introduction summarizes that the buying behaviour of the professionals is least influenced by attention.

## Signal construction
Inputs: an attention shock indicator for the asset (abnormal volume, absolute return in the prior interval above a high percentile, news count). Prediction: retail net buying rises in the following interval. In a perp market this maps to a forecast that the retail long/short account ratio and taker-buy share will rise after any large move. It forecasts flow direction of one participant class, not price.

## Relevance to SOL perpetuals at minutes to hours
The mechanism transfers in part. Crypto retail traders can short perps with one click, which removes the short-sale asymmetry that drives the result, so the buy-only response must be re-tested. A direct test is cheap: after SOL absolute returns in the top 5% of hourly moves, does the Binance global long/short account ratio rise regardless of the move's sign? If so, attention shocks create a predictable build-up of retail longs that later becomes liquidation fuel after down-moves.

## Caveats
US equities in the 1990s, daily data, a long-only retail population. The paper documents order imbalance, not profitable trading against it in this text. Crypto evidence in this folder (Kogan et al. 2023) shows retail crypto behaviour differs from retail stock behaviour, so the transfer is a hypothesis.
