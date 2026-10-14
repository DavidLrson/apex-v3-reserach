# Pass 2 — Incremental evidence, methods, and executed checks

Research edition: 2026-10-15. This file adds evidence to [the original register](01-sources.md); it does not renumber or duplicate its S01–S24/P01–P05 entries. It also records the local checks actually executed in pass 2. The main decision owner is [the information-architecture report](02-information-architecture.md).

## 1. Evidence limits

Official rolling documentation describes intended behavior for the stated product. Its retrieval date is not a release date or an immutable runtime version. Source ranges below are the parts used by this research; no claim is made that every linked document or repository was read. A code file at a fixed revision can support a static observation without proving its hosted deployment, test coverage, or execution in Apex.

The six classifications remain DOCUMENTED PLATFORM BEHAVIOR; VERIFIED TECHNICAL EVIDENCE; THIRD-PARTY EXPERIENCE; INFERENCE / HYPOTHESIS; RECOMMENDATION; UNKNOWN / REQUIRES LIVE TEST. In particular, a maintainer's feature/savings claim is not promoted to verified Apex performance because its README is hosted on GitHub.

## 2. Additional official sources

### S25 — Official Help Center section for the new Projects beta

URL: https://support.claude.com/en/articles/9517075-what-are-projects

**Inspected section:** "The new version of projects (beta)," including its usage and product-boundary text; parsed lines 48–63 in this session. The directly read body displayed a relative update age, not a precise publication date. Search-result freshness labels differed from the fetched body; they are not treated as version evidence.

**Supports:** the high-level new-Projects conversation/thread model and provision of project context at thread start. **Does not support:** complete prompt contents, exact coordinator tools, memory synchronization/locking, or the older product's RAG/collaboration behavior. The article explicitly says its remainder concerns the older version.

**Effect on prior evidence:** strengthens C01/PB-01. It does not close C05/C27 or Q01–Q03. Following its link to the detailed Projects page still produced a retrieval error. The error is a tool-access limitation, not proof that the page or feature does not exist.

### S26 — Anthropic: Writing effective tools for AI agents—using AI agents

URL: https://www.anthropic.com/engineering/writing-tools-for-agents

Publication: 2025-09-11. **Inspected scope:** article guidance on tool design, response usefulness, realistic evaluations, and avoiding misleading evaluation targets. **Use:** methodological support for AR-007/AR-017 and task-level evidence. **Limit:** this is engineering guidance, not the hidden native Projects implementation or proof that a particular Apex prompt will improve results.

### Previously registered sources rechecked for pass 2

The relevant portions of S04/S05/S07/S08/S12/S16/S19/S20/S21/S22/S23 were revisited for instruction and rule loading, cloud carryover, skill invocation/distribution, routine context, hook contracts, tool access, and context design. S09 remains a boundary reference; final effort calibration is reserved for pass 3.

Particularly decision-relevant sections are S07 "Import additional files," "How CLAUDE.md files load," and "Path-specific rules"; S08 "Use skills in Cowork and cloud sessions," "Using skill frontmatter outside Claude Code," "Skill content lifecycle," and "Pre-approve tools for a skill"; S05 "Environment caching" and "Setup scripts vs. SessionStart hooks"; S12 "View and interact with runs" and "Connectors"; S16 "Exit code output," "Block the action when a hook fails," and "Stop."

Exact contracts may change. Generic CLI behavior is not silently promoted to a native Projects memory guarantee. Read the applicable environment and version notes before converting any recommendation into configuration.

## 3. Additional pinned external evidence

Each link fixes the inspected source revision. None is a recommendation to install that exact version without checking its later status.

