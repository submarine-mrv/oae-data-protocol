# AGENTS.md

This file provides guidance to AI coding agents working in this repository.

## Project Overview

This is a LinkML-based project for defining data schemas and ontologies for Ocean Alkalinity Enhancement (OAE) projects, experiments, and field trials. It serves as a technical complement to Submarine Scientific's OAE Data Protocol, developed in conjunction with Carbon To Sea and NOAA.

## Common Commands

The project uses `uv` for dependency management and `just` as the task runner:

### Essential Commands
- `just` - List all available tasks
- `just setup` - Initial project setup (run this first)
- `just install` - Install dependencies via uv
- `just site` - Build all project artifacts
- `just test` - Run all tests (schema validation, Python tests, examples)
- `just lint` - Perform LinkML schema linting
- `uv run python -m pytest` - Run Python tests directly

### Schema Generation
- `just gen-project` - Generate Pydantic model + JSON Schema + TypeScript from LinkML schema
- `just gen-all` - gen-project + gen-validation-schema (full OAE build)
- `just gen-validation-schema` - Generate validation JSON Schema with include_range_class_descendants

### Documentation
- `just gen-doc` - Generate documentation (gen-doc + overlay hand-written pages from src/docs/files/)
- `just testdoc` - Build docs and run local test server
- `just deploy` - Deploy site to GitHub Pages
- `just clean` - Clean generated files

### Dynamic Enums
- `just enums` - Expand dynamic enum definitions from external vocabularies
- `just fetch-vocabularies` - Fetch NERC (C16/L06) and QUDT TTL files into ontologies/
- Uses vskit (bundled with oaklib) to expand dynamic enums

### Template Management
- `copier update --trust` - Pull upstream template improvements from linkml-project-copier

## Architecture

### Schema Structure

The project uses LinkML (Linked Data Modeling Language) with a modular schema architecture:

**Core Schema Files** (src/oae_data_protocol/schema/):
- `oae_data_protocol.yaml` - Main schema file that imports all modules
- `core.yaml` - Fundamental slots and base classes (Any, PropertyValue)
- `oae_project.yaml` - Main OAEProject class with project metadata
- `enums.yaml` - Static enumerations for experiment types, MCDR pathways, etc.
- `dynamic_enums.yaml` / `dynamic_enums_expanded.yaml` - Dynamically generated enums from external vocabularies

**Additional Schema Modules**:
- `experiment.yaml`, `intervention.yaml`, `measurement.yaml` - Domain-specific classes
- `dataset.yaml`, `model_simulation.yaml` - Data and modeling components

### Key Configuration

- `config.public.mk` - Environment variables (schema name, paths) loaded by justfile
- `config.yaml` - LinkML generator configuration (includes: jsonschema)
- `pyproject.toml` - Python package configuration using hatchling + uv
- `vskit-config.yaml` - Configuration for vocabulary expansion
- `project.justfile` - Custom justfile recipes (gen-validation-schema, enums)
- `.copier-answers.yml` - Template answers for copier update

### Generated Artifacts

- `src/oae_data_protocol/datamodel/` - Generated Pydantic model from LinkML schemas
- `project/` - Generated project files (JSON Schema, TypeScript)
- `project/jsonschema/oae_data_protocol.schema.json` - Main JSON Schema (consumed by oae-form)
- `project/jsonschema/oae_data_protocol.validation.schema.json` - Validation schema with polymorphism support
- `docs/` - Generated documentation site (gitignored; rebuilt by `just gen-doc`)

### Documentation Layout

- `src/docs/files/` - Hand-written explainer pages (tracked in git, source of truth)
- `docs/` - Fully generated at build time (gitignored). `just gen-doc` writes LinkML class/slot pages flat into `docs/`, renames the generated index to `OAEDataSchema.md`, then overlays `src/docs/files/*`.
- Published at https://schema.oaedata.org

### Data Flow

1. LinkML schemas define the data model structure
2. `just gen-project` generates the Pydantic model + JSON Schema + TypeScript
3. `just gen-validation-schema` generates validation schema with `include_range_class_descendants=True`
4. External vocabularies are fetched and expanded into dynamic enums
5. Examples validate against the schema
6. Documentation is generated from schema annotations + hand-written pages

Versioning: the schema's semantic version is declared as `version:` in
`oae_data_protocol.yaml` and flows into the JSON Schema as the root `version`
field (consumed by oae-form). The Python package version is separate and derived
from git tags via uv-dynamic-versioning. There is no committed VERSION file and
no version-injection step; bump `version:` in the schema and tag the release.

## Development Workflow

1. Edit LinkML schemas in `src/oae_data_protocol/schema/`
2. Run `just gen-project` (or `just gen-all` for full build) to regenerate artifacts
3. Run `just test` to validate schemas and examples
4. Run `just lint` to check schema quality
5. Use `just gen-doc` to preview documentation changes
6. Run `just testdoc` to test documentation locally

The project follows LinkML conventions with semantic mappings to schema.org and domain-specific vocabularies for oceanographic research.

## Workflow Guidelines

### Commits
- Don't commit unless explicitly asked
- Review the diff and run linting/tests before committing
- When asked to commit: stage specific files, write clear messages, push only if asked

### Planning
- Plan before schema changes, multi-file refactors, and architectural decisions
- Proceed directly for small fixes and single-file changes

### Beads Issue Tracking

This project uses `bd` (beads) in **stealth mode** for issue tracking — the `.beads/` directory is local-only and not committed to git.

**When to use beads:**
- Check `bd ready` at session start if no specific task is given
- Update issue status when starting/completing tracked work
- Create beads issues for discovered work that spans sessions or has dependencies
- Prefix agent-created suggestions with "[agent suggestion]" in issue titles

**When NOT to use beads:**
- Trivial single-session tasks — use a lightweight in-session task list instead
- Work that will be completed in the current session

**Essential commands:**
```bash
bd ready                           # Show unblocked work
bd list --status=open              # All open issues
bd update <id> --status in_progress  # Claim work
bd close <id>                      # Complete work
bd create "Title" -d "Description" # New issue
```
