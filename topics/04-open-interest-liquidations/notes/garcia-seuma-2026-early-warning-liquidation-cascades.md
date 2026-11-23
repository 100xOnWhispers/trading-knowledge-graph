---
title: "Where does the criticality live? Early-warning signals are event-heterogeneous across seven crypto-perpetual liquidation cascades"
authors: "Garcia Seuma, Ramon Marc"
year: 2026
venue: "arXiv preprint 2607.27070"
url: "https://arxiv.org/pdf/2607.27070"
pdf: "sources/04-open-interest-liquidations/garcia-seuma-2026-early-warning-liquidation-cascades.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "04-open-interest-liquidations"
asset_class: "crypto"
horizon: "hours"
tags: "early-warning, critical-slowing-down, open-interest, taker-flow, cascades, negative-result, placebo-test"
---

## Key insight
A direct test of whether liquidation cascades announce themselves in price, open interest, positioning or order flow. Across seven major BTC cascades no single variable gives a consistent early-warning signal, and the attractive pattern found in October 2025 (rising autocorrelation in open interest and flow but not in price) inverts when tested on August 2024. The only regularity that survives all events and a placebo test is a fall in the variance of the taker buy/sell ratio before the cascade, and it is too weak to act as a per-event alarm.

## Method
For each series `x_t` (log price, log open interest, log long/short ratios, log taker buy/sell ratio) the residual is `r_t = x_t - trailing mean over w_d`, using a causal window. Rolling variance and lag-1 autocorrelation of `r_t` are computed over a shorter window `w_r`, and their trend into the cascade onset is measured with Kendall's tau over a pre-window of 1 to 3 days. A grid of 39 configurations (detrend about 2 to 16 hours, roll about 0.5 to 4 hours) is swept and the share of configurations with a positive, significant trend is reported. Onset is the minute ending the most negative 60-minute log return on the documented crash day. The surviving result is tested against 300 placebo onsets from ordinary windows.

## Data and sample
Binance USD-margined BTCUSDT perpetual, about two months around each of seven cascades: May 2022, November 2022, August 2024, December 2024, February 2025, April 2025 and October 2025. One-minute klines and 5-minute public metrics (open interest, top-trader and global long/short ratios, taker buy/sell ratio), plus a daily panel of liquidations. Intraday liquidation snapshots are no longer served by Binance, so liquidations are observed only through their consequences.

## Reported results
- 10 October 2025 was the largest long-liquidation day in the Binance BTC sample at USD 1.05 billion against about USD 130 million the day before; intraday open interest fell 24.6%. Daily long liquidations have a Gini coefficient of 0.677.
- October 2025: lag-1 autocorrelation trend positive and significant in 4 of 39 configurations for price, 23 of 39 for open interest, 29 of 39 for taker ratio.
- August 2024: 28 of 39 for price, 3 of 39 for open interest, 1 of 39 for taker ratio.
- Price carries the signature in five of seven events (0.67 to 0.85 of configurations) and is absent in February and October 2025, both sudden tariff-news shocks.
- Rising variance appears for nearly every variable in nearly every event and is judged non-specific.
- Taker-ratio variance falls before all six events with data (median tau -0.13 to -0.44); four are below the 5th percentile of the placebo distribution; sign test p about 0.014, Fisher-combined p about 5e-6.

## Signal construction
Candidate feature: rolling variance of the detrended log taker buy/sell ratio at 5-minute resolution, with its Kendall trend over the past 1 to 3 days; a persistently falling value means aggressive flow has become one-sided. Open interest autocorrelation and variance trends are documented as unreliable and should not be used alone.

## Relevance to SOL perpetuals at minutes to hours
This is the strongest caution in the topic against building a "leverage build-up predicts a cascade" rule from one episode. The inputs are free and available for SOL on Binance, so the test can be replicated on SOL directly. The result argues for treating open interest as a conditioning variable for move size and for position sizing, not as a timing signal.

## Caveats
Single author, not peer-reviewed, seven events, one venue, BTC only. The placebo windows come from the same files as the events. Funding-cycle periodicity is not removed. The endogenous versus exogenous typing is a hypothesis from two exceptions.
