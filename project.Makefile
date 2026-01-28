## Add Makefile targets here that are specific to oae-data-protocol

# Generate dynamic enums
ontologies/sea_names.ttl:
	rm -rf ontologies/sea_names.ttl
	curl 'https://vocab.nerc.ac.uk/collection/C16/current/' -H "Accept: text/turtle" > ontologies/sea_names.ttl

# Generate dynamic enums for platform types
ontologies/platform_types.ttl:
	rm -rf ontologies/platform_types.ttl
	curl 'https://vocab.nerc.ac.uk/collection/L06/current/' -H "Accept: text/turtle" > ontologies/platform_types.ttl

# Generate dynamic enums for QUDT units
# Note: We append a triple declaring qudt:hasQuantityKind as an ObjectProperty
# because the QUDT unit.ttl uses this property but its definition lives in a separate
# schema file. vskit needs this declaration to properly traverse the ontology.
ontologies/unit.ttl:
	rm -rf ontologies/unit.ttl
	curl 'https://qudt.org/3.1.7/vocab/unit' -H "Accept: text/turtle" > ontologies/unit.ttl
	echo 'qudt:hasQuantityKind rdf:type owl:ObjectProperty .' >> ontologies/unit.ttl

enums: ontologies/sea_names.ttl ontologies/unit.ttl ontologies/platform_types.ttl
	$(RUN) vskit expand -s src/oae_data_protocol/schema/dynamic_enums.yaml -o src/oae_data_protocol/schema/dynamic_enums_expanded.yaml --config vskit-config.yaml
