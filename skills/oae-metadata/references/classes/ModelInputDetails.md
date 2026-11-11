# ModelInputDetails

Details about input data sources used to drive the model.

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| bathymetry | no | yes | [NamedLink](NamedLink.md) | Bathymetry data source(s). |
| initial_conditions | no | yes | [NamedLink](NamedLink.md) | Initial condition data source(s). |
| boundary_conditions | no | yes | [NamedLink](NamedLink.md) | Boundary condition data source(s). |
| atmospheric_forcing | no | yes | [NamedLink](NamedLink.md) | Atmospheric forcing data source(s). |
| tidal_forcing | no | yes | [NamedLink](NamedLink.md) | Tidal forcing data source(s). |
| river_sediment_flux_details | no | yes | [NamedLink](NamedLink.md) | River and/or sediment flux data source(s). |
| processing_of_input_data | no | no | string | Narrative description of any processing applied to input data before use in the model. |
| processing_code | no | yes | [NamedLink](NamedLink.md) | If applicable, link to any code for processing of raw forcing and input data listed in the fields above. |
