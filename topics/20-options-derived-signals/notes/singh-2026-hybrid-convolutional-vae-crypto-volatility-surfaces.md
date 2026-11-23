---
title: "Beyond the Smile: A Hybrid Convolutional VAE for Crypto Volatility Surfaces"
authors: "Singh, Sadanand; Reddy, Allam; Chopra, Manan"
year: 2026
venue: "arXiv preprint 2606.16961"
url: "https://arxiv.org/abs/2606.16961"
pdf: "sources/20-options-derived-signals/singh-2026-hybrid-convolutional-vae-crypto-volatility-surfaces.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "C"
topic: "20-options-derived-signals"
asset_class: "crypto"
horizon: "hours"
tags: "implied-volatility-surface, variational-autoencoder, machine-learning, surface-completion, anomaly-detection, cross-asset-transfer, binance-options"
---

## Key insight
A small convolutional variational autoencoder trained on hourly BTC and ETH implied-volatility surfaces fills in missing parts of a surface far better than a per-maturity smile fit when whole maturities or wings are unquoted, and a model trained on one coin transfers to the other with modest loss. The same model's reconstruction error rises during known dislocations, giving an unsupervised "the surface looks abnormal" indicator. This is machine learning applied to building option-derived inputs, not to predicting prices.

## Method
Each hourly option chain is converted to a fixed 6 by 7 grid (six maturities, seven deltas) by a quadratic-in-log-moneyness smile fit per expiry and interpolation across expiries. A masked-input VAE (three 3x3 convolutional layers, latent dimension 16, about 318 thousand parameters) is trained to reconstruct hidden cells. A routing rule uses the ordinary smile re-fit whenever a maturity row still has at least three observed cells and the VAE otherwise. Baselines: smile re-fit alone, a principal-component completion, a multilayer perceptron and a self-attention model. Splits are time-ordered 70/15/15. Static no-arbitrage (calendar and butterfly) is checked at the grid strikes.

## Data and sample
Public Binance Options end-of-hour archive, BTC and ETH, May to October 2023 (147 days); 6,034 fully filled hourly surfaces (2,821 BTC and 3,213 ETH across train, validation and test).

## Reported results
- Hidden-cell error of 0.94 to 1.56 volatility points across both coins and mask rates of 10% to 50%.
- At 50% random masking the hybrid reaches 0.83 points against 7.00 for the smile re-fit alone.
- When an entire maturity row is removed, the smile re-fit errs by 9.6 to 13.1 points and the VAE by 1.5 to 1.9.
- A BTC-only model evaluated on ETH is within 5% to 27% of in-sample accuracy; joint training improves both coins by 9% to 27% over the better single-coin model.
- The smile re-fit alone admits butterfly arbitrage on 38.9% (BTC) and 33.1% (ETH) of reconstructions at 50% masking; the hybrid output is arbitrage-free at the listed strikes.
- Reconstruction error is elevated around the 17 August 2023 flash crash and the late-October 2023 rally.

## Signal construction
Two uses for a bot:
1. Surface completion for thin underlyings: train on BTC and ETH grids, then complete a sparse SOL surface (few quoted maturities) to obtain at-the-money volatility, skew and term slope at fixed tenors. The paper shows BTC to ETH transfer only; transfer to SOL is untested.
2. Anomaly feature: per-hour reconstruction RMSE of the unmasked BTC surface, standardised by its trailing distribution, as a "volatility surface dislocation" flag that can gate or scale other signals.

## Relevance to SOL perpetuals at minutes to hours
The SOL option surface on the main venue is sparse ([deribit-2026-option-book-summary-sol-liquidity](deribit-2026-option-book-summary-sol-liquidity.md)), which is the situation this method targets. Hourly cadence fits the trading horizon. The anomaly score is reported only as coinciding with two events; whether it leads or lags price moves is not analysed, and that is the question that matters for trading.

## Caveats
Five months of data from one venue (Binance Options, not Deribit), covering one crash and one rally; the authors list the short window as their first limitation. The targets are themselves produced by a parametric fit, which makes the smile baseline unbeatable when rows are well populated and may flatter the grid representation. No forecasting or trading test. Preprint from an industry group; code is said to be released but was not inspected.
