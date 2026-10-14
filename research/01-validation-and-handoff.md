# Validation register and audit handoff

Edition: 2026-10-15. Shared by passes 1 and 2. Existing IDs T01–T08 are retained; T09–T15 extend the coverage.

**Execution status: every test below is NOT RUN in this research stream.** Reading documentation, inspecting a manifest, and committing a report are not live Claude Projects tests.

## 1. Use tests to make decisions, not to create another bureaucracy

Run only a test that can change a concrete architecture decision. Start with an isolated test Project or reversible copy, a fixed repository revision, recorded relevant settings, and harmless data. Do not interrupt production threads, spend advertising money, send campaigns, alter live customer records, or publish private transcripts for these probes.

A run record should contain the task and candidate configuration, date and runtime version where visible, coordinator/worker model and effective effort where obtainable, repository/ref and working directory, relevant tool/connection state, expected observable result, actual result, evidence location, and the decision affected. Keep secrets and hidden provider prompts out of the record.

Prefer actual artifacts, authoritative readback, and narrow observations. A model's self-report that it followed a rule is not enough. For creative work, artifact existence is objective but usefulness still needs business judgment; do not fabricate a universal automatic creativity score.

A small pilot is diagnostic, not a reliability estimate. When model variability matters, repeat equivalent tasks in alternate order and record all results, including failures. Do not quietly tune one candidate on the evaluation cases and compare it with an untuned baseline. Stop testing when the remaining uncertainty would not change the decision, or when a safety boundary prevents a valid probe. Report that boundary instead of bypassing it.

## 2. Original platform probes, clarified

### T01 — Effective configuration of a real work thread

**Decisions:** AR-001, AR-006, AR-009. **Status:** NOT RUN.

Start a harmless diagnostic task in a target Projects thread. Record whether it is hosted cloud, local, or Remote Control, the repository/ref, working directory, visible runtime version, and available configuration diagnostics. Use `/context`, `/status`, `/hooks`, `/skills`, or `/mcp` only if supported in that surface; otherwise use visible metadata and tool logs. Never invent successful command execution.

Compare an existing file with evidence that it was loaded. A harmless, distinctive instruction in a test-only file can help observe behavior, but quoting that instruction back is weaker evidence than carrying out the corresponding task. Do not rely only on the assistant naming the file.

**Decision rule:** configure a component only where its loading path is established. If the necessary diagnostic is unavailable, retain that uncertainty and use a narrower task-level probe. Sources: S04, S05, S15.

### T02 — Single attached repository versus multiple attached repositories

**Decisions:** AR-001, AR-010. **Status:** NOT RUN.

Compare otherwise equivalent hosted sessions with one and two actually attached repositories. In the isolated fixture, use a harmless marker-producing hook rather than a blocking guard or an external write. Record the working directory, configuration source, matching event, and marker result. Distinguish attached repositories from a reference repository cloned as ordinary data.

**Decision rule:** a missing repo hook in the documented multi-repository case is an expected compatibility boundary, not automatically a malfunction. A critical control must have a supported execution path; failing this probe blocks reliance on that control, not necessarily all work in the environment. Sources: S04, S05.

### T03 — Memory identity and correction across threads

**Decisions:** AR-002, AR-003, AR-004. **Status:** NOT RUN.

First establish which visible memory surface corresponds to which readable/writable store. Record the route, not sensitive memory contents. In a test Project, use a harmless invented preference unrelated to the business. Save it through the native route, retrieve it in a new thread, explicitly correct it, then compare a new thread with an already-running thread. Do not assume the running thread refreshes automatically.

Where permitted, remove the test note and verify that a new thread does not retrieve it from another active store. If an old conversation still contains it, distinguish retained conversation history from reintroduced persistent memory.

**Decision rule:** preserve native memory as the baseline if its actual behavior meets the need. A failed correction with a known path can justify a targeted lifecycle change. Failure to identify the store is not permission to delete all memory files. Source: S07 is a generic reference; native Projects behavior must be observed directly.