| ID | Source and range inspected | Git blob SHA | What the inspection establishes |
|---|---|---|---|
| P06 | [context-mode PreToolUse entry point, lines 1–240](https://github.com/mksglu/context-mode/blob/655c67f9e1bb2d1c2a6db850447f1cfdcbbb1220/hooks/pretooluse.mjs) | `51d307a2539f1b2e58d383cc8b6c15b5907dc63a` | Conditional plugin-cache maintenance, routing delegation, availability flag, and diagnostic markers exist in the read code |
| P07 | [context-mode shared router, lines 1–190 only](https://github.com/mksglu/context-mode/blob/655c67f9e1bb2d1c2a6db850447f1cfdcbbb1220/hooks/core/routing.mjs) | `e92ab46b2faf6597789bdc5eb3a5a90460d9da3c` | Readiness passthrough and advisory-throttling logic in that range; not a full router audit |
| P08 | [claude-mem cloud-sync documentation, lines 1–240](https://github.com/thedotmack/claude-mem/blob/fef3402e674bebbf72a23aeb735e91c92cd34afd/docs/public/cloud-sync.mdx) | `b5e100134dcec2508523e811434c0ceaf578f592` | Version-pinned maintainer description of sync, uploaded data, identity, status, and configuration; includes the timeout ambiguity discussed in the dossier |
| P09 | [claude-mem sync store, lines 1–100 only](https://github.com/thedotmack/claude-mem/blob/fef3402e674bebbf72a23aeb735e91c92cd34afd/services/sync-api/src/store.ts) | `82ba2e79d2b5e80e737d8991baa7fb9b4121a732` | Declared device-limit/error constants and interface context; not verification of all server paths |

Directory listings and search hits were used to locate these sources, not counted as full-file reads. Plans and fixtures found in search were not used as proof that a proposed change had shipped. Live claude-mem documentation was also consulted to orient the investigation; revision-sensitive conclusions use the pinned files above rather than blend different documentation generations.

Two targeted Reddit searches concerning Projects coordinator/memory and context-mode hooks returned no usable directly relevant evidence in this session. No claim about community consensus or the absence of real-world problems is drawn from that retrieval failure.

## 4. Supplied methods and exact audit inputs

The user supplied the methods as research tools, not as a required V3 runtime package. Their contents were read for their applicable purpose. Default artifact names and ecosystem-specific routing are not product requirements.

| ID | Supplied artifact | SHA-256 |
|---|---|---|
| D01 | `docs-governance` SKILL.md | `499ac59071e6e2b8fb60f085e337a3a1ec16e200adb8f5b8bc027afb338cf3eb` |
| D02 | `artifact-role-contract.md` | `4c22a702c6b0c44659d7999d2cf0a706b7af064562025e28a425c753f0393183` |
| D03 | `audit-docs.py` | `889156ec7b22fa5f08b4f9e5b9a9c918c53b357b24c5aa9f322fdc7e97107622` |
| D04 | `markdown_links.py` | `148cc371d8143bd5070a9a5c5a1a7cc3e142acfad53c7dae4c4c5f9896ec0b20` |
| D05 | `agent-architecture-audit` SKILL.md | `64f57e232c3533877403703bc95b3c75df9de23f657899a306f13c703009ff57` |

The public repository does not redistribute the uploaded skill/script sources. Hashes identify the exact supplied versions. Reproducing the DG checks requires those matching inputs; their unavailable presence in a fresh reader's environment must not be disguised as a bundled dependency.

### Applied-method accounting

- `docs-governance`: separated roles from filenames; rejected automatic governance-spine creation; used the supplied read-only audit on disposable contract fixtures. Its Issue-tracker convention was not imposed on native Projects.
- `agent-architecture-audit`: separated context pollution, stale persistence, missing tools, interpretation, and false completion. It was not represented as inspection of Anthropic's hidden twelve-layer implementation or a second full V2 code audit.
- `writing-for-agents`: used consumer/trigger pointers, co-located caveats, stable decision anchors, and explicit completion boundaries. No final operational CLAUDE.md was written.
- `idea-refine`: considered six candidates, grouped native/minimal-hybrid/external alternatives, and identified assumptions that could reverse the selection. No extra user interview was imposed after requirements were already clear.
- `spec-driven-development`: tied each candidate decision to needed/avoided components, disconfirmation, and existing tests. This research specification was not turned into implementation or an unapproved module tree.
- `context-engineering` and `context-budget`: distinguished loaded text, retrieval, current facts, task checkpoints, and historical evidence. No universal instruction quota or fixed per-tool token charge was asserted.
- `karpathy-guidelines`: challenged additions and removals by purpose and reversibility; a justified broad redesign is not ruled out by a slogan about small edits.
- `doubt-driven-development`: applied a labelled same-context critique. No fresh-context or cross-model reviewer was invoked. The third/fourth chats can supply a different perspective later.
- `verification-before-completion`: kept local mechanical checks distinct from live Projects tests and required a published commit/readback for delivery.

This extends [the earlier method record](01-method.md). It does not claim that all 30 supplied skills were executed end to end, that unavailable references inside them were read, or that method names prove the resulting research is correct.

## 5. Executed local documentation-auditor probes

**VERIFIED TECHNICAL EVIDENCE — execution scope:** Python 3.13.5 on Linux, using D03/D04. Thirteen disposable test repositories were created. The auditor ran in the narrow scope shown below; bytecode writes were disabled. File-content/path/symlink-target fingerprints of each target were compared before and after. All thirteen targets were unchanged by the audit.

These fixtures intentionally include false statements and malformed references. They are tests of the checker contract, **not** claims about the real business, V2 defects, agent intelligence, or performance in Claude Projects. Expected exit codes were defined before execution. All observed exit codes matched those expectations. A deliberately false fixture receiving exit 0 is evidence of the checker's scope, not an endorsement of the false statement.

| ID | Fixture | Scope | Actual exit | Interpretation |
|---|---|---|---:|---|
| DG01 | Valid local Markdown target | artifacts | 0 | Local target existence accepted |
| DG02 | Missing local target | artifacts | 1 | Missing file detected |
| DG03 | Existing file with nonexistent fragment | artifacts | 0 | Anchor existence is not checked by this path |
| DG04 | Contradictory prose with valid links | artifacts | 0 | No semantic consistency judgment |
| DG05 | Small repo without default governance files | full | 0 | Missing default roles are warnings, not a demand to create files |
| DG06 | Explicit mapping to nonexistent file | context | 1 | Invalid declared target detected |
| DG07 | Mapping outside repository root | context | 1 | Path containment enforced in the tested case |
| DG08 | Unresolvable external URL | artifacts | 0 | External URL availability not checked |
| DG09 | Undefined reference-style link | artifacts | 0 | This undefined-reference case does not reach target validation |
| DG10 | Existing TEST-ID with fabricated pass narrative | artifacts | 0 | Reference integrity does not prove execution |
| DG11 | Unlinked document under docs/ | artifacts | 0 | Emits possible-orphan warning |
| DG12 | Unlinked document under research/ | artifacts | 0 | No equivalent orphan warning; heuristic is directory-scoped |
| DG13 | Markdown symlink outside root | artifacts | 1 | Escaping source and target rejected in this fixture |

[Raw sanitized execution record](validation/02-docs-probes.json) contains per-case stdout/stderr, expected/actual codes, input hashes, and unchanged-target checks. Temporary paths were replaced with markers. No private project contents were used.

To rerun with the matching user-supplied scripts, place the parser beside the auditor and invoke the auditor on an isolated fixture:

```text
PYTHONDONTWRITEBYTECODE=1 python3 <auditor-directory>/audit-docs.py --root <fixture> --scope artifacts
```

Use `--scope full` only for the missing-defaults case and `--scope context` for the explicit mapping cases. This command documents the research experiment; it is not proposed as an always-on Apex hook. The checker does not certify its own parser completeness or every possible filesystem/Markdown edge case.

## 6. Incremental claim register

C01–C42 remain in [the original evidence matrix](01-evidence.csv). The following additions are owned here to avoid changing their historical meaning.

| ID | Classification | Claim and scope | Source / verification |
|---|---|---|---|
| C43 | DOCUMENTED PLATFORM BEHAVIOR | The applicable Help Center beta section supports native parallel threads and project context at thread start, at a high level | S25; not a synchronization test |
| C44 | VERIFIED TECHNICAL EVIDENCE | The selected context-mode router range contains an unavailable-MCP passthrough | P07; static only |
| C45 | VERIFIED TECHNICAL EVIDENCE | The inspected context-mode entry point contains conditional installation-metadata/legacy-path maintenance | P06; not executed |
| C46 | THIRD-PARTY EXPERIENCE | claude-mem's pinned sync documentation describes upload of observations and prompts | P08; selected provider behavior not tested |
| C47 | VERIFIED TECHNICAL EVIDENCE | The pinned sync document contains different timeout descriptions that should not be reduced to one universal value | P08 textual inspection; actual effective timeout unknown |
| C48 | VERIFIED TECHNICAL EVIDENCE | The inspected sync-store range declares a device-limit constant and associated error | P09; enforcement/deployed version not certified |
| C49 | VERIFIED TECHNICAL EVIDENCE | All thirteen auditor fixtures produced their expected exit code and unchanged-target result | DG01–DG13; local mechanical scope only |
| C50 | RECOMMENDATION | A checker pass should remain separate from semantic and business completion | AR-017/AR-018; DG03/DG04/DG10 support the boundary |
| C51 | DOCUMENTED PLATFORM BEHAVIOR | Skill distribution/body/permission lifetimes differ by mechanism; preapproval is not an exclusive allowlist | S08 applicable sections; T11 not run |
| C52 | UNKNOWN / REQUIRES LIVE TEST | Neither inspected package is established as compatible shared native Projects memory | T07/T13; no installation/runtime test |

## 7. What remains untested

Every live Projects test T01–T15 remains NOT RUN. Native memory locking, fresh/old-thread visibility, real connector authority, routine context, external-provider retention/deletion, and measured effort quality are unresolved where the shared Q register says so. A documentation link or successful publication does not close those questions.

The pass-2 reports underwent a same-context factual and recommendation check, not an independent expert panel. The other audit repositories were not treated as finished evidence. The final Architecture Research Handoff remains reserved for pass 3 and must expose these limits to a fresh fourth chat.

## 8. Publication verification boundary

The delivery uses immutable Git blobs and a commit based on the observed branch head, preserving prior files and history. Publication verification checks the updated branch ref, tree entries, expected blob identities, changed paths, and selected content readback. This demonstrates that the intended research documents were published; it does not validate the native runtime.

The terminal delivery message identifies the verified commit. Any later correction should be a new commit with an explicit reason, not an unrecorded alteration of earlier evidence or a claim that the original uncertainty never existed.
