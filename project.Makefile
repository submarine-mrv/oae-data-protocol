## Add Makefile targets here that are specific to oae-data-protocol

# Generate dynamic enums
ontologies/sea_names.ttl:
	rm -rf ontologies/sea_names.ttl
	curl 'https://vocab.nerc.ac.uk/collection/C16/current/' -H "Accept: text/turtle" > ontologies/sea_names.ttl

enums: ontologies/sea_names.ttl
	vskit expand -s src/oae_data_protocol/schema/dynamic_enums.yaml -o src/oae_data_protocol/schema/dynamic_enums_expanded.yaml --config vskit-config.yaml