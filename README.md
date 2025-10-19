# OAE Data Protocol Schemas

> ⚠️ **Alpha Software**: These schemas are under active development and may change
> without notice. We do not currently guarantee backwards compatibility between
> versions. Once the schemas stabilize, we will establish a formal release process
> with semantic versioning to support clients and integrators who need stability
> guarantees.

The [OAE Data Management Protocol](http://carbontosea.org/oae-data-protocol/1-0-0/) outlines recommendations
for producing consistent data and metadata for Ocean Alkalinity Enhancement (OAE) research projects.

This repository provides machine-readable schemas and data standards for the protocol. It focuses on formal specifications for metadata about OAE projects, experiments, and datasets—not the individual data variables within datasets themselves.

**For Protocol Compliance**: As of the v1.0 protocol launch (August 25, 2025), projects seeking to comply with the protocol guidelines should use the Excel templates available on the [protocol website](http://carbontosea.org/oae-data-protocol/1-0-0/). These templates are also available in the [`templates/excel`](./templates/excel) directory of this repository.

**Beta Testing**: Organizations and researchers interested in testing the software tooling under development in this repository should contact [jacki@submarine.earth](mailto:jacki@submarine.earth).

## What's Inside

This repository contains [LinkML](https://linkml.io) schema definitions that can generate:

- **JSON Schema** for data validation and form generation
- **Python dataclasses** for programmatic data handling
- **Documentation** (what you're reading now!)
- Support for multiple serialization formats (JSON, YAML, RDF, etc.)

## Documentation

📖 **[View the schema documentation](https://submarine-mrv.github.io/oae-data-protocol)**

## Quick Start



### Using the Schemas

The generated schemas are available in the `project/` directory:

- `project/jsonschema/` - JSON Schema definitions
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
make gen-project       # Regenerate schemas and Python code
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