# Pass 2 — Information, instruction, and control architecture

Research edition: 2026-10-15. **Status: decision research delivered; all AR decisions remain proposals for the fourth chat. No V3 backend has been built.**

## Read this first

Apex is an e-commerce operator's working environment in the new Claude Code Projects experience. The native coordinator, called Tim, assigns work to threads. The intended work spans store development, marketing, email, customer operations, SEO, research, images, video, and recurring business tasks. The owner wants useful, creative, self-directed work without repeatedly repairing or cleaning the AI backend. The owner's phrase "allt för min ehandel" means the whole e-commerce operation; "inte restriktivt" means enabling rather than unnecessarily restrictive, not permission for uncontrolled external actions.

This is the architecture-research stream, not the V2 implementation audit or the independent Red Team stream. The fourth chat must compare all three at recorded commits before choosing a design. This report does not endorse recent V2 merges, diagnose unread V2 code, or judge the quality of the owner's existing business skills. It also does not promise faultless memory or attribute longstanding shallow work to a recently low usage balance.

The decision objective is **reliable useful work with low operator maintenance**, not the smallest possible number of files. The proposed starting candidate is a **native foundation with a minimal, explicit information contract**. Additional storage, control code, and automation must earn their place through a demonstrated requirement. This is narrower than rebuilding coordination, but more deliberate than deleting every custom file and hoping the native product handles all business knowledge.

### Reading and evidence contract

Read [platform boundaries](01-projects-architecture.md) for the product distinctions. Sources S01–S24, P01–P05, G01–G03, O01–O03, and U01 resolve in [the existing source register](01-sources.md). New sources S25–S26, P06–P09, and D01–D05 resolve in [pass-2 evidence and validation](02-evidence-and-validation.md). The [external-tool dossier](02-external-tools.md) records what was actually inspected in the two named candidate packages. Live tests T01–T15 and unresolved contracts Q01–Q09 remain in [the shared validation register](01-validation-and-handoff.md); they are not duplicated here.

Evidence labels retain their exact meaning:

- **DOCUMENTED PLATFORM BEHAVIOR** describes the inspected official documentation for its named surface, not every beta execution.
- **VERIFIED TECHNICAL EVIDENCE** identifies a directly inspected artifact or an actually executed local check; static inspection is not runtime verification.
- **THIRD-PARTY EXPERIENCE** includes maintainer descriptions and user reports not reproduced in Apex.
- **INFERENCE / HYPOTHESIS** is an explanation or predicted effect, not an observation.
- **RECOMMENDATION** is a candidate design choice, not production approval.
- **UNKNOWN / REQUIRES LIVE TEST** is a material unresolved contract.

All design sections below are RECOMMENDATION unless a different evidence label is attached. Each AR identifier is stable and may be accepted, rejected, or amended by the fourth chat. IDs are research navigation, not a proposal to load this report into every Apex session.

## 1. Supplement and corrections to pass 1

**DOCUMENTED PLATFORM BEHAVIOR — S25:** the Help Center's specifically labelled "The new version of projects (beta)" section describes one project conversation, parallel cloud threads, continuing work after the laptop is closed, project material available at thread start, and a Library for supplied/generated files. The section explicitly separates itself from the rest of that article, which describes the older product.

This strengthens PB-01 and C01 in pass 1: support for the basic native model is no longer confined to historical launch excerpts and UI observations. It does **not** establish that every file is fully inserted into every prompt, that threads see each other's full event streams, or that memory has transactional updates. S03, the detailed Projects page, remained inaccessible, including when followed directly from S25. Q01–Q03 and Q07 therefore remain open.

**Correction P2-COR-01:** do not reject every Help Center page as old-Projects evidence. Select the expressly applicable section and exclude the unrelated remainder. In particular, do not import the older article's RAG-capacity or collaboration claims into this beta design.

**Correction P2-COR-02:** "one authoritative owner" does not mean "one physical copy anywhere." A traceable, refreshable projection can be appropriate. The problem is independent competing authorities and lost provenance. A handoff summary is not wrong merely because its source also exists elsewhere.

**Correction P2-COR-03:** a documentation checker can pass materially false content. The new local probes demonstrate this boundary rather than merely warn about it. Do not interpret either the supplied auditor's exit code or a native routine's green status as substantive approval. The former is tested here; the latter is documented in S12.

**Correction P2-COR-04:** deeper external inspection supersedes the earlier manifest-only reading boundary for the particular files listed as P06–P09. It is still not a full code audit, package installation, or Projects compatibility test.

## 2. Compare complete options before selecting components

Using the divergent/convergent method from `idea-refine`, six candidates were considered before grouping the design into three families. The owner's requirements already establish the audience and desired outcomes; another interview or forced brainstorming checkpoint would not improve this decision.

| Candidate | Why it could help | Principal cost or failure | Disposition |
|---|---|---|---|
| Native context and memory only | Minimum custom machinery; uses the surface already visible to the owner | May leave important business facts, reproducibility, or recovery underspecified | Baseline worth testing, not proven sufficient |
| Everything in a versioned repository | Reviewable history and explicit artifacts | Repeated status snapshots, private data exposure, stale facts, and an agent maintaining its own bureaucracy | Reject as the default; retain versioned policy and durable source material where useful |
| Native foundation plus a small canonical business/reference layer | Makes non-derivable knowledge and responsibilities explicit without duplicating the coordinator | Requires careful boundaries and a few well-chosen references | Preferred candidate, conditional on loading and recovery tests |
| Automatic external history memory | May recover forgotten discoveries across isolated sessions | Capture, provider, synchronization, deletion, identity, and maintenance dependencies | Conditional pilot after a demonstrated history-retrieval gap |
| Off-context tool processing | May reduce oversized output while preserving searchable evidence | A short retrieved result can conceal missing coverage; routing adds behavior | Conditional processing option, not a replacement for authoritative memory |
| Automatic housekeeping/repair on every startup | Could detect broken links and stale pointers before work | Repeated overhead, shared-state races, unnecessary rewrites, and repair loops | Reject as a default architecture; consider a narrow measured check only |

