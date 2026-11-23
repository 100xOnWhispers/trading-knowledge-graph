---
title: "Up or down? Short-term reversal, momentum, and liquidity effects in cryptocurrency markets"
authors: "Zaremba, Adam; Bilgin, Mehmet Huseyin; Long, Huaigang; Mercik, Aleksander; Szczygielski, Jan J."
year: 2021
venue: "International Review of Financial Analysis 78, 101908"
url: "https://ideas.repec.org/a/eee/finana/v78y2021ics1057521921002349.html"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "13-momentum-reversal"
asset_class: "crypto"
horizon: "daily"
tags: "short-term-reversal, daily-momentum, liquidity, cross-sectional, crypto"
---

## Key insight
The previous day's return is a strong cross-sectional predictor of coin returns, and its sign depends on liquidity. Across more than 3,600 coins, yesterday's losers beat yesterday's winners (daily reversal), which the authors attribute to illiquidity. Among the handful of largest and most tradeable coins the sign flips: they show daily momentum. The authors suggest this reconciles earlier conflicting findings of momentum and reversal in crypto.

## Method
Only the abstract was read. It describes cross-sectional tests and portfolio sorts on the prior-day return, with controls for a broad set of other return predictors, and a split by liquidity and size. Weighting scheme, liquidity measure and cost treatment were not confirmed.

## Data and sample
Daily prices for more than 3,600 coins. Period and data vendor not confirmed from the abstract.

## Reported results
From the abstract only:
- Coins with low prior-day returns significantly outperform coins with high prior-day returns.
- The effect is robust across cross-sectional tests and sorts and is not subsumed by other known predictors.
- The reversal is driven by illiquidity; the largest and most tradeable coins exhibit daily momentum instead of reversal.
No magnitudes were seen.

## Signal construction
Input: daily close-to-close return and a liquidity rank (dollar volume, spread or Amihud measure). Rule implied by the abstract: for illiquid coins, fade yesterday's return; for the most liquid coins, follow it. For a SOL bot the signal is simply the sign of yesterday's SOL return, with the expected sign conditional on which side of the liquidity divide SOL sits.

## Relevance to SOL perpetuals at minutes to hours
This is the cleanest statement of the liquidity rule that organises the crypto momentum-versus-reversal literature: liquid means continuation, illiquid means reversal. SOL on Binance, Bybit or Hyperliquid is among the most liquid coins, so the expected daily sign is momentum. The same asset on a new, thin venue is a different matter: price moves on Kalshi that are not matched on the large venues are more likely illiquidity-driven and should be expected to revert toward the reference price. That cross-venue reading is an inference to test, not a result of the paper.

## Caveats
Abstract-only; no magnitudes, costs or dates confirmed. Daily reversal in illiquid coins is largely a bid-ask bounce and stale-price effect that cannot be captured after costs; Bianchi, Babiak and Dickerson (2022) reach a compatible conclusion with explicit volume conditioning. Whether "largest coins show daily momentum" still holds after 2021 needs re-testing.
