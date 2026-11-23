---
title: "The Flash Crash: The Impact of High Frequency Trading on an Electronic Market"
authors: "Kirilenko, Andrei; Kyle, Albert S.; Samadi, Mehrdad; Tuzun, Tugkan"
year: 2017
venue: "Working paper version of 5 May 2014 hosted by the CFTC, the version read; published in the Journal of Finance, 2017 (journal version not opened)"
url: "https://www.cftc.gov/sites/default/files/idc/groups/public/@economicanalysis/documents/file/oce_flashcrash0314.pdf"
pdf: "sources/28-shock-response-price-pressure/kirilenko-2017-flash-crash-high-frequency-trading.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "28-shock-response-price-pressure"
asset_class: "futures"
horizon: "minutes"
tags: "flash-crash, liquidity-crash, hot-potato, inventory, trading-pause, v-shaped-recovery"
---

## Key insight
The 6 May 2010 Flash Crash is the best-documented case of a pure price-pressure event: a large sell program met intermediaries who hold very small inventories, price fell 5.1% in 13 minutes and recovered 6.4% in the next 23. High-frequency traders did not cause it and did not absorb it either; they passed contracts among themselves at rising speed. The fall stopped after a five-second exchange pause, when slower buyers stepped in.

## Method
Audit-trail data with account identifiers for the E-mini S&P 500 futures. Accounts are classified by behaviour into High Frequency Traders, Market Makers, Fundamental Buyers, Fundamental Sellers, Opportunistic Traders and Small Traders, using volume and end-of-day or intraday inventory rules (for example, a Fundamental Seller trades at least 10 contracts and ends the day net short by at least 15% of its volume). Second-by-second regressions relate each group's inventory change to current and lagged price changes, with dummies for the Down phase (13:32:00 to 13:45:28 CT) and Up phase (13:45:33 to 14:08:00 CT), compared with 3 to 5 May.

## Data and sample
CME E-mini S&P 500 June 2010 contract, transaction-level regulatory data, 3 to 6 May 2010.

## Reported results
- The trigger named by the regulators' report was an automated program to sell 75,000 contracts.
- Volume per minute during the 36 minutes was nearly 8 times that of earlier in the day; total volume was about 14 times the size of the sell program.
- High-frequency traders bought about 3,000 contracts in the first ten minutes, then sold aggressively. They did not significantly change net inventory during the Down phase.
- "Hot potato" trading: between 13:45:13 and 13:45:27 CT high-frequency traders traded over 27,000 contracts, about 49% of volume, while their net position changed by about 200 contracts.
- The decline was interrupted by a five-second pause triggered by CME stop logic. Prices then stabilized and rebounded as Fundamental Buyers and Opportunistic Traders lifted offers. By 14:08 CT, 36 minutes after the start, prices were back to pre-crash levels.
- In the Up phase high-frequency traders reduced inventory ahead of and with price increases.
- Scope record: horizon minutes; conditioning variable a volume spike with intermediaries' net inventory flat; sign full reversal within about 36 minutes; one event, no strategy, no costs.

## Signal construction
Two measurable features follow. (1) A churn ratio: gross traded volume divided by the absolute net change in aggregate positions over a short window. For perps, use taker volume over the absolute change in open interest. A very high ratio during a fast move says contracts are being passed around, not absorbed. (2) An absorption marker: the first interval after a fast move in which the opposite-side aggressor flow dominates, or a venue-level pause or circuit breaker. In this event the turn came within seconds of the pause. Both are hypotheses to test, not validated signals.

## Relevance to SOL perpetuals at minutes to hours
Crypto liquidation cascades share the anatomy: a large mechanical seller, thin intermediary inventory, a volume explosion, then a rebound when discretionary buyers arrive. Two differences matter. First, there is no co-ordinated pause across crypto venues, so the natural stopping point is the exhaustion of forced flow, which is harder to time. Second, in crypto the falling price itself creates more forced selling through liquidations, so the down phase can extend in a way a single finite sell program cannot. The paper supports reversal as the base case for a liquidity-driven crash but gives no rule for when to step in.

## Caveats
A single event in an index future with a fundamental anchor from the cash market. Trader classification is by observed behaviour and is partly circular. The version read is the 2014 working paper; the published version may differ in detail.