No numerical score is invented: the live performance and maintenance data needed to justify one do not exist. Native-first and minimal hybrid are configurations to compare, while the external options are separate interventions. Installing both external tools together would confound diagnosis and multiply overlapping startup/capture paths.

The initial selection fails if native memory cannot preserve a needed correction, a required source is unreachable from the target thread, or the operator still has to reconstruct task state repeatedly. A failed native baseline is evidence to add the smallest effective missing capability, not a reason to defend native-first as an ideology.

## 3. Information ownership model

### 3.1 Separate three kinds of authority

**Instruction authority** asks what behavior the agent is supposed to follow. **Factual authority** asks which source establishes a business fact. **Action authority** asks who or what permits a real-world change. A text file can guide behavior without making its facts current or granting account permissions.

For example, a memory entry saying a promotion was approved last week cannot authorize a new send. A customer message is evidence of the customer's request, not authority to alter store policy. A product record can establish the currently recorded price, but it does not decide which future marketing strategy the owner prefers. These are proposed decision boundaries, not claims that native Projects automatically enforces them.

### 3.2 Canonical owners and bounded projections

| Information class | Candidate owner | Useful representation elsewhere | What should not happen |
|---|---|---|---|
| Owner preferences and stable working agreements | Native memory or a deliberately maintained policy source, with one clearly chosen owner per item | A small relevant extract in an assignment | Every thread invents a separate permanent preference file |
| Repository operation and non-obvious conventions | Repository instruction/contract source | A conditional pointer from project-level guidance | Full duplication in Project instructions, memory, and every skill |
| Brand vocabulary, product claims, reusable examples | Existing approved business source, or a compact reference document when no source exists | Task-selected excerpt with provenance | Treat generated copy as newly verified product truth |
| Price, stock, campaign status, account configuration | The relevant live business system for the queried scope | Dated report/cache with explicit limitations | A memory snapshot silently overrides a current authoritative read |
| Open task scope and progress | Native task/thread surface when adequate | A handoff checkpoint only when needed across a real context boundary | A second status ledger for every action and conversation |
| Durable architecture rationale | A decision entry in the existing documentation system | Link from affected instructions | Turn every small edit into a new ADR or historical file |
| Research and review evidence | Versioned report, source references, relevant logs | Concise claim plus pointer | Summaries become unqualified facts detached from their evidence |
| External-action approval | Supported authorization path for a concrete operation and target | Scope-preserving delegation message | A permanent "approved" memory entry becomes general permission |
| Secrets and customer-identifying data | Appropriate credential/data systems | Non-sensitive references only where needed | Raw secrets or private transcripts in the public research repo |

This table specifies logical ownership, not required filenames. One small document can fill multiple roles. A business system, UI setting, or task thread can own information without a corresponding Markdown file. D01/D02 support this role-first approach; assigning the owner's whole workflow to GitHub Issues is **not** an Anthropic requirement and is not recommended merely because the ECC contract uses an Issue tracker.

### 3.3 A correction lifecycle, not a memory bureaucracy

For information worth retaining, the writer should be able to identify its subject, scope, source, and whether it is a preference, observation, decision, or open hypothesis. The design does not require a universal YAML schema in native memory. Use the simplest format the actual store supports and the reader needs.

An explicit user correction is strong evidence about their intention or preference. A correction about an objective account state may need reconciliation with the live system. Neither "newest timestamp wins" nor "user text always overrides database state" is a generally adequate rule.

Updating a note requires locating its active owner, changing or superseding that representation, and checking that another active index is not reintroducing the old claim. Old transcripts may retain historical text without being active memory. Distinguish history retention from failed memory deletion. Storage deletion, retrieval exclusion, and removal from an already-running context are also different operations; Q03/Q09 cover the unresolved native and external details.

Cleanup should be driven by a demonstrated issue—contradiction, invalid pointer, ended temporary scope, or a corrected fact—rather than an arbitrary date or token ceiling. Low maintenance does not mean no lifecycle. It means the agent or supported workflow handles the ordinary lifecycle while surfacing only ambiguities that materially affect the user's decision.

## 4. Candidate decision register

