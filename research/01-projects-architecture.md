# Pass 1 — Claude Projects platform boundaries

Research edition: 2026-10-15. Replaces the Swedish edition delivered on 2026-10-14; the original remains in Git history at `ac598758dfba6eedc1be1d4ce9f02999fa376a9c`.

**Status: completed documentary platform study, supplemented during pass 2. Not a certification of any live Apex installation.**

## 1. Read this without the original conversation

Apex is an e-commerce operator's working environment, not a product for selling an agent framework. Its intended work includes store development, search optimization, advertising, email, customer operations, organic content, images, video, research, and recurring business tasks. The owner wants to concentrate on the business rather than maintain an AI backend.

Apex V2 runs in the Claude Code Projects experience with a native project coordinator, called Tim by the owner, and multiple work threads. The owner reports shallow reviews, unsupported completion claims, confusing restrictions, stale information, and growing administrative files. These are requirements and incident reports, not findings that this research has independently reproduced. Problems reportedly existed before usage became scarce. A low remaining quota must not be adopted as the default root cause.

This repository is the independent research stream. A second stream audits V2 files and a third challenges the system through Red Team analysis. A future fourth chat will compare all three repositories and decide what to build. This stream has not audited the V2 implementation, approved its recent merges, or inspected every installed business skill. Existing useful skills and reference repositories are migration assets, not presumed defects.

The decision is not simply whether to shorten `CLAUDE.md`. It is which responsibilities belong to the platform, which need configuration, and which justify additional software. A smaller system that repeatedly loses important work would not satisfy the goal. Neither would a larger system that mostly maintains itself.

## 2. Evidence vocabulary and reading contract

Use these labels literally when comparing this report with the other streams:

- **DOCUMENTED PLATFORM BEHAVIOR:** a statement supported by the inspected official source for its stated product and environment. Documentation is not proof that every beta execution behaves that way.
- **VERIFIED TECHNICAL EVIDENCE:** something directly inspected, such as a particular configuration artifact, source file, screenshot field, or publication commit. The verification scope must be named. Static inspection is not execution.
- **THIRD-PARTY EXPERIENCE:** a reporter's experience or a maintainer's untested product claim. An issue hosted in Anthropic's repository is not automatically an Anthropic-confirmed defect.
- **INFERENCE / HYPOTHESIS:** a proposed explanation or conclusion from the evidence, not an observed runtime fact.
- **RECOMMENDATION:** a design choice proposed for evaluation, not a requirement already implemented.
- **UNKNOWN / REQUIRES LIVE TEST:** a material fact unavailable from the inspected sources or requiring execution in the user's environment.

Source identifiers resolve in [the shared source register](01-sources.md). Tests resolve in [the validation register](01-validation-and-handoff.md). Pass 2 supplies the implementation decision records; this document defines their platform boundaries.

### Critical retrieval limitation

The official documentation index lists a dedicated Projects page, but direct retrieval of that page and its Markdown variant failed again in this research session. The failure is an access limitation, not evidence that the feature does not exist. The earlier official launch article was available through search-rendered text in pass 1, not as a fully fetched current specification. That historical evidence is retained with its limitation, not silently upgraded. [S01–S03]

Consequently, exact native Project memory synchronization, coordinator tool visibility, thread inheritance, and restart semantics remain conditional. Generic CLI auto-memory documentation cannot fill those gaps. Ordinary Claude chat Projects help pages are also not substitutes for Claude Code Projects documentation.

## 3. Product and responsibility boundaries

| Surface | What this study can establish | What must not be inferred |
|---|---|---|
| Claude Code Projects | A separately documented project experience; native coordination and shared context are described by its index/launch material and visible in the supplied UI. [S01, S02, O01–O03] | Exact hidden prompt order, complete coordinator access, or guaranteed successful coordination. |
| A Projects work thread | The UI presents threads and separate defaults; cloud documentation constrains the hosted session environment. [O02, S05] | Every thread is equivalent to a CLI subagent or shares all state with every other thread. |
| Claude Code subagents and Agent Teams | Distinct extension/execution mechanisms described in their own documentation. [S10, S19, S21] | Their memory and tool-inheritance rules automatically govern native Projects threads. |
| Local or Remote Control execution | Execution can depend on the user's machine and its local configuration. [S11] | A cloud thread inherits the laptop's entire installed environment. |
| Routines | Separately configured automated runs with their own execution context. [S12] | A routine automatically receives this Project's latest memory or approval. |
| This research chat's GitHub connector | It can publish research commits when the write succeeds and is read back. | That Claude Projects has equivalent authentication, scopes, or permission behavior. |

