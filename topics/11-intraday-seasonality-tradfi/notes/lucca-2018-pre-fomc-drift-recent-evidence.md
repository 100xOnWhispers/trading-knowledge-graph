---
title: "The Pre-FOMC Announcement Drift: More Recent Evidence"
authors: "Lucca, David O.; Moench, Emanuel"
year: 2018
venue: "Liberty Street Economics, Federal Reserve Bank of New York (26 November 2018)"
url: "https://libertystreeteconomics.newyorkfed.org/2018/11/the-pre-fomc-announcement-drift-more-recent-evidence.html"
pdf: "none"
access: "full-text"
source_type: "industry-research"
evidence_grade: "C"
topic: "11-intraday-seasonality-tradfi"
asset_class: "equities"
horizon: "hours"
tags: "pre-announcement-drift, fomc, anomaly-decay, post-publication, press-conference, event-window"
---

## Key insight
Seven years after their original sample ended, the authors re-examined the pre-FOMC drift and found it had become conditional: it survived only before meetings followed by a Fed Chair press conference, and it started earlier in the pre-announcement window. Meetings without a press conference showed no drift. Together with later evidence that the drift faded further after 2015, this is a documented case of a calendar anomaly changing shape after publication.

## Method
Out-of-sample update of the original event study on S&P 500 returns around scheduled FOMC announcements, splitting meetings by whether a press conference followed. Average cumulative returns are compared from the open of the day before the announcement through the end of the press conference. The post was read through a fetched text rendering; charts were not viewed directly and no formal test statistics are reported for the press-conference subsample.

## Data and sample
S&P 500, scheduled FOMC meetings from April 2011 to June 2018, compared with the original 1994 to March 2011 sample. Only some meetings in this period were followed by a press conference; the post notes that all meetings would have one from the following year.

## Reported results
- Original sample: equities ended the announcement day almost 50 basis points higher than at the prior day's open.
- April 2011 to June 2018, meetings with press conferences: about 40 bp from the prior day's open to around midday of announcement day, plus about 30 bp more by the end of the press conference.
- Meetings without press conferences: no evidence of pre-announcement excess returns, and negative (not statistically significant) returns after the statement.
- Returns in the recent sample begin in the morning of the day before the announcement, earlier than in the original sample.
- Explanations offered: investors pay attention only to meetings where policy changes are expected; arbitrageurs front-running the drift, which would push it earlier and eventually eliminate it; and a post-announcement risk premium.
- Separately, the RePEc abstract of Kurov, Wolfe and Gilbert (2021, Finance Research Letters 40, "The disappearing pre-FOMC announcement drift"), read as an abstract only, states that with data through December 2019 the drift essentially disappeared after 2015 for announcements both with and without press conferences, and suggests reduced uncertainty as a possible reason.

## Signal construction
Not a new signal. It modifies the event rule in the 2015 paper: condition on event importance (is a policy change or major communication expected?) and allow the entry window to move earlier over time. For a research pipeline it argues for rolling re-estimation of every calendar effect and for an explicit decay check on post-publication data.

## Relevance to SOL perpetuals at minutes to hours
If every meeting now has a press conference, as the post anticipated from 2019, the conditioning variable no longer discriminates; event importance would need another proxy such as implied volatility ahead of the event or the rate-change probability implied by futures. The broader lesson for a crypto bot is that pre-event drift is unstable in its home market, so any pre-FOMC or pre-CPI long bias in SOL needs evidence from crypto data in the current regime, not from the 1994 to 2011 equity sample.

## Caveats
Blog post covering roughly seven years of meetings (fewer than 60 events) split into two groups; no standard errors for the main subsample. The Kurov et al. result is reported from an abstract only. Neither source examines 2020 to 2026, which includes a full hiking and easing cycle; current status is unknown from these sources.
