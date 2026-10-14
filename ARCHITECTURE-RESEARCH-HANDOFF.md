# Architecture Research Handoff — Apex V3

Edition: 2026-10-15. **Final research handoff for a fresh fourth chat. No original conversation is required.**

Repository: `DavidLrson/apex-v3-reserach`. Pin the commit containing this handoff before using it as an implementation input. The final pass builds on research commit `141002f54e2de684b237ca0ce8a2edcd248708ff`; earlier files remain historical evidence. This document and the final-pass reports supersede their statements that pass 3 is pending. They do not convert earlier proposals or unexecuted tests into completed work.

## 1. Mission and owner requirements

Apex is an ecommerce operator's working environment in the **new Claude Code Projects experience**, not a framework being built for resale. Its intended scope includes store work, SEO, advertising, email, customer operations, organic social content, image/video production, research, and daily routines. The native coordinator is called **Tim** by the owner.

The owner's phrases “allt för min ehandel” and “inte restriktivt” mean broad business usefulness and enabling collaboration rather than unnecessary restrictions. The owner wants to work on the business, not maintain an AI backend, clean memory files, route every thread, or repeatedly discover that “done” was unsupported.

Reported problems include shallow reviews, premature implementation, stale information, confusing guards, duplicated instructions, and excess process. These are the owner's requirements and reports, not proof of a particular V2 defect. They reportedly predate low remaining usage. Recent V2 merges are not presumed improvements.

The target is **reliable useful work with low manual maintenance**, not the shortest possible CLAUDE.md, the fewest files, the most agents, or the longest report. Preserve useful existing skills, their supporting assets, and reference repositories. Unfinished custom business skills do not need a full quality audit before the foundation can improve.

## 2. Your remit and required inputs

You are the fourth design/build chat. Compare the three evidence streams before choosing the V3 architecture. This research is independent of the implementation audit and Red Team analysis; it has not read their completed conclusions or approved their proposed removals.

| Input | Known state in this handoff | Required action before relying on it |
|---|---|---|
| Architecture research | This repository; final handoff plus linked reports | Pin this delivery's commit and read by the routing below |
| V2 implementation audit repository | URL, commit, and final findings were not supplied to this stream | Obtain the actual repository and audited source revision; do not invent them |
| Red Team repository | URL, commit, and final findings were not supplied to this stream | Obtain its actual artifact and examined revision |
| V2 implementation and retained assets | Not audited or bundled by this research | Use the authorized source snapshot from the audit or obtain the matching repo/ZIP before copying assets |
| Actual Projects configuration | Only earlier owner screenshots informed this research | Confirm the required current non-secret settings, memory identity, execution route, and connectors before cutover |

Missing implementation inputs block a final migration decision, not reading this dossier or preparing a conditional design. Resolve available inputs through the connected tools first; ask the owner only for genuinely missing material. Never reconstruct an unprovided business skill or permission policy from a report summary.

Do not treat this public research repository as the new main backend. Do not load the whole dossier into every production thread. It is design evidence for you, not permanent runtime context for Tim.

## 3. Recommended architecture in one statement

**RECOMMENDATION:** begin with native Projects coordination and its actual native memory surface, then add a small, explicit information/action contract and only the controls or recovery mechanisms justified by demonstrated requirements. Compare this minimal-hybrid candidate with the existing baseline before broad cutover.

The native foundation can lose the comparison if it fails an important correction, continuation, or retrieval case. An external memory service can earn adoption, but not through popularity or a successful installer. A specific safety control can remain necessary even when it has never recorded an incident.

The evidence and alternatives behind this position are in [pass 2](research/02-information-architecture.md). The [final operating model](research/03-operating-model-and-release.md) adds role-separated effort evaluation, missing-worker accounting, meaningful completion, and staged release. The [challenge record](research/03-challenge-and-resolution.md) contains the strongest counterarguments and reversal conditions.

## 4. Five responsibility buckets

### What Claude Projects already handles at a documented high level

The specifically applicable beta Help Center section describes a project conversation, parallel cloud threads, project context available at thread start, and a Library for supplied/generated artifacts. [S25] This is sufficient to avoid assuming a coordinator must be invented. It does not prove detailed memory locking, exact tool visibility, complete file injection, or reliable behavior in every beta run.