**RECOMMENDATION:** treat a V3 release as repository content plus the minimum necessary runtime configuration and connection information. Do not create a parallel platform administration system merely to describe those boundaries. This recommendation is developed as AR-001 in pass 2.

## 4. Platform fact cards

These cards centralize facts so later design records can discuss implications without repeatedly reproducing documentation.

### PB-01 — Coordination is not omniscience

**DOCUMENTED PLATFORM BEHAVIOR, limited/historical:** the official Projects index and launch description identify native coordination and parallel work. **VERIFIED TECHNICAL EVIDENCE, UI only:** the supplied settings distinguish coordinator and thread model/effort. [S01, S02, O02]

**UNKNOWN / REQUIRES LIVE TEST:** which thread events reach Tim automatically, which he can retrieve, what he actually retrieves, and which results he verifies. These are four different questions. An earlier statement that Tim can only see summaries was too categorical and is withdrawn.

**INFERENCE / HYPOTHESIS:** an inadequate handoff can occur even when full source access exists. Conversely, a perfect instruction cannot grant an unavailable tool. Test T04 before choosing a new coordination layer.

### PB-02 — Native Project memory and local auto-memory are not interchangeable

**VERIFIED TECHNICAL EVIDENCE, UI only:** the user's `MEMORY.md`, titled as team memory, appears under native Projects Auto memory with topic files. That establishes its presentation, not its storage path, correctness, or writer behavior. [O01]

**DOCUMENTED PLATFORM BEHAVIOR, generic Claude Code:** local auto-memory is repository-scoped and machine-local; its index has a documented bounded startup load. Those storage and loading details are not a verified contract for native Projects memory. [S07]

**UNKNOWN / REQUIRES LIVE TEST:** whether V2 merely adds policies to native memory or also maintains a separate store; how updates reach already-running threads; conflict handling and export/restore behavior. T03 and the V2 audit must resolve these questions. Deleting a file because it is called a memory index is not justified.

### PB-03 — Instruction prose and technical settings have different semantics

**DOCUMENTED PLATFORM BEHAVIOR:** discovered `CLAUDE.md` content is combined as guidance, not merged as deterministic settings overrides. Imports expand into context; splitting text into imported files alone does not reduce loading. Unscoped rules load broadly, while path-scoped rules depend on matching file activity. Technical settings have separate precedence and enforcement rules. [S07, S04]

**INFERENCE / HYPOTHESIS:** conflicting prose should be reconciled at its source, not left in multiple files with an invented promise that the preferred file always wins. A procedural guide for campaign writing is not necessarily a path-specific rule merely because it lives in a campaign folder. Pass 2 separates instruction ownership from activation.

### PB-04 — Attached repository topology changes configuration loading

**DOCUMENTED PLATFORM BEHAVIOR, Anthropic-hosted cloud:** single-repository sessions can load project settings. With multiple attached repositories, only specified plugin-related settings are read from the repositories; repo hooks, permissions, and environment entries are not applied the same way. Plugin declarations do not themselves install the plugins in the cloud. Personal/local settings do not automatically transfer. [S04, S05]

**VERIFIED TECHNICAL EVIDENCE, UI only:** one standard project repository was shown. A reference repository merely cloned into a directory is not thereby a second attached session repository. [O03]

**RECOMMENDATION:** record actual session topology before relying on a hook. T01/T02 check loading and behavior; they do not assume that a missing hook in a documented multi-repo case is a product defect.

### PB-05 — Provisioning, stored files, and running services are different

**DOCUMENTED PLATFORM BEHAVIOR:** hosted environment setup and session-start hooks are different lifecycle mechanisms. Environment caching preserves a filesystem snapshot, not every process that setup started. A resumed or recreated session is not equivalent to a new installation. [S05]

