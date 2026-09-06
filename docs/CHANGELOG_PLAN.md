# CHANGELOG_PLAN — append-only

Every amendment to `00_MASTER_PLAN.md` (Principle 12). Reality moves; the plan is amended **first**,
then the days follow. A day is never silently patched around a changed world.

**The order is fixed and it matters:** verify what actually moved → state the cost → write an ADR
if the change is structural → edit the plan and bump its version → append the entry here → only
then touch days or code.

A wording fix is not a version bump. A moved ID, a changed gate, or a new day is.

| Date | Plan version | What changed | Why | ADR | Days affected |
| --- | --- | --- | --- | --- | --- |
| TODO(me) | v1.0.0 | Initial plan | Derived from the source roadmap "Production LLM Engineering — RAG, Agents & Fine-Tuning V1.0" | ADR-0001 | none written yet |
| 2026-09-07 | v1.1.0 | §4 gains §4.1, the hardware profile: the curriculum's default assumption becomes a laptop with no GPU, one `YANTRA_PROFILE` variable selects the accelerated path, and rules 4–6 bind every day to two budget lines, a profile on every measured number, and a laptop path that is a smaller true version rather than a stub. The "correct this before Day 0" warning is replaced by what remains open — the free-tier half | The working machine has no GPU. Left alone this makes Phase 2 onward readable rather than runnable, and makes every ledger number unattributable between machines. Deciding at Day 15 instead of now would mean editing fifteen days' setup blocks and expected outputs | ADR-0005 | Day 1 §3 (torch install becomes profile-driven); every future day that touches an accelerator |
