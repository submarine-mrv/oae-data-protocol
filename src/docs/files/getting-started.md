# Getting Started

## The OAE Data Protocol

The [OAE Data Management Protocol](https://www.carbontosea.org/oae-data-protocol/1-0-0/) is a set of guidelines for collecting, documenting, and sharing data from ocean alkalinity enhancement research. It covers:

- What metadata to include with your data submissions
- Recommended column header names for data files
- Controlled vocabularies for consistent terminology
- Guidelines for quality control documentation

!!! info "New to the OAE Data Protocol?"
    If you're new to the protocol and want to learn about its guidelines and recommendations before diving into the technical schema, start with the [protocol website](https://www.carbontosea.org/oae-data-protocol/1-0-0/) on Carbon To Sea. It includes the full narrative guidelines, [controlled vocabularies](https://www.carbontosea.org/oae-data-protocol/1-0-0/#controlled-vocabularies), and [recommended column header names](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name).

## The OAE Data Schema

This site is the technical reference for the protocol's machine-readable schema — the formal data model that defines how OAE metadata is structured, validated, and exchanged. Use it to:

- Understand the [variable class hierarchy](../variables/) and how to describe different measurement types
- Look up required fields for [experiments](../projects-experiments/), [datasets](../datasets/), and [instruments](../instruments-calibration/)
- Browse [controlled vocabularies](../vocabularies.md) used across the protocol
- Reference the [full schema index](../schema_index.md) for every class, slot, and enum

The schema generates [JSON Schema](https://github.com/submarine-mrv/oae-data-protocol/blob/main/project/jsonschema/oae_data_protocol.validation.schema.json) for validation, [Python dataclasses](https://github.com/submarine-mrv/oae-data-protocol/blob/main/src/oae_data_protocol/datamodel/oae_data_protocol.py) for programmatic access, and a [JSON-LD context](https://github.com/submarine-mrv/oae-data-protocol/blob/main/project/jsonld/context.jsonld) for linked data compatibility.

## Creating Metadata

The easiest way to create metadata is with the **[OAE Metadata Builder](https://metadata.oaedata.org)** — a web app that walks you through each section and exports a valid JSON file. See the [Metadata Builder](../metadata-builder.md) page for details.

## Working with Metadata Files

Metadata files are JSON documents that follow the [Container format](../metadata-format.md). You can:

- **Create** them using the Metadata Builder or programmatically
- **Validate** them against the [JSON Schema](https://github.com/submarine-mrv/oae-data-protocol/blob/main/project/jsonschema/oae_data_protocol.validation.schema.json)
- **Import** them back into the Metadata Builder for editing
- **Submit** them alongside your data files

See [Metadata File Format](../metadata-format.md) for the full specification.
