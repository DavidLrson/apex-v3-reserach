# Research method, adaptations, and corrections

Edition: 2026-10-15. Applies to passes 1 and 2. This is a record of the research method, not an additional runtime policy for Apex V3.

## 1. What was actually done

The supplied review archive contains 30 `SKILL.md` files. The relevant methods were read and applied selectively. No claim is made that all 30 were executed as complete workflows. No external reviewer agent, fresh-context council, or live Claude Projects test was run in this research stream.

Pass 1 mapped product and configuration boundaries. Pass 2 examines information ownership, memory alternatives, activation, controls, and implementation consequences. Official documentation was checked at the relevant sections, and the two named external candidates were inspected at fixed Git revisions. Their entrypoint hook manifests were read; their complete implementations were not audited or installed.

The research repository was read before changing it. The original pass-1 edition remains available in Git history. Publication uses Git objects and a guarded branch update, followed by readback. Publication evidence is distinct from evidence of a working Apex runtime.

## 2. Applied skills and concrete effects

| Skill | Contribution to the deliverable | Boundary or adaptation |
|---|---|---|
| `writing-for-agents` | Reader orientation, explicit evidence types, condition-linked decisions, source pointers, and actionable handoffs | Research prose is written for a new builder without chat history. No final operational CLAUDE.md was produced. Linked material absent from the supplied package is not claimed as read. |
| `spec-driven-development` | Stable recommendation IDs, requirements, candidate interfaces, falsification conditions, and tests tied to decisions | The owner already authorized research; repeated approval gates and a code implementation phase were not imposed. Proposed contracts are not falsely labeled platform APIs. |
| `context-engineering` | Separation of durable policy, relevant sources, transient task state, recovery, and untrusted external content | Its ordering and percentage heuristics are design suggestions, not evidence of the provider's hidden prompt order or hard capacity limits. |
| `idea-refine` | Deliberate comparison of native, repository-centric, checkpoint, external-memory, and output-processing options before clustering them into three architecture families | No further interview was needed. Native-first is a testable baseline rather than an assumed winner. |
| `karpathy-guidelines` | Explicit assumptions, limited scope, reversible proposals, and a burden of justification for every added mechanism | A justified redesign can be large. Minimality means avoiding unjustified responsibilities, not retaining a broken foundation because edits should be small. |
| `claude-md` | A focused instruction-writing checklist and separation of general guidance from task-specific reference material | Outdated or unsupported assertions in this skill were rejected where current official documentation disagrees. See section 3. |
| `context-budget` | Questions about loading, repetition, tool output, and measured context rather than file counts | Fixed per-tool token estimates were not presented as measurements, especially given current MCP deferred loading. |
| `workspace-surface-audit` | Separation of configured, available, authenticated, and behaviorally verified capabilities | There is no live inspection of the user's Projects account here, and no automatic preference for the skill author's ecosystem. |
| `automation-audit-ops` | Trigger/handler/dependency/effect analysis and avoidance of changes before evidence | Specific V2 hook defects belong to the separate audit. This report evaluates control designs and their compatibility gates. |
| `agent-architecture-audit` | Differentiating context failure, memory contamination, tool failure, and false verification | Not a full twelve-layer runtime audit. Anthropic's hidden implementation is not claimed to have been inspected. |
| `doubt-driven-development` | Strongest counterarguments and disconfirming evidence for important recommendations | This is same-context self-critique, not an independent fresh-context or cross-model panel. The separate Red Team stream can challenge it later. |
| `verification-before-completion` | Requiring source boundaries, accurate NOT RUN labels, and GitHub readback before declaring delivery | A successful commit proves publication, not that the suggested architecture works. |

`santa-method` is not simulated here. The independent Red Team stream has a different remit. The quality of the user's installed e-commerce skills remains outside this stream's scope.

## 3. Skill statements that must not become platform facts

**Correction M-01 — automatic context is not exclusively CLAUDE.md.** The uploaded `claude-md` skill presents an overly exclusive account of automatic loading. The current memory, extension, and cloud documentation identifies other context sources. Use S07/S19 and runtime observations, not the exclusivity claim.

**Correction M-02 — no universal instruction quota.** Numbers such as 150–200 reliable instructions, a fixed system-prompt allowance, or a fixed percentage at which quality collapses were not substantiated for the target model and Projects environment. They must not become deletion rules or acceptance thresholds. The official guidance about concise instructions is advice, not a proven universal capacity law. [S07]

**Correction M-03 — automatic drafting is not categorically forbidden.** The uploaded skill's rejection of generated instruction files is too broad. Official documentation describes `/init` as a starting-point workflow. A generated draft still needs source checking and relevance review; neither generated nor handwritten text is trustworthy merely because of its origin. [S07]

**Correction M-04 — no universal token charge per installed tool.** The context-budget method is useful for measurement questions, but current deferred MCP loading changes the cost model. Do not multiply an assumed schema size by every tool and call the result observed startup context. [S20]

**Correction M-05 — positive phrasing is a writing technique, not a safety proof.** Prefer concrete desired behavior where it helps. Keep necessary boundaries explicit. Replacing every prohibition with positive language does not establish correct authorization, and adding a hook for every missed instruction is not justified.

**Correction M-06 — the writing skills are not the target platform.** A skill may recommend JSON envelopes, permanent ledgers, multiple reviewers, or repeated confirmation. Each has to earn its place in this use case. We adopt the analytical purpose where useful, not every implementation prescription.

**Correction M-07 — source-listing and full reading are different.** A linked page that cannot be fetched remains unread. A directory listing establishes available names, not the contents or quality of every file. Source registry entries explicitly record those boundaries.

## 4. Decision construction

The pass-2 decision format is: problem; documented or inspected mechanism; unknowns; realistic options; trade-offs; recommendation; components needed; components avoided; disconfirming condition; verification. Stable `AR-###` IDs identify recommendations, not approvals. `T##` identifies proposed tests and `Q##` identifies open contracts. Source IDs are global across the two passes.

Keep assertions proportional to evidence. A static hook manifest can establish that a handler is declared but not that it starts, captures all events, or improves results. A documentation statement can establish the intended contract, but a beta defect can still violate it. A successful demonstration can establish that one case worked, not broad reliability.

Recommendations primarily consist of original design analysis and proposed tests, not copied source text. Native-first, minimal hybrid, and external tooling are compared against the same business requirements. No recommendation depends on a popularity threshold.

## 5. Independence and publication boundaries

This stream does not read the other chats' unfinished conclusions as authority. Shared problem statements can still anchor all three streams, so three agreeing reports are not three independent experiments. The fourth chat must reconcile evidence and counterexamples rather than count votes.

Only the research repository is modified. No production settings, customer systems, or V2 files are changed. No raw private source materials are uploaded. Documentation filenames and recommendation IDs are research navigation aids; they are not a proposed set of permanent V3 memory or governance files.

The final Architecture Research Handoff is reserved for pass 3. Until then, the README provides the standalone reading order and the pass-2 records provide candidate decisions with explicit gates.
