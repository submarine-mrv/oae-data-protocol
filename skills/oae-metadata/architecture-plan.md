# AI Skills for OAE metadata: use cases and discussion guide

## 1. Purpose and proposed direction

Help researchers independently turn project documents and field datasets into a downloadable OAE metadata JSON draft. They then upload it into Metadata Builder, review and edit it to match their expectations, and export the revised file before publication or sharing.

**Workflow:** AI draft → researcher review/edit in Metadata Builder → export reviewed JSON → publish with the dataset, with optional later Data Commons submission.

|                       | Working assumption                                                                                                                                                                                        |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Starting examples     | 3-5 datasets with metadata curated by Jacki through ad hoc Claude web sessions using the JSON Schema and project documentation.                                                                           |
| Expected scale of use | 5-10 projects over the next year; a project may contain multiple datasets.                                                                                                                                |
| Initial scope         | Field projects, experiments, datasets, and variables; <br/> model-specific workflows are not the focus for MVP                                                                                            |
| Data outputs          | Researchers will take JSON outputs from an AI and upload it into Metadata Builder for further refinement, review, and auditing of content.                                                                |
| Publication           | After reviewing and finalizing the metadata, researchers can publish JSON metadata alongside a dataset on Zenodo or other data repository. Inclusion in the OAE Data Commons will require admin approval. |

## 2. Architectural overview

All ai-skills workflow artifacts and schema assets will be managed directly in `oae-data-protocol` repo on github. The skill will be packaged for multiple supported AI environments, and the Metadata Builder used as the researcher’s primary auditing / review interface for finalizing metadata.

