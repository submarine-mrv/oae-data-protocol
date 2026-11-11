# Reading OAPMetadata (OCADS) XML

OAPMetadata XML is what researchers submit to NOAA OCADS. Its root is `<oads_metadata>`. It is a good source for dataset and variable metadata and a thin one for project and experiment metadata.

One XML file usually describes a whole data package: several data files, with a `<variable>` for every column in any of them. Match variables to the file in scope by `datasetVarName` against that file's column headers. A name can appear more than once with a different `observationType`; pick the one that fits the file. Ignore variables with no matching column.

The mapping below was checked against XML schema version a0.2.2. Field names on the right are OAE fields; check each against the class's definition before using it.

## Package level

| XML | OAE | Notes |
|---|---|---|
| `title`, `abstract` | dataset `name`, `description` | They describe the package. Narrow them to the file in scope |
| `temporalExtents` | dataset `temporal_coverage` | Check against the data file's own time range; they can differ |
| `spatialExtents` | no dataset field | Use for a project's or experiment's `spatial_coverage` if those are in scope. The XML gives west, east, north and south as separate elements; a `box` is `"south west north east"` |
| `dataSubmitter` | dataset `data_submitter` | |
| `investigators`, `authors` | `author_list_for_citation`; project or experiment leads if in scope | |
| `platforms` | dataset `platform_info` | |
| `dataLicense`, `useLimitation` | `license`, `fair_use_data_request` | |
| `fundingInfo`, `researchProjects` | project fields, if a project is in scope | |
| `expocodes`, `cruiseIds` | no field | Mention in the description or the report |
| `references`, `supplementalInfo` | no field | Report under "Not used" unless a variable's method cites them |

## Variable level

| XML | OAE | Notes |
|---|---|---|
| `xsi:type` on `<variable>` | the variable class | `dic_variable_type`, `ta_variable_type`, `ph_variable_type`, `co2_autonomous`, `co2_discrete` point at the typed classes. No `xsi:type` means a generic class |
| `measuredOrCalculated` | `genesis`, and so the class | `CALCULATED` means CalculatedVariable even when the column looks like a sensor value |
| `observationType` | `observation_type`, and discrete vs continuous | "discrete samples" means a `Discrete…` class; a sensor record means `Continuous…` |
| `datasetVarName` | `dataset_variable_name` | Must equal the column header exactly |
| `fullName` | `long_name` | |
| `units` | `units` | |
| `uncertainty` | `uncertainty` | The XML rarely says what the number represents, so `uncertainty_definition` is usually a gap |
| `qcFlag/description` | dataset `qc_flag_scheme`; the flag column name goes in `dataset_variable_name_qc_flag` | A flag scheme is not a QC procedure. `qc_steps_taken` is usually a gap |
| `researcher` | `measurement_researcher` | |
| `methodReference` | `method_reference` | |
| `samplingInstrument` | `sampling_instrument_type` | Map to a listed value; otherwise `other` with `sampling_instrument_type_custom` |
| `analyzingInstrument` | `analyzing_instrument` (`manufacturer`, `model`, `instrument_type`) | Instrument `accuracy` is rarely stated; a measurement uncertainty is not an instrument accuracy |
| `detailedInfo` | `sampling_method`, `analyzing_method` | Split by content. If it describes only one, the other is a gap |
| `standardization` (`description`, `frequency`, `crm`) | the instrument's `calibration` | CRM manufacturer and batch number are required for DIC and TA and often missing |
| `poison` | `sample_preservation` | |
| `phScale`, `measurementTemperature`, `phReportTemperature`, `temperatureCorrectionMethod` | the pH class's matching fields | |
| `titrationType`, `cellType`, `curveFitting` | the TA class's matching fields | |
| `gasDetector`, `equilibrator`, `waterVaporCorrection`, `co2ReportTemperature`, `depthSeawaterIntake` | the CO2 class's matching fields | |

An XML element with no row here: look for a field with the same meaning in the class's definition. If there is none, list it in the report under "Not used".
