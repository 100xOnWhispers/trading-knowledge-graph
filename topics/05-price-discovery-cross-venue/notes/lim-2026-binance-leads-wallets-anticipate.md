---
title: "Binance Leads, but Some Wallets Anticipate: Wallet-Level Cross-Venue Informed Flow in BTC Perpetual Futures"
authors: "Lim, Boon Chuan"
year: 2026
venue: "Research Square preprint (posted July 6, 2026)"
url: "https://www.researchsquare.com/article/rs-10147582/v1.pdf"
pdf: "sources/05-price-discovery-cross-venue/lim-2026-binance-leads-wallets-anticipate.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "05-price-discovery-cross-venue"
asset_class: "crypto"
horizon: "seconds"
tags: "hyperliquid, binance, perpetuals, information-share, lead-lag, wallet-level, informed-flow, on-chain"
---

## Key insight
In mid-2026 BTC perpetuals, Binance leads Hyperliquid in every tested window and holds the majority Hasbrouck information share under both orderings. Even the most "informed" Hyperliquid wallets follow Binance on average. A persistent minority of wallets, however, trade ahead of Binance moves, and this ranking survives a split-sample test, so on-chain wallet identity carries information that venue-level averages hide.

## Method
Venues are aligned on their own event timestamps, not receipt times. Venue level: cross-correlation of 5-second grid log-returns at leads and lags, and a bivariate VECM with cointegrating vector (1, -1) and one lag, reporting Hasbrouck information share bounds from both Cholesky orderings; a transaction-time re-estimation checks stale-fill bias. Wallet level: signed forward markouts on Hyperliquid, adjusted for same-day drift, rank wallets; the top quintile of persistent wallets forms the informed cohort. For each cohort trade the signed Binance mid move over h seconds before (pre) and after (post) is computed; a wallet's lead score is post minus pre. Persistence is tested by Spearman rank correlation of lead scores between sample halves; a shuffled-direction placebo is run.

## Data and sample
Binance USD-margined BTC perpetual book snapshots (about 1 s spacing) and Hyperliquid BTC perpetual trades and book (about 4 s spacing after cleaning), May 25 to June 22, 2026; about 13.2 million Hyperliquid trades in the analysis window.

## Reported results
- Receive lag: Binance median about 0 ms; Hyperliquid median about 479 ms with a tail near 2 s.
- Of 580 one-hour windows, Binance leads in 400 (69.0%), contemporaneous at grid resolution in 177 (30.5%), Hyperliquid leads in 3 (0.5%).
- Binance information share bounds in four windows: [59.1%, 97.3%], [55.5%, 99.1%], [85.4%, 100.0%], [77.0%, 96.7%]. In transaction time: [68.4%, 77.1%], [63.0%, 83.0%], [63.0%, 81.8%].
- A 250 ms grid gives an implausible 99.7% Binance share from stale-filling and is excluded.
- Informed cohort (658 wallets, 2,337,051 trades): Binance moves +1.731 / +2.043 / +2.371 bps before versus +0.604 / +0.654 / +0.720 bps after cohort trades at 2 / 5 / 10 s.
- 156 of 644 wallets show a lead tilt; 59 are "clean anticipators". Half-to-half Spearman correlations of lead scores: +0.477, +0.548, +0.532.

## Signal construction
(1) Leader feed: use Binance perp mid returns over the last 1 to 10 s as the reference for where Hyperliquid (and slower venues) will go. (2) Wallet filter: on a trailing window, compute each Hyperliquid wallet's lead score L_w(h) = post_w(h) - pre_w(h) against Binance mids; keep the top quintile with enough trades; the net signed flow of those wallets over the last few seconds to minutes is a candidate directional feature. Refresh rankings weekly.

## Relevance to SOL perpetuals at minutes to hours
Confirms the venue hierarchy the bot should assume: Binance first, on-chain perp DEX second, a small new venue presumably after both. The wallet-level idea is the novel part: Hyperliquid SOL perp wallets that persistently anticipate Binance could be tracked as an input. Needs re-testing on SOL, at longer horizons than 10 s, and net of the bot's own latency.

## Caveats
Single independent author, non-peer-reviewed preprint, one asset, 29 days. Markouts are gross of fees and spread; effects are fractions of a basis point to a few basis points. The 5-second grid cannot resolve the true lag. Wallets are not legal identities and can be rotated. Information share bounds are wide.
