---
title: "Leverage Causes Fat Tails and Clustered Volatility"
authors: "Thurner, Stefan; Farmer, J. Doyne; Geanakoplos, John"
year: 2010
venue: "arXiv preprint 0908.1555v2 (journal version cited by later papers as 2012; journal not confirmed in this session)"
url: "https://arxiv.org/pdf/0908.1555"
pdf: "sources/04-open-interest-liquidations/thurner-2010-leverage-fat-tails-clustered-volatility.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "04-open-interest-liquidations"
asset_class: "multi"
horizon: "n/a"
tags: "leverage-cycle, margin-calls, fat-tails, volatility-clustering, agent-based-model"
---

## Key insight
Leverage limits alone are enough to produce heavy-tailed returns and volatility clustering, even when every investor is a stabilizing value buyer and the news process is normal and independent. A leverage cap forces funds to sell into a falling market, and when many funds hit the cap together the forced selling amplifies the fall. The effect appears at all time scales, with crashes as the extreme case.

## Method
An agent-based simulation with one risky asset, noise traders, and leveraged value funds that borrow from a bank. Each fund buys when the asset is under-priced, with demand scaled by an aggression parameter, subject to a maximum leverage. When the price falls and a fund's leverage exceeds the maximum, it must sell to repay part of its loan (a margin call). Investors move capital into and out of funds based on an exponential moving average of recent performance, so high-leverage funds attract capital in good times. The authors simulate tens of thousands of periods and compare return distributions with and without leverage.

## Data and sample
Simulated data only. The abstract and introduction motivate the model with pre-2008 leverage levels (the text cites 60-to-1 on AAA mortgage securities in 2006) but no market data are fitted in the pages read.

## Reported results
From the abstract and introduction: without borrowing, price fluctuations are approximately normal and uncorrelated in time. As leverage rises, fluctuations become heavy-tailed with clustered volatility, producing a power law of price disturbances. A volatility-based leverage limit (the bank lends more when volatility is low and less when it is high) makes the extreme fluctuations worse, because leverage rises in calm periods and contracts quickly when volatility increases. A fund at leverage lambda loses lambda percent of its equity for each one percent price drop and must raise (lambda minus 1) over lambda of new cash per dollar of price decline. Specific tail exponents were not extracted for this note.

## Signal construction
Not a signal. It supplies two design ideas for a bot: (1) treat aggregate leverage (open interest relative to collateral or to depth) as the amplifier that conditions how large a move a given shock can become; (2) expect the most leverage to accumulate in quiet, low-volatility regimes, so a low-volatility, high-open-interest state is the dangerous one.

## Relevance to SOL perpetuals at minutes to hours
The mechanism is the same one that perp liquidation engines mechanize: a hard leverage cap enforced by forced selling. The statement that the effect appears on fast time scales supports looking for it at minutes to hours. The volatility-linked leverage result is a warning about cross-margin and tiered-margin systems that allow more leverage in calm markets. What does not transfer: the model has long-only funds, a single asset and a patient bank; perps have both long and short liquidations, cross-venue arbitrage and insurance funds. The empirical cascade papers in this topic find that realized cascades were subcritical within a venue, which limits how literally the runaway-feedback picture should be taken.

## Caveats
A stylized simulation, not an empirical test. Parameter choices drive the tail behavior. The note is based on the arXiv version; the peer-reviewed version was not opened.
