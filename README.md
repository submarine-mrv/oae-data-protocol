# OAE Data Protocol Schemas

Machine-readable schemas for the [OAE Data Management Protocol](https://www.carbontosea.org/oae-data-protocol/1-0-0/),
which sets out how to produce consistent data and metadata for Ocean Alkalinity Enhancement (OAE)
research. The schemas cover OAE projects, experiments, datasets and the variables inside them,
including instrument, analysis and calibration metadata.

📖 **Documentation: [schema.oaedata.org](https://schema.oaedata.org)**

To write a metadata file, use the [OAE Metadata Builder](https://metadata.oaedata.org). It walks
through each section and exports JSON that validates against these schemas. The Excel templates
from the protocol's v1.0 launch (August 25, 2025) are in [`templates/excel`](./templates/excel).

## Status and versioning

The schemas are pre-1.0 and still changing. Each release is tagged (`v0.5.0`) with notes on
[GitHub Releases](https://github.com/submarine-mrv/oae-data-protocol/releases). Until 1.0, a minor
version bump means a breaking change: metadata valid under the previous version may not validate.
The version is the `version` field of `oae_data_protocol.yaml` and of the generated JSON Schema.

## Generated artifacts

The schemas are written in [LinkML](https://linkml.io). Generated files are committed:

- `project/jsonschema/oae_data_protocol.schema.json`: JSON Schema, used by the Metadata Builder
- `project/jsonschema/oae_data_protocol.validation.schema.json`: JSON Schema for validating
  documents, which accepts every variable subclass where a variable is expected
- `project/typescript/`: TypeScript types
- `src/oae_data_protocol/datamodel/`: Pydantic models

## Repository layout

```
src/oae_data_protocol/schema/   LinkML schemas, the source of truth
src/oae_data_protocol/datamodel/ generated Pydantic models
src/docs/files/                 hand-written documentation pages
project/                        generated JSON Schema and TypeScript
templates/excel/                v1.0 protocol Excel templates
ontologies/                     vocabulary files for dynamic enums (NERC, QUDT)
tests/                          tests
```

`docs/` is built by `just gen-doc` and is not committed.

## Development

Requires [uv](https://docs.astral.sh/uv/) and [just](https://just.systems/).

```bash
git clone https://github.com/submarine-mrv/oae-data-protocol.git
cd oae-data-protocol
just install
just gen-all
```

| Command | What it does |
|---|---|
| `just gen-all` | Regenerate JSON Schema (both), TypeScript and Pydantic models |
| `just test` | Validate the schema and run the tests |
| `just lint` | LinkML lint |
| `just enums` | Expand dynamic enums from the NERC and QUDT vocabularies |
| `just testdoc` | Build the docs and serve them locally |
| `just` | List every command |

Edit the YAML in `src/oae_data_protocol/schema/`, run `just gen-all`, and commit the schema and
generated files together. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Credits

Built with [LinkML](https://linkml.io) and
[linkml-project-copier](https://github.com/linkml/linkml-project-copier). Developed by
[Submarine Scientific](https://www.submarine.earth), with funding and steering from
[Carbon to Sea](https://www.carbontosea.org). Questions: [data@carbontosea.org](mailto:data@carbontosea.org).

## License

[Apache 2.0](LICENSE)