### T04 — Delegation preserves scope and evidence

**Decisions:** AR-008, AR-017. **Status:** NOT RUN.

Use a small representative review with a defined source set and one material uncertainty. Compare the original request, coordinator assignment, worker evidence, and final synthesis. Observe separately what Tim receives automatically, what he can fetch, what he actually reads, and what he verifies.

**Decision rule:** a successful handoff preserves the requested coverage, important uncertainty, artifact/source references, and relevant action boundaries without requiring a transcript dump. If full evidence is accessible but ignored, test an assignment/return contract before adding a new transport or agent. If inaccessible, change the supported handoff path rather than assert that better wording grants access. Sources: S01–S03, S19, S21.

### T05 — Coordinator and worker effort as separate interventions

**Decisions:** AR-015. **Status:** NOT RUN.

Keep model, source material, tools, instruction revision, and task as similar as possible. Change only coordinator effort for a coordination-heavy task; in a separate comparison change only worker effort for an analysis-heavy task. Record effective values where observable, not just menu defaults. Alternate run order and keep unsuccessful attempts.

Measure source coverage, supported findings, unresolved uncertainty, unnecessary user intervention, elapsed work, and available usage metrics. For writing or creative tasks, separate factual correctness from subjective usefulness.

**Decision rule:** choose effort by observed marginal usefulness, not an assumption that Low caused all failures or Max is always optimal. More compute does not resolve missing access. Exact calibration is a pass-3 concern. Sources: S09, S21.

### T06 — Attribute a blocked operation to the correct layer

**Decisions:** AR-011. **Status:** NOT RUN.

Use an approved, harmless action on a disposable target. Preserve the exact operation and target approval in the assignment. If blocked, identify whether the rejecting layer is a custom hook, client permission, hosted classifier, network proxy, missing authentication, or the target API. Record the actual error without secrets.

**Decision rule:** choose the supported remedy for that layer. A correctly rejected unauthorized action is a successful safety result. Do not reword, reroute, or move to a less protected environment merely to defeat a denial. Sources: S14, S22; G01/G02 provide unverified incident leads.

### T07 — Fresh start, restored session, and local unavailability

**Decisions:** AR-001, AR-013, AR-016. **Status:** NOT RUN.

On isolated work, inspect a required executable and, only if relevant, a small service in a newly provisioned cloud session, a cached new session, and a resumed session. Separately observe the supported behavior when a local task's computer is unavailable. Do not assume these are equivalent lifecycle events.

**Decision rule:** the migration plan must distinguish installed files, a ready process, a durable result, and recoverable task state. An installer success or a preserved filesystem alone does not prove service readiness. Source: S05/S11.

### T08 — Routine context, completion, and duplicate avoidance

**Decisions:** AR-005, AR-012. **Status:** NOT RUN.

Start with a read-only report or an unsent draft using harmless input. Record the routine's repositories, environment, connectors, prompt, and actual access to required context. Check the output itself, not just the run status. Repeat the same logical job to observe whether it produces a clearly distinguishable duplicate, updates a previous draft, or recognizes completion.

Before any future externally visible side effect, test recovery from an ambiguous result: the target may have accepted a request even when the caller did not receive confirmation. Use only a sandbox. Reconcile against the target's record or supported idempotency mechanism before retrying.

**Decision rule:** native scheduling is sufficient when the required inputs, output retrieval, stop control, and recovery behavior are established. Projects-memory inheritance remains unproven until observed. A green infrastructure status is not the acceptance criterion. Source: S12.

## 3. Pass-2 decision probes

### T09 — Instruction ownership and activation

**Decisions:** AR-003, AR-006. **Status:** NOT RUN.

Make two test-only instruction variants with equivalent useful meaning: one broadly loaded and one deliberately activated only for its relevant task. Check imports and rule scoping against current documentation. Include a non-matching task to detect unwanted activation. Use valid frontmatter; test malformed configuration only in an isolated diagnostic fixture and never as a production trick.

