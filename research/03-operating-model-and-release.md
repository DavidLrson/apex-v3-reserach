# Pass 3 — Operating model, effort calibration, and release decisions

Edition: 2026-10-15. **Final research pass; recommendations, not a deployed or runtime-certified Apex system.**

Read this report when deciding how the proposed information architecture should behave during real work, how much autonomy and effort to use, and when a candidate is ready to replace V2. The [Architecture Research Handoff](../ARCHITECTURE-RESEARCH-HANDOFF.md) is the entry point for the fourth chat. The [pass-2 decision records](02-information-architecture.md) remain the canonical rationale for AR-001–AR-018; this report refines their operational consequences rather than creating eighteen new modules.

Sources S01–S24 are in [the first register](01-sources.md), S25–S26 and the supplied audit methods are in [the second register](02-evidence-and-validation.md), and S27–S32 plus refreshed sources are in [the final source and quality register](03-sources-and-quality.md). Tests T01–T15 and questions Q01–Q09 retain their meanings in [the shared validation register](01-validation-and-handoff.md). **All live Claude Projects tests remain NOT RUN.**

## 1. Final design position

**RECOMMENDATION:** build a candidate on the native Projects foundation, with a small, explicit information and action contract. Preserve useful skills and business assets. Add machinery only where a specific missing capability and a supported execution route have been established. This is the preferred candidate for evaluation, not a finding that native memory is sufficient or that all existing hooks are unnecessary.

The alternative to an overcomplicated backend is not an empty backend. It is a backend whose responsibilities are intelligible: where current facts come from, how relevant instructions reach a task, how work is handed back, which effects are authorized, and how unfinished work is resumed. The owner should not have to maintain those mechanics during an ordinary working day.

The fourth chat should produce one selected design, not a catalogue of mutually incompatible recommendations. It can adopt a recommendation now, amend it with V2 evidence, defer a conditional feature, or reject it with a reason. “Research finished” means the evidence and decisions are usable; it does not mean all product uncertainties have disappeared.

The minimum successful outcome is practical: an owner can give a meaningful ecommerce task, receive the promised artifact with honest limitations, and continue later without reconstructing the backend. A configuration that is easy to explain but regularly loses work is not adequate. A configuration that needs constant manual cleaning is not adequate either.

## 2. Diagnose the failed boundary before changing a setting

AR-015 must be applied alongside AR-006–AR-009 and AR-017. The same short answer can result from very different failures. Use a trace from the actual failing task, not a new theoretical prompt that happens to work.

| Observed failure | First discriminating evidence | Smallest candidate intervention | What would not establish a fix |
|---|---|---|---|
| The worker did not receive the requested source set | Original assignment, received references, access errors | Repair the assignment or supported source route | Raising effort while the sources remain missing |
| A source was available but only a summary was inspected | Read ranges and source coverage behind the final claim | Clarify the promised coverage; test sufficient work effort | Counting tool calls or file names |
| Correct source was read but interpreted incorrectly | Exact passage, surrounding exception, resulting claim | Improve task framing or model/effort capability on that task | Adding an unrelated memory cleaner |
| A detailed report became an overconfident final summary | Compare worker artifact and coordinator synthesis | Preserve material caveats and evidence at the handoff | Asking the worker to generate an even longer report |
| A correction was lost when work resumed | Active source of the old fact, timing, store identity | Correct the relevant owner and refresh path | Deleting every memory file |
| The task stopped at an account operation | Actual rejecting layer and target state | Supported authorization or connection repair | Rephrasing approval to evade a denial |
| A duplicate effect occurred after retry | Target-side result, logical job identity, retry sequence | Reconcile outcome before retry; use supported idempotency | Marking a Markdown task “done” |

This is a diagnostic tool for recurring or consequential failures, not a required form for every message. A problem can have several causes. If changing one factor cannot be isolated because the old configuration is unusable, record that limitation and evaluate the combined candidate honestly; do not invent a causal attribution.

A source can be present, accessible, selected, understood, and reflected in the result. Those are separate transitions. The need for evidence does not imply exposing private hidden reasoning. Observable assignments, tool outcomes, artifacts, source passages, and target-system state are sufficient kinds of evidence for the proposed checks.

## 3. Effort: a practical candidate, not another control subsystem

### 3.1 What the refreshed sources establish

