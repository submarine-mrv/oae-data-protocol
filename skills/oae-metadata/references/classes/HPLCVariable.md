# HPLCVariable

HPLC (High-Performance Liquid Chromatography) measured variable for pigment analysis. Always measured, not calculated.

Parent: DiscreteMeasuredVariable

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| hplc_lab | yes | no | string | The name of the lab where the HPLC analysis was run (e.g., 'NASA_GSFC' |
| analyzing_instrument | yes | no | [AnalyzingInstrument](AnalyzingInstrument.md) | Instrument used to analyze the water samples or measure the water body continuously. Instrument includes calibration information. |
| sampling_method | yes | no | string | Method used to collect samples. |
| analyzing_method | yes | no | string | Additional information describing how the sample was analyzed. DOIs provided as applicable. |
| observation_type | yes | no | enum: `profile`, `surface_underway`, `time_series`, `laboratory_experiments`, `mesocosm`, `field_experiments`, `natural_analogues`, `model_outputs` |  |
| sampling | yes | no | always `discrete` |  |
| sampling_instrument_type | yes | no | enum: `ctd_rosette`, `niskin_bottle`, `flow_through_system`, `flask_for_discrete_co2_measurement`, `biological_trawl`, `phytoplankton_net`, `zooplankton_net`, `edna_sampler`, `autonomous_sensor`, `other` |  |
| qc_steps_taken | yes | no | string | Describe what QC steps have been taken to improve the quality of the data (e.g., DOI, software and settings used, outlier removal, etc.). If quality control procedures are described in a separate document uploaded with the data, provide the name of the document here. |
| uncertainty | yes | no | string | It is recommended to provide uncertainty for each data point in the data file. Else provide a single value representative of the dataset. If uncertainty is provided as a variable, please list the column header name here. |
| uncertainty_definition | yes | no | string | A description of the uncertainties involved in this method. |
| missing_value_indicators | yes | no | string | The indicator used to represent missing values in the data file, e.g., -999, NaN, etc. |
| genesis | yes | no | always `measured` |  |
| units | yes | no | string | Unit of measurement for this variable. |
| variable_type | yes | no | always `hplc` | High-level classification of the variable. Determines which standard identifiers are available and, combined with genesis and sampling, which schema class to use. |
| schema_class | yes | no | always `HPLCVariable` | The schema class name for this variable (e.g., "DiscretePHVariable"). Auto-populated by the metadata builder. |
| dataset_variable_name | yes | no | string | The name for the variable as it is identified in the dataset data file. This could be the column header in a CSV or the variable name in a NetCDF file. Standard common recommended column header names can be found in protocol documentation [here](https://www.carbontosea.org/oae-data-protocol/1-0-0/#column-header-name). |
| long_name | yes | no | string | Full descriptive name of the variable. |
| hplc_lab_technician | no | no | string | Name and contact information for HPLC technician. |
| field_replicate_information | no | no | string | Repetition of sample collection and measurement, e.g., triplicate samples. |
| sampling_instrument_type_custom | no | no | string |  |
| qc_researcher | no | no | string | The name of the PI whose research team QCed this parameter. |
| qc_researcher_institution | no | no | string | The institution of the PI whose research team QCed this parameter. |
| dataset_variable_name_qc_flag | no | no | string | If applicable, the column header name used for the quality control flag corresponding to this variable. |
| dataset_variable_name_raw | no | no | string | If applicable, the column header name used for the raw data corresponding to this variable. |
| other_detailed_information | no | no | string | Any additional information about this variable. |
| method_reference | no | no | string | Citation for the method used. |
| measurement_researcher | no | no | [Person](Person.md) | The name of the PI whose research team measured or derived this parameter. |
| standard_identifier | no | no | [VocabularyItemReference](VocabularyItemReference.md) | A term from a community vocabulary that identifies this variable. CF standard names (NERC P07) are recommended. |
