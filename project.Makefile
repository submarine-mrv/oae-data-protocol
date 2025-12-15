## Add Makefile targets here that are specific to oae-data-protocol

# Generate dynamic enums
ontologies/sea_names.ttl:
	rm -rf ontologies/sea_names.ttl
	curl 'https://vocab.nerc.ac.uk/collection/C16/current/' -H "Accept: text/turtle" > ontologies/sea_names.ttl

# Generate dynamic enums for platform types
ontologies/platform_types.ttl:
	rm -rf ontologies/platform_types.ttl
	curl 'https://vocab.nerc.ac.uk/collection/L06/current/' -H "Accept: text/turtle" > ontologies/platform_types.ttl

# Generate dynamic enums
ontologies/unit.ttl:
	rm -rf ontologies/unit.ttl
	curl 'https://qudt.org/3.1.7/vocab/unit' -H "Accept: text/turtle" > ontologies/unit.ttl

enums: ontologies/sea_names.ttl ontologies/unit.ttl ontologies/platform_types.ttl
	$(RUN) vskit expand -s src/oae_data_protocol/schema/dynamic_enums.yaml -o src/oae_data_protocol/schema/dynamic_enums_expanded.yaml --config vskit-config.yaml
