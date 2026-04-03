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

For protocol requirements pertaining to dataset formatting, column header names, and data file structure, see the [published protocol](https://www.carbontosea.org/oae-data-protocol/1-0-0/).

## Getting Started

Use the navigation menu to explore:

- **Classes** — Core data structures organized by domain
- **Enumerations** — Controlled vocabularies and valid value sets
- **Schema Reference** — Complete auto-generated index of all classes, slots, and enums

### Published Artifacts

- [JSON Schema (validation)](https://github.com/submarine-mrv/oae-data-protocol/blob/main/project/jsonschema/oae_data_protocol.validation.schema.json)
- [JSON-LD Context](https://github.com/submarine-mrv/oae-data-protocol/blob/main/project/jsonld/context.jsonld)
- [Python Dataclasses](https://github.com/submarine-mrv/oae-data-protocol/blob/main/src/oae_data_protocol/datamodel/oae_data_protocol.py)
- [LinkML Source Schemas](https://github.com/submarine-mrv/oae-data-protocol/tree/main/src/oae_data_protocol/schema)
- [OAE Metadata Builder](https://metadata.oaedata.org) — Web app for creating metadata

## Built with LinkML

Schemas are defined using [LinkML](https://linkml.io), generating JSON Schema, Python dataclasses, and documentation from a single source. Variable class hierarchy is aligned with [NOAA-PMEL's OAPMetadata](https://github.com/NOAA-PMEL/OAPMetadata) XSD schema.

## Questions or Feedback?

Visit the [GitHub repository](https://github.com/submarine-mrv/oae-data-protocol) or contact [data@carbontosea.org](mailto:data@carbontosea.org).

---

*Development of the OAE Data Protocol has been made possible with funding and steering support from [Carbon To Sea](https://carbontosea.org).*

