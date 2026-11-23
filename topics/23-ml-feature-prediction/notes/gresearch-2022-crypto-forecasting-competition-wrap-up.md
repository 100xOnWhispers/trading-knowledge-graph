---
title: "Wrapping up the G-Research Crypto Forecasting Competition"
authors: "G-Research"
year: 2022
venue: "G-Research news post, 30 May 2022"
url: "https://www.gresearch.com/news/wrapping-up-the-g-research-crypto-forecasting-competition/"
pdf: "none"
access: "full-text"
source_type: "industry-research"
evidence_grade: "D"
topic: "23-ml-feature-prediction"
asset_class: "crypto"
horizon: "minutes"
tags: "kaggle, lightgbm, feature-engineering, live-evaluation, weighted-correlation, competition"
---

## Key insight
In the largest public contest on short-horizon crypto return forecasting, judged on three months of live data after submissions were frozen, all three top finishers used LightGBM, and all said feature engineering mattered far more than model development. The organiser describes the data as very noisy with large leaderboard swings. This is the closest thing to a prospective, out-of-sample test of the "boosted trees on engineered features" approach in crypto, though the post gives almost no technical detail.

## Method
A Kaggle competition run by the quantitative trading firm G-Research. Participants built models on historical data to forecast short-term returns of 14 crypto coins. Scoring used a weighted Pearson correlation between predictions and realised returns. After a three-month development phase each team chose two models, which then ran for three months against live market data to produce the final ranking. The post does not describe the target construction, data fields, bar frequency or any validation scheme; from memory the data were one-minute bars and the target a 15-minute residualised return, but that was not confirmed on a page I could open (the Kaggle pages did not render to the fetch tool).

## Data and sample
Historical crypto market data for 14 coins supplied by the organiser. Competition launched late 2021 and concluded May 2022. The number of teams is not stated in the post.

## Reported results
- Winners: first, the team Meme Lord Capital (two members, 50,000 USD prize); second, Nathaniel Maddux; third, GABA. The top ten shared a 125,000 USD pool.
- "All of our top three used a LightGBM model", though some experimented with other approaches including neural networks.
- Developing and testing features had "a far greater impact on their final scores than model development"; the winners spent most of their time on it.
- The leaderboard showed many large jumps and drops, especially early in the live phase.
- No scores, feature lists or hyperparameters are given.

## Signal construction
Not a signal. The transferable recipe is the competition design itself: freeze the model, then score it on a correlation metric over a live forward period before trusting it. The model class it points to is a gradient-boosted tree regressor on hand-built features across a panel of coins, with a target that removes the market-wide move.

## Relevance to SOL perpetuals at minutes to hours
Solana was, to my recollection, among the 14 assets, but that is not stated in the post. The useful points are qualitative: boosted trees remained the practical winner over neural networks on minute-bar crypto data as of 2022; effort is best spent on features; and three months of live evaluation produced unstable rankings, which implies that a short paper-trading period cannot distinguish a good model from a lucky one. The winning correlation levels, which would calibrate how much signal exists, are not reported.

## Caveats
A promotional post by the sponsor that ends with a recruitment pitch; the statements about methods are the winners' self-reports as relayed by the organiser. No numbers. A correlation metric ignores costs and execution, so even the winners' models were never shown to be profitable. The winners' own write-ups on Kaggle were not accessible in this session and remain the primary source to read.