| ID | Decision | Principal validation |
|---|---|---|
| [AR-001](#ar-001) | Treat the release as repository plus explicit runtime configuration | T01, T02, T07, T15 |
| [AR-002](#ar-002) | Identify native memory before replacing or deleting it | T03 |
| [AR-003](#ar-003) | Give each fact/rule an owner; allow traceable projections | T03, T09 |
| [AR-004](#ar-004) | Preserve corrections and manage concurrent/stale memory use | T03, T10 |
| [AR-005](#ar-005) | Keep volatile state and task execution out of durable memory authority | T08, T10 |
| [AR-006](#ar-006) | Separate instruction purpose from actual activation | T01, T09 |
| [AR-007](#ar-007) | Optimize context without substituting search snippets for promised coverage | T14 |
| [AR-008](#ar-008) | Use native coordination with a small evidence-preserving handoff | T04 |
| [AR-009](#ar-009) | Preserve skills; validate their real distribution and invocation path | T01, T11 |
| [AR-010](#ar-010) | Keep only justified, bounded control mechanisms | T02, T12 |
| [AR-011](#ar-011) | Separate creative autonomy from external-action authorization | T06 |
| [AR-012](#ar-012) | Prefer native scheduling with explicit inputs and outcome recovery | T08 |
| [AR-013](#ar-013) | Gate an external history-memory pilot on a demonstrated need | T07, T13 |
| [AR-014](#ar-014) | Evaluate output offloading as an independent processing intervention | T13, T14 |
| [AR-015](#ar-015) | Instrument effort before prescribing it | T05 |
| [AR-016](#ar-016) | Make migration selective and reversible | T07, T15 |
| [AR-017](#ar-017) | Tie completion to an artifact and task-specific evidence | T04, T12, T14, T15 |
| [AR-018](#ar-018) | Adopt documentation governance progressively, not as another platform | DG01–DG13 locally executed; semantic review still required |

<a id="ar-001"></a>
### AR-001 — A release is more than a repository

**Basis:** PB-04/PB-05, S04–S06 distinguish repository loading, hosted environment settings, and provisioning. **Unknown:** the target Project's exact configuration and existing-thread update semantics remain Q06/Q07.

**Options:** ship a repo alone; maintain a comprehensive machine/profile mirror; or ship the repo with a concise installation/verification description for only the external configuration it actually requires. A repo-only package is easy to copy but may silently omit dependencies. A complete mirror becomes another state store, can leak secrets, and drifts rapidly. The narrow description is the recommended compromise.

**Implementation implication:** the builder records the chosen execution route, attached repositories, required account capabilities, relevant environment setup, and where the owner configures each item. Record key names and purposes, not values. A dependency should have a supported installation route and a harmless capability probe. Do not store an ever-changing full tool catalog or mirror account settings for their own sake.

**Needed:** a reproducible configuration handoff, plus only genuinely necessary bootstrap commands. **Avoided:** a new platform launcher, an authentication mirror, and assumptions that a successful ZIP extraction proves a working environment.

**Disconfirming condition:** the actual product exports/restores all required non-secret configuration reliably, making part of the guide redundant. Prefer that supported export rather than maintain a second representation.

**Verify:** T01/T02 identify actual loading; T07 distinguishes stored dependencies from ready processes; T15 tests setup from the distribution. This decision does not choose the exact cloud/local topology before the other audits.

<a id="ar-002"></a>
### AR-002 — Identify native memory before prescribing another engine

**Basis:** O01 shows the team-memory index inside native Auto memory; S25 supplies applicable high-level Projects context. Generic CLI memory facts in S07 are not native Projects synchronization guarantees.

**Options:** preserve the existing store without inspecting its contents; remove all memory files; or identify the store and evaluate its contents/writers separately. Blind preservation accepts pollution; blind deletion risks removing a native capability. Choose the third option, with native memory as the initial baseline.

**Implementation implication:** the V2 auditor should trace a visible memory item to its actual read/write route, identify custom scripts touching it, and identify additional copies if any. Classify separately the storage service, index text, topic content, write policy, and cleaner. A correct native store with bad notes requires a different change from two independent engines writing incompatible summaries.

**Needed:** an identity map at migration time and a safe export/snapshot where supported. This can be a section of the migration review, not a permanent memory-map daemon. **Avoided:** installing a package based on stars, deleting indexes based on names, or copying both native memory and stale repo mirrors into V3 by default.

**Disconfirming condition:** native memory fails a required recovery/correction case while another supported solution succeeds with tolerable maintenance. That justifies a targeted hybrid or external trial, not indefinite loyalty to the baseline.

**Verify:** T03. Treat inability to inspect the store as unresolved evidence, not evidence it is broken. No particular V2 memory file is approved or condemned here.

<a id="ar-003"></a>
### AR-003 — One authoritative owner, not one physical copy

**Basis:** D02 permits multiple logical roles in one artifact; `writing-for-agents` emphasizes pointers and co-location. These are supplied design methods, not enforced product behavior.

**Options:** duplicate instructions broadly for discoverability; prohibit all duplication; or define canonical ownership and permit small labelled projections. Broad duplication makes corrections expensive. A no-copy rule can make independent threads miss essentials. Choose explicit ownership with proportionate projections.

**Implementation implication:** for each significant rule or business fact the builder retains, specify who may change it, its scope, and how consumers find it. A summary should identify the source/ref and material uncertainty when these affect use. It should not become a writable competing policy. Automatically generating projections is optional and only justified if manual alignment demonstrably fails; a generator is not the default.

**Needed:** useful context pointers and a way to recognize stale or superseded guidance. **Avoided:** parallel fact/decision/status files maintained separately merely because an older template used them.

**Example:** an email assignment may repeat the currently applicable offer boundary and link to its source. That repetition serves an isolated task. Persisting an unqualified copy of the offer indefinitely in every thread's memory does not.

**Disconfirming condition:** consumers cannot access the canonical source reliably or a critical boundary repeatedly disappears at handoff. Permit a narrowly scoped, traceable copy at that boundary and test it. Do not solve accessibility through purity about deduplication.

**Verify:** T03/T09, including a changed source and a non-matching task. Assess whether the correction reaches consumers, not just whether duplicate text was removed.

<a id="ar-004"></a>
### AR-004 — Make correction and concurrency explicit requirements

**Basis:** native locking, conflict resolution, and refresh in existing threads remain UNKNOWN. The audit skill identifies pollution and stale persistence as mechanisms to investigate; it does not establish that Apex suffers each one.

**Options:** allow every thread to rewrite every memory item; serialize all writes through Tim; or use native behavior and narrow the write path only where concurrent updates fail. Fully centralizing every note could turn Tim into the bottleneck the owner already dislikes. Unrestricted shared rewriting may lose corrections. Start with native behavior and test, then constrain the smallest affected operation if needed.

**Implementation implication:** identify whether an update is a new observation, a correction, or a replacement. Do not compress contradictory claims into a falsely confident blend. Preserve provenance sufficient to revisit a material dispute. A running thread holding stale context should re-read a critical current source before an irreversible action; a timestamp on a file is not proof of renewed factual validation.

**Needed:** a correction/deletion workflow compatible with the native store and a clear escalation for unresolved contradictions. **Avoided:** a global lock manager, automatic daily rewrites, and a blanket rule that all memory edits must go through the coordinator before evidence shows necessity.

**Disconfirming condition:** loss or contamination persists across realistic concurrent cases, or native updates expose no safe path. Then a single writer for the affected collection, a small reconciliation step, or different storage becomes reasonable. The change should target the observed failure, not introduce a universal transaction system.

**Verify:** T03/T10. One successful interleaving is not proof of concurrency safety; failed or delayed refresh must be recorded without overgeneralizing beyond the tested surface.

<a id="ar-005"></a>
### AR-005 — Durable memory must not impersonate current task or account state

**Basis:** S23 distinguishes persistence and context retrieval as design techniques; no inspected source proves memory is a current business-system replica. The ownership table above is a proposed Apex contract.

**Options:** put all open work and account facts in memory; use native task state plus live sources exclusively; or add small recovery checkpoints when native task context is insufficient. The first invites stale instructions and repeated rewriting. The second is clean but may fail at genuine context boundaries. Choose native task state and live reads, with bounded checkpoints only for observed recovery needs.

**Implementation implication:** a checkpoint should identify an unfinished objective, relevant artifact/ref, verified completed effects, unresolved effects, and next dependency. It should not be a second full transcript or a new permanent personal diary for every worker. Ended tasks need not be deleted from historical conversation, but should stop presenting themselves as current work.

**Needed:** source-aware reads for volatile facts and recovery data for long or interrupted work where necessary. **Avoided:** storing "campaign sent" only as narrative memory, polling every file to reconstruct status, and a parallel Issue tracker unless it adds real workflow value.

**Disconfirming condition:** native task surfaces repeatedly fail to resume important work or cannot provide the state to a routine. A concise external checkpoint may then be justified. Its scope should follow the task, not silently become another global memory engine.

**Verify:** T08/T10, including the ambiguous-effect case: a request may have succeeded externally even when the caller did not receive confirmation. Resolve that through the target's state or supported idempotency facility, not by believing or clearing a note.

<a id="ar-006"></a>
### AR-006 — Decide instruction purpose and activation separately

**DOCUMENTED PLATFORM BEHAVIOR — S07/S08:** imported CLAUDE.md content loads at launch; unscoped rules load broadly, while path-scoped rules depend on relevant file activity. Skills have a separate discovery/invocation lifecycle. These contracts do not establish the hidden priority of native Project Goal or Project instructions.

**Options:** one giant global instruction; many always-loaded files; or a small global core with task-conditioned references and supported scoped mechanisms. The first two may differ in file count but not loaded content. Choose the third, while testing whether the intended consumer can actually reach a reference.

**Implementation implication:** Project-level guidance should express shared business intent and working agreements that both coordination and work need. Repository instructions should identify how to operate this repo and reach relevant sources. Skill bodies should carry their specialized methods. A path-scoped rule for local content files does not automatically cover a campaign action performed entirely through an external tool. Critical action boundaries belong in a supported enforcement route, not only a conditional document.

**Needed:** a content specification for each retained instruction source: consumer, trigger, expected behavior, evidence owner, and exception path. Keep concepts and caveats together. **Avoided:** fake numeric precedence between prose files, a mandatory four-file governance spine, and moving text into imports while claiming reduced context.

**Disconfirming condition:** conditional discovery repeatedly misses a short essential instruction. Move that specific boundary into the shared core or strengthen its pointer; do not load the entire procedure globally.

**Verify:** T01/T09 across matching and non-matching tasks. The writing specification in section 5 is a blueprint for the fourth chat, not a finished CLAUDE.md.

<a id="ar-007"></a>
### AR-007 — Preserve evidence while reducing context

**Basis:** S23 supports deliberate retrieval and context selection. The owner explicitly requires deep review rather than superficial summarization; that requirement controls coverage.

**Options:** always load every source; use only search snippets/summaries; or perform scoped retrieval with a coverage contract and preserve access to originals. Exhaustive loading can waste attention, while snippets can miss interactions and exceptions. Choose the third, with full reading wherever the task actually promises it.

**Implementation implication:** distinguish discovery, substantive reading, analysis, and summarization. A script may enumerate files or compute statistics without proving the model evaluated every instruction. During an exhaustive backend review, each relevant file needs a clear read status and evidence-backed findings. For a focused lookup, a narrow source passage may be sufficient. These are different tasks and should not share one universal context policy.

A concise handoff can carry a finding, source/ref, affected behavior, and uncertainty while leaving the full evidence reachable. Exact wording, exceptions, and surrounding context should be re-read before an instruction-dependent conclusion. A compressed note is a derivative view, not stronger evidence than its source.

**Needed:** task-appropriate coverage and source pointers; local computation for operations where computation is actually the task. **Avoided:** mandatory transcript dumps, blanket "always summarize before reading" rules, and declaring success from lower token counts alone.

**Disconfirming condition:** the retrieval approach fails a material cross-file interaction or cannot recover exact source context. Expand the reading boundary or use direct reading for that class of work; reject the optimizer if fidelity remains worse.

**Verify:** T14, not a fabricated permanent benchmark suite. Record false positives and unsupported assurances, not just the number of findings.

<a id="ar-008"></a>
### AR-008 — Keep native coordination, improve the handoff contract first

**Basis:** S25 supports native parallel threads. Q01 still separates what Tim receives automatically, can retrieve, actually reads, and verifies.

**Options:** build another coordinator; force every worker through a rigid multi-stage ceremony; or use native coordination with a compact assignment and result contract for substantial tasks. Choose the last until an actual missing transport or capability is demonstrated. A second coordinator cannot fix unavailable evidence simply by renaming the role.

**Implementation implication:** Tim should convert a vague business request into a useful scoped assignment rather than just forward the wording. For a substantial assignment, preserve objective, boundaries, required sources, expected artifact, material dependencies, and any action approval. A returned result should identify what exists, what evidence supports it, and what remains blocked or uncertain. This need not appear as a visible template in every message.

Parallelize separable work; reconcile shared facts before combining results. Keep a coherent source/ref when two workers modify related material. Do not assume instructions to a worker constitute successful delivery or that a worker's reassuring summary proves its report was read.

**Needed:** evidence-preserving task briefs and synthesis discipline, implemented in the smallest supported instructional surface. **Avoided:** a parallel agent registry, mandatory reviewer swarms, and a coordinator that approves every harmless thought.

**Disconfirming condition:** the native tools cannot return or retrieve the evidence needed to coordinate. Then select a supported artifact handoff or a limited connector—not an undocumented invented API.

**Verify:** T04. Compare request, assignment, underlying artifact, and synthesis. Track loss at each boundary rather than blame the final model by default.

<a id="ar-009"></a>
### AR-009 — Preserve working skills and verify their actual route

**DOCUMENTED PLATFORM BEHAVIOR — S08:** local personal skills are not automatically available in cloud sessions. Account and repository routes differ. `allowed-tools` grants turn-scoped preapproval; it is not an exclusive tool allowlist. Synced skills can also differ in supported frontmatter/body behavior.

**Options:** load every skill at startup; impose a receipt gate on every response; or preserve skills and verify representative discovery-to-result paths. Choose the third. A large library is not by itself a defect, and unfinished business skills need not become production-certified before the backend can improve.

**Implementation implication:** preserve skill directories with supporting files and relevant licenses. Resolve names/collisions, invocation route, required scripts, credentials, and environment separately from prose quality. A standalone library file may need packaging rather than rewriting. Changing from repo-distributed to account-synced is not assumed behavior-neutral; test any dynamic injection or execution-specific feature that the skill relies on.

Show actual skill use through relevant behavior and diagnostic evidence when the user asks, not by trusting a self-authored name list. A skill that was mentioned or opened for a link audit was not necessarily invoked for business work. Conversely, its whole body need not be in startup context to be available.

**Needed:** a few representative load/dependency checks and precise discoverability text. **Avoided:** a broad skill-content audit, an inventory-based token cost formula, and mandatory chaining of unrelated stylistic skills after all writing.

**Disconfirming condition:** automatic selection repeatedly fails on a useful skill despite a sound route. Repair its trigger or invoke it explicitly for the affected workflow; do not globally preload the entire library.

**Verify:** T01/T11, including a supporting-file skill and the real cloud/local route. No blanket declaration that all copied skills will work is made.

<a id="ar-010"></a>
### AR-010 — Controls must have an explicit contract and bounded cost

**DOCUMENTED PLATFORM BEHAVIOR — S16:** matching hooks can run in parallel. Their exit/error semantics depend on the event. A post-tool hook cannot retroactively prevent an already-executed tool. Stop continuation is not business completion. Supported failure handling is not identical across hook types.

**Options:** remove all guards; retain every legacy guard; or justify each control by the actual event, protected outcome, failure mode, and cost. Choose the third. The lack of a recorded incident is not proof a safety boundary is useless; the existence of many passing tests is not proof it protects the intended outcome.

**Implementation implication:** distinguish advisory guidance, mechanical validation, and authorization enforcement. An advisory helper should normally fail without trapping unrelated work. A critical authorization check needs a supported fail-closed route, tested in the actual environment. Its absence must not silently become permission. Define behavior for malformed input, missing executable, timeout, duplicate delivery, parallel handlers, and unavailable dependencies.

Prefer a native facility where it provides the required protection. A custom hook is justified when it closes a specific gap with lower total risk than the alternative. A bounded on-demand checker may be better than a startup hook when its subject rarely changes. Do not assume a stop-loop cap protects against every repair pattern or is identical in native Projects.

**Needed:** a small retained set with clear contracts and observable failures. **Avoided:** form-based reassurance checks masquerading as truth verification and chains of agents repeatedly fixing one another's wording.

**Disconfirming condition:** removal measurably restores an important error or a native replacement misses the protected case. Retain or narrow that control.

**Verify:** T02/T12. Exact production hook code remains the fourth chat's responsibility after V2 evidence is compared.

<a id="ar-011"></a>
### AR-011 — Preserve autonomy in thought; scope authority for effects

**Basis:** S14/S22 describe permission mechanisms, while S04/S05 constrain where configuration applies. G01/G02 are incident leads, not blanket explanations for an Apex denial.

**Options:** ask before every action; let broad prose approval authorize everything; or distinguish exploration/drafting from externally consequential operations using supported permissions and concrete approval scope. The first destroys useful autonomy; the second is unsafe and can be technically ineffective. Choose the third.

**Implementation implication:** an exploratory analysis should be free to investigate and propose alternatives within its authorized tools. Sending, publishing, spending, deleting, or modifying a live business record requires the applicable action boundary. An approval should identify the operation and target sufficiently to survive delegation. The exact supported approval route must be tested; do not invent a memory token that bypasses platform controls.

Classify an action by its meaning, not only its tool name or HTTP verb. A generic shell or API client may reach several systems. Read capability is not write authorization; a successful credential check is not approval. If blocked, identify the actual layer before changing policy. Use a supported remediation or report the blocker; do not try alternate routes merely to evade denial.

**Needed:** appropriately scoped connectors/credentials and an intelligible distinction between drafts and committed effects. **Avoided:** needless approvals for creative thinking, global wildcard permissions adopted for convenience, and duplicate contradictory authorization ledgers.

**Disconfirming condition:** the available hosted surface cannot express or reliably execute the required approved workflow. Reduce that workflow's automation or select a supported authorized route; do not claim better prose fixes an unavailable control.

**Verify:** T06 in a disposable target. No production permission policy is certified by this research.

<a id="ar-012"></a>
### AR-012 — Native routines first, with explicit outcome and recovery

**DOCUMENTED PLATFORM BEHAVIOR — S12:** routines have separately configured inputs and connections; their green run status is infrastructure status, not evidence that the requested task succeeded. Native Project memory inheritance remains unresolved.

**Options:** build a custom scheduler, assume every routine inherits all Project context, or configure native routines with explicit dependencies and outcome retrieval. Prefer native scheduling where its supported behavior meets the task. Add only a narrow adapter for a demonstrated gap.

**Implementation implication:** specify the task's required sources, relevant working agreement, output location, and how a blocked or partial result becomes visible. A daily report may need a time window and clear data freshness. A draft workflow needs a stable way to locate its draft. A side-effecting workflow also needs duplicate prevention or reconciliation against the target system when a prior response was ambiguous.

Do not treat a session ID as a logical job identity or promise exactly-once effects through narrative instructions. A rerun should recognize the intended unit of work where the provider supports such a check. If the API offers no idempotency and the result is ambiguous, human reconciliation can be the correct safe boundary.

**Needed:** minimal routine configuration and a task-specific completion/recovery definition. **Avoided:** cron infrastructure duplicating native scheduling and an always-growing Markdown log of every wakeup.

**Disconfirming condition:** a necessary trigger, connection, or recovery behavior is unavailable. Evaluate a small integration for that gap, or keep the activity interactive. An unsupported assumption should not be hidden in the routine prompt.

**Verify:** T08 before unattended external effects. A read-only or draft-only starting case reduces risk without pretending every e-commerce workflow must remain read-only forever.

<a id="ar-013"></a>
### AR-013 — External history memory requires a deployment and data case

**Basis:** P01/P02 describe and declare claude-mem capture/recall; P08/P09 deepen synchronization and device-identity evidence. No installation or end-to-end Projects test was performed. See the external dossier for the static evidence and unresolved provider details.

**Options:** native memory; a compact task checkpoint; local external history memory; or a hosted/shared external history service. These solve different continuity boundaries. Native memory may be enough for preferences; checkpoints may solve unfinished work; searchable external history may help repeatedly rediscoverable technical findings.

**Recommendation:** do not include claude-mem in the default V3 foundation merely because it is popular or promises automatic operation. Trial it only after identifying a repeatable retrieval gap that the simpler options do not solve. Conversely, do not reject it solely because it introduces a process: that process can be worthwhile if it reliably removes a larger operator burden.

**Needed if adopted:** a supported package route, worker readiness, durable storage, meaningful project/identity boundaries, approved provider/data handling, correction/deletion/export behavior, and rollback. These are operational requirements, not an instruction to build a custom sync service.

**Avoided while unproven:** overlapping automatic memory writers and a service whose local success is advertised as shared cloud-thread memory.

**Disconfirming condition:** a controlled pilot shows materially better correct recall across the needed boundary, with manageable total cost and no unacceptable stale/privacy failures. That would justify adoption or a narrow deployment despite this conservative default.

**Verify:** T07/T13. Evaluate correction rejection and failed/offline recovery, not just the ability to retrieve one saved observation. Provider marketing savings are not an Apex measurement.

<a id="ar-014"></a>
### AR-014 — Output offloading is not the same decision as long-term memory

**Basis:** P03/P04 describe context-mode's processing and capture. P06/P07 show selected routing, readiness, and maintenance paths. These establish inspected code behavior, not operational success or native Projects compatibility.

**Options:** direct scoped reading, native tool-output handling plus small local computation, MCP-only processing, or a full routing/capture plugin. Begin with direct/native handling for ordinary tasks; consider the narrower processing route when oversized results genuinely block useful work. A full plugin needs additional lifecycle evidence.

**Implementation implication:** assess what the agent must understand, not just how many bytes it can avoid seeing. Aggregating sales rows is a computational task where compact output may preserve the result. Reviewing every backend instruction is a semantic task where a count or search snippet does not meet the coverage promise. A retrieval index must retain a path to exact originals and surrounding context.

**Needed if adopted:** supported tools, preserved provenance, meaningful availability checks, reproducible source coverage, and understood persistence/capture boundaries. **Avoided:** claiming this is a shared Project memory replacement and enabling routing restrictions before the alternative tool is available.

**Disconfirming condition:** the pilot preserves or improves finding quality and source coverage while lowering real workload cost enough to justify the added dependency. If it suppresses exact evidence, creates extra repair work, or cannot be supported in the chosen cloud route, do not adopt it there.

**Verify:** T13/T14. Compare MCP-only and plugin variants separately. A successful doctor command certifies neither the full business task nor the safety of every maintenance path.

<a id="ar-015"></a>
### AR-015 — Measure effective effort without confusing it with architecture

**Basis:** S09/S21 and O02 distinguish configurable/model-dependent effort from observed UI defaults. No controlled comparison has been run.

**Options:** set maximum effort everywhere; optimize for minimum effort/usage; or measure coordinator and worker interventions separately. The first may waste resources, the second can trade away needed depth, and neither diagnoses missing context. Choose the third.

**Implementation implication:** record the model, effective effort where observable, instruction revision, source availability, and task type in a comparison. A coordination-heavy task tests decomposition and synthesis; a reasoning-heavy worker task tests analysis with equivalent sources. Keep failed attempts visible. Do not change both the backend and the model and credit the backend alone.

**Needed:** a small measurement record during evaluation and a practical default justified by results. **Avoided:** new runtime code enforcing a universal thought duration, prompt phrases asserted to set API effort, and repetitive "think harder" additions throughout the backend.

**Disconfirming condition:** representative tasks show a stable simpler default with no meaningful quality loss. Use that default rather than maintain complex per-task routing. If important tasks need higher effort, scope the exception to those tasks.

**Verify:** T05. Exact production calibration, model/effort recommendations, and the broader quality comparison belong to pass 3. This record deliberately supplies experimental boundaries rather than pretend to settle that future work.

<a id="ar-016"></a>
### AR-016 — Migrate responsibilities selectively and preserve recovery

**Basis:** the user wants a new foundation while preserving working skills/reference assets. This is a scope requirement, not a technical finding about which V2 files are sound.

**Options:** mutate V2 in place, copy V2 wholesale and rename it, or construct a separate candidate with explicit keep/change/omit decisions. Choose the separate candidate. It allows a broad redesign without destroying the fallback or automatically carrying forward obsolete control layers.

**Implementation implication:** pin the V2 snapshot, identify retained assets and dependencies, and record the reason for each meaningful omission. A removed file's active references must be redirected or deliberately retired. Preserve important historical evidence without injecting it into active instruction context. Include configuration outside Git in the migration review. Test representative business workflows, not just JSON syntax and link resolution.

**Needed:** a reversible migration checklist and a clear cutover point after live evidence. **Avoided:** reimplementing the business skill library, copying raw memory indiscriminately, or a giant new administration tree built only to track the migration.

**Disconfirming condition:** the smallest adequate repair is demonstrably a narrow V2 change and a separate deployment creates more risk than benefit. The fourth chat should be allowed to retain more of V2 than expected if evidence supports it; the V3 name is not a mandate to replace useful behavior.

**Verify:** T07/T15 plus relevant feature probes. A file's age, a prior merge, or an impressive test count cannot substitute for its functional role in this decision.

<a id="ar-017"></a>
### AR-017 — Completion evidence must match the task's claim

**Basis:** S12/S16 distinguish run/response events from task success. S26 discusses evaluating tools through useful task outcomes. The local DG probes independently show that structural success can coexist with false content.

**Options:** require a keyword/receipt, mandate multiple AI approvals, or attach proportionate evidence to the promised outcome. Choose the last. Independent review can be valuable for high-impact changes, but agreement between reviewers is not proof if each relies on the same unsupported summary.

**Implementation implication:** separate artifact produced, artifact checked, and external effect confirmed. For a review, evidence is coverage plus supported findings and uncertainty. For copy, it includes the actual draft and factual/brand constraints, with creative judgment still visible. For a store change, it includes the intended effect checked in an appropriate environment. For an external send, a target-system confirmation and authorized scope matter more than a local test log.

A record may be prose or structured data. Typed JSON can prevent schema mistakes but cannot make an invented field truthful. Avoid a single universal completion form imposed on every small task. Tim should be able to surface what is done, what is blocked, and why a remaining uncertainty matters without burying the user in process.

**Needed:** observable artifacts, precise claims, and retained evidence for consequential outcomes. **Avoided:** reassurance-word policing, automatic extra reviewers for trivial tasks, and tests designed merely to agree with the new instructions.

**Disconfirming condition:** a proportionate approach leaves a recurring serious class of failures undetected. Add a narrowly targeted independent check for that class, preserving its cost and false-positive evidence.

**Verify:** T04/T12/T14/T15. The same-context challenges below are not represented as an outside reviewer.

<a id="ar-018"></a>
### AR-018 — Documentation governance must remain smaller than the work

**Basis:** D01/D02 explicitly define optional, role-based adoption. D03/D04 were inspected and exercised in DG01–DG13. Their success means only the specified mechanical checks passed.

**Options:** install the whole default governance spine, ignore documentation integrity, or reuse actual information owners and run narrowly useful checks on demand. Choose the third. Neither a missing default filename nor a warning is sufficient reason to create another file.

**Implementation implication:** begin with what already owns instructions, navigation, decisions, and evidence. Map roles only when the mapping resolves a real ambiguity. The supplied router's Issue-tracker ownership is an ecosystem convention; the builder should choose the supported native task owner for Apex unless a separate tracker proves valuable. Keep decision IDs in this research corpus for cross-stream comparison, not as mandatory files in production.

The mechanical auditor can help find broken local targets or invalid mappings. It does not establish that a source is true, an anchor exists, an external link works, a task finished, or an instruction was followed. Its orphan heuristic has a directory boundary. The executed probes document these limits without calling the script a failure for not being a semantic reviewer.

**Needed:** a small information-role map in the design and optional integrity checks appropriate to the actual structure. **Avoided:** empty constitution/map/status/history shells, automatic archive mutations, a second task tracker, and an every-startup documentation repair loop.

**Disconfirming condition:** repeated real documentation failures impose higher operator cost than a simple scheduled or commit-time check. Introduce that check with an explicit scope and measured noise; do not promote all warnings into blockers.

**Verify:** DG01–DG13 were run locally on disposable fixtures. No live Apex check is implied. Semantic review and the clean-reader test remain separate obligations.

## 5. Writing specification for the eventual backend

This section defines what the fourth chat should produce after reconciling the audits. It deliberately does not provide a final CLAUDE.md or a mandatory file tree.

### 5.1 Test each proposed instruction against its job

For a permanent instruction, identify its intended reader, the situation in which it matters, the observable behavior it asks for, and the authoritative source of any embedded fact. If the instruction is a procedure, consider a skill or a conditional reference. If it is ordinary repo data readily available from a single reliable lookup, embedding another copy needs justification. If it governs a real-world effect, identify the enforcing surface rather than pretend the wording enforces itself.

A useful pointer gives both the subject and the condition for reading it. "More details in docs" is weak. A candidate such as "For a customer-facing claim, consult the approved product-claim source before drafting the claim" is clearer because it identifies a consumer and a trigger. Its exact target must exist in V3; this example is not a literal filename or final operational instruction.

Group a concept with its caveats. Do not put the primary rule in one file, exceptions in another always-loaded file, and the authority to change it in memory. A reference should be short enough to find but complete enough for its decision. Shorter is not necessarily better when removing a caveat changes the meaning.

### 5.2 Assign roles deliberately

**Project Goal:** use only for the supported purpose established in the actual product. A broad business aspiration is not a testable assignment, and the empty field does not prove the rest of the instructions are absent. Its precise effect remains a live configuration question.

**Project instructions:** candidate home for shared intent, owner collaboration style, task interpretation, and navigation relevant across the project's activities. Do not duplicate the entire repository guide here. A private business context need not be placed in a public repo to be available to the project.

**CLAUDE.md:** candidate home for repo-specific operation, non-obvious conventions, and concise pointers needed by repo workers. Discoverable commands and interface facts should have a reliable source; avoid restating long lists that drift. The file should not become a transcript, live task board, or encyclopedia of every e-commerce method.

**Rules and specialized documents:** use when their activation and reader are clear. Grouping Markdown into folders is not evidence of conditional loading. Do not depend on an unsupported frontmatter field silently doing what its name suggests.

**Skills:** retain specialist methods and supporting resources. Change packaging or triggers only for demonstrated issues within scope. Skill content may persist while permission grants have different lifetimes; the writer should not conflate those states.

**Memory:** retain useful non-derivable preferences/corrections and compact context, subject to the native store's verified lifecycle. It should not be the sole place where external completion or current account state is asserted.

**Evidence and history:** preserve important findings and rationale in retrievable artifacts, without forcing every new thread to read the entire history. A prior failure remains useful evidence after a clean current state; it is not necessarily an active instruction.

### 5.3 Avoid brittle universal language

"Always use three agents," "never ask a question," "every answer under fifteen lines," and "a passing check means done" would erase distinctions the design needs. More useful specifications describe when parallel work helps, when ambiguity blocks an irreversible step, what constitutes sufficient evidence, and how the user receives the result.

Likewise, positive wording is a clarity technique, not a theorem that prohibitions cannot work. Preserve necessary explicit boundaries. Use concrete outcomes instead of ceremonial adjectives such as "be extremely thorough" with no coverage requirement. Do not add timers or word counts as proxies for analytical depth.

## 6. Representative end-to-end examples

These are design walkthroughs, not executed tests or templates that every task must follow.

### A. A source-backed email campaign draft

Tim interprets the commercial objective and locates the approved offer/product context. The worker uses the relevant existing writing skill and supporting examples. Current offer details are verified against the chosen source; brand guidance is selected without loading unrelated SEO or system-repair instructions. The artifact is an actual draft, with unresolved factual questions visible. Draft creation and sending remain separate actions. Only reusable approved preferences belong in durable memory; the draft's status belongs with the task/artifact. This exercises AR-003, AR-005, AR-008, AR-009, AR-011, and AR-017.

### B. A detailed SEO or backend review

The assignment states the source set and the depth promised. A source inventory helps plan reading but does not replace it. The reviewer reads the relevant content, traces interactions, and marks inaccessible material. Automation may enumerate links or calculate counts; semantic claims still need evidence. Tim receives the report and its coverage, not just "all clear." The result can be concise for the owner while the underlying evidence remains accessible. This exercises AR-006, AR-007, AR-008, and AR-017.

### C. A creative short-video concept and production handoff

The worker has the brand, audience, and necessary constraints, but is not forced into the same checklist as a code change. It proposes distinct concepts with useful rationale and flags factual claims that require support. A rendered asset, a storyboard, and a production plan are different deliverables. A remote/local tool dependency should be stated rather than hidden by calling a concept "finished video." Publication is a later authorized effect. This exercises AR-001, AR-009, AR-011, and AR-017.

### D. Resuming a task in another thread after a correction

The new worker uses the current task artifact and the corrected preference's owner. It distinguishes a historical conversation from active policy. Where the old thread is still running, a critical current fact is reread before action. If two threads updated different notes, their disjoint updates should survive; if not, the observed failure informs AR-004. The owner should not have to reconstruct the story manually unless there is a substantive unresolved choice.

### E. A daily operational report

A native routine has explicit data sources, period, and output destination. Its configuration does not assume the laptop's personal skills or the Project's full memory are inherited. The output identifies missing data and successful retrieval separately. A green session without a usable report is not accepted. Repeating the same job should not create an unnoticed externally consequential duplicate. This exercises AR-005, AR-009, AR-012, and AR-017.

## 7. Same-context challenge and changes to the recommendation

The `doubt-driven-development` method normally requests a fresh-context reviewer. None was invoked here. The following is explicitly a same-context challenge; the independent Red Team and fourth chat remain necessary opportunities for different criticism.

| Claim challenged | Strong counterargument | Resolution and disconfirming evidence |
|---|---|---|
| Native-first is the simplest good design | A native beta with unclear correction/recovery semantics can demand more manual repair than a mature external service | Recommend a tested native foundation with minimal explicit contracts, not unconditional native-only. T03/T10/T13 can reverse the selection. |
| Every fact should have only one representation | Isolated threads or routines may lack access at the moment they need it | Narrowed to one authoritative owner; allow traceable bounded projections and test staleness at handoff. |
| Removing guards improves autonomy | Some controls protect customers even when no past incident was recorded | Use event/outcome/failure contracts to retain justified controls. Do not equate no incident with no value. |
| A context-saving tool improves deep work | Its retrieval may hide a caveat or omit interacting files, making a shorter answer confidently wrong | Require source coverage and exact-evidence recovery. Reject an optimizer that wins only on bytes. |
| Documentation governance will prevent disorder | A role map can create more files and a green checker can hide semantic failure | Adopt roles progressively; the actual DG probes demonstrate why semantic review is separate. |
| One shared coordinator should own every correction | It can become an approval bottleneck and may itself lack complete context | Constrain only the memory operation shown to fail; preserve direct supported native updates elsewhere. |

The recommended architecture is therefore not "remove everything and install nothing." It is **separate information responsibilities, prove activation, preserve trustworthy evidence, and add machinery only at demonstrated boundaries**. That direction remains conditional on the other streams' concrete V2 findings.

## 8. Builder-facing implications and remaining work

The fourth chat should first pin the three input repositories and reconcile incompatible evidence. It can then group changes by responsibility rather than blindly copy or delete filenames. Start with an unchanged V2 fallback, a selected native/hybrid candidate, and a small set of tasks that can reveal the reported failures. Change one causal factor at a time where diagnosis matters; large structural changes can still be justified after the contracts are understood.

The dependency order is: identify actual storage/loading/authority boundaries; decide information owners; specify instruction consumers and activation; select required controls; validate external dependencies; construct the candidate; test representative outcomes and recovery. Parallel work is appropriate inside independent responsibilities, not across contradictory assumptions about the same memory store.

Do not copy this entire research corpus into the active V3 instruction path. It exists for the architect. The eventual runtime should contain only the contracts and references the selected design needs. Likewise, AR records do not imply eighteen production modules.

**Still unresolved:** native memory concurrency/refresh; complete coordinator visibility; effective permissions and routine context; external-provider deletion/retention in a selected deployment; actual V2 mechanisms worth preserving; and measured effort trade-offs. These map to Q01–Q09 and T01–T15 rather than being concealed behind confident defaults.

**Pass 3 remains pending.** It should calibrate effort and outcome quality, challenge the cross-cutting recommendations with the user's additional skill instructions, reconcile remaining research contradictions, and publish the standalone Architecture Research Handoff. The other audit repositories have not been read or treated as approved inputs by this stream. No final production architecture or backend is authorized by this pass alone.
