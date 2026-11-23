---
title: "PreBit - A multimodal model with Twitter FinBERT embeddings for extreme price movement prediction of Bitcoin"
authors: "Zou, Yanzhao; Herremans, Dorien"
year: 2022
venue: "arXiv:2206.00648 (preprint marked as accepted in Expert Systems with Applications, vol. 233)"
url: "https://arxiv.org/pdf/2206.00648"
pdf: "sources/18-positioning-sentiment/zou-2022-prebit-multimodal-twitter-finbert.pdf"
access: "full-text"
source_type: "peer-reviewed"
evidence_grade: "B"
topic: "18-positioning-sentiment"
asset_class: "crypto"
horizon: "daily"
tags: "machine-learning, finbert-embeddings, twitter, svm, cnn, extreme-moves, ablation, class-imbalance"
---

## Key insight
Adding Twitter text (as FinBERT sentence embeddings, not a sentiment score) to a price-and-technical-indicator model modestly improves prediction of next-day large upward Bitcoin moves, and does not help for downward moves. A model on tweets alone performs worst. The improvement is not statistically significant under a Diebold-Mariano test, as the authors acknowledge. Text is a marginal complement to price features, not a replacement.

## Method
Four binary tasks: will the next-day close be up more than 5%, down more than 5%, up more than 2%, down more than 2%. Three model families:
- TA SVM: support vector machine on OHLCV candles, technical indicators and correlated asset prices (Ethereum, gold and others), tuned by grid search with 4-fold cross-validation on F1.
- Twitter CNN: a convolutional network over FinBERT sentence embeddings of the day's tweets.
- Fusion: the SVM output fused with the text CNN (parallel and sequential variants).
Baselines are a uniform random classifier and a stratified random classifier, each simulated 1,000 times for 95% intervals. A long-only backtest buys at the close when an up-5% move is predicted and sells at the next close, with probability thresholds from 0.5 to 0.99.

## Data and sample
Up to 5,000 tweets per day containing "Bitcoin", 1 January 2015 to 31 May 2021 (9,435,437 tweets, released publicly). Daily price data from the same period; 2,337 daily rows after cleaning. Test set is the final year, 1 June 2020 to 31 May 2021 (365 days). Positive class share in the test set is 16.44% for the 5% tasks and about 46% to 48% for the 2% tasks.

## Reported results
- Up 5%: TA SVM positive-class F1 0.26 and accuracy 71.23%; Twitter CNN (parallel) F1 0.28, accuracy 59.22%; Fusion (sequential) F1 0.38, accuracy 73.70%. Stratified baseline F1 0.16, accuracy 72.49% (interval 69.86 to 75.34). The fusion model roughly doubles recall (0.50 against 0.22) at the same precision (0.31 against 0.32).
- Down 5%: TA SVM and Fusion (sequential) are identical at F1 0.33 and about 81.4% accuracy. Tweets add nothing.
- Down 2%: all models between 53% and 57% accuracy against about 50% for random.
- The authors report that Diebold-Mariano p-values do not reject the null of equal performance.
- Ethereum price and 20-day volatility are the features most correlated with next-day Bitcoin price.

## Signal construction
Inputs: the interval's posts about the asset, OHLCV, technical indicators, correlated asset prices. Embed each post with a finance-tuned sentence encoder, pool through a small CNN, fuse with a price-feature classifier, output probability of a large move. Trade only above a high probability threshold (0.95 or 0.99 in the paper) to trade precision for frequency. Retrain periodically; daily update in the paper.

## Relevance to SOL perpetuals at minutes to hours
Three lessons transfer: use embeddings of raw text instead of a single sentiment number, always run a price-only ablation to measure what text adds, and evaluate against a stratified baseline when predicting rare large moves. The asymmetry (text helps for upside, not downside) matches the idea that hype is more visible in social text than fear is. The daily horizon and Bitcoin-only sample do not transfer; an hourly SOL version would need a far faster text pipeline.

## Caveats
Backtest assumes no fees, no slippage and full liquidity. One test year (mid-2020 to mid-2021) that was a strong bull market, which flatters a long-only up-move predictor. Random 5,000-tweet daily samples contain bots. No statistical significance for the headline improvement.
