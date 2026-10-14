# Shared evidence and source register

Edition: 2026-10-15. Covers passes 1 and 2. Source IDs S01–S18, G01–G03, and O01–O03 are preserved from pass 1 so existing references remain meaningful.

## How to use this register

A retrieval date is not a publication date, a version pin, or proof that a cached page reflects the latest production rollout. Unless a date is stated below, the live documentation has no publication date established in this study. Record the runtime version again before implementing a version-sensitive feature. Only the named sections were relied on; no claim is made to have read the whole documentation site or every example in its largest pages.

Official documentation supports **DOCUMENTED PLATFORM BEHAVIOR** within its stated scope. Inspected Git objects and configuration entries support **VERIFIED TECHNICAL EVIDENCE** only about those artifacts. Reporter experience and maintainer performance assertions are **THIRD-PARTY EXPERIENCE**, not measured Apex outcomes. Proposed designs are **RECOMMENDATION**; their predicted effects are **INFERENCE / HYPOTHESIS**. Unresolved contracts remain **UNKNOWN / REQUIRES LIVE TEST**.

Do not turn a source link into stronger evidence than the access actually obtained. In particular, S03 is an unresolved retrieval target, not a read specification.

## Official platform sources

| ID | Source and relevant section | Access and scope |
|---|---|---|
| S01 | [Documentation index](https://code.claude.com/docs/llms.txt), entry for Projects and adjacent product pages | Inspected in passes 1 and 2. Establishes the listed product surfaces and links, not detailed execution semantics. |
| S02 | [Projects redesigned](https://claude.com/resources/articles/projects-redesigned) | Historical official launch article dated 2026-09-17. Search-rendered body text was read in pass 1; direct retrieval failed. Retained as historical evidence, not freshly verified as a full page in pass 2. |
| S03 | [Claude Projects](https://code.claude.com/docs/en/claude-projects) | Direct page and Markdown retrieval failed in both passes. Its existence in S01 and links from reports do not establish its detailed content. |
| S04 | [Settings files and precedence](https://code.claude.com/docs/en/settings), especially Settings in cloud sessions and precedence | Relevant sections refreshed 2026-10-15. Distinguishes hosted single-/multi-repository loading from local settings. Do not transfer self-hosted exceptions to Anthropic-hosted sessions. |
| S05 | [Configure cloud environments](https://code.claude.com/docs/en/cloud-environments), What carries over from your setup; Setup scripts; Environment caching; Setup scripts vs. SessionStart hooks; Limitations in cloud sessions | Relevant sections refreshed 2026-10-15. Includes environment configuration and filesystem/process lifecycle. Exhaustive network allowlist analysis was not performed. |
| S06 | [Use Claude Code in the cloud](https://code.claude.com/docs/en/claude-code-on-the-web), GitHub authentication options and environment distinction | Pass-1 reading retained. Projects-specific repository authentication wording was distinguished from ordinary cloud sessions. Recheck before an authentication migration. |
| S07 | [How Claude remembers your project](https://code.claude.com/docs/en/memory), Write effective instructions; Import additional files; How CLAUDE.md files load; Path-specific rules; Rule frontmatter reference; Auto memory | Relevant sections refreshed 2026-10-15. Generic Claude Code memory and instruction behavior, not a substitute for S03. The page identifies version limits for some diagnostics and rule handling. |
| S08 | [Extend Claude with skills](https://code.claude.com/docs/en/skills), cloud/account availability; frontmatter; invocation; troubleshooting; Skill descriptions are cut short | Relevant sections refreshed 2026-10-15. Listing, full invocation, supporting files, and scoped execution are separate concerns. The current listing-budget section differs from older generic percentage claims. |
| S09 | [Model configuration](https://code.claude.com/docs/en/model-config), effort and configuration sources | Relevant sections refreshed during pass 2. Model-specific defaults and runtime overrides must be recorded; a UI screenshot alone does not identify historical effective settings. |
| S10 | [Agents overview](https://code.claude.com/docs/en/agents) | Pass-1 overview retained. Useful for separating agent mechanisms, not for native Projects internals. |
| S11 | [Remote Control](https://code.claude.com/docs/en/remote-control), local execution and availability | Pass-1 reading retained. Does not by itself specify every Projects-to-device interaction. |
| S12 | [Automate work with routines](https://code.claude.com/docs/en/routines), triggers; View and interact with runs; Connectors; Environments and network access | Relevant sections refreshed 2026-10-15. Describes separately configured automated cloud runs. Does not establish inheritance of native Projects memory. |
| S13 | [Prompt caching](https://code.claude.com/docs/en/prompt-caching) | Pass-1 reading retained. Used only for separating processing reuse from active context and durable factual memory; no subscription billing calculation was performed. |
| S14 | [Permission modes](https://code.claude.com/docs/en/permission-modes), auto mode and hosted behavior | Relevant sections refreshed during pass 2. Safety classification is not substantive task evaluation. No recommendation to bypass a platform rejection follows from this source. |
| S15 | [Debug your configuration](https://code.claude.com/docs/en/debug-your-config) | Pass-1 diagnostic reading retained. Suggested diagnostics must be checked for availability in the actual target session. None was executed in the user's Projects here. |
| S16 | [Hooks reference](https://code.claude.com/docs/en/hooks), Hook handler fields; event semantics; Stop; exit/error behavior; asynchronous handlers | Relevant sections refreshed 2026-10-15. This is a large reference, not exhaustively audited. Matching, parallelism, timeout behavior, and lifecycle scope matter before relying on a guard. |
| S17 | [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works) | Pass-1 general execution explanation retained; not a reconstruction of the hidden Projects coordinator implementation. |
| S18 | [Best practices](https://code.claude.com/docs/en/best-practices) | Pass-1 advice retained. Verification and exploration recommendations are not a proof that a particular Apex configuration works. |
| S19 | [Extend Claude Code](https://code.claude.com/docs/en/features-overview), context costs and choosing extension mechanisms | Relevant sections read in pass 2. Helps distinguish skills, tools, hooks, and isolated/forked subagent contexts. |
| S20 | [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp), tool search and deferred loading | Relevant sections refreshed 2026-10-15. Current deferred loading invalidates a universal fixed schema-token cost multiplied by installed tool count. Account connectors and local configuration are distinct surfaces. |
| S21 | [Create custom subagents](https://code.claude.com/docs/en/sub-agents), configuration, skills, model and effort, tool access | Relevant sections read in pass 2. Includes explicitly versioned behavior. Applies to Claude Code subagents; native Projects threads are not silently treated as the same mechanism. |
| S22 | [Configure permissions](https://code.claude.com/docs/en/permissions), tool rules and scope | Relevant sections refreshed 2026-10-15. Rules govern particular tool surfaces; an apparently read-only agent description is not an end-to-end authorization audit. |

## Official engineering guidance, not a current Projects specification

| ID | Source | Publication and use |
|---|---|---|
| S23 | [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), The anatomy of effective context; Context retrieval and agentic search; Context engineering for long-horizon tasks | Published 2025-09-29; read 2026-10-15. Supports a design method balancing useful context, retrieval, and persistence. Historical examples do not define current native Projects behavior. |
| S24 | [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), When (and when not) to use agents; Orchestrator-workers; Evaluator-optimizer | Published 2024-12-19; read 2026-10-15. The page itself warns that the tooling landscape has changed. Used for explicit trade-off reasoning, not as installation advice or current product defaults. |

## Version-pinned external tool evidence

The commit IDs below were read through the GitHub connector. These are review snapshots, not recommended deployment pins. No package installer, observer, server, hook, or plugin was run. README descriptions and promotional savings figures were not independently benchmarked.

| ID | Artifact | Inspection and what it can support |
|---|---|---|
| P01 | [claude-mem README at fef3402e](https://github.com/thedotmack/claude-mem/blob/fef3402e674bebbf72a23aeb735e91c92cd34afd/README.md) | Lines 1–250 inspected. Maintainer-described capture, summaries, future-session recall, installation/provider choices, and the difference between library-only installation and plugin/worker setup. It is not proof of Projects compatibility. |
| P02 | [claude-mem plugin hook manifest at fef3402e](https://github.com/thedotmack/claude-mem/blob/fef3402e674bebbf72a23aeb735e91c92cd34afd/plugin/hooks/hooks.json) | Full manifest inspected. Blob `603bacf9d77fef300d318e3ab9c4548db8fa68fa`. Static evidence of startup, context, capture, summarization, and session lifecycle handlers, including asynchronous entries. Does not prove handler execution or capture completeness. |
| P03 | [context-mode README at 655c67f9](https://github.com/mksglu/context-mode/blob/655c67f9e1bb2d1c2a6db850447f1cfdcbbb1220/README.md) | Lines 1–235 inspected, including problem framing, Claude Code installation, and MCP-only alternative. Maintainer-described off-context processing and session-continuity behavior are not Apex measurements. |
| P04 | [context-mode hook manifest at 655c67f9](https://github.com/mksglu/context-mode/blob/655c67f9e1bb2d1c2a6db850447f1cfdcbbb1220/hooks/hooks.json) | Full manifest inspected. Blob `9c2b9285ce0ef831080372857a90cfe13014ecfd`. Static evidence of PreToolUse routing and lifecycle/capture handler declarations. The handler implementations were not audited. |
| P05 | [context-mode LICENSE at 655c67f9](https://github.com/mksglu/context-mode/blob/655c67f9e1bb2d1c2a6db850447f1cfdcbbb1220/LICENSE) | License text inspected; identifies Elastic License 2.0. This register does not give legal advice or a redistribution clearance. Any repackaging decision must preserve and review the actual terms. |

Full reviewed revisions: claude-mem `fef3402e674bebbf72a23aeb735e91c92cd34afd`; context-mode `655c67f9e1bb2d1c2a6db850447f1cfdcbbb1220`. A repository's stars, README badge, or recent commit is not evidence that it solves Apex's failure mode. No license conclusion was inferred from the claude-mem badge alone.

## First-person GitHub incident reports retained from pass 1

| ID | Report | Reading boundary |
|---|---|---|
| G01 | [anthropics/claude-code issue 96775](https://github.com/anthropics/claude-code/issues/96775) | Filed 2026-09-24. Issue and its two then-existing comments read in pass 1; both comments were from the original reporter. Approval propagation and blocked actions are reported experience, not reproduced here. |
| G02 | [anthropics/claude-code issue 99688](https://github.com/anthropics/claude-code/issues/99688) | Filed 2026-10-05. Issue and its then-existing comment read in pass 1. The second person's comment supports only part of the claimed failure chain. |
| G03 | [anthropics/claude-code issue 102074](https://github.com/anthropics/claude-code/issues/102074) | Filed 2026-10-14. Issue read in pass 1; no comments then. Scope is two projects on one account. No cross-account access was reported as observed. |

These issues were open at the pass-1 retrieval. Their current resolution status was not revalidated in pass 2 and is not asserted here. No inspected maintainer response established the entire reported mechanism as a confirmed platform defect.

## User evidence retained privately

| ID | Material | Permitted evidentiary use |
|---|---|---|
| O01 | Memory settings screenshots, 2026-10-14 | Establishes the displayed native Auto memory index/topic-file surface, not the correctness of stored facts or the actual filesystem identity. |
| O02 | General, model, effort, and usage screenshots, 2026-10-14 | Establishes displayed defaults and distinct settings fields, not effective historical runtime values or causal explanations. |
| O03 | Environment screenshots, 2026-10-14 | Establishes visible local/cloud and configuration surfaces, not successful authentication or actual execution of placeholder setup text. |
| U01 | Owner's task instructions and workflow requirements in the research conversation | Defines desired business outcomes, scope exclusions, and tolerance for maintenance. It is not technical proof about Claude's internals. |

Raw screenshots, transcripts, local usernames/paths, account credentials, and customer data are intentionally not published. The reports include only the minimum non-sensitive observations needed to understand the design problem. The V2 code itself remains outside this stream's inspection scope.

## Search coverage, exclusions, and unresolved access

The research followed official documentation links and targeted terms for memory loading, instruction precedence, skill activation, hosted settings, routine outcomes, and hook execution. Both named external candidates were read at pinned Git revisions. Their entrypoint manifests were inspected; their full codebases and all supporting dependencies were not.

Targeted Reddit searches included Claude Code Projects, coordinator, and memory terms. No sufficiently relevant first-person result was admitted as evidence. This is not a claim that no such discussion exists. General chat-Projects memory help pages, unrelated terminal agent-team incidents, anonymous best-practice lists, and secondary documentation mirrors were not used to establish native Code Projects contracts.

The missing S03 page is still a material gap. Search-rendered excerpts, a link in an index, and an AI's earlier confident statement cannot collectively substitute for the unread specification. A live probe may resolve a narrow behavior even while documentation retrieval remains unavailable, but the probe must record its environment and not become a universal claim.

## Citation and change rules for the builder

Refer to stable S/P/G/O/U IDs plus the named section. Prefer commit-pinned links for external source code. When a source or runtime contradicts a recommendation, record which AR decision it changes and why. Do not silently edit away historical uncertainty. The relevant alternatives and live tests should change with the evidence rather than preserve a decision for consistency with an earlier report.
