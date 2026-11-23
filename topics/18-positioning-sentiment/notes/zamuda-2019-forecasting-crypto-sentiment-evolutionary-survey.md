---
title: "Forecasting Cryptocurrency Value by Sentiment Analysis: An HPC-Oriented Survey of the State-of-the-Art in the Cloud Era"
authors: "Zamuda, Ales; Crescimanna, Vincenzo; Burguillo, Juan C.; Dias, Joana Matos; Wegrzyn-Wolska, Katarzyna; Rached, Imen; Gonzalez-Velez, Horacio; Senkerik, Roman; Pop, Claudia; Cioara, Tudor; Salomie, Ioan; Bracciali, Andrea"
year: 2019
venue: "High-Performance Modelling and Simulation for Big Data Applications, LNCS 11400, pp. 325-349 (Springer, open access)"
url: "https://norma.ncirl.ie/3752/1/Forecasting%20cryptocurrency%20value%20by%20sentiment%20analysis%20chapter.pdf"
pdf: "sources/18-positioning-sentiment/zamuda-2019-forecasting-crypto-sentiment-evolutionary-survey.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "C"
topic: "18-positioning-sentiment"
asset_class: "crypto"
horizon: "n/a"
tags: "survey, sentiment-analysis, differential-evolution, genetic-algorithms, multi-objective-portfolio, feature-selection, tweet-filtering"
---

## Key insight
This position survey is one of the few sources that places sentiment analysis and evolutionary optimization in the same crypto pipeline. It frames the problem as a chain of challenges: collecting and annotating social feeds, filtering tweets, selecting text features, building sentiment indicators, combining them with technical analysis, and then choosing a portfolio with multi-objective metaheuristics such as Differential Evolution and genetic algorithms. It contains no new empirical test. Its value is as a map of design choices and as evidence that, as of 2019, evolutionary methods were applied to portfolio weights and rule parameters, not to sentiment signals themselves.

## Method
Literature survey organized as lettered "specific challenges" (portfolio selection is Challenge H), with a cloud and high-performance-computing perspective on the compute each stage requires. Sections cover: market sentiment dictionaries for social media (for example a public dictionary of 8,331 words, 112 hashtags and 115 emojis built from StockTwits posts); tweet preprocessing split into transformation and filtering; feature selection metrics such as chi-squared; technical analysis; ranking of initial coin offerings; and multi-objective cryptocurrency portfolio selection.

## Data and sample
None of its own. It cites datasets used by others, including a StockTwits set of 334,798 labelled posts from 13,059 users and the FiQA 2018 task with 675 training instances.

## Reported results
Only statements from the surveyed literature, as summarized in the chapter:
- Sentiment dictionaries built from investor posts show that an investor's expressed sentiment can depend on the position held, so positive investor sentiment does not necessarily imply bullish market sentiment.
- Trading rules whose parameters are tuned by a genetic algorithm are cited as prior practice, with roots in foreign-exchange work.
- For portfolio selection, the chapter cites reviews of evolutionary algorithms for multi-objective portfolio management, a genetic algorithm that includes transaction costs, and a comparison of five multi-objective evolutionary algorithms in which SPEA2 "seems to be better" while all multi-objective approaches beat single-objective ones.
- A cited copula-based multiperiod portfolio study uses Differential Evolution and states that the freedom to rebalance is advantageous given crypto volatility; another cited study adds "market psychology" evaluated by fuzzy reasoning to the rebalancing decision.
No performance numbers for a sentiment-driven evolutionary strategy are given.

## Signal construction
Not a signal. It is used as a design checklist: (1) build or adopt a finance-specific sentiment lexicon including emojis and hashtags; (2) filter and deduplicate posts before scoring; (3) select text features with an explicit metric; (4) treat strategy and portfolio parameters as a multi-objective search (return, risk, turnover) that an evolutionary algorithm can explore, keeping the Pareto front instead of a single optimum.

## Relevance to SOL perpetuals at minutes to hours
Indirect. For a single-instrument bot the portfolio material does not apply, but the multi-objective framing does: thresholds on sentiment, attention and positioning features can be searched jointly against return, drawdown and trade count. The observation that posted sentiment depends on the poster's position is relevant to reading perp-trader chatter, where longs talk their book. Empirical evolutionary work on trading rules is covered in topics 07, 08, 13 and 16; none of those notes use sentiment or positioning inputs.

## Caveats
A 2019 survey chapter from a networking project, broad and uneven, with no experiments. The literature it covers predates transformer language models and the perp-dominated market. Evolutionary search over many signal thresholds is a strong data-snooping risk unless paired with walk-forward validation and multiple-testing control.
