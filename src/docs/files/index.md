# Schema Documentation

The [OAE Data Management Protocol](https://www.carbontosea.org/oae-data-protocol) outlines recommendations for
producing consistent data and metadata across Ocean Alkalinity Enhancement projects, developed by [Carbon To Sea](https://carbontosea.org) and [Submarine Scientific](https://submarine.earth) in collaboration with NOAA and the broader OAE community.

This site documents the machine-readable schema that turns those recommendations into metadata
software can validate and exchange: the classes, fields and controlled vocabularies for OAE field
trials, experiments and the data they produce.

## Schema Scope

- **[Project](projects-experiments/index.md)**: the overall field trial or modeling effort, with its
  leads, funding, site and coverage.
- **[Experiments](projects-experiments/index.md#experiments)**: baseline, intervention, tracer and
  model experiments, including dosing details.
- **[Datasets](Datasets/index.md)**: field datasets and model output datasets.
- **[Variables](Variables/index.md)**: each column in a dataset, with
  [instrument and calibration](instruments-calibration/index.md) details for measured variables.

For protocol requirements on general metadata management, Excel templates, dataset formatting and
column header names, see the [published protocol](https://www.carbontosea.org/oae-data-protocol).

### Published Artifacts & Resources

- [OAE Metadata Builder](https://metadata.oaedata.org): web app for creating and managing JSON metadata files
- [JSON Schema](https://github.com/submarine-mrv/oae-data-protocol/blob/main/project/jsonschema/oae_data_protocol.validation.schema.json): for validating metadata files
- [LinkML source schema](https://github.com/submarine-mrv/oae-data-protocol/tree/main/src/oae_data_protocol/schema): the source every other artifact and these docs are generated from
- [Pydantic models](https://github.com/submarine-mrv/oae-data-protocol/blob/main/src/oae_data_protocol/datamodel/oae_data_protocol_pydantic.py): for working with metadata in Python
- [JSON-LD context](https://schema.oaedata.org/context.jsonld): for reading metadata files as linked data

## Built with LinkML to support FAIR data practices

The OAE Data Protocol schema is defined using [LinkML](https://linkml.io), a 'linked-data modeling language' that allows
for data schemas to be authored as YAML files, integrating with external data standards and vocabularies, and output in
a variety of machine-readable formats such as JSON Schema, Python models and documentation.

One of the primary features of LinkML is the ability to support [RDF](https://www.w3.org/RDF/) &
[JSON-LD](https://json-ld.org) mappings and serialization for improved interoperability with existing data standards.
Where applicable, this project strives to align with existing scientific data standards (such as [science-on-schema.org](https://science-on-schema.org), or controlled vocabularies hosted on [NERC Vocabulary Server](http://vocab.nerc.ac.uk)).

As the OAE Data Protocol has been developed in close collaboration with NOAA and the OCADS team, several parts of this
schema (the Variable class and subclasses in particular) aim to align closely with [NOAA-PMEL's OAPMetadata](https://github.com/NOAA-PMEL/OAPMetadata) XSD schemas.

## Questions or Feedback?

Visit the [GitHub repository](https://github.com/submarine-mrv/oae-data-protocol) or contact [data@carbontosea.org](mailto:data@carbontosea.org).

---

*Development of the OAE Data Protocol has been made possible with funding and steering support from [Carbon To Sea](https://carbontosea.org).*