**DOCUMENTED PLATFORM BEHAVIOR, generic Claude Code:** the model configuration reference describes model-dependent effort, explicit overrides, per-model saved settings, and different persistence rules. Opus 5.5 has a documented Medium default; an old user-level top-level `effortLevel` is not necessarily its effective setting. `ultrathink` is not an API-effort setter. Ultracode is a separate orchestration setting, with version-sensitive behavior. [S09, sections “Adjust effort level,” “Choose an effort level,” and “Set the effort level.”]

**DOCUMENTED GUIDANCE, not a measured Apex result:** Anthropic's model/effort article explains that the setting can affect investigative and verification work, not merely the duration of private reasoning. The article was read through search-rendered text; its direct page retrieval failed. [S28]

These generic configuration facts do not establish how native Projects exposes or inherits every setting. In particular, do not paste a CLI settings recipe into the repository and claim it changed the native coordinator. Use the actual Projects controls and available runtime evidence. The owner's screenshots are historical observations, not a live account inspection in this pass.

### 3.2 Recommended starting comparison

**RECOMMENDATION — refinement of AR-015:** keep the currently selected, available model fixed for the first comparison. Capture the existing coordinator/worker settings before changing them. For this owner's substantial, multi-threaded business work, the first candidate worth testing is **High for the coordinator and Medium/model-default for ordinary workers**, with **High for a deep review or other worker task where missing an edge case is costly**, if those controls are supported in the target surface.

This is a hypothesis-led pilot configuration, not an optimal setting established by experiment. It is motivated by the coordinator's synthesis responsibility and the owner's dissatisfaction with under-investigation. The evidence does not show that Low caused the historical problems. A well-scoped simple exchange can remain simple; the goal is not to make every task expensive.

Use three comparisons only as they become informative:

1. **Coordination comparison:** keep the worker, task, sources, and instruction revision fixed; compare the recorded baseline with higher coordinator effort. Examine assignment quality, lost requirements, evidence retrieval, and final synthesis.
2. **Worker comparison:** keep the chosen coordinator and all inputs fixed; compare worker effort on a bounded, analysis-heavy task. Examine supported findings and missed exceptions rather than response length.
3. **Configuration comparison:** only after effort is understood sufficiently, compare the old and simplified backend under the same model/effort conditions. A better model plus a new backend is an end-to-end candidate, not evidence that backend simplification caused the improvement.

Do not turn these comparisons into a permanent routing engine. If one practical default works across representative tasks, use it. Exceptions should be few and understandable. The owner should not have to choose an effort setting for every prompt; an explicit high-stakes or deep-review task is a reasonable exception, not a demand for continuous manual tuning.

Maximum effort is not the default proposal. Retain it as a conditional experiment only when a harder task still fails with correct inputs and adequate tools, and its marginal benefit is worth the extra time and usage. No fixed thinking duration, mandatory agent count, or “spend the whole budget” instruction is proposed.

### 3.3 Measure the result the owner cares about

A compact evaluation record should retain the source revision, candidate settings, task, actual artifact, important errors, user intervention required, elapsed time, and available usage measures. Report these dimensions separately. Do not invent a weighted score that hides a severe error behind cheap execution.

Useful quality observations include: a material unsupported claim; a missing required source; a correction not honored; an incomplete result presented as complete; unnecessary requests for facts already available; and repeated administrative repairs by the owner. For creative work, usefulness and originality need business judgment. A machine-readable artifact can still be a poor campaign.

When variability could change the decision, repeat a small number of comparable tasks in alternate order, preserving failures. A few trials diagnose; they do not establish a reliability percentage. Neither the first successful run nor the best run from many attempts represents ordinary performance. Record unsuccessful attempts and any intervention that made success possible.

Subscription usage, cached-token totals, API billing, and elapsed work are different measurements. Use actual available measures and their units. Do not convert a cumulative token screenshot into a monetary saving claim. Optimize useful work per total operator burden, including the time spent repairing wrong or incomplete outputs.

## 4. Autonomy that continues useful work without inventing completion

### 4.1 Define the next useful outcome, not an endless mandate

AR-008 and AR-017 should make substantial assignments concrete enough to finish without excessive supervision. A useful assignment identifies the objective, source boundary, output, material dependencies, and authorized action scope. It does not need to dictate every intermediate thought.

A worker should be able to continue through reversible analysis and drafting without asking permission at every step. It should stop or narrow the claim when it lacks a required source, encounters an unresolved material contradiction, reaches an authorization boundary, or cannot produce the promised artifact. “Blocked” should name the blocked dependency and preserve work already done. It should not be a vague refusal or a claim of completion.

A resumed task should use the latest authorized scope and current authoritative facts. A long-running instruction should not continue an obsolete request after the owner changes direction. Before another externally visible effect, reconcile what has already happened. These are design requirements, not verified native cancellation guarantees.

