# Apex V3 — Architecture Research

Independent research for a future builder of an e-commerce working environment in Claude Code Projects. This is a decision repository, **not the Apex V3 backend**.

## Start here

The owner uses Projects across store development, marketing, email, customer operations, SEO, and media creation. The goal is useful, creative, self-directed work with little manual backend maintenance. The owner describes the intended scope as "allt för min ehandel" — everything needed for the e-commerce business — and wants the system to be "inte restriktivt": enabling rather than unnecessarily restrictive. This does not authorize uncontrolled customer-facing actions.

Three independent streams will inform a fourth, fresh builder chat: this architecture research, a V2 implementation audit, and a Red Team analysis. This stream does not decide which unread V2 files are defective, does not rewrite the installed skill library, and does not build the final CLAUDE.md. The builder must compare evidence across the three streams rather than count agreeing conclusions.

## Delivery state

- **Pass 1:** delivered; English replacement and technical clarifications completed in this edition.
- **Pass 2:** source comparison and decision records in preparation. Do not treat reserved AR decision references as a completed architecture approval.
- **Pass 3:** not performed. Final calibration, cross-cutting challenge, and the standalone Architecture Research Handoff remain to be delivered.

No live Claude Projects verification test has been run by this research stream. A successful GitHub publication is not a runtime certification.

## Reading order

1. [Platform boundaries](research/01-projects-architecture.md): scope, product distinctions, observed settings, and corrections.
2. [Shared source register](research/01-sources.md): exact source scope, access limitations, and pinned external revisions.
3. [Evidence matrix](research/01-evidence.csv): stable C IDs with evidence category and verification status.
4. [Validation and audit handoff](research/01-validation-and-handoff.md): decision-linked T01–T15 probes and Q01–Q09 open contracts; all NOT RUN.
5. [Methods and adaptations](research/01-method.md): actual skill use and unsupported heuristics deliberately rejected.

The pass-2 report will add stable `AR-###` candidate decisions, realistic alternatives, components needed/avoided, and falsification conditions. Recommendations are proposals, not approvals to change production.

## Evidence and privacy

Reports distinguish documented platform behavior, directly inspected technical evidence, third-party experience, inference, recommendation, and unknowns. The detailed official Projects page remains inaccessible to the research tools; generic CLI documentation is not substituted for native Projects memory or coordinator contracts.

Raw private screenshots, transcripts, local paths, credentials, and customer data are not published. The original Swedish pass-1 edition remains in Git history at `ac598758dfba6eedc1be1d4ce9f02999fa376a9c`. Existing source IDs and test IDs are retained for traceability. `connection-test.md` is historical publication evidence, not a system health check.

The future fourth chat should pin each input repository to a commit, reconcile incompatible findings, and record why it accepts or rejects each relevant AR recommendation. No decision may depend on access to the original conversation.
