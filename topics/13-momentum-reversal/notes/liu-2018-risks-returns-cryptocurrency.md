---
title: "Risks and Returns of Cryptocurrency"
authors: "Liu, Yukun; Tsyvinski, Aleh"
year: 2018
venue: "NBER Working Paper 24877"
url: "https://www.nber.org/system/files/working_papers/w24877/w24877.pdf"
pdf: "sources/13-momentum-reversal/liu-2018-risks-returns-cryptocurrency.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "B"
topic: "13-momentum-reversal"
asset_class: "crypto"
horizon: "daily"
tags: "crypto-momentum, time-series-momentum, investor-attention, bitcoin, daily, weekly"
---

## Key insight
Bitcoin, Ripple and Ethereum returns have no meaningful exposure to equity, currency, commodity or macro factors, but they are predictable from crypto-specific variables: their own past returns and investor attention. Time-series momentum shows up at daily and weekly frequencies, which is far shorter than the monthly horizons documented in traditional assets.

## Method
Standard empirical asset-pricing regressions. For momentum, the current daily (weekly) return is used to predict returns 1 to 7 days (1 to 8 weeks) ahead. Weekly returns are also grouped into quintiles and the subsequent returns of each group compared. A version fixes the quintile cut-offs on the first two years of data to avoid look-ahead. Attention proxies are Google searches and Twitter post counts.

## Data and sample
CoinDesk prices. Bitcoin 1 January 2011 to 31 May 2018; Ripple from 4 August 2013; Ethereum from 7 August 2015. Daily and weekly returns.

## Reported results
(From the working-paper version read; the paper was later published in the Review of Financial Studies, details not confirmed in this session.)
- Bitcoin daily: today's return significantly and positively predicts returns 1, 3, 5 and 6 days ahead. A one-standard-deviation rise in today's return (5.55%) predicts a 0.33% higher return the next day (coefficient 0.06).
- Bitcoin weekly: this week's return predicts returns 1 to 4 weeks ahead; a one-standard-deviation rise (16.64%) predicts a 3.16% higher return next week (coefficient 0.19).
- Quintiles: at the 1-week horizon the top quintile of past weekly returns averages 11.22% per week (Sharpe 0.45) against 2.60% (Sharpe 0.19) for the bottom quintile.
- The effect is somewhat smaller in the post-2013 sample and survives the no-look-ahead quintile design.
- Ripple: significant at 1 to 5 days. Ethereum: weaker, significant at 1 and 5 days, with the 5-day coefficient negative.
- High Google search interest predicts higher returns over 1 to 2 weeks for Bitcoin.

## Signal construction
Inputs: daily or weekly close. Signal = sign or z-score of the last 1-day and 1-week return; hold 1 day to 1 to 4 weeks. An attention overlay would use Google Trends at weekly frequency. This is a slow regime input for an intraday bot, not an entry trigger.

## Relevance to SOL perpetuals at minutes to hours
Establishes that crypto trends at daily to weekly horizons, so a daily or weekly trend state is a reasonable conditioning variable for intraday trade direction. Nothing here tests SOL, perpetuals, or horizons under one day. Ethereum already looked weaker than Bitcoin, which is a warning that the effect is not uniform across coins.

## Caveats
Sample ends May 2018 and is dominated by the 2013 and 2017 bubbles; the daily coefficient of 0.06 is small. Regressions, not a costed strategy. Later work (Dobrynskaya; Fieberg et al.; Zaremba et al.) finds the sign depends on horizon and liquidity. Momentum in a sample with huge positive drift is hard to separate from the drift itself (see Huang et al. 2020).
