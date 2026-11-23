---
title: "The effectiveness of technical trading rules in cryptocurrency markets"
authors: "Corbet, Shaen; Eraslan, Veysel; Lucey, Brian; Sensoy, Ahmet"
year: 2019
venue: "Finance Research Letters 31, 32-37 (read as the authors' preprint from the DCU repository)"
url: "https://doras.dcu.ie/25053/"
pdf: "sources/16-oscillators-technical-rules/corbet-2019-technical-trading-rules-cryptocurrency-intraday.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "16-oscillators-technical-rules"
asset_class: "crypto"
horizon: "minutes"
tags: "bitcoin, one-minute, moving-average, trading-range-breakout, intraday, no-costs"
---

## Key insight
On one-minute Bitcoin data, the "always in the market" moving-average rule separates subsequent returns strongly: minutes classed as buys have positive mean returns and minutes classed as sells negative ones. Fixed-holding-period MA crossovers do not work, and breakouts of the recent range are followed by reversal, not continuation. No transaction costs are applied, so this is evidence of predictability, not of profit.

## Method
The Brock, Lakonishok and LeBaron design moved to minutes.
- Variable-length MA (VMA): a minute is a buy when the short MA (1, 2, 5 or 10 minutes) is above the long MA (5, 10, 20, 50, 100, 150 or 200 minutes), with either no band or a 1% band; 48 specifications.
- Fixed-length MA (FMA): after a crossover, record the return over the next n minutes (n from 10 to 1,440) and ignore signals in between; 480 tests.
- Trading range breakout (TRB): buy when price exceeds the maximum of the previous n minutes (with or without a 1% band), sell below the minimum; 20 tests.
Mean buy, sell and buy-minus-sell returns are tested against unconditional returns with Bonferroni-adjusted significance levels.

## Data and sample
Bitcoin in US dollars on Bitfinex, one-minute closes from Kaiko, 1 January 2014 to 25 June 2018 (2,341,440 minutes). Minutes without trades carry the last price forward.

## Reported results
- VMA: buy-minus-sell differences are significant at 1% in 43 of 48 specifications. Average buy return 0.072% and average sell return -0.071%. The average spread is 0.0224% without a band and 0.2637% with the 1% band. Spreads are largest when the short MA is 1 or 2 minutes.
- FMA: buy-minus-sell is positive in only 87 of 480 tests, significant in 21, and not significant in 346. Average difference is -0.0428% without a band.
- TRB: buy-minus-sell is positive in 4 of 20 tests (1 significant) and negative in 16 (11 significant), averaging -0.1245%. Returns after buy breakouts average 0.0872% and after sell breakouts 0.2116%, so downside breakouts are followed by rebounds.
- The unconditional mean one-minute return is 0.000195%.
- The authors state that liquidity and transaction costs "must be further considered".

## Signal construction
VMA state: s_t = sign(MA_short(t) - MA_long(t)), optionally zero inside a band of 1% of price. Update every minute. The paper's own results suggest using it as a regime feature (which side of the long MA price sits on) and treating fresh breakouts of the n-minute range as fade candidates.

## Relevance to SOL perpetuals at minutes to hours
The horizon matches, and two findings are worth re-testing on SOL: the sign of short-minus-long MA carries information at minute scale, and intraday range breakouts mean-revert. The breakout reversal agrees with Bakker's finding that contrarian rules dominate at five minutes. But the average edge per minute (hundredths of a percent) is far below any taker fee, and a 1 or 2 minute MA crossing a 5 minute MA flips constantly. The realistic use is as an input to a slower decision, not as a trade trigger.

## Caveats
No costs, no spread, no out-of-sample period, and last-price carry-forward in illiquid minutes of 2014 to 2015, which can manufacture apparent continuation. Bonferroni is the only multiple-testing control. The closing claim that technical trading earns 100 to 10,000 times buy-and-hold per minute ignores turnover and should be disregarded. A 1% band on one-minute Bitcoin prices selects extreme moves, so banded results mostly describe volatile episodes. One coin, one exchange.
