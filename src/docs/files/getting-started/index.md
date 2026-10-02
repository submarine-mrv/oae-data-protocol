# Getting Started

## New to the protocol?

Start with the [protocol website](https://www.carbontosea.org/oae-data-protocol) on Carbon To Sea.
It covers the guidelines behind this schema, including
[controlled vocabularies](https://www.carbontosea.org/oae-data-protocol#controlled-vocabularies) and
[recommended column header names](https://www.carbontosea.org/oae-data-protocol#column-header-names).

## Creating a metadata file

Use the **[OAE Metadata Builder](https://metadata.oaedata.org)**. It has a form for each part of the
schema and exports a JSON file that validates against it. See [Metadata Builder](../metadata-builder.md).

## Working with metadata files

A metadata file is a JSON document with one project, its experiments and its datasets. The
[Metadata File Format](../metadata-format.md) page covers its structure, a complete example and how to
validate a file. To work with files in code, use the
[JSON Schema](https://github.com/submarine-mrv/oae-data-protocol/blob/main/project/jsonschema/oae_data_protocol.validation.schema.json)
or the [Pydantic models](https://github.com/submarine-mrv/oae-data-protocol/blob/main/src/oae_data_protocol/datamodel/oae_data_protocol_pydantic.py).
