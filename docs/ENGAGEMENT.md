# ENGAGEMENT - the client, the process, the number

status: draft

> **This is the scaffold, not the brief.** Day 1 fills it in as a draft. Day 3 replaces the
> guessed baseline with a measured one and flips `status` to `baselined`. Day 5 turns it into a
> scoped SOW and flips it to `signed`.
>
> `tests/test_engagement_brief.py` checks the **shape** of this document: five sections, a valid
> status, no unfilled markers, a criterion carrying at least two numbers and a unit, and a number
> with both an owner and an end. It cannot check whether any figure here is true. That is what
> day 3 is for.
>
> Guidance is written as blockquotes and the checker ignores them, so leave them in place. Write
> your answers as plain lines underneath.
>
> The client is fixed by plan §3. Do not invent a different one.

---

## The process

> One process, named narrowly enough that you could stand behind someone and watch them do it.
> Not "claims" - a stage of claims, at named locations, for one line of business.

First response on a newly filed motor claim, at the three regional triage centres.

The stage begins when a claim lands in the intake queue and ends when the claimant receives the
first substantive reply from a handler - not an acknowledgement email, a reply that says what
happens next. It excludes everything downstream of that: adjuster visits, liability disputes,
settlement and payment.

The population is motor claims only. The insurer also writes home and commercial; neither is in
this engagement. Volume across the three centres is roughly a third of the forty-two thousand
claims a month the business takes in total, and that share is itself provisional until day 3.

## The success criterion

> All five parts in one sentence: baseline, target, unit, owner, exit condition. Day 1 part 2.2
> carries the shape and a worked example. The checker refuses a sentence with fewer than two
> numbers or no unit.
>
> On day 1 the baseline is a guess, and it stays a guess until day 3 measures it. Mark it as one:
> writing `(provisional)` beside a number you have not measured is principle 7 in one word.

Reduce median days to first response on motor claims across the three regional triage centres
from 4.0 days (provisional) to 1.5 days, owned by the claims operations lead, sustained for four
consecutive weeks with no manual intervention from the delivery team.

The 4.0 is a guess and is marked as one. It is inferred from the 7.5 days the business quotes for
end-to-end settlement, which is a different measurement of a different stage. Day 3 replaces it
with a measured figure and this line changes; the target and the unit do not.

## Who owns the number

> A role, never a person's name. Roles survive people leaving, and this document outlives the
> engagement. If the honest answer is that nobody owns it, write "nobody" - an unowned number that
> has been named is a scope item, and an unowned number that has not been named is the reason the
> project will be late.

The claims operations lead.

The number is already theirs: triage throughput is what they are asked about in the monthly
operations review, which is also why they are the person who can produce the baseline on day 3.
Finding the owner and finding the baseline is one errand, not two.

The regional centre managers each own their own centre's figure and none of them owns the median
across all three. That gap is real and it is a scope item, not a footnote - a per-centre
improvement and a per-centre regression can be reported as either result while nobody owns the
combined number.

## The exit condition

> How long the target must hold, and what must be true about your own involvement when it does.
> The second half is the one that gets forgotten, and the one that makes day 175's handoff
> possible.

When the median has held at or below 1.5 days for four consecutive weeks, and the delivery team
has touched nothing during those four weeks.

Four weeks rather than one, because one good week is a launch effect and four is a process. The
second half is the half that gets forgotten: if the number only holds while somebody from the
delivery team is re-running a job on Monday mornings, the target has not been met - the work has
just been moved. This is the clause the day 175 handover is measured against.

## What this engagement will not do

> The boundary, agreed while everyone is calm. Day 1 part 1.3 explains why this section is the
> counterweight to owning a gap: ownership without a written boundary is how an engagement becomes
> unbounded. Three or four lines is enough.

Home and commercial claims. Motor only, at all three centres.

Everything downstream of first response - adjuster scheduling, liability decisions, settlement
amounts, payment. The engagement moves one stage and does not touch the rest of the pipeline.

Replacing or migrating the existing claims management system. The work reads from it and writes
back to it through whatever interface already exists.

Any use of real claimant data. The corpus this is built and evaluated against is synthetic,
generated on day 4 and version-controlled.

Retraining the three centres on a common triage standard. The inconsistency between them is real,
it is named here, and it is the client's to fix - it is not a system change.

---

## Amendments

> Append-only. Every later change to this document lands here as a dated row, so that a number
> which moved can be told apart from a number that was always that.

| Date | Day | What changed | Why |
| --- | --- | --- | --- |
| 2026-09-07 | 1 | Scaffold created; status `draft` | Day 1 part 2.3 |
| 2026-09-08 | 1 | All five sections drafted; baseline written as `4.0 days (provisional)` | Day 1 part 2.3 - the brief is a draft until day 3 measures the baseline |
