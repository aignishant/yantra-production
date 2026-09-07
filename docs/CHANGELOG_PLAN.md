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
| 2026-09-07 | v2.0.0 | **The merge.** Yantra v1.1.0 (229 days, 400 IDs, 9 tracks) and Setu v1.0.0 (180 days, 181 IDs, 8 tracks) become one plan: 182 days, 373 IDs, 13 tracks, 29 phases, four deliverables shipped to one client. §1–§17 and §22 rewritten; §18–§21 (gates, ledgers, the depth contract, the style guide) carried over unchanged. New: the `SE`, `CLD`, `ENT`, `FDE` tracks and §4.2's two lanes, all from Setu. Reordered: the model is met as a dependency (Phase 5) before it is taken apart (Phase 8). Cut and enumerated in §22.3: speech, a vendor agent runtime, the A2A block, five services collapsed to four deliverables, vision internals from 12 days to 2 | Run in sequence the two plans cost 409 days and taught ~130 IDs twice — the same retrieval, agent, security and observability material on both sides. Neither half is employable alone: Setu's stated non-goal is fine-tuning, and Yantra ships to nobody, with no client, KPI, identity model or handover. The constraint is six months | ADR-0006 | all; `days/day-001-what-language-model-is/` deleted (its subject is now Day 53). Day 0 stands unchanged and is the only inherited day |
