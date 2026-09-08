# PROGRESS — append-only

One row per **completed** day. **The last row is where we are.** Appended by whoever finishes the
day; `granth.py done NNN` refuses to commit without it.

**Leave the bad days in.** A ledger with no failures in it is a ledger nobody has been honest in,
and readers can tell. The `Notes` column is where a day that went wrong says so.

| Day | Title | IDs closed | Date | Checks | Notes |
| --- | --- | --- | --- | --- | --- |
| 0 | Toolchain and skeleton | — | 2026-09-07 | green | Setup day; closes no IDs by design (ADR-0004). |
| — | *no days completed yet* | — | — | — | Plan v1.0.0 accepted; day map not yet corrected. See §17. |
| 1 | What a forward deployed AI engineer actually owns | FDE-01, FDE-02 | 2026-09-08 | green | Parts read 09-07; brief written 09-08 with the assistant rather than solo, so day 3 re-derives the criterion from scratch rather than inheriting it. Baseline 4.0 days is marked (provisional) - it is inferred from the 7.5-day settlement figure, which measures a different stage. test_the_number_has_an_owner_and_an_end is weak: it asserts on length, not content. |
