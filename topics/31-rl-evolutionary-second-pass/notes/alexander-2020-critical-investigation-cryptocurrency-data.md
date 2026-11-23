---
title: "A critical investigation of cryptocurrency data and analysis"
authors: "Alexander, Carol; Dakos, Michael"
year: 2020
venue: "Quantitative Finance 20(2), 173-188"
url: "https://econpapers.repec.org/RePEc:taf:quantf:v:20:y:2020:i:2:p:173-188"
pdf: "none"
access: "abstract-only"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "31-rl-evolutionary-second-pass"
asset_class: "crypto"
horizon: "n/a"
tags: "data-quality, crypto-data-sources, non-traded-prices, replication, training-data"
---

## Key insight
The only text of this paper that could be read in this session is the one-sentence abstract on its RePEc record: "Less than half the crytocurrency papers published since January 2017 employ correct data" (spelling as in the record). The claim is that a majority of the empirical crypto literature of that period rests on flawed price series. Everything beyond that sentence in this note is marked as not confirmed.

## Method
Not confirmed from the source. The RePEc record gives only the abstract sentence, the journal reference and the DOI (10.1080/14697688.2019.1641347). A search-result summary of the University of Sussex repository entry (a secondary description, not opened) said the paper compares data sources and reports that market betas of major coins differ markedly depending on the source. The repository copy returned HTTP 403 to a direct request and the publisher page is paywalled.

## Data and sample
Not confirmed. The abstract sentence refers to papers published since January 2017.

## Reported results
From the abstract only: fewer than half of cryptocurrency papers published since January 2017 use correct data. No other number was read.

## Signal construction
Not a signal. Its use here is as a pointer for the data-audit step: before training anything, establish for each input series whether it is a traded price on a named venue, a composite index, or an aggregator's average, and which timestamp convention it uses.

## Relevance to SOL perpetuals at minutes to hours
Indirect. RL and evolutionary methods are very sensitive to data artifacts because they optimize against whatever regularities the series contains, including those created by averaging across venues, stale quotes or mismatched timestamps. The bot's inputs should be venue-level traded prices and books with exchange timestamps, and any published crypto result it relies on should be checked for which data source it used. The specific guidance of this paper on which sources are sound could not be read and should not be assumed.

## Caveats
Abstract-only note; the grade reflects the journal and not content that was verified. The assessment in the paper dates from 2019 and concerns data vendors and aggregators of that time. A related lead on survivorship and delisting bias in crypto universes (Ammann, Burdorf, Liebi and Stockl, SSRN 4287573) could not be opened at all (SSRN returned HTTP 403), so no note exists for it.
