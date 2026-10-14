# Pass 3 — Sources, coverage, and verification boundaries

Edition: 2026-10-15. This register adds S27–S32 and final claim identifiers without renumbering [S01–S24](01-sources.md), [S25–S26 and P06–P09](02-evidence-and-validation.md), or AR-001–AR-018. Access dates are not publication dates, version pins, or proof of the latest production rollout.

## 1. Evidence contract

**DOCUMENTED PLATFORM BEHAVIOR** is scoped to an inspected official description. **VERIFIED TECHNICAL EVIDENCE** names the actual artifact or executed local check. **THIRD-PARTY EXPERIENCE** remains reported or maintainer-described behavior, not an Apex measurement. **INFERENCE / HYPOTHESIS** identifies a proposed explanation. **RECOMMENDATION** identifies a candidate choice. **UNKNOWN / REQUIRES LIVE TEST** preserves a material unresolved contract.

No live Claude Projects run, external memory installation, model comparison, or new independent reviewer was performed in pass 3. The other two audit repositories were not supplied or read. This final study is not a certification of a built V3 system.

## 2. New primary sources

### S27 — Agent evaluations

[Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents). Published **2026-01-09**. Read 2026-10-15, especially “The structure of an evaluation,” “Types of graders for agents,” and capability/regression distinctions.

Supports distinguishing a transcript from an outcome and choosing checks appropriate to the claim. This is engineering guidance, not a mandatory evaluation framework for a small ecommerce operation. The proposed lightweight comparisons are our design, not experiments performed by the article on Apex. No benchmark percentage or general reliability estimate is imported.

### S28 — Model versus effort