**INFERENCE / HYPOTHESIS:** an external memory worker could be installed on disk yet unavailable when a new session needs it. Conversely, reinstalling every dependency at every turn can create unnecessary work. Select initialization behavior only after the actual deployment mode is known. T07 distinguishes installation, process readiness, durable state, and resume behavior.

### PB-06 — Skill availability is not skill application

**DOCUMENTED PLATFORM BEHAVIOR:** cloud sessions can use repository and account-available skills, but they do not simply read the user's laptop skill folder. Skill listing, invocation, and body loading are separate mechanisms. Subagent preloading is a separate case. [S08, S19, S21]

**RECOMMENDATION:** preserve working skills and their supporting files. Verify the route from availability to relevant application rather than make every business task print a ritual receipt. The V2 audit owns specific broken paths; this stream defines a small set of representative loading checks.

### PB-07 — Connectivity, authorization, and successful execution are separate

**DOCUMENTED PLATFORM BEHAVIOR:** environment networking, external authentication, client permission rules, and hosted approval behavior form distinct controls. A permissive network setting is not an authorization to send a campaign or alter an account. The cloud documentation also states a Projects-specific GitHub App requirement for repository access. [S05, S06, S14, S22]

**RECOMMENDATION:** classify a blocked operation at the layer that rejected it. Do not weaken unrelated protections to make a diagnostic turn green. Preserve actionable error information so Tim can explain the actual boundary. T06 uses a harmless test resource, not real customer actions.

### PB-08 — A run finishing is not proof of business completion

**DOCUMENTED PLATFORM BEHAVIOR:** a routine's green status reports infrastructure success, not that its task succeeded. A Stop event means an assistant response ended, not that a whole business objective was accomplished. [S12, S16]

**INFERENCE / HYPOTHESIS:** checking for a particular completion word can enforce presentation without checking the deliverable. That is a hypothesis to test against V2, not a finding about an unread guard script. A usable receipt should point to an actual result and name incomplete work when relevant.

### PB-09 — Effort is a variable, not a diagnosis

**VERIFIED TECHNICAL EVIDENCE, UI only:** the supplied snapshot showed coordinator effort Low and thread default Medium. It does not establish the effective value in past sessions. [O02]

**DOCUMENTED PLATFORM BEHAVIOR:** effort has configuration sources and model-specific calibration. Explicit settings and overrides matter. [S09, S21]

**RECOMMENDATION:** vary coordinator and worker effort separately on unchanged inputs. Do not change model, instructions, memory, and effort together and attribute an improvement to one of them. T05 records quality as well as usage and latency. Full operational calibration remains part of pass 3.

### PB-10 — Context, cached computation, and stored memory are different resources

**DOCUMENTED PLATFORM BEHAVIOR:** prompt caching reuses eligible processing; it is not a persistent factual knowledge store. [S13]

**INFERENCE / HYPOTHESIS:** aggregate cached-token volume cannot be read as the size of one active context window or as a direct measure of wasted business work. The useful question is whether avoidable retrieval, repetition, or orchestration reduced the quality delivered per task. Current MCP deferred loading also invalidates simplistic fixed-token-per-tool estimates. [S20]

### PB-11 — First-person incidents are test leads, not general diagnoses

**THIRD-PARTY EXPERIENCE:** three pass-1 GitHub reports describe approval propagation problems, device-linked network/OAuth restrictions, and unclear Debug access behavior. They were read with their available comments in pass 1; they have not been reproduced here or freshly checked for resolution in this supplement. [G01–G03]

The comment on the device issue supports a narrower trusted-device/Remote Control problem, not every causal claim in the original report. The Debug access report concerns projects within one account, not demonstrated cross-account access. Keep these limits when constructing tests or discussing security.

## 5. A conceptual task path, not an invented internal prompt stack

Use the following as an investigation model:

`business request -> coordinator interpretation -> scoped work assignment -> thread environment and relevant context -> tool work -> result artifact and residual uncertainty -> coordinator synthesis`

For each transition, ask whether the required information existed, was accessible, was selected, was interpreted correctly, and was reflected in the result. This is an analytical model proposed by this research, not a reconstruction of Anthropic's hidden execution order.

