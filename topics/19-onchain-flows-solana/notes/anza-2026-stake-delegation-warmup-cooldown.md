---
title: "Stake Delegation and Rewards (Anza validator documentation; page title not confirmed)"
authors: "Anza"
year: 2026
venue: "Anza (Agave validator client) documentation"
url: "https://docs.anza.xyz/consensus/stake-delegation-and-rewards"
pdf: "none"
access: "full-text"
source_type: "documentation"
evidence_grade: "C"
topic: "19-onchain-flows-solana"
asset_class: "crypto"
horizon: "multi-day"
tags: "solana, staking, unstaking, warmup, cooldown, epoch-boundary, supply-schedule"
---

## Key insight
SOL cannot move from staked to liquid at will. Stake activates and deactivates only at epoch boundaries, and the protocol caps how fast total network stake can change, with the rate set to 25 percent per epoch in the current implementation. Unstaking is therefore visible on-chain before the coins become transferable, which gives a look-ahead on potential SOL supply that most assets lack.

## Method
Protocol documentation for the stake program in the Agave validator client. It describes mechanics; it contains no market analysis. The page is undated; the year in the front matter is the access year.

## Data and sample
Not applicable (specification).

## Reported results
Mechanics as stated on the page:
- Delegated stake passes through a warmup period in which part is "effective" and the rest "activating". Changes take place on epoch boundaries.
- The rate of change of total network stake is limited by the stake program's `warmup_rate`, "set to 25% per epoch in the current implementation". The amount that can warm up in an epoch depends on the previous epoch's total effective stake, the total activating stake and this rate.
- Worked example on the page, using a hypothetical 20 percent rate: 1,000 of stake activated at epoch N into a network of 2,000 is effective at 0, then 400, then 880, then 1,000 by epoch N+3.
- Cooldown mirrors warmup. Deactivating stake continues to earn rewards and remains exposed to slashing while it cools down.
- During warmup effectively nothing can be withdrawn; during cooldown, lamports above the effective stake can be withdrawn.
- Not stated on the page: the length of an epoch and the number of cooldown epochs in normal conditions.

## Signal construction
A supply-pipeline feature, to be tested:
- Inputs: the sum of stake in deactivating state, the sum in activating state, current epoch progress (slots remaining), and total effective stake, read from stake accounts via RPC.
- Features: `net_deactivating = deactivating - activating` as a fraction of circulating liquid SOL; `time_to_epoch_boundary`; a flag for unusually large single-account deactivations and who owns them (exchange, treasury company, ETF custodian, liquid-staking pool).
- Timing: the supply becomes liquid at the next epoch boundary, so the feature has a known release time.
- By the page's formula the cap matters only when the stake changing state is large relative to total effective stake; how many epochs a typical deactivation takes in practice was not stated and should be measured. Holders of liquid-staking tokens can exit by selling the token instead of unstaking (general background, not from the page), which weakens the look-ahead.

## Relevance to SOL perpetuals at minutes to hours
Specific to SOL and potentially useful at the hours scale around epoch boundaries: a known quantity of SOL becomes transferable at a known time. With about two thirds of supply staked (see [blockworks-2026](blockworks-2026-solana-tokenholder-report-q2.md)), swings in the deactivation queue can be large relative to exchange float. No source read in this session tests whether deactivation queues or epoch boundaries predict SOL returns or exchange inflows; this is an open, testable idea, not an established effect.

## Caveats
Documentation, so the evidence grade reflects that there is no empirical test at all. Parameters can change through governance, and the consensus redesign described in the Blockworks report may alter staking mechanics. Unstaked SOL is not necessarily sold; much of it is re-delegated or moved between validators. Epoch length was not confirmed here and must be read from the chain.
