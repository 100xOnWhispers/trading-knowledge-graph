---
title: "A Reassessment of Monetary Policy Surprises and High-Frequency Identification"
authors: "Bauer, Michael D.; Swanson, Eric T."
year: 2022
venue: "NBER Working Paper 29939 (prepared for the NBER 37th Annual Conference on Macroeconomics)"
url: "https://www.nber.org/system/files/working_papers/w29939/w29939.pdf"
pdf: "sources/30-macro-state-intraday-transmission/bauer-2022-reassessment-monetary-policy-surprises.pdf"
access: "full-text"
source_type: "working-paper"
evidence_grade: "A"
topic: "30-macro-state-intraday-transmission"
asset_class: "multi"
horizon: "minutes"
tags: "fomc, monetary-policy-surprise, predictability, orthogonalization, fed-chair-speeches, eurodollar-futures, pre-2020"
---

## Key insight
High-frequency monetary policy surprises are predictable after the fact from public data available before the meeting: recent payroll surprises, employment growth, the prior three-month stock return, the yield-curve slope, commodity prices and Treasury skewness. The authors attribute this to markets underestimating how strongly the Fed responds to news, not to inside information. For measuring asset-price responses in a narrow window the predictability does not matter; for macro effects it does. Speeches and testimony by the Fed Chair are as important as FOMC statements.

## Method
The surprise mps is the first principal component of changes in the first four quarterly eurodollar futures (ED1 to ED4) over a 30-minute window starting 10 minutes before each announcement, scaled so one unit moves ED4 by one percentage point. Predictive regression (15): mps_t = alpha + beta' X_(t-) + e_t with six predictors known before the announcement. The orthogonalised surprise is the residual. Event-study regressions of yield and S&P 500 changes on mps and on the residual are compared. The announcement set is extended with press conferences, testimony and speeches by the Chair.

## Data and sample
Swanson and Jayawickrema intraday dataset, 1988 to 2019: 322 FOMC announcements and 880 Chair speeches, of which 295 are judged to contain monetary policy news. S&P 500 futures to August 1997, E-mini from September 1997. Ends before 2020; no crypto.

## Reported results
- Predictive R-squared is about 16 percent for FOMC announcements over 1988 to 2019, a little higher from 1994 and in the pre-2007 sample. Earlier work cited reports 10 to 40 percent.
- Signs: strong payrolls, a strong stock market and high commodity prices predict a hawkish surprise; a steepening curve or negative Treasury skewness predicts an easing surprise.
- A 100 basis point surprise raises the 30-year yield by 25 basis points (t above 6, R-squared above 20 percent) and lowers the S&P 500 by 5.4 percent (t near 8).
- Estimates with the orthogonalised surprise are almost identical; the predictors have no independent effect on asset prices once the surprise is included.
- Two- and five-year yields respond almost identically to Chair speeches and to FOMC announcements, and ten- and 30-year yields respond even more strongly to speeches; the equity response to speeches is more modest.
- Speeches often last an hour or more, so their event windows are longer.

## Signal construction
Two uses. First, the response coefficient: about -5.4 percent on the S&P 500 per 100 basis points of mps gives the equity benchmark against which a crypto beta is expressed. Second, a pre-meeting lean: fit regression (15) on a rolling basis and compute the predicted surprise from the six predictors on the eve of each meeting. This is a weak, ex post documented tilt (R-squared 16 percent over 322 events), not a tested trading rule. The event calendar should include Chair press conferences, Jackson Hole and congressional testimony.

## Relevance to SOL perpetuals at minutes to hours
The widened event set is the practical takeaway: a macro gate that only flags the 8 FOMC statement times per year misses roughly as many policy-news events again. The predictability result suggests that a hawkish outcome is more likely after strong data and strong equities, which is a testable conditional prior for the direction of the post-FOMC crypto move. Neither has been tested on crypto.

## Caveats
Predictability is in-sample and the authors argue it was not exploitable ex ante. Sample ends in 2019. Eurodollar futures no longer exist; a live version would use SOFR futures. Selecting speeches partly by whether rates moved 3 basis points introduces selection on the outcome.