Record what actually entered context and whether the task could find the required procedure. Do not call a split into `@` imports a context optimization unless the measured loading changed.

**Decision rule:** choose the arrangement that preserves behavior and improves relevance without multiplying authoritative copies. A shorter root file with equal or greater loaded text is not evidence of lower context cost. Sources: S07, S19.

### T10 — Concurrent memory updates and stale readers

**Decisions:** AR-004, AR-005. **Status:** NOT RUN.

In the same isolated Project, let two threads make disjoint harmless updates and inspect whether both survive. Then introduce an explicit correction to one test fact while another thread still has an older context. Observe synchronization, overwrite behavior, and the answer to a question depending on the corrected fact. Do not infer guarantees from one successful interleaving.

**Decision rule:** prefer native conflict handling if adequate. If updates are lost, restrict the affected write path or serialize only that operation; do not immediately invent a full memory service. Time-sensitive business state should instead be re-read from its authoritative source. If the underlying store exposes no safe update operation, document that constraint. Native behavior is unknown until this probe.

### T11 — Skill discovery, invocation, and supporting files

**Decisions:** AR-009. **Status:** NOT RUN.

Select a small representative set of existing, owner-used skills: a plain instruction skill, one with a supporting reference/script, and a delegated use case when available. Confirm name/description discoverability, actual body loading, dependency reachability, and one observable task-specific behavior. Test in the real target cloud/local route rather than assume a laptop installation transfers.

Distinguish an explicit request to use a skill from automatic relevance detection. If an invocation fails before its body is supplied, record that failure rather than reporting the skill as used. Do not audit the whole library or rewrite unfinished business skills in this probe.

**Decision rule:** repair a demonstrated loading/dependency fault with minimal packaging changes. Absence of full content in startup context is not itself a defect. Sources: S08, S19, S21.

### T12 — Hook contracts and bounded failure behavior

**Decisions:** AR-010, AR-017. **Status:** NOT RUN.

For a proposed necessary hook, test a matching event, a non-matching event, repeated delivery, handler failure, timeout, and overlapping handlers in an isolated fixture. Observe whether it blocks, allows, warns, or retries as intended for that event. Check working directory and tool-name matching. A Stop-based checker must be tested after an incomplete answer and after a legitimate answer with no further work.

**Decision rule:** a protection whose failure mode is undefined is not certified. An advisory helper should not deadlock unrelated work. A safety control must not silently turn a missing checker into permission. Never assume sequential execution of separate matching handlers. Source: S16; P02/P04 show why external plugins can add overlap.

### T13 — External memory or context tool pilot

**Decisions:** AR-013, AR-014. **Status:** NOT RUN.

Run only after a baseline failure establishes a need and the proposed installation route is supported. Pin the version and provider/storage configuration. Use isolated data; record which events are captured, where content goes, whether another new thread can retrieve it, and whether a correction/deletion propagates to all active retrieval paths. Check cold start, resumed process, and uninstall/rollback behavior.

For history memory, compare relevant recall and stale-fact rejection. For output processing, compare original-source coverage and evidence quality at lower context cost. These are different goals and must not share a misleading single score. Include a counterexample where exact wording is necessary and a short retrieved snippet is insufficient.

**Decision rule:** adoption requires a meaningful task improvement, an operable lifecycle, understood data handling, and acceptable maintenance. A successful installation, a doctor command, or a vendor percentage alone is insufficient. Sources: P01–P05, S05, S08, S20.

### T14 — Comprehensive review without source-loss through compression

**Decisions:** AR-007, AR-017. **Status:** NOT RUN.

Choose a bounded review with an explicit source set. Compare direct scoped reading with a retrieval/offloading approach. Require a coverage record distinguishing fully read, partially read, and inaccessible material. Include information whose interpretation depends on surrounding paragraphs or interacting files, not just an isolated keyword.

