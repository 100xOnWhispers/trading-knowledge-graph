---
title: "From Locked to Liquidity: What 16,000+ Token Unlocks Teach Us"
authors: "Keyrock (authors not listed)"
year: 2024
venue: "Keyrock research (company website)"
url: "https://keyrock.com/from-locked-to-liquidity-what-16000-token-unlocks-teach-us/"
pdf: "none"
access: "full-text"
source_type: "industry-research"
evidence_grade: "C"
topic: "19-onchain-flows-solana"
asset_class: "crypto"
horizon: "multi-day"
tags: "token-unlocks, vesting, supply-events, team-unlocks, hedging, event-study, sol, jup"
---

## Key insight
Scheduled token unlocks are known in advance, yet prices tend to weaken for about 30 days before a large unlock and stabilise about 14 days after. Who receives the tokens matters more than how many are released: team unlocks are the worst, ecosystem-development unlocks are roughly neutral to positive, and investor unlocks are mild, which the authors attribute to hedging and OTC distribution.

## Method
Each vesting schedule is split into discrete unlock events, classified by size as a share of supply (nano under 0.1 percent, micro 0.1 to 0.5, small 0.5 to 1, medium 1 to 5, large 5 to 10, huge over 10 percent) and by recipient category (team, investors, ecosystem development, public or community, and others). Daily prices are tracked from 30 days before to 30 days after each event. A baseline of median price and volatility is taken from the month before the pre-unlock window, to handle back-to-back linear unlocks. Prices are normalised against ETH to remove market beta.

## Data and sample
More than 16,000 unlock events across 40 tokens; named examples include APE, OP, ARB, SOL and JUP. The sample period and the price and schedule data sources are not stated. The publication date is not stated on the page; image paths are dated December 2024.

## Reported results
The text gives few exact numbers; most per-bucket results are in charts.
- About 90 percent of unlocks create negative price pressure.
- Larger unlocks produce sharper drops, summarised as "2.4x"; the baseline for this multiple is not defined. The link between size and impact weakens beyond seven days. Huge unlocks did no worse than large ones.
- For large unlocks, price drifts down over the prior 30 days and faster in the final week, then stabilises within roughly 14 days. Volume tends to peak 14 or 28 days before.
- Team unlocks: the largest drawdowns, summarised as -25 percent.
- Ecosystem-development unlocks: +1.18 percent on average, the only consistently positive category.
- Investor unlocks (106 events): slow, small declines.
- More than USD 600 million of tokens unlock each week.
- Case study: APE fell 77 percent over the seven months after team unlocks began, against 9 percent for ETH.

## Signal construction
- Inputs: a token unlock calendar with size as a percentage of circulating supply and recipient category.
- Features: `days_to_next_large_unlock`, `unlock_size_pct`, `recipient_category`, and a flag for an active linear team-vesting period.
- The report's own rule: reduce exposure about 30 days before a major unlock and re-enter about 14 days after.
- This is a slow bias or risk filter, updated daily, not an intraday trigger.

## Relevance to SOL perpetuals at minutes to hours
SOL itself has no large recurring cliff of the type studied; its supply events are inflation, staking and unstaking at epoch boundaries, and one-off releases of locked stake held by large holders (no source on the size or schedule of these was read in this session). The report is more useful for tokens in the Solana ecosystem (JUP and others), whose unlocks can affect SOL through sentiment and DEX activity. For the reference instrument the practical use is a calendar flag that raises caution around known large SOL releases; the 30-day drift is far outside the trading horizon.

## Caveats
Published by a market maker that sells hedging, OTC and options services to token holders, so the framing favours hedged, managed unlocks. Sample period undisclosed; no statistical tests, confidence intervals or cost-adjusted backtest. Normalising by ETH does not remove sector effects. Overlapping linear unlocks confound the pre-event window, as the authors admit. If altcoins broadly fell against ETH during the undisclosed sample, every category would be biased negative regardless of unlocks.