### 4.2 Distinguish native product mechanisms

**DOCUMENTED PLATFORM BEHAVIOR, CLI:** `/goal` is a session-scoped prompt-based Stop-hook wrapper. Its evaluator judges surfaced conversation evidence without independently using tools; it does not change action permissions. [S31] **UNKNOWN:** this does not establish the semantics of the native Projects Goal field. A matching label is not a shared contract.

**DOCUMENTED PLATFORM BEHAVIOR, dynamic workflows:** the current workflow documentation describes another subagent orchestration mechanism. It includes unsuccessful subagent outcomes and version/availability constraints. [S32] This is neither proof that the native coordinator uses it nor a requirement to enable it for Apex.

**RECOMMENDATION:** let Projects provide its supported coordination first. Treat a continuation goal, a Stop hook, an explicit workflow, and the Project coordinator as separate mechanisms until their actual interaction is known. Do not stack them to compensate for unclear completion criteria. One bounded supported mechanism that achieves the task is better than several loops each believing it owns the next turn.

A diagnostic comparison that also enables Ultracode or an additional workflow no longer changes effort alone. Record the orchestration change as a second intervention. No new workflow file, coordinator agent, or always-running continuation hook is included in this research deliverable.

### 4.3 Missing worker output must not become “no problems found”

A significant coordination failure can occur after apparently successful dispatch: one required worker never returns, returns unusable data, or reports a narrower source set than requested. Aggregating only the successful responses can silently turn partial coverage into a complete verdict.

**RECOMMENDATION — refinement of AR-008/AR-017:** for a substantial delegated task, Tim's synthesis should account for each required responsibility as completed with evidence, partial, blocked, failed, or no longer required under a revised scope. These are conceptual states, not a demanded JSON schema or an extra task database. Use the native surface if it can represent them adequately.

The result “nothing returned” is not the result “this area was checked and no defect was found.” The workflow reference supplies a concrete example of an execution surface with nullable unsuccessful results; the broader completeness requirement is this research's inference, not a diagnosis of V2. [S32]

Apply this only where missing coverage matters. Two alternative creative sketches are not the same dependency structure as a migration requiring both data validation and permission verification. The owner should receive a clear useful synthesis, not every internal status transition.

## 5. Task-specific completion and proportionate review

### 5.1 A common boundary with different evidence

Use three distinct claims where relevant: **artifact produced**, **artifact checked**, and **external effect confirmed**. They need not all occur in the same task. A research report can be complete while deployment remains untested. A campaign draft can be complete without permission to send it.

| Task class | Evidence that matters | Common misleading substitute | Appropriate additional judgment |
|---|---|---|---|
| Detailed system or SEO review | Agreed coverage, exact sources, supported findings, remaining uncertainty | Long answer, file count, “twelve layers checked” | Whether interactions and exceptions were actually examined |
| Email or product copy | Usable draft, correct approved facts, audience and brand fit | Merely naming a writing skill | Business quality; publication/send remains separate |
| Image or video work | The requested asset or clearly scoped production deliverable, reachable and inspected | Calling a storyboard or prompt a finished rendered video | Visual/audio usefulness and factual claims |
| Store/code change | Intended behavior observed in an appropriate environment and affected paths checked | Passing unrelated tests or a reviewer keyword | Risk-specific review and deployment authority |
| Daily operational report | Correct period, sources, data freshness, usable destination | Green routine/session status | Missing data and material anomalies |
| External account action | Concrete authorized target and authoritative outcome/readback | Local success text or a persistent “approved” note | Reconciliation if the result is ambiguous |

This table is an implementation requirement derived from the owner's goals and AR-017. It is not an Anthropic guarantee or a universal scoring formula. Existing tests and provider receipts should be reused when they prove the relevant effect; do not add a separate proof file for every row.

### 5.2 When another review is worth its cost

**DOCUMENTED ENGINEERING GUIDANCE:** Anthropic distinguishes evaluation of an interaction from evaluation of the resulting state, and discusses code, model, and human checks with different limitations. [S27] Its best-practices guidance also warns that review can generate unnecessary changes when criticism is not constrained to substantive requirements. [S18, adversarial review section]

**DOCUMENTED ENGINEERING EXPERIENCE:** Anthropic reports useful generator/evaluator separation in long-running application work, while noting that separation alone does not eliminate generous grading. The models and workload differ from Apex. This is a counterexample to “extra review is always waste,” not proof that Apex needs the same harness. [S30]