Keep native Projects distinct from older chat Projects, CLI subagents, Agent Teams, CLI `/goal`, and dynamic workflows. Their contracts cannot be transferred merely because the words sound similar. [Platform boundaries](research/01-projects-architecture.md)

### What Apex needs to configure

Choose the actual execution route and required repositories, account capabilities, model/effort settings, relevant business context, and supported permission/routine configuration. Decide the owner and activation route of each retained instruction or fact. Verify that required skills and dependencies reach their real consumer.

Treat these as a small reproducible configuration handoff. Do not mirror every account setting or tool inventory into permanent Markdown. Secret values and private customer data belong outside the public research corpus. AR-001, AR-003, AR-006, AR-009, AR-011, AR-012, and AR-015 apply.

### What Apex may need to build or retain

Possible justified additions are a concise business reference where no existing source owns stable knowledge; an evidence-preserving assignment/return convention; a bounded task checkpoint for a demonstrated recovery gap; a narrow mechanical or authorization control; or a small adapter for a required unsupported workflow.

These are conditional responsibilities, not a prescribed file tree. Native facilities or existing working code may already provide them. Decide from exact V2 evidence and targeted probes. AR-004, AR-005, AR-008, AR-010, and AR-017 apply.

### What should not be built by default

Reject a second coordinator, parallel task/status registries for every thread, compulsory multi-agent review for trivial work, every-startup repair loops, arbitrary memory truncation, automatic promotion of agent assertions to facts, or keyword-based “truth” gates. Also reject a universal Max-effort policy and blind copying of all old memory and rules.

Do not install `claude-mem` and `context-mode` together as a speculative fix. They address different needs and can add overlapping integration behavior. Their [version-pinned dossier](research/02-external-tools.md) supports conditional evaluation, not production certification. AR-007, AR-013, AR-014, and AR-018 apply.

### What must be settled after comparing the other audits

Which V2 files or hooks actually execute; which prevent meaningful failures; whether “team memory” is native storage with custom policies or a parallel store; which instruction conflicts are real; which retained skills depend on changed paths; and which recent changes helped or hurt actual work.

Do not decide these questions from this research alone. Native-first is not permission to delete specific unread V2 files. The implementation and Red Team evidence should identify their exact source references and failure mechanisms. AR-002, AR-010, and AR-016 are particularly important.

## 5. Decision and evidence navigation

All eighteen recommendations retain stable **AR-001–AR-018** IDs. Their full options, trade-offs, required/avoided components, and disconfirming conditions remain in the [pass-2 decision register](research/02-information-architecture.md). The compact [final decision index](research/03-decision-index.json) provides final dispositions, dependencies, and test links; it is navigation metadata, not a competing rationale or production configuration.

Read selectively by decision, without losing the acceptance boundary:

| Decision area | Read next |
|---|---|
| Native versus custom memory, corrections, current facts | AR-002–AR-005; shared T03/T10; external dossier only if the missing capability warrants it |
| Project instructions, CLAUDE.md, skills, context | AR-006–AR-009 and the pass-2 writing specification |
| Hooks, permissions, routines | AR-010–AR-012; final operating report sections 4–7 |
| External memory or processing | AR-013/AR-014 and the pinned external-tool dossier |
| Effort and honest completion | AR-015/AR-017; final operating report sections 2–5 |
| Migration and documentation | AR-016/AR-018; final operating report sections 7–8 |

Sources are owned by [register 1](research/01-sources.md), [register 2](research/02-evidence-and-validation.md), and [register 3](research/03-sources-and-quality.md). Live tests and unknowns are owned by the [shared validation register](research/01-validation-and-handoff.md). Do not duplicate these registries inside the runtime backend.

Evidence labels distinguish DOCUMENTED PLATFORM BEHAVIOR, VERIFIED TECHNICAL EVIDENCE, THIRD-PARTY EXPERIENCE, INFERENCE / HYPOTHESIS, RECOMMENDATION, and UNKNOWN / REQUIRES LIVE TEST. A static source inspection, local test, published commit, and live business result are different verification scopes.

## 6. Concrete next sequence for the builder

### A. Establish the input boundary

