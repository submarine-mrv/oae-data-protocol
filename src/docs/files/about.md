# About the OAE Data Protocol

This documentation site provides technical schemas and data models for
Carbon To Sea's [OAE Data Management Protocol](http://carbontosea.org/oae-data-protocol/1-0-0/).


## What is this?

The OAE Data Protocol is a structured approach to collecting, documenting,
and sharing data from ocean alkalinity enhancement field trials and related
experiments. This repository contains machine-readable schema definitions
that support the
[OAE Data Protocol v1.0.0](http://carbontosea.org/oae-data-protocol/1-0-0/)
developed by [Carbon To Sea](https://carbontosea.org) in collaboration with [Submarine Scientific](https://submarine.earth), NOAA and the broader OAE research community.

## Built with LinkML

These schemas are defined using [LinkML](https://linkml.io) (Linked Data Modeling Language), a flexible framework for defining data models that can be used to:

- Generate JSON Schema for data validation
- Create Python data classes for programmatic access
- Produce documentation automatically
- Enable semantic web compatibility
- Support multiple serialization formats

LinkML makes it easy to maintain complex data models while keeping them interoperable with modern data tools and scientific workflows.

## Scope of These Schemas

The schemas defined in this repository primarily correspond to the metadata components of the OAE Data Protocol:

- **Project metadata** - Information about OAE field trials and initiatives
- **Experiment metadata** - Details about specific experiments and interventions within a project
- **Dataset metadata** - Metadata pertaining to specific datasets within a project or experiment
- **Model metadata** - Information about relevant computational models and simulations used within the context
of an OAE project

For protocol requirements pertaining to dataset formatting, column header names, and data file structure, please refer to the [published protocol documentation](http://carbontosea.org/oae-data-protocol/1-0-0/) on Carbon To Sea's website, which serves as the primary resource for dataset formatting requirements.

## Getting Started

Browse the schema documentation using the navigation menu to explore:

- **Classes**: Core data structures like `OAEProject`, `Experiment`, and `Dataset`
- **Enums**: Controlled vocabularies and valid value sets

This documentation serves primarily as a way to navigate and explore the data model of the various metadata used in the protocol.

Published schemas and artifacts can be found on GitHub:
- [JSON Schema](https://github.com/submarine-mrv/oae-data-protocol/blob/main/project/jsonschema/oae_data_protocol.schema.json)
- [Python Dataclasses](https://github.com/submarine-mrv/oae-data-protocol/blob/main/project/jsonschema/oae_data_protocol.schema.json)
- [LinkML Schema](https://github.com/submarine-mrv/oae-data-protocol/tree/main/src/oae_data_protocol/schema)

## Questions or Feedback?

This is an evolving project. If you have questions, find issues, or want to contribute, please visit the [GitHub repository](https://github.com/submarine-mrv/oae-data-protocol).

## Funding Acknowledgment

Development of the OAE Data Protocol and its corresponding technical tooling has been made possible with
funding and steering support from [Carbon To Sea](https://carbontosea.org).

