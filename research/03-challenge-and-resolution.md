# Pass 3 — Challenge, corrections, and cross-stream reconciliation

Edition: 2026-10-15. **Same-context critical review; no fresh-context reviewer, council, or cross-model execution was performed.**

The method adapts `doubt-driven-development`: isolate a proposal and its contract, construct the strongest relevant counterexample, and reconcile it against the available evidence. The skill's independent-review stage was not simulated. The separate Red Team stream and the fourth chat can challenge these results later, but their conclusions have not been imported as if already known.

This document records changes and accepted trade-offs. It does not repeat all eighteen rationales from [pass 2](02-information-architecture.md). Source identifiers resolve through [the final source register](03-sources-and-quality.md) and its linked earlier registers. The [final operating report](03-operating-model-and-release.md) owns the operational refinements.

## CH-01 — Native-first might be harder to maintain than an external service

**Artifact under test:** use native Projects coordination and memory as the baseline, adding only a small explicit information contract. Related decisions: AR-002, AR-004, AR-013.

**Contract:** correct useful context must be available after a relevant correction or interruption, without the owner repeatedly repairing backend state.

**Strong counterexample:** a beta memory system may lack adequate correction, recovery, or sharing for the actual work. A maintained external service might remove more administration than it introduces. Counting custom files or local processes would then choose the wrong design.

**Reconciliation — valid trade-off:** native-first remains the first comparison, not an unconditional winner. Exact native synchronization remains unresolved because S03 is inaccessible and no live probe ran. The external dossier establishes integration costs, not native superiority. T03/T10 can expose a missing native capability; T13 can then test the narrowest external candidate. A task checkpoint may solve interruption without adding history search.

**What would reverse the recommendation:** reproducible baseline failure on a required continuity case and a supported alternative that improves correct recall or recovery with acceptable data handling and operator burden. “It has many stars” and “the native system is already excellent” are both insufficient.

## CH-02 — Higher coordinator effort may merely produce more elaborate administration

**Artifact under test:** first test High coordinator effort with unchanged ordinary worker effort, and separately test High worker effort for demanding reviews. Related decision: AR-015.

**Contract:** improve useful decomposition, evidence preservation, and supported conclusions without unnecessary work or excessive owner intervention.

**Strong counterexample:** higher effort may create extra subtasks, revisit settled decisions, or generate a longer answer while missing the same source. It could make an overcomplicated system more expensive rather than more capable.

**Reconciliation — actionable refinement:** the final recommendation is explicitly a pilot, not a default certified by this research. The model and orchestration mechanism remain fixed while one role changes. The acceptance observations include needless delegation and repair work, not just more findings. A failed higher-effort comparison is retained as evidence; Max everywhere is rejected as an unproved default.

**What would reverse the recommendation:** comparable tasks perform as well or better at the lower setting with less overhead, or the failure is resolved entirely by correcting the assignment or source route. Effort cannot grant an unavailable permission, but it can affect whether an available source is investigated; the old shorthand “effort cannot fix context” must not erase that distinction. [S09, S28]

## CH-03 — Fewer instructions can remove the one boundary an isolated worker needed

**Artifact under test:** reduce duplicated global instructions and move specialized procedures to relevant references or skills. Related decisions: AR-003, AR-006, AR-009.

**Contract:** the intended reader actually receives the essential information at the time of use, including critical exceptions and action boundaries.

**Strong counterexample:** a short root file can point to a perfect procedure that is never reached. A worker using an external tool may never touch the local path that activates a rule. An isolated routine may need a small repeated constraint.

**Reconciliation — valid trade-off:** preserve one authoritative owner but allow traceable projections. Measure activation rather than file length. Where an essential short rule repeatedly fails to arrive, strengthen its pointer or include that specific boundary in the shared core. Do not respond by loading the whole library globally. Imports and conditional activation are not equivalent. [S07, S08; T09/T11]

**What would reverse the proposed split:** direct evidence that the new consumer cannot discover or access necessary content, or that its exception is lost. Restore the smallest effective representation. This research does not prescribe a universal line cap or rule count.

## CH-04 — Removing a ceremonial guard may accidentally remove a genuine protection

**Artifact under test:** remove or narrow controls whose result is only a keyword, reassuring phrase, or ritual skill receipt. Related decisions: AR-010, AR-011, AR-017.

**Contract:** meaningful unauthorized or materially incorrect effects remain prevented or detected at an appropriate point.

**Strong counterexample:** an apparently noisy hook could also perform a real authorization check or a useful stale-version check. Its unit tests may cover that value even if they do not prove business quality. No observed past incident is not proof of no preventive value.

**Reconciliation — actionable boundary:** no specific V2 hook is condemned by this research. The implementation audit must trace the exact event, input, consequence, and failure behavior. Preserve the protected outcome or restrict the affected feature before removing its only supported protection. The static and live evidence must identify which role is real; a single script can mix advisory, integrity, and authorization roles.

**What would reverse a removal:** the candidate permits a previously prevented meaningful failure or relies on a native replacement that does not execute in the target route. Conversely, a check that only demands reassuring wording does not become a truth test because it runs deterministically.

## CH-05 — A green document audit can support an unsound architecture

**Artifact under test:** use docs-governance for documentation roles and integrity, with a passing result contributing to delivery readiness. Related decision: AR-018.

