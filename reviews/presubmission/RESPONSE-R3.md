# Response to Referee 3

We thank the referee for checking the artefact rather than the prose about the artefact. Two of
these findings are the most serious in the review round, and one of them concerns a
methodological contribution we had written into the paper three hours before the referee read
it.

---

**R3-M1, the reviewer is a measured family and a ground-truth rater.** *Accepted in full.*

All nine review directories record `gpt-6-astra`, which is one of the four auditor routes whose
ranking the paper reports and one of the two raters behind the residual labels. For the claims
that rank `astra` the reviewer is the subject, and the manuscript said none of it.

The methods section now names the reviewer and states which claims it is conflicted on. A
seventh limitation records it. The `astra`-ranking comparisons are marked as self-assessed until
a model that audited nothing here has checked them. The referee's observation that this
project's own P3 Amendment 10 disqualified the same model as a rater for the same reason, and
that we did not apply the standard to ourselves, is exact and we have quoted it in the methods.

**R3-M2, the blinding was not enforced.** *Accepted in full; the inference is withdrawn.*

The prompt's own text withheld every figure. Its binding-artefact list then named
`plan/P1-ANALYSIS-REGISTRATION.md` and `manuscript/CLAIMS.md`, both of which state them, the
second being the ledger entry for the result under review. We verified this by reading the
prompt.

We have withdrawn the inference entirely. The paper no longer claims the headline was not an
artefact of being told, because that claim rested on an agreement whose independence we cannot
establish. What survives is a disagreement count of six findings, reported as **n = 1,
uncontrolled and unregistered**, with the referee's point that a seventh round might have found
new things under any prompt stated in the text. The experiment note keeps its original wording
under a withdrawal banner rather than being rewritten, because a withdrawal that hides what it
withdrew is worse than the error.

The referee is also right that the design was not preregistered and has no matched briefed
control. We describe it as a reason to test blinding properly, not as a result about blinding.

**R3-M3, the repository does not contain what the Reproducibility section claims.** *Accepted;
partly done.*

The availability statement now says what the repository cannot carry and why — the raw run
directories hold model outputs derived from corpora under a non-commercial,
no-redistribution licence, so what is published is every derived record and not the bytes behind
them. The referee's fuller finding is not yet addressed: nine of ten cited reports are absent,
the review rounds live outside the repository, the analysis code does not import, and no figure
regenerates from a clean checkout. We accept all of it. The one-command reproduction of Figure 1
that the referee proposes as the acceptance test is the right test and we have not met it.

**R3-M4, the universal preregistration claim.** *Accepted in full.*

The P1 analysis was registered a day after its contrast had been computed and committed, in a
document that claimed the opposite, and that document is withdrawn in the repository. Three
sites now carry the exception. We note with appreciation that the referee checked the P3
amendment chronology and found it clean; the overclaim was gratuitous and is gone.

**R3-M5, "no measurement ever moved".** *Accepted in full.*

Two counterexamples, both now in the paper: the clarification study's second review moved its
primary from 9 of 31 to 9 of 32 instances and its contrast from +29.0 to +28.1 points, and a
label count inside a reviewed report moved from 71 to 67. The sentence is scoped and the
counterexamples are named.

**R3-M6, the manuscript carries a framing its own ledger corrected.** *Accepted; mostly done.*

The results section and `CLAIMS.md` now agree that the group overlap is definitional — two
different definitions of *caught* — rather than clerical, and the fourth limit about the
three-input display is carried in both. Figure 3's panel labels still use the superseded
wording; that is open.

**R3-M7, stale and contradictory review-status statements.** *Accepted in full.*

The introduction said three studies had cleared review and four were in it; the abstract said
otherwise; the round count was forty-four where the studies' own clearing rounds sum to
forty-seven. All corrected, with the counting convention stated. The referee is right that a
generated status block would prevent recurrence, and the repository has one; wiring the
manuscript to it is open.

**Minor comments.** R3-m2 is fixed: both figures are now referenced from the text and the
manuscript checker passes. R3-m5 is accepted — a registration that falsely claimed the analysis
had not been run is an overstatement *toward* our interest and was misfiled in a list of
overstatements away from it; the repository's own withdrawal document says so in better words
than the manuscript used. R3-m7 is accepted: "survives a third model rater" is exact and
"survives a rater who is not an author" is not, given that no human outside the project has
validated anything here. The others are accepted and open.