**RECOMMENDATION:** use an additional focused review for hard-to-reverse changes, broad instruction rewrites, ambiguous authority, or a recurring serious error that ordinary checks miss. Give the reviewer the changed artifact and its acceptance contract, not only the author's reassuring summary. Ask for specific contract violations and counterexamples; a stylistic preference is not a release blocker.

A second model is not automatically independent evidence. Reviewers may share the same erroneous source or assumptions. A clean review is useful but not proof of runtime behavior. When the artifact can be checked directly—an existing output, a local link, a known test, an external readback—prefer that evidence over another model's confidence.

Do not require a reviewer on every harmless draft or minor wording change. Do not permanently install a reviewer swarm because this one migration warrants careful scrutiny. The overhead should be justified by the error it catches and the decision it changes.

### 5.3 Small evaluation set, not a new testing bureaucracy

The builder should select existing tests and a few representative owner tasks that expose the failure mechanisms being changed. Suitable starting examples are an evidence-heavy review, a resumed task after a correction, and a creative deliverable. An unattended action requires its own narrowly relevant authorization/recovery check before that feature is enabled.

There is no mandatory fixed number of tests, no target number of discovered defects, and no requirement for a permanent synthetic benchmark suite. A deliberately invalid link or missed-source fixture can validate a mechanical checker, but cannot stand in for a real creative or business task. Test cases that merely repeat the new instruction wording risk rewarding compliance theater.

Keep a difficult case that the candidate has not been repeatedly tuned against when feasible. If all available cases were used while editing the instructions, label the result developmental evidence rather than independent generalization. Stop evaluation when additional testing would not change the current reversible decision; retain unresolved risk for higher-impact deployment stages.

## 6. Unattended routines, account effects, and operational stopping

### 6.1 Configuration is not inherited authorization

**DOCUMENTED PLATFORM BEHAVIOR:** routines have their own configuration and connections; their green status is not evidence of successful business completion. [S12] The required context and authorization must therefore be established for the routine actually being deployed, not inferred from a successful interactive thread.

**RECOMMENDATION:** begin a routine with a clear logical unit of work: subject/account, period or event, intended artifact/effect, necessary inputs, and outcome destination. Reuse identifiers provided by the business system where available. A session ID describes execution, not necessarily the logical job. Two sessions can otherwise perform the same job twice.

For read-only work, a partial-data report should visibly identify missing sources instead of silently outputting a normal-looking total. For drafts, locate and update or clearly distinguish the intended draft rather than create uncontrolled duplicates. For sends, publishing, spending, or destructive changes, use supported scoped authority and reconcile ambiguous outcomes before retrying.

Do not promise exactly-once behavior from prompt wording. A remote service may accept a request even when the client times out. A retry policy must distinguish a known failure from an unknown result. When the target offers no reliable query or idempotency mechanism, keeping that operation interactive is a legitimate limitation, not a reason to add an unproven general-purpose transaction engine.

### 6.2 A stop button must stop the relevant path

**DOCUMENTED PLATFORM BEHAVIOR, hosted cloud:** archiving an environment affects future sessions; running sessions can continue. The environment's network allowlist does not cover every connection route, including enabled connectors and the separate GitHub path. [S05, “Archive an environment” and “Network access.”]

**RECOMMENDATION — refinement of AR-011/AR-012/AR-016:** define operational stopping around the actual effect path. Disabling a schedule, ending active work, removing a connector or credential through its supported control, and reconciling effects already accepted by the target are different operations. Do not label an environment archive, Git revert, or network setting a universal kill switch.

The builder should document the smallest supported stop/recovery procedure for each enabled unattended high-impact workflow. It does not need a new central control plane. The important acceptance condition is that the owner can stop new effects without guessing which old worker is still active. No production stop or credential revocation was exercised by this research.

Keep that scope precise: a failure in an automated send does not imply all read-only research should be disabled. Conversely, a healthy read-only diagnostic does not authorize the send. During migration, do not leave both old and new routines targeting the same consequential action unless duplicate behavior is explicitly managed.

## 7. Reversible migration and staged release

### 7.1 Four state categories require different treatment

**DOCUMENTED PLATFORM BEHAVIOR, generic Claude Code:** checkpointing tracks particular file changes and is not a replacement for Git or an undo mechanism for every change path. [S29] **RECOMMENDATION:** never use a local checkpoint claim as evidence that external customer effects or native memory can be restored.

