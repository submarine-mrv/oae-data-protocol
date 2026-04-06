# OAE Data Protocol Schema

Machine-readable schema definitions for the [OAE Data Management Protocol](https://www.carbontosea.org/oae-data-protocol/1-0-0/), developed by [Carbon To Sea](https://carbontosea.org) in collaboration with [Submarine Scientific](https://submarine.earth), NOAA, and the broader OAE research community.

!!! warning "Alpha Software"
    These schemas are under active development. We do not currently guarantee backwards compatibility between versions.

## What is this?

The OAE Data Protocol is a structured approach to collecting, documenting, and sharing data from ocean alkalinity enhancement field trials and related experiments. This site provides the technical schema documentation — browse the class hierarchy, controlled vocabularies, and field definitions that make up the protocol's metadata model.

## Schema Scope

- **Project** — OAE field trials, leads, permits, spatial/temporal coverage
- **Experiment** — Interventions, tracer studies, model experiments, dosing details
- **Dataset** — Field datasets, model output datasets, platform info
- **Variables** — Measured, calculated, and contextual variables with instrument and calibration metadata

For protocol requirements pertaining to general metadata management, excel metadata templates, dataset formatting, and
column header names, see the [published protocol](https://www.carbontosea.org/oae-data-protocol/1-0-0/).


### Published Artifacts & Resources
- [OAE Metadata Builder](https://github.com/submarine-mrv/oae-metadata-builder) — Web app for creating and managing JSON metadata files
- [JSON Schema](https://github.com/submarine-mrv/oae-data-protocol/blob/main/project/jsonschema/oae_data_protocol.schema.json) — Machine readable schemas used for validation
- [LinkML Source Schema](https://github.com/submarine-mrv/oae-data-protocol/tree/main/src/oae_data_protocol/schema) — The source of truth for generating all schema artifacts and documentation (contributors should only edit these files)
- [Python Dataclasses](https://github.com/submarine-mrv/oae-data-protocol/blob/main/src/oae_data_protocol/datamodel/oae_data_protocol.py) — For managing metadata directly in Python workflows (WIP)

## Built with LinkML to support FAIR data practices

The OAE Data Protocol schema is defined using [LinkML](https://linkml.io), a 'linked-data modeling language' that allows
for data schemas to be authored as YAML files, integrating with external data standards and vocabularies, and output in 
a variety of machine-readable formats such as JSON Schema, Python dataclasses, and documentation.

One of the primary features of LinkML is the ability to support [RDF](https://www.w3.org/RDF/) &
[JSON-LD](https://json-ld.org) mappings and serialization for improved interoperability with existing data standards.
Where applicable, this project strives to align with existing scientific data standards (such as [science-on-schema.org](https://science-on-schema.org), or controlled vocabularies hosted on [NERC Vocabulary Server](http://vocab.nerc.ac.uk)).

As the OAE Data Protocol has been developed in close collaboration with NOAA and the OCADS team, several parts of this
schema (the Variable class and subclasses in particular) aim to align closely with with [NOAA-PMEL's OAPMetadata](https://github.com/NOAA-PMEL/OAPMetadata) XSD schemas.

## Questions or Feedback?

Visit the [GitHub repository](https://github.com/submarine-mrv/oae-data-protocol) or contact [data@carbontosea.org](mailto:data@carbontosea.org).

---

*Development of the OAE Data Protocol has been made possible with funding and steering support from [Carbon To Sea](https://carbontosea.org).*