**Contract:** correctly identify what was mechanically checked without implying the text is true or the system works.

**Strong counterexample:** a document can contain valid links and valid test IDs while claiming an unexecuted test passed. A complete file tree can contain conflicting instructions. The pass-2 DG fixtures directly exercised examples of this limitation.

**Reconciliation — actionable separation:** research-file checks are labeled as reference/structure checks. The previous DG results remain narrow historical local evidence. The original user-supplied checker sources were not redistributed, so a new reader cannot claim to rerun those probes without obtaining them. The final pass instead supplies its own small, self-contained research-reference verifier and negative controls; it does not claim equivalence to the DG suite.

**What would invalidate a delivery claim:** missing target documents, inconsistent IDs, or a failure to disclose that substantive behavior was never tested. A positive structural result does not close any live Projects question. [D01–D04; DG03/DG04/DG10]

## CH-06 — A clean handoff may still be biased by three correlated reports

**Artifact under test:** combine this research, the V2 audit, and Red Team analysis in a fresh fourth chat.

**Contract:** select a design supported by evidence, not by repetition of a shared starting assumption.

**Strong counterexample:** all three chats may inherit the owner's understandable frustration and the same preliminary theories. Three reports could all recommend deleting native memory based on the same mistaken identity assumption. Fresh context does not erase correlated source errors.

**Reconciliation — actionable procedure:** the builder must compare claim, source revision, execution surface, and verification type before choosing. Shared citations are one evidence chain, not several replications. A dissenting reproducible finding can outweigh several agreeable summaries. The other repository URLs and revisions remain missing inputs here; they are not invented to make the handoff appear complete.

**What would strengthen confidence:** the builder traces a consequential disagreement to the actual V2 source, exact official section, or narrowly relevant live observation. Agreement alone is not the requested evidence.

## CH-07 — A rollback plan can restore code while leaving dangerous work active

**Artifact under test:** construct V3 separately and preserve V2 as fallback. Related decisions: AR-001, AR-012, AR-016.

**Contract:** switching or reverting must not silently duplicate externally consequential work or reintroduce stale controlling state.

**Strong counterexample:** an old routine or worker continues while the new one begins. Reverting Git does not reverse an accepted send. Archiving the old environment does not necessarily terminate existing execution. A native file checkpoint has a narrower scope than the whole business system.

**Reconciliation — actionable refinement:** the final release model separates repository, runtime configuration, memory/task continuity, and external effects. The cutover plan accounts for active work, supported stopping, and target-side reconciliation. A rollback procedure is operation-specific; a universal script or transaction service is not proposed. [S05, S29]

**What blocks production enablement:** inability to identify or stop the relevant consequential path, unknown outcome of an earlier effect, or loss of the required context/authority after switching. This blocks that capability, not all drafting or read-only analysis.

## CH-08 — Excessive caution can prevent any useful system from shipping

**Artifact under test:** retain unresolved questions and require evidence before asserting reliability.

**Contract:** allow useful work and a justified migration without pretending unknowns are solved.

**Strong counterexample:** the builder might treat all fifteen proposed tests and every source gap as mandatory prerequisites, then spend the whole effort building evaluators and documentation. That would recreate the owner's process problem.

**Reconciliation — actionable scope:** each unresolved question blocks only decisions that depend on it. A missing external-memory deletion contract blocks ingesting sensitive data into that service, not selecting a native drafting workflow. A missing authorization contract blocks unattended external effects, not producing a reviewed draft. Use existing checks and a few decision-changing probes. Do not add a permanent benchmark infrastructure or enforce the research report at runtime.

**Stop condition:** the chosen reversible stage has adequate evidence, remaining limitations are explicit, and additional research would not change that stage's decision. Higher-impact expansion can wait for its own evidence.

## Cross-stream disagreement procedure for the builder

For a consequential conflict, create one compact reconciliation entry in the design report:

`Claim -> input revision/surface -> evidence type -> decisive counterexample or probe -> selected disposition -> remaining limit.`

Read the underlying artifact, not just the report's verdict. First check whether the apparent disagreement is actually about a different version, environment, task, or meaning of “works.” A generic platform capability can coexist with a V2 loading defect. A mechanically correct guard can coexist with a poor review process. A useful native memory store can coexist with contaminated notes.

If the dispute survives those checks, prefer a small discriminating observation over another unrestricted review. When no safe observation is available, record a conditional decision and restrict its impact. The builder should not invent certainty through scores, reviewer counts, or arbitrary confidence decimals.

### Final changes resulting from this challenge

1. AR-015 now has a concrete role-separated pilot and explicit reversal criteria rather than indefinite “measure later” advice.
2. AR-008/AR-017 explicitly require accounting for missing required worker results without prescribing a new task database.
3. AR-011/AR-012/AR-016 distinguish stopping future triggers, active execution, and already accepted effects.
4. AR-018 separates a reproducible research-reference checker from the unbundled historical DG checker and from semantic/live acceptance.
5. The handoff separates missing audit inputs from research conclusions and allows feature-scoped progress under unresolved questions.

No fresh reviewer was run, no live architecture comparison was executed, and no V2 finding was independently reproduced. These are disclosed boundaries, not hidden exceptions to a “fully verified” label.
