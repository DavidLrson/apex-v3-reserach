# Pass 2 — External memory and context tools: technical evidence

Research edition: 2026-10-15. **Static, version-pinned inspection only. Neither package was installed, executed, benchmarked, or certified in native Claude Projects.**

Read this dossier when evaluating [AR-013 or AR-014](02-information-architecture.md#ar-013). Those records own the recommendations. This file owns the deeper external evidence and compatibility questions; it is not a competing set of architecture decisions.

## 1. Scope and source identity

| Candidate | Inspected revision | Question being evaluated |
|---|---|---|
| `thedotmack/claude-mem` | `fef3402e674bebbf72a23aeb735e91c92cd34afd` | Can an external history-memory service solve a demonstrated cross-session retrieval problem? |
| `mksglu/context-mode` | `655c67f9e1bb2d1c2a6db850447f1cfdcbbb1220` | Can off-context processing improve large-output work without losing evidence or adding unacceptable operational cost? |

Pinned files P01–P05 are registered in [the pass-1 source register](01-sources.md). P06–P09 and the exact additional read ranges are registered in [pass-2 evidence and validation](02-evidence-and-validation.md). The revisions are research snapshots, not recommended versions to deploy blindly. Their current security status, release suitability, and compatibility would need checking at installation time.

A README describes the maintainer's intended product. A hook manifest establishes configured entry points. Reading a handler reveals a code path. None of these establishes that the path executed in Apex, that every capture was correct, or that a given provider has the expected retention/availability guarantees. The same distinction applies to tests present in a third-party repository: this research did not run them.

## 2. Different problems, overlapping integration surfaces

The two tools should not be compared as interchangeable brands of Project memory. A system can need historical recall without oversized tool output, or oversized-output handling without a new history database. It may need neither if native retrieval and simple scoped computation suffice.

The overlap is operational: both candidates can participate in session startup, tool events, and context injection. Installing both at once would therefore obscure which component changed behavior. A proposed pilot should name one failure being addressed, one selected installation route, and one bounded workload. Evaluation begins with the native/minimal baseline, not with every optimization already enabled.

The relevant alternatives are not only these two packages. A dated artifact checkpoint, a direct source lookup, or a short script that computes an aggregate may be adequate. Conversely, repeatedly reconstructing extensive historical discoveries can justify a maintained external service. Its maintenance cost must be compared with the operator work it replaces, not with an imaginary cost-free native system.

## 3. claude-mem: capture, processing, storage, and retrieval

### 3.1 What the inspected sources establish

**THIRD-PARTY EXPERIENCE / maintainer description — P01:** the README presents automatic observation capture, summaries, search/recall, and multiple provider/install choices. These are intended features, not measurements of Apex improvement.

**VERIFIED TECHNICAL EVIDENCE / static manifest — P02:** the pinned hook configuration declares setup/version checking; session-start worker startup and context loading; prompt initialization; tool-success and tool-failure capture; pre-tool file-context activity; stop summarization; and session-end activity. Several handlers are asynchronous. The manifest therefore shows more than a passive Markdown index, but does not establish which events are supported in a native Projects thread or whether asynchronous work drains before termination.

**THIRD-PARTY EXPERIENCE / version-pinned documentation — P08:** the cloud-sync document describes a local database replicated through a per-user hub, worker-driven push/pull, optional live notifications, and propagation of several content/mutation classes. It explicitly identifies observation narratives and user prompts as data uploaded to the hub when sync is enabled. A selected provider's real deletion, retention, isolation, and account behavior remain unverified.

**VERIFIED TECHNICAL EVIDENCE / selected source range — P09:** `services/sync-api/src/store.ts`, lines 1–100, declares a device-limit constant of 64 and a corresponding error identifier. This corroborates the existence of a configured limit in that source version, not a complete audit of all admission paths or the currently deployed hosted service.

### 3.2 Why a local install does not prove shared Project memory

The deployment has to explain at least four distinct boundaries: where a capture event occurs; where the worker processes it; where the durable record survives; and how another intended consumer retrieves it. A new cloud VM with its own local database may have no history from another thread. A database file in an environment snapshot may be a copied starting point, not a shared live store. A stopped worker can leave installed files without an available service. These are deployment risks inferred from the component model and S05, not failures reproduced here.

A working synchronization route could address part of this problem. However, it introduces identity, credentials, network, catch-up, and deletion behavior that must be made explicit. A provider's same-account sync is not automatically the desired boundary between separate businesses, projects, or customers. The pilot must demonstrate the intended scope without using sensitive production material.

Do not solve an uncertain identity lifecycle by assigning the same device identity to every VM, and do not create fresh identities indefinitely without understanding the provider's contract. With ephemeral workers, new identities may accumulate; with copied snapshots, identities may collide or be reused unexpectedly. Both are hypotheses requiring a supported deployment design. They do not establish an actual incident in either package or Apex.

### 3.3 A concrete documentation inconsistency

P08's push-lane discussion says each request is timeboxed at 30 seconds, while its settings table gives the content-push timeout a 90,000 ms default and describes a longer projection-related requirement. These could refer to different paths or a documentation transition, but the inspected document does not make a universal timeout unambiguous.

The report therefore does not specify "all sync requests time out after 30 seconds." A pilot must determine the effective path and setting rather than build a startup budget around that sentence. P09's source comments/constants identify a newer service implementation, while other repo material also describes an older hub. A file's presence in the same repository is not proof it is the active deployment.

This is not evidence that the product cannot work. It is a reason to pin the intended release and deployment, inspect its actual configuration, and test lifecycle assumptions rather than combine claims from different documentation generations.

### 3.4 Recovery and freshness questions that matter for Apex

A short bounded startup pull should be measured against the amount of outstanding history. Does the context supplied to the agent correspond to a completed catch-up, a useful partial view, or an error? A successful worker health response is not the same as an up-to-date local search index. A zero pending-upload count says nothing by itself about missing remote records or the correctness of retrieved facts.

Corrections also need a semantic boundary. A well-synchronized incorrect summary is still incorrect. The system should distinguish an approved preference, a historical observation, a provisional hypothesis, and a current business fact. Capturing an agent's assertion automatically must not promote it to verified truth in future sessions.

Deletion should be assessed across active retrieval paths: local rows, indexes, sync mutations, and provider storage as relevant to the selected mode. Historical transcripts and backups may have separate retention. The research has not established deletion guarantees for any hosted provider and does not imply that removing one visible note erases every copy.

### 3.5 What a justified pilot would prove

T13 should demonstrate a recurrent history question the baseline misses, successful correct retrieval in a separate intended consumer, a correction that defeats a stale version, and usable recovery after interruption. Record provider selection, data egress, storage scope, version, startup behavior, and uninstall/rollback. Include the cost of processing observations and recovering failures, not merely retrieval latency.

Adoption would be justified by meaningful task-level improvement that persists across the needed boundary with acceptable operator effort. Installation success, a memory UI, a high star count, or a single recalled note does not establish that case. The converse also matters: an external worker that removes substantial repeated work may be simpler for the owner than a custom collection of fragile notes and repair scripts.

## 4. context-mode: selective processing versus routing/capture machinery

### 4.1 What the inspected sources establish

**THIRD-PARTY EXPERIENCE / maintainer description — P03:** the README describes MCP processing/search, reduced raw-output exposure, and session-continuity capture. Its savings examples and retention narrative were not reproduced. In particular, a claim about clearing prior session data should not be treated as a full guarantee for every persistent content index or every host integration.

**VERIFIED TECHNICAL EVIDENCE / static manifest — P04:** the pinned manifest registers multiple routing/capture lifecycle hooks and named tool matchers. It is not just a tool that sits idle until a user calls it.

**VERIFIED TECHNICAL EVIDENCE / inspected handler — P06:** the Claude Code PreToolUse entry point delegates routing and formatting, includes conditional plugin-cache repair behavior, records diagnostic markers, and passes an explicit availability flag for detected subagent contexts. Some conditions can rewrite installed-plugin metadata or legacy hook paths. The source also states that an earlier destructive settings-removal block was removed; this research does not attribute that removed behavior to the current code.

**VERIFIED TECHNICAL EVIDENCE / selected router range — P07:** the inspected beginning of the common router defines a passthrough when MCP alternatives are unavailable/not ready and implements advisory throttling. Only the registered range was read; the entire router, search implementation, security model, and every adapter were not audited.

### 4.2 The full plugin and MCP-only route are different candidates

The README describes an MCP-only alternative without the automatic hook routing. Treat that as a separate pilot, not as proof it works in every cloud environment. It may provide the needed processing benefit with fewer automatic modifications. The full plugin may improve consistent selection and recovery, but also brings routing, capture, and lifecycle responsibilities.

Compare them on the actual task. For a large tabular aggregation, a sandboxed computation returning checked totals may be ideal. For a detailed instruction audit, reducing a file to keywords or counts may discard the very conflict the agent was asked to find. Token savings alone cannot choose between these outcomes.

The appropriate sequence is to show that ordinary scoped reading/computation is insufficient, confirm the target environment can expose the MCP service, test a narrower processing path, and only then evaluate whether automatic routing/capture adds net value. That is a proposed evaluation order, not an installation script.

### 4.3 Readiness fallback is useful but has a boundary

P07's availability checks are a useful design signal: an optimization should not deny the normal route while its replacement is absent. This is an advisory availability concern, not permission to bypass a safety control. A separate authorization boundary must still operate on the actual effect regardless of whether computation ran through Bash, a direct API tool, or an MCP service.

Changing the tool route may change which hook matchers, logs, and permission checks observe an operation. The pilot should therefore verify both evidence visibility and intended protection after routing. This report does not claim that context-mode bypasses a control; it identifies a compatibility question that should be answered before relying on existing controls around a different route.

Subagent handling in P06 also cannot be used as a universal native Projects rule. A package's test for subagent-related fields is its own integration choice. Native work threads and Claude Code subagents are distinct surfaces until their relevant contracts are demonstrated.

### 4.4 Self-repair is a trade-off, not automatically a defect

The inspected entry point contains code that can reconcile version directories and installation metadata under certain plugin-cache conditions. Such repair may prevent broken-path failures after upgrades. It also means a read-like user task can coincide with local integration maintenance.

The builder should know which files a selected package can modify, under what condition, whether concurrent sessions can still reference older paths, and how rollback works. It should not assume a package advertised as a context optimizer has no configuration side effects. Equally, it should not claim those side effects happened in this research or in the user's environment.

A freeze/pin strategy can make a pilot reproducible, but permanently freezing a dependency has its own maintenance/security costs. After evaluation, choose an intentional upgrade procedure with a quick compatibility check. Do not let the optimizer silently become a second installer, policy owner, and recovery authority without deciding whether those roles are acceptable.

### 4.5 Preserve source semantics

A retrieved snippet should retain an identifiable source and sufficient surrounding material for the question. A search index should not convert an old assistant summary into the only accessible representation of a source. When an exact instruction conflict matters, retrieve the actual text and its exceptions. When computation is the task, verify inputs and result invariants rather than force a model to reread every row.

T14 includes a case where a cross-file interaction or nearby caveat changes the conclusion. A lower context footprint that loses that case is not a win. A successful pilot should show at least comparable supported findings, fewer unnecessary reads, and no misleading claim that all sources were examined when only a sample was retrieved.

### 4.6 License and deployment boundary

P05 records the pinned repository's Elastic License 2.0 text. This report does not provide legal clearance for redistribution, a modified package, or a hosted offering. If the fourth chat proposes copying package code into a deliverable or exposing it as a service, it must check the applicable terms and intended use. Reusing an idea or evaluating a tool is not the same decision as redistributing its implementation.

## 5. Common compatibility gates

| Gate | Evidence required before reliance | Why a superficial check is insufficient |
|---|---|---|
| Distribution | Actual package/skill/MCP route in the selected hosted/local environment | A laptop plugin declaration does not prove a cloud install |
| Lifecycle | Fresh, cached, resumed, interrupted, and retired worker behavior | A filesystem snapshot does not preserve a running process |
| State | Correct retrieval after another intended writer updates information | Same folder names or successful local reads do not establish shared storage |
| Identity | Supported project/device/user boundaries across restarts and clones | A label may be metadata rather than an isolation boundary |
| Authorization | The intended protected effects remain governed after routing | A different tool name may change which existing checks observe the action |
| Provenance | Findings retain source identity, revision, and relevant caveats | A synchronized summary can still be wrong or stale |
| Correction/deletion | Corrected or removed content stops controlling active retrieval as intended | Deleting one visible note does not prove every representation changed |
| Operations | Clear health, dependency failure, rollback, and upgrade behavior | A doctor/health success is not a useful business result |
| Cost | End-to-end task quality and operator effort, including capture and repair | A vendor reduction percentage is not measured Apex value |

None of these gates calls for building a new service merely to test a service. Use a disposable native Project and harmless fixtures through supported interfaces. If the installation path itself is unsupported, stop at that finding rather than improvise an unsafe deployment.

## 6. Decision consequence for the fourth chat

AR-013 and AR-014 deliberately leave both tools as conditional options. The current evidence supports neither "the native system is certainly enough" nor "a popular external repo will fix it." It supports a more useful separation: diagnose whether the missing capability is durable recall, task recovery, current factual access, or oversized-output processing, then test the smallest candidate that actually addresses that boundary.

The fourth chat should not turn this dossier into another mandatory startup reading. It should use it to reject unsupported installation assumptions and to select an evaluation only when the V2 audit and Red Team evidence identify a corresponding problem. No change to live memory, account data, or production hooks has been made by this research.