| State category | Candidate preservation method | Release hazard |
|---|---|---|
| Versioned repository | Pin V2 commit; construct V3 separately; compare retained assets and references | Copying old instructions accidentally, or deleting a dependency of a retained skill |
| Project/account configuration | Record or export only required non-secret settings through supported surfaces | A ZIP appears complete while its tools, permissions, or routine context differ |
| Memory/task continuity | Identify actual store; preserve supported export/snapshot and selected current context | Reintroducing stale guidance, losing corrections, or overwriting concurrent updates |
| External business effects | Read authoritative state and use operation-specific reconciliation/compensation | Assuming reverting code unsends mail, undoes spend, or reverses an accepted API call |

This table describes responsibilities, not four mandatory files. One concise migration section can record the applicable items. Protect sensitive data appropriately; do not move private memory into this public research repository.

### 7.2 Gates should block the affected feature, not all progress

**RECOMMENDATION:** use staged enablement rather than one grand “everything works” declaration.

- **Design gate:** the builder has the three actual input repositories, their revisions, and enough V2 evidence to justify consequential omissions. Missing audit inputs block a final migration decision, not the reading of this research.
- **Construction gate:** the candidate contains the intended retained assets and correct references; required configuration is understood. Mechanical checks establish integrity only.
- **Interactive-work gate:** representative analysis, drafting, and continuation work produces the promised outputs under the selected route. Failures narrow what is declared usable.
- **Unattended-effect gate:** the particular workflow's authority, destination, duplicate handling, stopping, and recovery are established. A failure blocks that workflow, not every other capability.
- **Cutover gate:** the old and new effect paths are coordinated, fallback is preserved, and the owner can identify which system is active.

The builder can use more or fewer explicit milestones if the chosen scope permits it. These gates must not become a compulsory ceremony on every task. They are a way to avoid both premature production claims and endless research paralysis.

### 7.3 Selective reconstruction is not a blank-cheque rewrite

For each meaningful V2 component, the implementation audit should identify its role, active references, observed value, and any failure mechanism. Chatt 4 then chooses keep unchanged, relocate, simplify, replace, omit with preserved history, or defer. A retained directory can be copied unchanged when no conflicting dependency is found. Content review of all business skills remains out of scope.

Large structural changes can be justified while individual edits remain purposeful. “Surgical” does not require preserving an incoherent architecture, and “V3” does not require replacing functioning behavior. A component should not be removed solely because it is old, long, custom, or unexciting. Nor should it be retained merely because a previous reviewer approved it.

After cutover, preserve only useful operational evidence. A list of every turn, repeated context inventories, and daily automatic rewrites can recreate the problem. Prefer native state and targeted checks tied to actual changes or failures. If a recurring integrity problem makes a commit-time or scheduled check worthwhile, introduce that narrow check with visible scope and false-positive cost.

## 8. How the fourth chat should reconcile the three repositories

The other repositories' URLs, commits, and completed findings were not supplied to this research stream. Their absence is explicit, not filled with invented names. The handoff tells the builder to obtain and pin them before deciding what to remove.

The builder should compare claims about the same responsibility, not count how many reviewers favor a solution. For each consequential disagreement, identify the exact claim, input revision, applicable environment, inspected evidence, and observation or assumption that separates the proposals. A static V2 code finding and a generic platform statement may both be correct while describing different execution routes.

Prefer the narrowest supported conclusion. If one report says “remove this hook” and another says “it protects account writes,” inspect whether the protection executes in the target route and whether the proposed replacement protects the same effect. If the evidence cannot resolve that, retain the safety boundary or restrict the affected feature while testing. Do not solve uncertainty by silently selecting the simpler-looking opinion.

A reconciliation entry can live in the builder's design report. It needs a decision, evidence, rejected alternative, and remaining verification—not another permanent task tracker. The [challenge report](03-challenge-and-resolution.md) provides concrete disputed propositions to test.

## 9. Final acceptance boundary for this research

This pass supplies an operating model, explicit conditional defaults, rejection reasons, release implications, a self-contained handoff, and mechanically checkable cross-references. It does not supply native runtime measurements, a completed independent panel, or the final V3 implementation.

A fresh reader should be able to identify the owner goal, scope exclusions, recommended starting candidate, all AR decisions, missing audit inputs, live unknowns, and the next build sequence. We test the document structure and reference integrity locally; whether another model follows the handoff correctly remains an unexecuted clean-reader trial, not a result claimed by the author.

The final practical direction is unchanged but more specific: **make useful work easy, keep evidence truthful, preserve the right action boundaries, and make every additional layer justify its ongoing cost.**
