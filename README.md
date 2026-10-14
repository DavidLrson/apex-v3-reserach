# Apex V3 — Architecture Research

**Final research delivery: all three research passes are complete. This is not the Apex V3 backend and is not a production approval.**

## Start here: fourth-chat handoff

Read [Architecture Research Handoff](ARCHITECTURE-RESEARCH-HANDOFF.md) first. It supplies the owner context, responsibilities, scope, missing inputs, recommended direction, and a concrete design/build sequence without requiring the original chat.

This repository is one of three inputs: architecture research, a separate V2 implementation audit, and a separate Red Team analysis. The fourth chat must obtain and pin the actual other repositories and the V2 source snapshot before final migration decisions. Their URLs and results are not invented here.

The owner wants useful, creative, self-directed help across ecommerce with little manual backend maintenance. Preserve useful business skills and assets. Do not turn this dossier into an always-loaded production instruction set or a second coordinator.

## Reading by purpose

| Need | Canonical document |
|---|---|
| Start the final design/build chat | [Architecture Research Handoff](ARCHITECTURE-RESEARCH-HANDOFF.md) |
| Understand information owners, instructions, memory and control alternatives | [Pass 2 main report: AR-001–AR-018](research/02-information-architecture.md) |
| Choose effort experiments, completion, autonomy and release gates | [Pass 3 operating model](research/03-operating-model-and-release.md) |
| Challenge the recommendations and reconcile disagreement | [Pass 3 challenge record](research/03-challenge-and-resolution.md) |
| Look up final decision dispositions and dependencies | [Decision index](research/03-decision-index.json); navigation, not a second rationale |
| Resolve platform/environment distinctions | [Pass 1 boundaries](research/01-projects-architecture.md), read with later corrections |
| Evaluate claude-mem or context-mode | [Pinned external-tool dossier](research/02-external-tools.md) |
| Find sources and evidence limits | [Register 1](research/01-sources.md), [register 2](research/02-evidence-and-validation.md), [register 3](research/03-sources-and-quality.md) |
| Find proposed live tests and unresolved contracts | [T01–T15 and Q01–Q09](research/01-validation-and-handoff.md) |
| Inspect actually executed local checks | [Pass 2 DG results](research/validation/02-docs-probes.json), [pass 3 reference checks](research/validation/03-delivery-checks.json) |

## What completion means

Pass 1 established documentary platform boundaries. Pass 2 delivered candidate decisions, alternatives and selected external code inspection. Pass 3 adds operational refinements, critical challenge, scoped local verification and the standalone handoff. Historical statements in earlier files that pass 3 is pending are superseded by this README and the final handoff; the earlier files remain unchanged for traceability.

**No live Claude Projects test, external memory installation, effort comparison, independent review panel, or fresh-builder trial was run in this stream.** The local checks have narrower scopes. The fourth chat may reject any recommendation when stronger evidence supports a different design.

The six evidence categories separate official behavior, inspected technical artifacts, third-party experience, inference, recommendations and unknowns. A published commit proves delivery, not correct runtime behavior. The detailed Projects documentation page remained inaccessible; the relevant Help Center beta section provides high-level context only.

## Preservation and privacy

Earlier research remains in Git history and in the retained report files. The final pass starts from `141002f54e2de684b237ca0ce8a2edcd248708ff`. The original Swedish pass-1 edition is at `ac598758dfba6eedc1be1d4ce9f02999fa376a9c`; its English supplement is at `bef1d2b5e5b31935b2d49ad3bbb7233e2e40f897`.

Raw private transcripts, screenshots, local account paths, credentials, customer data and supplied skill sources are not published. `connection-test.md` is historical write-access evidence. Research verification scripts are not proposed Apex startup hooks.
