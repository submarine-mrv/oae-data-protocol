# OAE Data Protocol Schemas

> ⚠️ **Alpha Software**: These schemas are under active development and may change
> without notice. We do not currently guarantee backwards compatibility between
> versions. Once the schemas stabilize, we will establish a formal release process
> with semantic versioning to support clients and integrators who need stability
> guarantees.

The [OAE Data Management Protocol](http://carbontosea.org/oae-data-protocol/1-0-0/) outlines recommendations
for producing consistent data and metadata for Ocean Alkalinity Enhancement (OAE) research projects.

This repository provides machine-readable schemas and data standards for the protocol. It focuses on formal specifications for metadata about OAE projects, experiments, datasets, and individual data variables within datasets themselves (including instrumet, analysis, and calibration metadata).

**Creating Metadata**: The easiest way to produce a valid metadata file is the [OAE Metadata Builder](https://metadata.oaedata.org) — a web app that walks you through each section and exports a JSON file validated against these schemas. Excel templates from the [v1.0 protocol launch](http://carbontosea.org/oae-data-protocol/1-0-0/) (August 25, 2025) remain available in [`templates/excel`](./templates/excel) and on the protocol website.

**Beta Testing**: Organizations and researchers interested in testing the software tooling under development should contact [data@carbontosea.org](mailto:data@carbontosea.org).

## What's Inside

This repository contains [LinkML](https://linkml.io) schema definitions that can generate:

- **JSON Schema** for data validation and form generation
- **Python dataclasses** for programmatic data handling
- **JSON-LD context** for linked-data interoperability
- **Documentation** (what you're reading now!)
- Support for multiple serialization formats (JSON, YAML, RDF, etc.)

## Documentation

📖 **[schema.oaedata.org](https://schema.oaedata.org)**

## Quick Start



### Using the Schemas

The generated schemas are available in the `project/` directory:

- `project/jsonschema/` - JSON Schema definitions (including `*.validation.schema.json` for runtime validation)
- `project/jsonld/context.jsonld` - JSON-LD context
- `src/oae_data_protocol/datamodel/` - Python dataclasses

## Repository Structure

```
├── src/
│   └── oae_data_protocol/
│       ├── schema/          # LinkML schema definitions (edit these!)
│       └── datamodel/       # Generated Python dataclasses
├── project/                 # Generated project files (don't edit)
├── examples/                # Example data files
├── tests/                   # Python tests
└── docs/                    # Generated documentation
```

## Development

### Installation

```bash
# Clone the repository
git clone https://github.com/submarine-mrv/oae-data-protocol.git
cd oae-data-protocol

# Install dependencies
make install

# Generate schema artifacts
make gen-project
```

### Common Commands

```bash
make help              # Show all available commands
make gen-schemas       # Regenerate Python, JSON Schema, validation schema, and JSON-LD context
make gen-project       # Regenerate Python dataclasses and base JSON Schema only
make test             # Run tests
make lint             # Lint LinkML schemas
make serve            # Build and serve documentation locally
```

### Working with Schemas

The schema files in `src/oae_data_protocol/schema/` are the source of truth. Edit these files and run `make gen-project` to regenerate all derived artifacts.

## Project Status 

**Current Status**: Alpha development

We're actively developing and refining these schemas based on real-world usage and community feedback.
Breaking changes may occur as we work toward a stable v1.0 release of these schemas which will have parity
with v1.0.0 of the protocol.

## Credits & Acknowledgments

This project is built with:
- [LinkML](https://linkml.io) for schema definitions
- [linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter) for project structure

Development of the OAE Data Protocol and its corresponding technical tooling has been made possible with 
funding and steering support from [Carbon To Sea](https://carbontosea.org).

## License

See [LICENSE](./LICENSE) for details.
