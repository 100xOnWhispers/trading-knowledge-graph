---
title: "Stop-Loss Orders and Price Cascades in Currency Markets"
authors: "Osler, Carol L."
year: 2002
venue: "Federal Reserve Bank of New York Staff Report 150"
url: "https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr150.pdf"
pdf: "sources/17-auction-orderflow-practitioner/osler-2002-stop-loss-orders-price-cascades.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "17-auction-orderflow-practitioner"
asset_class: "fx"
horizon: "minutes"
tags: "stop-loss, price-cascade, stop-run, round-numbers, breakout, positive-feedback"
---

## Key insight
Price moves faster than normal just after crossing levels where stop-loss orders are known to cluster, and that effect lasts for hours, whereas the reversal effect at take-profit clusters fades within thirty minutes. This is the empirical core of the practitioner idea of "running the stops": positive-feedback, price-contingent orders can fire in waves and create a cascade without news. This topic uses the paper to assess stop hunts and liquidity sweeps; topic 09 holds a note on the same paper from the price-impact angle.

## Method
Round numbers are rates ending in 00 or 50. A rate "reaches" a number when it comes within 0.01% of it. It "crosses" if it is beyond the number 15 minutes later and "reverses" otherwise. Three tests, each against arbitrary (non-round) numbers with a bootstrap over 58 ten-day intervals: (1) the average move in the 15 minutes after crossing; (2) the reversal frequency after reaching; (3) the difference between the move after crossing and the move after reversing, at 15 minutes, 30 minutes, 1 hour, 2 hours, 1 day and 2 days.

## Data and sample
Minute-by-minute quotes for dollar-mark, dollar-yen and dollar-pound, January 1996 to April 1998, New York hours. Order-clustering facts come from 9,655 stop-loss and take-profit orders (over $55 billion face value) at the Royal Bank of Scotland, 1 August 1999 to 11 April 2000.

## Reported results
- Dollar-mark moves 0.061% on average in the 15 minutes after crossing a round number against 0.054% after crossing an arbitrary number; round exceeds arbitrary in 51 of 58 intervals.
- Reversal frequency for dollar-mark: 59.3% at round numbers, 54.8% at arbitrary numbers (46 of 58 intervals). Not significant for dollar-pound over the full day.
- The post-crossing move exceeds the post-reversal move for all three pairs at 15 minutes, 30 minutes, 1 hour and 2 hours; for dollar-yen by 0.0130% at 15 minutes.
- The reversal effect is significant for less than thirty minutes; the continuation effect for at least two hours. Most results are significant for hours, not days.
- Effects are stronger in the New York afternoon, when liquidity is thinner.
- Orders of $50 million or more: the largest stop-loss order is almost $450 million against under $200 million for take-profit; over 62% of very large stop-loss value sits within about ten points of a 00 level, against 28% for take-profit.

## Signal construction
Event: mid price crosses a round level R by more than a tolerance and stays beyond it for a confirmation window (here 15 minutes; test 1 to 5 minutes for crypto). Feature: signed distance beyond R scaled by recent volatility, with a liquidity conditioner such as top-of-book depth or hour of day. Expected sign: continuation, with size inversely related to liquidity. A complementary event is a touch that fails to cross, with a short-lived reversal prior.

## Relevance to SOL perpetuals at minutes to hours
In perps the cascade mechanism is stronger in principle because liquidations are compulsory stop-losses whose trigger prices cluster by leverage tier. The paper's finding that continuation outlasts reversal argues for treating confirmed breaks of crowded levels as momentum events for one to two hours. It does not show that a sweep followed by an immediate reclaim predicts reversal, which is the popular retail claim.

## Caveats
The reported differences are about one basis point (0.007% and 0.013% in the examples above), smaller than a typical taker fee. Classification as cross or reverse uses the 15-minute outcome, so the conditional moves are not tradable as stated. Indicative quotes from 1996-98. I read the 2002 staff report; a later journal version was not opened in this session.
