---
title: "Supervised Autoencoders with Fractionally Differentiated Features and Triple Barrier Labelling Enhance Predictions on Noisy Data"
authors: "Slepaczuk, Robert; Bieganowski, Bartosz"
year: 2024
venue: "arXiv:2411.12753v2 (formatted for ICAIF-24, November 2024; proceedings publication not confirmed)"
url: "https://arxiv.org/pdf/2411.12753"
pdf: "sources/23-ml-feature-prediction/slepaczuk-2024-supervised-autoencoders-triple-barrier-crypto.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "23-ml-feature-prediction"
asset_class: "crypto"
horizon: "minutes"
tags: "triple-barrier, fractional-differentiation, supervised-autoencoder, noise-augmentation, walk-forward, bitcoin, ethereum, intraday-bars"
---

## Key insight
A crypto-specific application of the López de Prado toolkit at the bot's horizon: triple-barrier labels and fractionally differentiated features feed a supervised autoencoder network on 10, 20 and 30 minute bars of BTC, ETH and LTC. Over a 28-month out-of-sample period with a 5 basis point cost per fill, the strategies roughly matched or trailed buy-and-hold in raw return for BTC and ETH but with a third of the volatility and drawdown, and the 30-minute versions were the most stable.

## Method
Label at time t with barrier width lambda and maximum trade length n minutes: +1 if the maximum price over (t, t+n) reaches S_t(1 + lambda); -1 if the minimum reaches S_t(1 - lambda); 0 otherwise. Trades are assumed to carry a take-profit and stop-loss at the same barriers. Features are fractionally differenced with the smallest order d that passes an augmented Dickey-Fuller test at 1%, re-estimated on each training segment and applied to the following test segment. The model is a supervised autoencoder MLP: the bottleneck code is concatenated with the raw input and fed to a classifier, trained jointly on reconstruction and label loss, with Gaussian noise added to features in proportion to their historical volatility. Hyperparameters are chosen by a custom metric, Phi = (1 + lambda)^DCC x (1 - lambda)^DIC x (1 - lambda/delta)^TEC, where DCC, DIC and TEC count correct calls, incorrect calls and timed exits and delta is set to 20, so timed exits are mildly penalised. Validation is walk-forward with a training window capped at three periods.

## Data and sample
Binance 1-minute OHLC for bitcoin, ethereum and litecoin, January 2016 to April 2022, aggregated to 10, 20 and 30 minute bars; data before 2020 is used only for training, and January 2020 to April 2022 is out of sample. Six macro and commodity series (initial claims, WTI, natural gas, corn, gold, copper and aluminium futures) are added as features.

## Reported results
Out of sample, net of 0.05% per position open or close:
- Bitcoin: buy-and-hold total return 406.02%, annualised volatility 63.31%, maximum drawdown 53.30%. The 30-minute strategy had the highest information ratio (2.03), volatility 21.11% and drawdown 14.02%, with lower total return than buy-and-hold.
- Ethereum: buy-and-hold 1,929.01% total; the 20-minute strategy returned 1,658.93% with information ratio 2.64.
- Litecoin: buy-and-hold 118.92% total with 75.21% drawdown; the 30-minute strategy returned 382.49% with information ratio 2.11 and drawdown 25.88%. The 10-minute strategy underperformed.
- Equal-weight portfolio: 20-minute strategy 619.80% against 595.24% for buy-and-hold; the 30-minute strategy had information ratio 2.56 and drawdown 23.55% against 59.46%.
- The abstract states that moderate noise augmentation and bottleneck size help, while excessive noise and large bottlenecks hurt.

## Signal construction
On each bar compute the triple-barrier label for history with a fixed percentage barrier and a time limit; train a three-class classifier on stationary (fractionally differenced) price features; enter long or short on a class signal with a bracket order at the barriers, exit at whichever barrier is hit first. Select barrier width and time limit by walk-forward search on a profit-aware metric, not on accuracy.

## Relevance to SOL perpetuals at minutes to hours
The labeling scheme matches how a perp bot actually trades (entry with stop, target and time-out), and the 10 to 30 minute bar range is on target. The ordering of results (30 and 20 minute better than 10 minute) agrees with Jaquart, Dann and Weinhardt's finding that predictability net of costs improves with horizon. The barrier is a fixed percentage here; scaling it by current volatility, as in the original method, is the natural variant to test on SOL.

## Caveats
The out-of-sample window is the 2020 to 2021 bull run plus early 2022, and returns are compared with buy-and-hold instead of a simple trend rule, so directional skill is not isolated. Fills are assumed at the last close with no slippage, and barrier exits are assumed perfect; the authors list both as limitations. Macro series such as weekly jobless claims are odd inputs for 10-minute bars. No statistical tests or multiple-testing adjustment for the grid over bar size, noise level and bottleneck size.
