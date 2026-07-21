## Add your own just recipes here. This is imported by the main justfile.
##
## Overriding recipes from the root justfile by adding a recipe with the same
## name in this file is not possible until a known issue in just is fixed,
## https://github.com/casey/just/issues/2540

# ---------- Custom validation JSON Schema ----------
# Generates a second JSON Schema alongside the standard gen-project output.
# Uses LinkML's JsonSchemaGenerator from Python (not the CLI) so we can pass
# include_range_class_descendants=True and not_closed=True — required for
# runtime validation of user-authored metadata that uses class polymorphism.
# Referenced from docs (metadata-format.md, getting-started) and README.
gen-validation-schema:
    @mkdir -p project/jsonschema
    uv run python -c "from linkml.generators.jsonschemagen import JsonSchemaGenerator; \
        gen = JsonSchemaGenerator('src/oae_data_protocol/schema/oae_data_protocol.yaml', \
            top_class='Container', include_range_class_descendants=True, \
            not_closed=True, title_from='title'); \
        print(gen.serialize())" \
        > project/jsonschema/oae_data_protocol.validation.schema.json
    @echo "✓ Generated validation schema (with range class descendants)"

# Post-processing step: inject version metadata into generated artifacts.
inject-version:
    uv run python scripts/inject_version_metadata.py

# Convenience wrapper: run the upstream gen-project, then our custom steps.
# Call this instead of bare `just gen-project` when you want the full OAE build.
gen-all: gen-project gen-validation-schema inject-version
    @echo "✓ Full gen-all completed"

# ---------- Dynamic enum pipeline (NERC + QUDT) ----------

fetch-sea-names:
    @mkdir -p ontologies
    rm -f ontologies/sea_names.ttl
    curl 'https://vocab.nerc.ac.uk/collection/C16/current/' -H "Accept: text/turtle" > ontologies/sea_names.ttl

fetch-platform-types:
    @mkdir -p ontologies
    rm -f ontologies/platform_types.ttl
    curl 'https://vocab.nerc.ac.uk/collection/L06/current/' -H "Accept: text/turtle" > ontologies/platform_types.ttl

# QUDT's unit.ttl omits an rdf:type declaration for qudt:hasQuantityKind, so
# vskit/oaklib can't resolve it as an ObjectProperty when expanding the unit
# enum. We append the missing declaration to the fetched file.
fetch-qudt-units:
    @mkdir -p ontologies
    rm -f ontologies/unit.ttl
    curl 'https://qudt.org/3.1.7/vocab/unit' -H "Accept: text/turtle" > ontologies/unit.ttl
    echo 'qudt:hasQuantityKind rdf:type owl:ObjectProperty .' >> ontologies/unit.ttl

fetch-vocabularies: fetch-sea-names fetch-platform-types fetch-qudt-units

# Expand dynamic enums from external vocabularies via vskit (installed by oaklib).
enums:
    uv run vskit expand \
        -s src/oae_data_protocol/schema/dynamic_enums.yaml \
        -o src/oae_data_protocol/schema/dynamic_enums_expanded.yaml \
        --config vskit-config.yaml