Pin the three report repositories and the V2 source revision. Identify differing audit revisions before reconciling conclusions. Record missing inputs and the current target execution route. Do not assume this chat's GitHub write access proves that Tim has equivalent authority.

**Complete when:** the source of each consequential design claim is traceable, or explicitly unresolved.

### B. Reconcile the consequential disagreements

Group findings by responsibility rather than filename. For each major disagreement, compare claim, revision, environment, evidence type, and the observation that would distinguish the alternatives. Read underlying source where needed. More reviewers agreeing is not more independent evidence when they share the same premise.

**Complete when:** each important omission or replacement has an evidence-based disposition, not an inherited vote. Unresolved disputes have a bounded impact and a proposed discriminating check.

### C. Write the selected V3 specification

Choose information owners, consumers, activation paths, native configuration, retained assets, necessary controls, and completion/recovery expectations. State what is not being built. Use the pass-2 writing specification and appropriate writing skills to write clear backend instructions only after this selection. Do not blindly transplant the research prose.

**Complete when:** the proposed structure explains how ordinary business work happens and how consequential errors are detected or contained, without requiring a parallel administration platform.

### D. Construct a separate candidate

Preserve the V2 fallback and copy justified unchanged assets with their dependencies. Make meaningful changes traceable to a finding or chosen responsibility. Validate references, configuration syntax, and affected behavior using existing checks where appropriate. Keep private data and licenses handled deliberately.

**Complete when:** the candidate is internally coherent and its required non-repository configuration is documented. This is not yet proof it works inside Projects.

### E. Enable only the capabilities whose evidence is adequate

Begin with representative interactive work and continuation. Test high-impact unattended effects separately, including authorization, stopping, ambiguous-result recovery, and duplicate prevention where relevant. Keep old and new effect paths from unintentionally acting on the same logical job. Preserve a supported rollback plan for each state category.

**Complete when:** the owner receives the promised usable capability with known limitations, and can tell which system is active. A blocked optional service does not prevent shipping an otherwise useful bounded candidate.

## 7. Unresolved facts and how they affect progress

The detailed official Projects page, S03, remained inaccessible to the research tools. The applicable beta Help Center section is readable but does not establish all internals. Q01–Q09 and T01–T15 retain the exact open contracts. No live Projects test has been run in this stream.

Important unresolved facts include coordinator visibility, native memory identity/synchronization, current connector authority, routine context and recovery, existing-versus-new thread updates, external provider deletion/retention, and which V2 mechanisms genuinely protect the workflow. The other audit repositories may resolve some of these; use their evidence rather than repeat unnecessary research.

Treat unknowns proportionately. Unverified external memory does not block a native drafting baseline. Unverified send authority blocks unattended sending. Unknown memory identity blocks irreversible memory deletion. Unknown restoration behavior blocks claiming a migration is reversible, not writing a design document.

The recommended effort candidate is a controlled starting hypothesis, not a measured optimum. Keep the model fixed; compare coordinator and worker effort separately. Do not attribute a combined model/backend improvement to the backend alone. [Final operating report, section 3](research/03-operating-model-and-release.md)

## 8. What was actually verified here

The research inspected official documentation, selected pinned external code/documents, the supplied methods, and the published research artifacts. Pass 2 recorded thirteen disposable local tests of the user-supplied documentation auditor. Those source tools are not bundled for redistribution; their hashes and execution limits are recorded.

Pass 3 provides a self-contained local verifier for its new reference structure and decision index, with negative controls. It does not certify prose truth, native runtime behavior, or a fresh model's understanding. Its [execution record](research/validation/03-delivery-checks.json) defines the exact scope. No outside reviewer or clean-context builder trial was simulated. Publication is verified separately by Git object identity and readback.

## 9. Expected output from the fourth chat

Produce one reconciled architecture decision, a traceable keep/change/omit migration plan, a separate V3 candidate with justified retained assets, the necessary non-secret setup instructions, and a verification record distinguishing local integrity from live behavior. Keep the final owner's explanation simple enough to operate from.

The research is finished; the production decision is yours to make from all three inputs. Reject or amend any AR recommendation when stronger evidence warrants it, recording the reason. Success is not agreement with this handoff. Success is an Apex foundation that advances the business without recreating the old administrative burden.
