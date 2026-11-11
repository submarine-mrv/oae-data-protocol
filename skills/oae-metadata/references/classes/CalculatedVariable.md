# CalculatedVariable

A variable that is calculated or derived from other measured variables rather than directly measured by an instrument (e.g., carbonate system parameters computed via CO2SYS). Set genesis to "calculated". The variable_type should reflect the quantity being calculated (e.g., "pH", "ta", "dic", "co2", or "other").

Parent: InSituVariable

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| calculation_method_and_parameters | yes | no | string | Information about how the variable was calculated and the parameters used in calculation, e.g.: Calculation software = CO2SYSv1 (MATLAB) Input variables = pH and DIC (column header names 'ph_t_insitu' and 'dic' in associated dataset file) Additional information = the dissociation constants of Lueker et al., 2000 for carbonic acid, etc. |
| genesis | yes | no | always `calculated` |  |
| units | yes | no | string | Unit of measurement for this variable. |
| variable_type | yes | no | enum: `pH`, `ta`, `dic`, `co2`, `sediment`, `hplc`, `physiological`, `socioeconomic`, `other`, `non_measured` | High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use. |
| schema_class | yes | no | always `CalculatedVariable` | The schema class name for this variable (e.g., "DiscretePHVariable"). Auto-populated by the metadata builder. |
| dataset_variable_name | yes | no | string | The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name). |
| long_name | yes | no | string | Full descriptive name of the variable. |
| qc_steps_taken | no | no | string | Describe what QC steps have been taken to improve the quality of the data (e.g., DOI, software and settings used, outlier removal, etc.). If quality control procedures are described in a separate document uploaded with the data, provide the name of the document here. |
| uncertainty | no | no | string | It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset. If uncertainty is provided as a variable, please list the column header name here. |
| uncertainty_definition | no | no | string | A description of the uncertainties involved in this method. |
| missing_value_indicators | no | no | string | The indicator used to represent missing values in the data file, e.g., -999, NaN, etc. |
| qc_researcher | no | no | string | The name of the PI whose research team QCed this parameter. |
| qc_researcher_institution | no | no | string | The institution of the PI whose research team QCed this parameter. |
| dataset_variable_name_qc_flag | no | no | string | If applicable, the column header name used for the quality control flag corresponding to this variable. |
| dataset_variable_name_raw | no | no | string | If applicable, the column header name used for the raw data corresponding to this variable. |
| other_detailed_information | no | no | string | Any additional information about this variable. |
| method_reference | no | no | string | Citation for the method used. |
| measurement_researcher | no | no | [Person](Person.md) | The name of the PI whose research team measured or derived this parameter. |
| standard_identifier | no | no | [VocabularyItemReference](VocabularyItemReference.md) | A term from a community vocabulary that identifies this variable. CF standard names (NERC P07) are recommended. |
