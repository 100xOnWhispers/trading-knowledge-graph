---
title: "How Funding Rates Predict Crypto's Most Violent Reversals"
authors: "Tsentsura, Kostiantyn"
year: 2026
venue: "Yellow.com Learn (18 March 2026)"
url: "https://yellow.com/learn/how-to-read-funding-rates-crypto-reversals"
pdf: "none"
access: "full-text"
source_type: "practitioner"
evidence_grade: "D"
topic: "28-shock-response-price-pressure"
asset_class: "crypto"
horizon: "multi-day"
tags: "funding-rate, contrarian, open-interest, liquidation-cascade, folklore, untested"
---

## Key insight
A representative statement of the popular view that extreme positive funding, together with high open interest, warns of a violent long-liquidation reversal. The article supports the view with two episodes and vendor statistics and offers no threshold, hit rate, backtest or test. It is recorded here to document exactly what the folklore claims, and at what horizon, so that it can be tested. A second practitioner article opened in this session (ForkLog, 4 February 2026, "The funding rate: how it helps anticipate price reversals in bitcoin and Ethereum") makes the same claim with no numbers at all.

## Method
Narrative. The author describes funding mechanics, then cites two events and several third-party figures. Extreme funding is described as "multiple standard deviations above the historical mean" without a definition. The signal is called "probabilistic, not deterministic".

## Data and sample
No data set. Episodes: a December 2024 Bitcoin flash crash and the 10 October 2025 deleveraging. Third-party sources named in the article: FTI Consulting, a BitMEX derivatives report for the third quarter of 2025, an SSRN paper by Zeeshan Ali, Amberdata, Gate.io, CoinGlass through CryptoSlate, and PANews. None of these was checked against its original in this session; topic 04 holds a note on the FTI Consulting article.

## Reported results
As stated in the article:
- December 2024: funding exceeded 0.1% per eight-hour cycle in the days before Bitcoin fell 7%, from about USD 103,800 to 92,200, with more than USD 400 million of longs liquidated.
- October 2025: funding rose from about 10% to nearly 30% annualized by 6 October; more than USD 19 billion was liquidated in about a day, affecting about 1.6 million traders. Attributed to Amberdata: USD 3.21 billion was liquidated in one minute at the peak, 70% of the damage occurred in 40 minutes, and top-of-book Bitcoin liquidity fell by more than 90%.
- Lead time: extreme funding preceded the largest cascades "by days, not hours".
- Attributed to BitMEX: funding was positive more than 92% of the time in the quarter, because of the interest component built into the formula.
- Compressed or negative funding is said to precede upward reversals "in some cases".
- Scope record: horizon days; conditioning variable funding level with open interest; claimed sign contrarian (high funding, lower future price); costs not considered; no test.

## Signal construction
A testable form of the claim: `z_f = (funding - trailing mean) / trailing std` over 30 to 90 days, combined with open interest relative to its trailing level. The claim predicts that when `z_f` is high and open interest is high, (a) the left tail of the forward 1- to 7-day return is fatter and (b) the response to a negative shock is larger. Because funding is positive most of the time by construction, the level must be measured against the venue's built-in interest component (0.01% per 8 hours on Binance, per the ForkLog article), not against zero. Evaluate tail outcomes and conditional shock response, not the mean return.

## Relevance to SOL perpetuals at minutes to hours
The claimed lead time is days, so even if true this is a slow state variable for a minutes-to-hours bot: a regime flag that could switch the response to a shock from "fade" to "follow" or raise the stop distance. The evidence elsewhere in the repository is unfavourable to funding as a short-horizon predictor: Kitron and Wengrowicz (2026, topic 08) find funding and the funding clock do not condition 15-minute reversal, and Garcia Seuma (2026, topic 04) finds no event-invariant early warning across seven cascades and notes funding is too coarse intraday. Schmeling, Schrimpf and Todorov (topic 03, abstract only) report that high futures carry predicts crashes, which is the academic relative of this claim at a longer horizon.

## Caveats
Two hand-picked episodes; no count of the times funding was extreme and nothing happened. Figures are second-hand. Published on an educational page of a commercial site. Annualized and per-interval funding figures are mixed. The article's own sources disagree on the duration of the October 2025 event (24 versus 36 hours).
