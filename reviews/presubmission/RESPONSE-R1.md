# Response to Referee 1

We thank the referee for a review that changed the paper. Two of the concerns were things our
own archived studies contradict, and we had not noticed either. Every figure quoted below was
re-derived from the records before we acted on it.

**A note on what we did not have to change.** The referee verified five studies directly and
found no arithmetic error. That matches what we found: nothing in this revision required a
measurement to be recomputed. What changed is what the paper says about measurements.

---

**R1-M1, one estimator under two names.** *Accepted in full.*

The referee is right, and the ledger was on the wrong side of it. Study 20's own table heads the
column *P union recall* and reports `cross-R` at 67 of 110 = 60.9% [48.6, 72.5] at eight
readings, on the same instances under the same at-least-one-BLOCKER rule. We had been calling 33
of 110 union recall and 67 of 110 flag coverage.

The results section now uses one name for the estimator and reports the 60.9% with its price,
36.7% [28.5, 44.8] false positives against the shipped route's 16.0%. The caution that a flag is
not a catch is stated as attaching to both equally rather than to one. `CLAIMS.md`'s
forbidden-claims list, which asserted that no configuration measured here exceeds 48.2% union
recall, is corrected: the honest statement is that no configuration reaches a shippable
operating point, and the price is the reason.

**R1-M2, the residual across more families.** *Accepted, and it produced a better result than
the one it replaced.*

The referee is right that "flagged by no reading of any family" was true of three families and
false of the six this programme measured, and right that the class which leaves is the class
that supplies the third result's population. We computed the quantity the referee asked for.

Across six families at forty readings, including the same auditor under the rewritten rulebook,
the never-flagged set falls from 57 to **32 of 110**, and **43 of the 68 instances both raters
call specification-undetermined are flagged by some reading of some family**. Being
specification-undetermined is therefore not sufficient for being missed, and the paper now says
so. What does not move is the composition: the undetermined share of the never-flagged set is 44
of 57 (77.2%) at three families and twenty readings, and 25 of 32 (78.1%) at six families and
forty readings. The residual loses nearly half its members and keeps its shape.

We would not have found this without the concern, and the claim is narrower and better supported
for it.

**R1-M3, the rater is one of the auditors.** *Accepted as a disclosure; the re-rating is owed.*

`gpt-6-astra` rated the residual and is one of the three families whose readings define it. It
is also, as a second referee observed independently, the reviewer of record for every study in
this programme. Both facts are now in the methods section and in the Limitations, and the claims
that rank `astra` against the other families are marked as self-assessed pending a check by a
model that audited nothing here. We have not yet re-rated the residual with a non-participating
model; that is the right experiment and we state it as owed rather than done.

**R1-M4, the title and the framing sentence.** *Partly accepted; deferred, not declined.*

We accept that three legs measured on three populations in three currencies do not constitute a
decomposition, and that the body says so while the title does not. We have not retitled yet
because R1-M1's naming correction changes what the first leg says, and we would rather retitle
once against a settled result than twice. The current text no longer claims the legs are
commensurable.

**R1-M5, the scope statements.** *Accepted; open.*

The Method describes a two-substrate design in the present tense and one substrate produced no
quotable number. Population construction, drop counts and the generator's identity belong in
§2.1 and are not there. This is a writing task we have not completed.

**R1-M6, cross-vendor confounded with OpenAI.** *Accepted as an unidentified axis; the mirror
arm is declined for now, with a reason.*

The referee is right that every well-performing arm is OpenAI and the generator is Anthropic, so
"cross-vendor" and "OpenAI model" are not separated by this design. Running the mirror needs a
new generation ladder plus two audit ladders. We record it as an unidentified axis rather than
claim it away, and we would rather state the confound than spend the budget while the rest of
the revision is open.

**R1-M7, interval coverage.** *Accepted and measured.*

We have run it. Under the two strata's actual cluster profiles, coverage of a nominal 95% rate
interval is near nominal at the rates our headlines sit at and badly anticonservative at small
rates — 0.798 at a true rate of 0.03 on the 56-cluster stratum. A table replaces the scalar
range, and the one small-rate figure in the results is marked in place as narrower than it
claims. The simulation is committed and costs no model calls.

**R1-M8, family membership for p values.** *Accepted; open.*

**R1-M9, the false-positive stratum is unadjudicated.** *Accepted; open.* The referee's point
that our own §3.4 argument applies to the cost axis, and that nothing in the paper adjudicates a
single flag on correct code, is well taken and is the most interesting unaddressed item in this
review.

**Minor comments.** R1-m3's seed observation led us to find a cross-report inconsistency of
exactly the kind it describes, now fixed. R1-m9's ledger reconciliation is partly done. The
others are accepted and open.
