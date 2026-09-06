# PROGRESS — append-only

One row per **completed** day. **The last row is where we are.** Appended by whoever finishes the
day; `granth.py done NNN` refuses to commit without it.

**Leave the bad days in.** A ledger with no failures in it is a ledger nobody has been honest in,
and readers can tell. The `Notes` column is where a day that went wrong says so.

| Day | Title | IDs closed | Date | Checks | Notes |
| --- | --- | --- | --- | --- | --- |
| 0 | Toolchain and skeleton | — | 2026-09-07 | green | Setup day; closes no IDs by design (ADR-0004). |
| — | *no days completed yet* | — | — | — | Plan v1.0.0 accepted; day map not yet corrected. See §17. |
