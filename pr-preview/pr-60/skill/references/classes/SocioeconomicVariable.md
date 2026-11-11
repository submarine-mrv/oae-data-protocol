# SocioeconomicVariable

Socioeconomic variable for social and economic data such as survey responses, ecosystem service valuations, or text analysis. A field variable: includes method_reference and measurement_researcher, but does NOT include QCFields, instrument details, or calibration.

Parent: InSituVariable

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| quantitative_or_qualitative | yes | no | enum: `quantitative`, `qualitative` | Whether this variable captures quantitative (numerical) or qualitative (categorical/textual) data. |
| genesis | yes | no | enum: `measured`, `calculated` |  |
| units | yes | no | string | Unit of measurement for this variable. |
| variable_type | yes | no | always `socioeconomic` | High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use. |
| schema_class | yes | no | always `SocioeconomicVariable` | The schema class name for this variable (e.g., "DiscretePHVariable"). Auto-populated by the metadata builder. |
| dataset_variable_name | yes | no | string | The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name). |
| long_name | yes | no | string | Full descriptive name of the variable. |
| social_study_type | no | no | enum: `public_perception_survey`, `ecosystem_service_valuation_survey`, `text_analysis`, `other` | The type of social science study this variable comes from. |
| social_study_type_custom | no | no | string | Custom study type description when "other" is selected. |
| social_study_site_characterization | no | no | string | Time period and location description for the social study (e.g., "2023-2024, coastal communities in Maine, USA"). |
| dataset_variable_name_qc_flag | no | no | string | If applicable, the column header name used for the quality control flag corresponding to this variable. |
| dataset_variable_name_raw | no | no | string | If applicable, the column header name used for the raw data corresponding to this variable. |
| other_detailed_information | no | no | string | Any additional information about this variable. |
| method_reference | no | no | string | Citation for the method used. |
| measurement_researcher | no | no | [Person](Person.md) | The name of the PI whose research team measured or derived this parameter. |
| standard_identifier | no | no | [VocabularyItemReference](VocabularyItemReference.md) | A term from a community vocabulary that identifies this variable. CF standard names (NERC P07) are recommended. |

## Vocabularies

What each value means, for the fields above.

### social_study_type

- `public_perception_survey`: Public perception survey
- `ecosystem_service_valuation_survey`: Ecosystem service valuation survey
- `text_analysis`: Text analysis
- `other`: Other study type
