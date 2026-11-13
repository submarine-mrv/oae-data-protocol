## Add your own just recipes here. This is imported by the main justfile.
##
## Overriding recipes from the root justfile by adding a recipe with the same
## name in this file is not possible until a known issue in just is fixed,
## https://github.com/casey/just/issues/2540

# Full OAE build. Kept as the documented entry point; CI's drift check calls it.
gen-all: gen-project
    @echo "✓ Full gen-all completed"

# Assemble the distributable oae-metadata skill (and a zip) from skills/, the docs and the schema.
build-skill out="dist/oae-metadata":
    uv run python scripts/build_skill.py --out {{out}}

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