[Choosing a Claude model and effort level in Claude Code](https://claude.com/resources/articles/claude-model-and-effort-level-in-claude-code). Author Lydia Hallie; displayed date **2026-07-07**. Search-rendered article body was read on 2026-10-15; direct canonical retrieval returned an error. The model configuration reference links to this article.

Supports the distinction between model capability and the amount of investigative/verification work. It is guidance for Claude Code, not a native Projects settings export or a measured recommendation for this owner. The High-coordinator pilot is our inference and recommendation; its superiority remains untested.

### S29 — File checkpoint boundaries

[Checkpointing](https://code.claude.com/docs/en/checkpointing). Rolling documentation; publication date not established. Read 2026-10-15, especially “Limitations,” including Bash changes, subagent edits, concurrent changes, and the distinction from version control.

Applies to the documented Claude Code file/conversation mechanism. It does not establish restoration of native Project memory or external business effects. The broader migration-state separation in the final report is a recommendation drawn from this boundary, not an additional checkpoint feature.

### S30 — Evidence against simplistic harness removal

[Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps). Published **2026-03-24**, Prithvi Rajasekaran. Read the motivation, evaluator design, long-running application experiments, and later model/harness comparison sections.

Shows an official engineering experience in which additional structure and evaluator calibration mattered. Its models, tasks, and run budgets differ from Apex; its demonstrations do not isolate the effect of every component under identical conditions. It is a counterexample to unconditional “all extra orchestration is waste,” not a recommendation to copy that harness. No cost or outcome number is treated as an Apex forecast.

### S31 — CLI continuation goals

[Keep Claude working toward a goal](https://code.claude.com/docs/en/goal). Rolling documentation; read 2026-10-15. Relevant sections: “Compare ways to keep a session running,” “Write an effective condition,” “How evaluation works,” and “Requirements.”

Defines a session continuation/evaluation mechanism. Its evaluator relies on surfaced conversation evidence and does not independently use tools. This supports a verification boundary, not equivalence with the native Projects Goal field. Version-specific behavior and availability must be checked in the selected surface before use. No goal was enabled here.

### S32 — Dynamic workflow result semantics

[Orchestrate subagents at scale with dynamic workflows](https://code.claude.com/docs/en/workflows). Rolling documentation; read 2026-10-15. Relevant sections: script authoring, unsuccessful/stalled agents, costs, and availability. Parsed lines 363–370 and 472–478 were particularly relevant.

The inspected example and explanation preserve unsuccessful results as `null` before filtering; scripted subagent prompts also have an explicitly described approval boundary. This supports asking how a coordinator accounts for missing required work. It does not prove native Projects uses that runtime or that V2 drops such results. No workflow script was installed.

## 3. Earlier sources refreshed and limits retained

| ID | Refreshed scope in this pass | Consequence |
|---|---|---|
| S03 | Direct detailed Projects page and Markdown route attempted | Still inaccessible; no invented replacement specification |
| S05 | Cloud environment lifecycle, archive behavior, network routes, setup/caching | Stopping and rollback require attention to actual execution/effect paths |
| S09 | Model and effort configuration, overrides/persistence, model-dependent defaults, separate Ultracode setting | Preserve the distinction between a controlled effort change and an orchestration/model change |
| S12 | Routine result status, connectors, configuration, and run lifecycle | Do not treat infrastructure success as accepted business output |
| S18 | Verification and adversarial review guidance, specification and session boundaries | Reviews should target meaningful requirements, not cosmetic criticism |
| S25 | Only the explicitly applicable new-Projects beta section, parsed lines 48–63 | Retains high-level support for native threads/context, not detailed synchronization guarantees |

The remaining sources and pinned external artifacts retain their earlier reading scopes and dates; they were not silently refreshed. Old Github issues were not represented as newly confirmed or currently unresolved incidents in this pass. The external packages were not re-pinned, installed, or benchmarked.

Several searches for first-person Reddit reports on native Projects, coordination, and memory returned no sufficiently relevant evidence. No community consensus claim is made. Unrelated results and generic older chat-Projects advice were excluded. Search-rendered source text is labeled as such; a failed page fetch does not prove the feature is absent.

## 4. Final incremental claims

C01–C42 remain in [the original matrix](01-evidence.csv), and C43–C52 in the pass-2 evidence report.

| ID | Classification | Narrow claim or recommendation | Evidence / decision link |
|---|---|---|---|
| C53 | DOCUMENTED PLATFORM BEHAVIOR | Generic Code effort has model-dependent settings and lifecycle; native Project inheritance is not established by that fact | S09; AR-015 |
| C54 | RECOMMENDATION | Compare higher coordinator effort before altering worker effort and backend simultaneously | AR-015; T05; not measured |
| C55 | DOCUMENTED PLATFORM BEHAVIOR | The documented CLI goal evaluator does not independently execute tools or read source files | S31; AR-017 |
| C56 | UNKNOWN / REQUIRES LIVE TEST | Native Projects Goal and CLI goal equivalence has not been established | S03/S31; Q01/Q07 |
| C57 | DOCUMENTED PLATFORM BEHAVIOR | The inspected workflow surface has nullable unsuccessful subagent results | S32; not a V2 observation |
| C58 | RECOMMENDATION | Required missing worker results must not silently become complete review coverage | AR-008/AR-017; T04 |
| C59 | DOCUMENTED PLATFORM BEHAVIOR | Environment archiving affects future sessions rather than terminating all running work | S05 archive section |
| C60 | DOCUMENTED PLATFORM BEHAVIOR | The hosted network allowlist does not control every enabled connector/connection route | S05 network section |
| C61 | RECOMMENDATION | Cutover and rollback must account for active execution and already accepted external effects | AR-011/AR-012/AR-016; T06/T08/T15 |
| C62 | RECOMMENDATION | Block only capabilities that depend on unresolved evidence, rather than requiring every possible probe before useful work | Final operating report section 7 |
| C63 | VERIFIED TECHNICAL EVIDENCE | Final delivery reference checks and negative controls were executed locally within the stated scope | Execution record; not semantic/live certification |
| C64 | UNKNOWN / REQUIRES LIVE TEST | A genuinely fresh fourth-chat comprehension/build trial has not been executed | T15; no independent panel simulated |

## 5. Applied skills and concrete effects

The uploaded archive contains thirty skills. This pass selected methods rather than running all workflows. Relevant bodies or sections were re-read; linked references not present in the supplied material are not claimed as read. The actual adaptations matter more than a list of names.

| Method | Effect on this delivery | Explicit limitation |
|---|---|---|
| `writing-for-agents` | Self-contained handoff, conditional reading pointers, co-located caveats, completion criteria for builder stages | Leading-word and negation heuristics are not treated as proven universal laws |
| `spec-driven-development` | Responsibility boundaries, dependency order, acceptance gates, stable IDs | User already authorized the research; no additional interview or automatic end-turn gate was imposed; no V3 code phase executed |
| `idea-refine` | Final native/hybrid/external choice tested against alternatives and rejected defaults | No new idea catalogue or compulsory template files |
| `karpathy-guidelines` | Preserve prior reports, change only research deliverables, no speculative production subsystems | Simplicity does not justify removing useful protection without evidence |
| `docs-governance` and artifact-role contract | One owner for each report/register; roles do not require empty files; integrity separated from truth | Original D03/D04 checker was not rerun or redistributed in this pass |
| `agent-architecture-audit` | Distinguish missing context, selection, interpretation, stale state, and false completion | No inspection of hidden Anthropic implementation or full V2 audit |
| `context-engineering` | Keep this dossier out of runtime context; use decision-conditioned pointers and exact evidence retrieval | No universal token threshold, prompt-order reconstruction, or fixed per-tool cost |
| `doubt-driven-development` | Eight explicit proposal/contract/counterexample/reconciliation entries | Same-context adaptation only; fresh-review/cross-model stage was not executed |
| `verification-before-completion` | Local checks, negative controls, guarded Git publication and readback | Publication checks prove delivery, not system reliability |

The final pass did not invoke `santa-method`, a council, or a simulated outside reviewer. A fresh fourth chat and the separately commissioned Red Team are future comparison opportunities, not evidence this author can claim to have performed.

## 6. Local verification contract

The bundled [research verifier](validation/03-verify-delivery.py) is a small standard-library tool written for this delivery. It checks the final decision index, known identifiers, required handoff headings, and simple inline local Markdown links used in the new reports. It is **not a general Markdown parser, security scanner, prose fact checker, or Apex runtime tool**.

The working container could not resolve GitHub for a normal Git clone. GitHub connector reads and writes remained available. Accordingly, the pre-publication run used the new local files plus the explicitly recorded baseline Git tree. Missing baseline bytes were not fabricated. The metadata mode reports which target checks used baseline evidence and does not claim to re-parse every historical file.

To repeat the narrower publication check, use the delivered files and the explicit option:

```sh
python3 research/validation/03-verify-delivery.py --root . --allow-baseline-metadata
```

In a complete checkout, omit that option to require actual local target files and check their referenced anchors. Both modes validate only the declared final-pass documents. Neither executes historical DG probes nor live T01–T15 tests.

The [sanitized execution record](validation/03-delivery-checks.json) records the command mode, actual results, intentionally failing negative controls, and file hashes. A semantic falsehood can still satisfy these structural checks; the report says so explicitly. The checker source itself is included so the new reader can inspect what “pass” means.

## 7. Corpus review and publication

The full pass-2 decision report (lines 1–489), external-tool dossier, current README, and relevant evidence/method material were read through the GitHub connector against baseline `141002f54e2de684b237ca0ce8a2edcd248708ff`. Older platform/validation claims were carried forward with their recorded source boundaries, with targeted refreshes listed above. This was not a fresh exhaustive reread of every old web page or every repository linked by a source.

Final changes add the handoff, operational refinements, challenge record, source/quality register, compact decision index, and research verification artifacts; README becomes the final entry point. Earlier reports are preserved. Their “pass 3 pending” statements are historical and superseded by the current README/handoff, not silently edited away.

Publication uses the observed parent commit and base tree, verifies that the branch has not changed unexpectedly, and updates it without force. The terminal delivery identifies the final commit and the readback result. Expected new blob identities and sizes are compared with the remote tree; retained baseline files are checked by Git blob identity. These checks do not require or imply a successful local Git clone.

No private transcripts, raw screenshots, account paths, credentials, customer data, or original unlicensed skill sources are published. No V2 code, Project setting, installed package, or external business account is changed.