For example, a source-backed SEO investigation might fail because the thread never received the site boundary, because pages were inaccessible, because it inspected only a navigation summary, or because the coordinator later omitted the material limitations. These failures require different changes. More global rules are not the default repair for all of them.

The migration review should distinguish:

| Failure hypothesis | Evidence that would support it | Evidence that would weaken it |
|---|---|---|
| Required context was absent | Missing attachment, unresolved reference, or unloaded instruction in the failing session | Complete source was accessible and demonstrably read before the relevant decision |
| Context was stale | Old fact or superseded decision appears in the result with a traceable source | The correct current fact was used but reasoning still failed |
| Tool execution failed | Actual denied request, unavailable tool, missing process, or API error | Successful authoritative readback of the intended effect |
| Delegation lost the requirement | Parent request differs materially from assignment or returned scope | Thread had and followed the requirement but synthesis lost it |
| Reasoning was inadequate | Correct inputs and successful tools but unsupported interpretation | An upstream access or specification failure explains the result |
| Presentation created false certainty | Detailed work contains caveats absent from the final conclusion | The underlying investigation itself lacks coverage |

This matrix is not a complete causal model and should not become a new mandatory per-message checklist in V3. Use it for recurring failures whose diagnosis changes an architectural decision.

## 6. The baseline comparison that pass 2 must make

Three candidate architectures remain viable:

1. **Native-first:** use native coordination and available native memory with a compact business and repository brief. This is the cheapest baseline to test, not the presumed winner.
2. **Minimal hybrid:** retain that baseline and add only an explicit artifact, workflow, or bounded control that closes a demonstrated gap.
3. **External memory/context tooling:** add a separately operated component where its actual retrieval, persistence, or processing benefit outweighs deployment, privacy, and maintenance costs.

Judge them by useful completion, correction persistence, source coverage, clarity of handoffs, recovery, operator effort, and controlled external effects. File count is a secondary diagnostic, not the objective function. A duplicate derived view can be legitimate when it has an explicit source and refresh policy; multiple competing authorities are a different problem.

Do not treat a previous V2 merge or passing unit suite as evidence that it improved business outcomes. Do not treat failure to prove that improvement as proof that every changed component is harmful. The file audit and representative task evidence must settle those claims.

## 7. Corrections and scope changes made explicit

| Earlier formulation or risk | Corrected position |
|---|---|
| Team memory implies a custom memory engine | Its native UI location is known; storage identity and added mechanisms are not. |
| Tim sees only summaries | Exact automatic and retrievable access remains unknown. |
| One later instruction file overrides another | Instruction text is combined; deterministic settings precedence is a separate topic. |
| Splitting/importing a large CLAUDE.md reduces startup context | Imports can preserve the same loaded text; activation must change to save context. |
| A fixed estimate per MCP tool measures startup cost | Deferred loading changes what enters context; inspect the actual session. |
| Low effort explains the longstanding quality problem | It is one controlled experimental factor among several. |
| A screenshot of an empty Goal means no project instructions | Goal and Project instructions are distinct UI fields. |
| Full networking means external writes are authorized | Network reachability, identity, tool policy, and user approval are different. |
| Example setup text proves a saved script ran | The screenshot alone cannot establish that. |
| A short summary means the underlying work was shallow | Examine source coverage and artifacts before diagnosing depth. |
| A long or detailed response proves deep work | Length is not evidence either. |
| Native-first requires deleting all custom state | It is a baseline and can lose to a justified minimal hybrid. |

These corrections supersede less precise wording in earlier chat messages. They do not assert new V2 defects.

## 8. What the fourth chat can decide from this study

The fourth chat can use these boundaries to reject proposals that depend on impossible configuration transfer, invent instruction precedence, confuse memory identity, or certify outcomes from superficial completion signals. It can also identify exactly which uncertainties require a small live probe instead of a larger redesign.

It cannot use this study alone to authorize deleting specific V2 files, select all production permission rules, claim that native memory synchronizes correctly, or certify a memory plugin in Projects. Those decisions require the other audit streams and the indicated live observations.

Read pass 2 next for stable recommendation IDs, alternative designs, and implementation consequences. All tests in the validation register remain **NOT RUN** until a separate execution record supplies evidence. The final cross-report Architecture Research Handoff is reserved for pass 3; this platform report is not that final handoff.