| Component | Proposed layout / location | Responsibility |
|---|---|---|
| Shared skill | `skills/oae-metadata/SKILL.md` in `oae-data-protocol` | OAE guidance, source interpretation, drafting, uncertainty handling, and Builder handoff. |
| Supporting material | Skill-local `references/`, `assets/`, and optional `scripts/` | Published schema snapshot, generated field guidance, examples, and helpers justified by actual files. LinkML may be used at build time where useful. |
| Claude distribution | GitHub marketplace catalog at `.claude-plugin/marketplace.json`, plugin manifest at `.claude-plugin/plugin.json`, and the shared skill | A skills-only plugin will be distributed from `oae-data-protocol`; a standalone skill ZIP will be retained as a fallback. No MCP server or separate marketplace service is required. See [Claude marketplace packaging](https://code.claude.com/docs/en/plugin-marketplaces). |
| OpenAI distribution | Plugin package containing `plugin.json` and `skills/oae-metadata/` | Installable packages will be generated from the same shared skill source. See [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins). |
| Open-weight model support | Shared skill in an open-source harness such as [pi](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md), with a [locally served model](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/models.md) | A local open-weight model workflow will be supported alongside proprietary services; model and tool compatibility will be verified during the pilot. |
| Metadata Builder | Existing `oae-form` application | Import, researcher review and editing, validation, and JSON export. |
| Future integrations | MCP only when a concrete service capability is needed | Direct account storage or uploads later; the initial file workflow needs no OAE login or cloud storage. |

### Installation paths

These are proposed delivery paths based on current host documentation. Account availability, file access, helper execution, JSON download, and plugin update behavior will be verified in each target environment during the pilot.

**Update maintenance:** repository-backed plugin distribution will be preferred to simplify updates as the schema and extraction guidance evolve. With ZIP installation, researchers must know when a new release is available, download it, and upload it again. Marketplace distribution provides a managed update path; automatic-update behavior for personal browser and desktop installations will be verified during the pilot rather than assumed from [organization-managed GitHub sync](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization).

| User environment                        | Package | Installation path | Notes                                                                                                       |
|-----------------------------------------|---|---|-------------------------------------------------------------------------------------------------------------|
| Claude in a browser                     | Skills-only plugin via GitHub marketplace (preferred) | Customize → Plugins → + → Add marketplace → Add from a repository; add `submarine-mrv/oae-data-protocol`, then install the OAE plugin once published. [Claude plugins](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) | Paid Claude plan required. Automatic updates for personal installations are still TBC.                      |
| Claude desktop app                      | Same marketplace plugin (preferred) | Added through Customize → Plugins using the same repository marketplace; available in Desktop chat and Cowork. [Claude plugins](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) | Desktop installation and update behavior are still to be confirmed.                                         |
| Claude skill fallback                   | Standalone skill ZIP | Uploaded and enabled via Customize → Skills → Create skill → Upload a skill. Retained for Free-plan access or where marketplace installation is unavailable. [Claude skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude) | Code execution/file creation must be enabled. Updates require downloading and uploading a new ZIP.          |
| ChatGPT in a browser                    | Skills-only plugin | Installed through the plugin directory once distributed there; a local skill folder alone is not the browser delivery path. [OpenAI skills](https://learn.chatgpt.com/docs/build-skills) | Requires plugin distribution to browser users; bundled helper execution remains to be confirmed.            |
| ChatGPT desktop / Codex app experience  | Plugin or standalone skill | Plugin directory; standalone skills are also available through the desktop Skills experience. [OpenAI skills](https://learn.chatgpt.com/docs/build-skills) | Installation and file access depend on the selected desktop environment.                                    |
| Codex CLI / Claude Code / Local Harness | Standalone skill; plugin also an option | Installed under `~/.agents/skills/oae-metadata/` or repository `.agents/skills/oae-metadata/`. [Local skill discovery](https://learn.chatgpt.com/docs/build-skills) | Local helper dependencies may need installation; input and output files are managed in the local workspace. |

We should have one practical end-to-end check per supported environment, with helpers added where needed. Version tracking will be kept lightweight; migration infrastructure and exhaustive model/platform testing will be deferred until a later iteration.

## 3. Proposed order and existing issues

| Order | Task                                     | Intended outcome                                                                                                                                                                                               | Existing issue                                                                                                                                                                                |
|---|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1** | **Consolidate schema artifacts**         | `oae_data_protocol.validation.schema.json` and `oae_data_protocol.schema.json` will be reconciled into one generated protocol artifact.                                                                        | N/A                                                                                                                                                                                           |
| 2 | Establish examples and lightweight evals | 3-5 existing example metadata files (from OAE Data Commons launch), available inputs, expected facts, and coverage gaps will be inventoried and consolidated into an eval environment.                         | [#137 — Evals](https://github.com/submarine-mrv/oae-data-commons/issues/137)                                                                                                                  |
| 3 | Packaging workflow                       | The existing ad hoc process will be documented as repeatable OAE guidance. Claude marketplace packaging and the ZIP fallback will be generated with installation, use, and updates tested in the target hosts. | [#128 — Scaffold and packaging](https://github.com/submarine-mrv/oae-data-commons/issues/128), [#129 — Schema-aware extraction](https://github.com/submarine-mrv/oae-data-commons/issues/129) |
| 4 | Skill implementation                     | A draft will be generated and validation findings reported, with supported content preserved through researcher editing and re-export.                                                                         | [#135 — Generation and validation](https://github.com/submarine-mrv/oae-data-commons/issues/135), [#136 — Builder round trip](https://github.com/submarine-mrv/oae-data-commons/issues/136)   |
| 5 | Fill file-reading gaps                   | PDF/spreadsheet and NetCDF helpers will be added where needed.                                                                                                                                                 | [#133 — PDF/XLSX ingestion](https://github.com/submarine-mrv/oae-data-commons/issues/133), [#134 — NetCDF inspection](https://github.com/submarine-mrv/oae-data-commons/issues/134)           |
| 6 | Publish installation and usage guidance  | Marketplace setup, update behavior, ZIP fallback, supported inputs, limitations, and researcher review in Builder will be documented, and release packages completed.                                          | [#138 — Documentation](https://github.com/submarine-mrv/oae-data-commons/issues/138), [#128 — Packaging](https://github.com/submarine-mrv/oae-data-commons/issues/128)                        |

The first pilot needs a working file-to-Builder workflow. A full eval harness and every possible ingestion helper are not prerequisites.

## 4. Priority use cases

- **A.** As a researcher, I want to draft project and experiment metadata from documents.
- **B.** As a researcher, I want to draft dataset and variable metadata from tabular files.
- **C.** As a researcher, I want to port metadata embedded in a NetCDF file into a protocol compliant dataset metadata JSON file.
- **D.** As a researcher, I want to combine related sources into one coherent metadata draft.
- **E.** As a researcher, I want to review and edit the draft in Metadata Builder before publishing or sharing it.

| ID | Input data examples | Input data formats | Example request | Expected outcome |
|---|---|---|---|---|
| **A** | Project design document; sampling plan; methods description | PDF; text | “Use our project design document and sampling plan to start the metadata.” | Supported project and experiment details; missing information identified. |
| **B** | Bottle dataset; CTD observations; measurement metadata workbook | CSV; XLSX | “Create dataset and variable metadata for this bottle dataset.” | Variables match actual columns; units and methods retained where supported. |
| **C** | Gridded field observations; sensor time series | NetCDF (`.nc`) | “Use this NetCDF file to start the dataset metadata.” | Draft from dimensions and global/variable attributes; inspection limits identified. |
| **D** | Project design document plus bottle dataset, field notes, and instrument information | PDF; text; CSV; XLSX; NetCDF | “These files belong to the same field trial. Create one metadata draft.” | Correct project/experiment/dataset relationships; conflicts surfaced with source references. |
| **E** | N/A — draft already in progress | N/A — no new source files | “Give me the JSON so I can review and finish it in Metadata Builder.” | Downloadable JSON and handoff instructions; import/edit/export compatibility verified, including incomplete drafts and preservation of supported fields and relationships. |

**Across all cases:** uncertainty must be preserved, and scientific facts must not be invented. Importable, schema-valid, and scientifically reviewed describe different checks. Builder review precedes publication with a dataset and any optional sharing with Jacki.

## 5. Team decision: interview, report, or a combination?

The approach to handling gaps before researcher review in Metadata Builder remains to be decided. JSON remains the main artifact in every option.

| Approach | Researcher experience | Tradeoff |
|---|---|---|
| Q&A interview | Questions are answered before the draft is delivered or completed. | More gaps resolved in-session; more researcher time required. |
| Draft with report | JSON is delivered with a report of missing information, conflicts, and validation findings. | Faster handoff; more issues left for Builder review. |
| Hybrid | A few consequential questions are answered before JSON and remaining issues are delivered. | Requires agreement on which questions justify interruption. |

| Discussion question                            | Options / criteria |
|------------------------------------------------|---|
| Which approach should be the default?          | Interview, report, or hybrid. |
| Should researchers choose the approach?        | Fixed workflow or user-selectable mode. |
| What justifies needing an interview question? | Consequential ambiguities to resolve in-session versus gaps to flag for Builder review. |

## Appendix A. Lightweight evals

Here, **evals** means repeatable checks of the OAE skill’s behavior and metadata outputs. No model training or fine-tuning is proposed. The same workflow checks will be used when the skill is packaged as a plugin, with installation and update checks added for each supported host.

Initial evals will be based on the **3–5 existing examples**, with results reported case by case. Extraction quality and usability will be assessed; source accuracy cannot be established through schema validation alone. Concrete errors and regressions can be identified from this collection, but broad accuracy rates cannot be established. Repeated runs or many fields from one dataset do not add independent project coverage.

### Evaluation questions

| Dimension | Check |
|---|---|
| Skill activation | Explicit invocation works; where automatic selection is supported, relevant requests activate the skill and unrelated requests do not. |
| Plugin delivery | Installation and updates make the intended skill and schema assets available; any bundled helpers work in the target host. |
| Accuracy and evidence | Populated facts are supported by the inputs. |
| Coverage | Relevant available facts are captured; no credit is given for unsupported completeness. |
| Relationships and interpretation | Correct experiment links, variable types, units, and methods. |
| Uncertainty | Missing/conflicting evidence is flagged rather than guessed. |
| Builder handoff | Supported content survives import, researcher editing, and export. |
| Researcher effort | User can complete the workflow without a team-led session; corrections and useful questions are recorded. |
| Reliability | Selected cases are repeated, and each target host’s actual attachment-to-download workflow is checked. |

### Evaluation process

| Step | Small-scale approach |
|---|---|
| Inventory | Available sources, curated JSON, and schema versions will be listed, with uncovered use cases noted. Recovering old chat transcripts is optional. |
| Establish expectations | Curated JSON will be used as reference material, with equivalent descriptions accepted. Source-supported facts will be distinguished from information Jacki may have supplied during workshopping. |
| Compare | Schema-plus-documents and skill-assisted sessions will be run on the same available inputs, model, and host in separate fresh sessions. Errors and effort through Builder review will be compared separately from historical curated results. |
| Record | A short case/error/correction log will be maintained. Unresolved scientific judgments will be left open rather than assigned definitive grades. |
| Automate selectively | JSON, schema, reference, and Builder compatibility checks will be automated where useful; semantic review will initially be manual. No dedicated eval service or AI judge is required. |
| Iterate | Affected cases will be rerun, with model, host, skill, and schema versions recorded. Permission-cleared examples will be added when available, and synthetic cases labeled separately. |

**Interview/report comparison:** one or two examples will be worked through using the candidate approaches. Consequential errors, time to draft, question usefulness, and time to a reviewed Builder export will be compared. Any extra information supplied during interviews will be recorded. Findings will be treated as a usability comparison rather than a statistical experiment.

### Reading behind this approach

| Resource | Focus | Application to this plan |
|---|---|---|
| [Anthropic: Skill authoring best practices — evaluation and iteration](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#evaluation-and-iteration) | Skill development; start here | Three representative scenarios, a baseline without the skill, and minimal instructions refined against observed failures. Closely matches our starting scale. |
| [OpenAI: Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills) | Skill testing | Small checks for activation, workflow behavior, and output artifacts. The Codex automation example can inform later tooling; browser checks will still be needed. |
| [Anthropic: Improving skill-creator — test, measure, and refine Agent Skills](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills) | Optional skill authoring tool | Tests with prompts and files, skill/no-skill comparisons, and activation checks. Potential implementation aid; automated judging and benchmarking are optional for this plan. |
| [Awesome Agent Evals](https://github.com/benchflow-ai/awesome-evals) | Broad reference collection | Includes skill resources alongside product evals, benchmarks, and model-training/RL material. Useful for discovery; its training infrastructure and broad benchmarks are outside this project’s scope. |
| [Hamel Husain and Shreya Shankar’s evals guide](https://hamel.dev/blog/posts/evals-faq/) | Product evaluation background | Review actual outputs and turn observed failures into checks. Its larger sample sizes and recurring expert-review process are not requirements for our initial collection. |
| [Eugene Yan on the eval process](https://eugeneyan.com/writing/eval-process/) | Product evaluation background | Compare prompt/workflow changes against a baseline and inspect errors. Automated judges are discussed as a later scaling option. |
| [Anthropic’s agent eval guide](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Broader agent testing | Start from manual checks, inspect actual outcomes, and account for variation between runs. Large harnesses and simulated users are beyond our initial needs. |
