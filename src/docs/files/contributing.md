# Contributing

The OAE Data Schema is open source and developed collaboratively. We welcome contributions from researchers, data managers, and organizations across the OAE community.

## How the Schema is Built

The schema is written in [LinkML](https://linkml.io) (Linked Data Modeling Language), a framework designed for scientific data standards. LinkML lets us maintain a single source of truth that generates JSON Schema, Python dataclasses, documentation, and linked data artifacts — all from the same set of YAML definitions.

The source code is on GitHub: **[submarine-mrv/oae-data-protocol](https://github.com/submarine-mrv/oae-data-protocol)**

## Getting Involved

There are several ways to contribute:

**File an issue** — If you find a bug, have a question about a field definition, or want to suggest a new feature, [open an issue on GitHub](https://github.com/submarine-mrv/oae-data-protocol/issues). Issues are the best way to start a focused conversation about a specific change.

**Suggest a vocabulary mapping** — If your community uses a controlled vocabulary, ontology, or data standard that you'd like the protocol to align with, let us know. We're always looking for opportunities to improve interoperability (see below).

**Join the conversation** — For broader discussions about the protocol's direction, or to get involved in future iterations, reach out to [data@carbontosea.org](mailto:data@carbontosea.org).

## Interoperability & Standards Alignment

The scientific data standards landscape is large and complex. No single schema can integrate with everything, so we focus our alignment efforts where they serve the OAE community's real-world needs — based on what data tooling, repositories, and standards researchers are already using.

Some projects and data standards initiatives that we actively seek alignment with are:

- **[NOAA OCADS / OAPMetadata](https://github.com/NOAA-PMEL/OAPMetadata)** — Our variable and instrument class hierarchy is modeled after NOAA-PMEL's OAPMetadata XSD schema, ensuring compatibility with the [Ocean Carbon and Acidification Data System](https://www.ncei.noaa.gov/products/ocean-carbon-acidification-data-system) at NCEI.
- **[NERC Vocabulary Server](https://vocab.nerc.ac.uk/)** — We use NERC SKOS vocabularies for sea names (C16), platform types (L06), instrument types (L05/L22), and standard variable identifiers (P01).
- **[CF Conventions](https://cfconventions.org/)** — For netCDF datasets, we encourage alignment with CF Standard Names and related conventions.
- **[science-on-schema.org](https://science-on-schema.org/)** — Many general purpose fields in our schema (Person, Place, Organization) map to Schema.org terms to support dataset discoverability through standardized web metadata.

If you work with a data standard, vocabulary, or ontology that you think the protocol should map to, we'd love to hear about it. Please [open an issue](https://github.com/submarine-mrv/oae-data-protocol/issues) describing the standard, how your community uses it, and where you see alignment opportunities — or reach out to [data@carbontosea.org](mailto:data@carbontosea.org).

## Development

To work with the schema locally:

```bash
git clone https://github.com/submarine-mrv/oae-data-protocol.git
cd oae-data-protocol
make install        # Install dependencies via Poetry
make gen-schemas    # Generate all schema artifacts
make test           # Run validation tests
make serve          # Preview documentation locally
```

See the [repository README](https://github.com/submarine-mrv/oae-data-protocol) for full development setup instructions.

---

*Development of the OAE Data Protocol and its corresponding technical tooling has been made possible with funding and steering support from [Carbon To Sea](https://carbontosea.org).*