**Decision rule:** an optimizer is useful only if it preserves the evidence needed by the task. Counting files or summarizing search matches cannot stand in for a promised full content review. If a source cannot be read, the output must narrow its claim. No permanent synthetic benchmark suite is proposed. Source guidance: S23; the actual acceptance criteria are this research's proposal.

### T15 — Clean-reader handoff and reversible migration

**Decisions:** AR-016, AR-017. **Status:** NOT RUN.

Give a fresh builder only the three version-pinned research/audit repositories and the separately authorized installation context. Ask it to identify the owner's goals, scope exclusions, candidate decisions, unresolved blockers, required external configuration, and evidence needed before migration. It should be able to do this without guessing the original conversation.

For a later actual V3 candidate, preserve the V2 snapshot and verify a clean setup plus rollback using only the intended distribution and configuration guide. Re-read external state before resuming interrupted effects. A successful file extraction is not a successful migration.

**Decision rule:** missing context should be repaired in the handoff or explicit runtime manifest, not hidden in another permanent instruction file. This research does not perform the fresh-reader test or authorize a production migration.

## 4. Open contracts that affect implementation

| ID | Unknown | Evidence needed | Decision consequence |
|---|---|---|---|
| Q01 | Exact native coordinator visibility and retrieval tools | Accessible current Projects specification and/or T04 metadata and behavior | Choose the smallest working evidence handoff, not an invented omniscient coordinator. |
| Q02 | Native memory identity versus additional V2 stores | V2 read/write path trace and T03 | Blocks irreversible memory deletion or blind copying of all indexes. |
| Q03 | Native synchronization, stale readers, and concurrent updates | T03/T10 in target environment | Determines whether a narrow reconciliation/write policy is needed. |
| Q04 | Effective account/connector/hosted permissions | Actual configuration inventory and T06 | Blocks externally visible automation until supported authority is established. |
| Q05 | Routine context and duplicate-effect handling | T08 and target-system behavior | Determines whether a routine prompt suffices or a small transaction helper is justified. |
| Q06 | External plugin availability and persistence in the selected cloud route | T01/T07/T11/T13 | Blocks production reliance on a local-only installation assumption. |
| Q07 | Which changes reach existing versus new threads | T01/T05/T07 and current UI/runtime documentation | Determines restart and migration procedure; does not justify random restarts. |
| Q08 | Which V2 components currently prevent real failures | Separate audit/Red Team evidence at exact revisions | Prevents removal based solely on aesthetics or file age. |
| Q09 | External memory provider retention, export, deletion, and distributed-store semantics | Selected provider's current docs plus isolated tests | Blocks sensitive-data ingestion and cross-thread guarantees until resolved. |

Not every unknown blocks useful work. Read-only research can proceed with explicit limitations. Irreversible deletion, public posting, customer actions, and reliance on an unverified enforcement layer require stronger evidence.

## 5. Instructions for the other audit streams

Trace actual V2 read/write/loading paths before assigning a cause. A custom filename may refer to a native memory surface. A guard may be correctly implemented but absent in a particular environment. A skill may be discoverable but fail to invoke. A report may preserve evidence that its final summary omitted.

For each proposed removal, identify the behavior it currently provides, the evidence that the behavior matters, its native replacement if any, and the failure that the removal could reintroduce. A legacy protection does not become necessary simply because it exists; lack of an observed incident does not prove a safety boundary has no value.

For each claimed improvement, identify an observable outcome beyond fewer files, shorter text, or a passed format check. Do not present the owner's dissatisfaction as proof of a particular implementation bug. Do not present the old system's self-approval as proof that the bug is absent.

## 6. Self-critique boundary

The strongest counterarguments and disconfirming conditions are attached to the AR decision records in pass 2 rather than duplicated here. That critique was performed in the same research context. No independent panel, fresh-context reviewer, or cross-model validation was executed. The fourth chat should compare evidence across streams, not treat their agreement as an experimental replication.
