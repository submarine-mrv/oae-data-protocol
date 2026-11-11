# OAE Data Protocol - Technical Documentation



URI: https://schema.oaedata.org/OAEDataSchema

Name: OAEDataSchema



## Classes

| Class | Description |
| --- | --- |
| [AnalyzingInstrument](AnalyzingInstrument.md) | Base class for scientific instruments used in analyzing samples for measurement. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CO2GasDetector](CO2GasDetector.md) | CO2 gas detector with standard gas calibration. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContinuousCO2GasDetector](ContinuousCO2GasDetector.md) | CO2 gas detector for continuous measurements, with measurement frequency. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CRMInstrument](CRMInstrument.md) | Instrument calibrated with Certified Reference Materials, used for DIC and TA measurements. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PHInstrument](PHInstrument.md) | pH measurement instrument with dye-based calibration. |
| [Any](Any.md) | None |
| [Calibration](Calibration.md) | Base calibration information for instruments. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CO2Calibration](CO2Calibration.md) | Base CO2 gas detector calibration with standard gas information. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContinuousCO2Calibration](ContinuousCO2Calibration.md) | CO2 calibration for continuous measurements, with extended standard gas details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiscreteCO2Calibration](DiscreteCO2Calibration.md) | CO2 calibration for discrete measurements, with calibration temperature. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CRMCalibration](CRMCalibration.md) | Calibration using Certified Reference Materials, used for DIC and TA instruments. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PHCalibration](PHCalibration.md) | pH instrument calibration. Use this class directly for TRIS or other standards, and DyeCalibration when standard_used is dye. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DyeCalibration](DyeCalibration.md) | pH instrument calibration with an indicator dye standard. |
| [CO2Equilibrator](CO2Equilibrator.md) | Equilibrator used for continuous CO2 measurement. |
| [Container](Container.md) | None |
| [Dataset](Dataset.md) | Abstract base class for all dataset types. Contains fields common to both field/observational and model simulation datasets. Generally following guidelines & best practices as outlined in [science-on-schema.org](https://github.com/ESIPFed/science-on-schema.org/blob/main/guides/Dataset.md) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FieldDataset](FieldDataset.md) | A field or observational dataset related to an OAE experiment. Contains fields specific to in-situ data collection such as platform information, calibration files, QC flags, and measured variables. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ModelOutputDataset](ModelOutputDataset.md) | A model simulation output dataset. Contains fields specific to computational model output including simulation configuration, output variables, and hardware information. |
| [DosingConcentration](DosingConcentration.md) | Details of tracer concentration information |
| [DosingDetails](DosingDetails.md) | An abstract class (used as a mixin, not implemented directly) for detailing the required fields that are specific to an Experiment with active dosing (e.g. type "Tracer", "Intervention", or "InterventionWithDosing") |
| [Experiment](Experiment.md) | Abstract base class for all experiment types. Contains fields common to both in-situ and model experiments. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[InSituExperiment](InSituExperiment.md) | Experiment metadata for in-situ studies (interventions, tracer studies, etc.). Contains fields specific to field-based experiments that don't apply to model experiments. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such as an alkalinity addition, was conducted. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention was conducted simultaneously alongside a tracer study, using the same instrumentation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Tracer](Tracer.md) | Additional metadata that applies to experiments where a tracer study was conducted |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Model](Model.md) | A computational model experiment related to OAE. |
| [ExternalProject](ExternalProject.md) | A research project that is not directly managed by the OAE project, but whose location is proximal to the OAE project and whose data may be relevant to understanding the context or impacts of OAE activities. |
| [GenericSensor](GenericSensor.md) | Generic sensor base class used in continuous CO2 measurements. Subclasses (e.g., TemperatureSensor, PressureSensor) specialize accuracy and precision units via slot_usage. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PressureSensor](PressureSensor.md) | Pressure sensor used in continuous CO2 measurements. Accuracy and precision are reported in hectopascals (hPa). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TemperatureSensor](TemperatureSensor.md) | Temperature sensor used in continuous CO2 measurements. Accuracy and precision are reported in degrees Celsius. |
| [GeoCoordinates](GeoCoordinates.md) | A geographic coordinate in decimal degrees. |
| [GeoShape](GeoShape.md) | The geographic shape of a place. A GeoShape can be described using several properties whose values are based on latitude/longitude pairs. Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points. (imported from schema.org) |
| [HardwareConfiguration](HardwareConfiguration.md) | Details about the computational hardware used to run a model simulation. |
| [InterventionDetails](InterventionDetails.md) | An abstract class (used as a mixin, not implemented directly) for detailing the required fields that are specific to an Experiment with type "Intervention" |
| [MarineAirMeasurement](MarineAirMeasurement.md) | Information about CO2 measurements in marine air. |
| [MeasuredCO2Fields](MeasuredCO2Fields.md) | Fields applied to all measured CO2 variable types (discrete and continuous) |
| [MeasuredDICFields](MeasuredDICFields.md) | Fields applied to all measured DIC variable types (discrete and continuous) |
| [MeasuredPHFields](MeasuredPHFields.md) | Fields applied to all measured pH variable types (discrete and continuous) |
| [MeasuredPhysiologicalFields](MeasuredPhysiologicalFields.md) | Fields applied to all measured physiological variable types (discrete and continuous). Captures biological subject identification and experimental design information for organism response field studies. |
| [MeasuredSedimentFields](MeasuredSedimentFields.md) | Fields applied to all measured sediment variable types (discrete and continuous) |
| [MeasuredTAFields](MeasuredTAFields.md) | Fields applied to all measured TA variable types (discrete and continuous) |
| [ModelComponent](ModelComponent.md) | A component of a model (e.g., physics, biogeochemistry/ecosystem). |
| [ModelGrid](ModelGrid.md) | Details about a model grid. Use multiple ModelGrid entries to describe nested or multi-grid configurations. |
| [ModelInputDetails](ModelInputDetails.md) | Details about input data sources used to drive the model. |
| [MonetaryGrant](MonetaryGrant.md) | None |
| [NamedLink](NamedLink.md) | A link to a resource with a name and URL. |
| [Organization](Organization.md) | None |
| [Permit](Permit.md) | A permit associated with the project. |
| [Person](Person.md) | Information about a researcher or investigator involved in the experiment. |
| [Place](Place.md) | A geospatial area of interest, defined by a bounding box, polygon/line, or a point designated as a pair of geo-coordinates. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DosingLocation](DosingLocation.md) | A specific location of dosing for an OAE intervention and/or tracer study. Can be a point, line, or bounding box |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SpatialCoverage](SpatialCoverage.md) | A bounding box defined by latitude and longitude coordinates. |
| [Platform](Platform.md) | None |
| [Project](Project.md) | A project conducting OAE field trials or modeling. |
| [PropertyValue](PropertyValue.md) | None |
| [PublicComment](PublicComment.md) | A public comment document associated with a consultation for this experiment. |
| [QCFields](QCFields.md) | Quality control fields applicable to measured and calculated variables. Not applied to socioeconomic variables. |
| [SamplePreservation](SamplePreservation.md) | Sample preservation information for DIC and TA measurements. Reference: OAPMetadata XSD variables.xsd - sample_preservation |
| [StandardGas](StandardGas.md) | Standard gas used for CO2 calibration. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContinuousStandardGas](ContinuousStandardGas.md) | Standard gas used for continuous CO2 calibration, with additional traceability and count information. |
| [TracerDetails](TracerDetails.md) | An abstract class (used as a mixin, not implemented directly) for detailing the required fields that are specific to an Experiment with type "Tracer" |
| [Variable](Variable.md) | Abstract root for all variable types (including non-measured) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FieldVariable](FieldVariable.md) | Abstract root for every variable that can appear in a FieldDataset — measured, calculated or contextual. Exists so FieldDataset.variables can range over exactly these classes: ranging over Variable would also admit ModelOutputVariable, which belongs only to a ModelOutputDataset. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[InSituVariable](InSituVariable.md) | Base class for project-acquired variables (measured or calculated in-situ). Reference: OAPMetadata XSD variables.xsd - insitu_variable |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CalculatedVariable](CalculatedVariable.md) | A variable that is calculated or derived from other measured variables rather than directly measured by an instrument (e.g., carbonate system parameters computed via CO2SYS). Set genesis to "calculated". The variable_type should reflect the quantity being calculated (e.g., "pH", "ta", "dic", "co2", or "other"). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeasuredVariable](MeasuredVariable.md) | Variable that is directly measured in-situ using instruments. Reference: OAPMetadata XSD variables.xsd - basic_measured_observation_base |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContinuousMeasuredVariable](ContinuousMeasuredVariable.md) | A variable measured in-situ by a continuous autonomous sensor (e.g., temperature, salinity, conductivity, pressure from a deployed sonde or underway system). Use this class for generic measured variables that do not fall under a specific category (pH, TA, DIC, CO2, sediment). For those, use the type-specific subclass instead (e.g., ContinuousPHVariable). Set variable_type to "other", genesis to "measured", and sampling to "continuous". |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContinuousCO2Variable](ContinuousCO2Variable.md) | CO2 continuous (sensor) measured variable (xCO2/pCO2/fCO2). Reference: OAPMetadata XSD variables.xsd - co2_continuous |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContinuousDICVariable](ContinuousDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from continuous autonomous sensor. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContinuousPHVariable](ContinuousPHVariable.md) | pH measured variable from continuous autonomous sensor |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContinuousPhysiologicalVariable](ContinuousPhysiologicalVariable.md) | Physiological response variable from continuous autonomous field sensors (e.g., respiration rates from deployed oxygen consumption monitors, heart rate from bio-loggers). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContinuousSedimentVariable](ContinuousSedimentVariable.md) | Measured sediment variable collected from continuous autonomous sensor |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContinuousTAVariable](ContinuousTAVariable.md) | Total Alkalinity (TA) measured variable from continuous autonomous sensor |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiscreteMeasuredVariable](DiscreteMeasuredVariable.md) | A variable measured in-situ from discrete water samples (e.g., bottle samples analyzed in a lab or shipboard). Use this class for generic measured variables that do not fall under a specific category (pH, TA, DIC, CO2, sediment, HPLC). For those, use the type-specific subclass instead (e.g., DiscretePHVariable). Set variable_type to "other", genesis to "measured", and sampling to "discrete". |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiscreteCO2Variable](DiscreteCO2Variable.md) | CO2 discrete (bottle) measured variable (pCO2/fCO2). Reference: OAPMetadata XSD variables.xsd - co2_discrete |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiscreteDICVariable](DiscreteDICVariable.md) | Dissolved Inorganic Carbon (DIC) measured variable from discrete bottle samples. Uses CRM-calibrated instrument and includes sample preservation information. Reference: OAPMetadata XSD variables.xsd - DIC_measured |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiscretePHVariable](DiscretePHVariable.md) | pH measured variable with dye-based spectrophotometric measurement. Reference: OAPMetadata XSD variables.xsd - pH_measured |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiscretePhysiologicalVariable](DiscretePhysiologicalVariable.md) | Physiological response variable from discrete field samples (e.g., organism growth rates, calcification rates, gene expression from bottle or tissue samples collected in the field). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiscreteSedimentVariable](DiscreteSedimentVariable.md) | Measured sediment variable collected from discrete bottle samples |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiscreteTAVariable](DiscreteTAVariable.md) | Total Alkalinity (TA) measured variable from discrete bottle samples |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HPLCVariable](HPLCVariable.md) | HPLC (High-Performance Liquid Chromatography) measured variable for pigment analysis. Always measured, not calculated. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SocioeconomicVariable](SocioeconomicVariable.md) | Socioeconomic variable for social and economic data such as survey responses, ecosystem service valuations, or text analysis. A field variable: includes method_reference and measurement_researcher, but does NOT include QCFields, instrument details, or calibration. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NonMeasuredVariable](NonMeasuredVariable.md) | A contextual or ancillary variable that is NOT directly measured or calculated by the project. Use for identifiers (Cruise_ID, Exp_ID), timestamps (Year_UTC, Time_UTC), coordinates (Latitude, Longitude), and any other data included in the dataset for context. Do NOT create a NonMeasuredVariable for quality control flag columns — instead, set dataset_variable_name_qc_flag on the parent measured or calculated variable that the flag relates to. variable_type must be "non_measured". |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ModelOutputVariable](ModelOutputVariable.md) | A variable output by a model simulation (e.g., air-sea CO2 flux, dissolved inorganic carbon, total alkalinity, pH, temperature, salinity from an OAE model run). Model outputs are produced by the simulation itself, so they carry none of the sampling, instrument, calibration or in-situ QC metadata that field-collected variables do — how the output was produced is described by the simulation configuration on the parent ModelOutputDataset. |
| [VerticalExtent](VerticalExtent.md) | The vertical extent of a place or structure in meters. |
| [VocabularyItemReference](VocabularyItemReference.md) | None |



## Slots

| Slot | Description |
| --- | --- |
| [accuracy](accuracy.md) | Accuracy of the instrument measurements |
| [additional_details](additional_details.md) | Open text area to include additional information |
| [affiliation](affiliation.md) | Institutional affiliation of the investigator |
| [agency_contact](agency_contact.md) | The point of contact at the permitting agency |
| [alkalinity_dosing_effluent_density](alkalinity_dosing_effluent_density.md) | Fixed density or provide link/source to effluent density data if applicable |
| [alkalinity_feedstock](alkalinity_feedstock.md) | Examples may include: olivine, potassium hydroxide, magnesium hydroxide, lime... |
| [alkalinity_feedstock_co2_removal_potential](alkalinity_feedstock_co2_removal_potential.md) | Maximum CO₂ removal potential of a feedstock material |
| [alkalinity_feedstock_custom](alkalinity_feedstock_custom.md) | Custom description of alkalinity feedstock when using a feedstock type not li... |
| [alkalinity_feedstock_description](alkalinity_feedstock_description.md) | Information such as feedstock source, characteristics, impurities, dilution p... |
| [alkalinity_feedstock_form](alkalinity_feedstock_form.md) | The phase upon delivery to the ocean |
| [alkalinity_feedstock_processing](alkalinity_feedstock_processing.md) | Method(s) used to process the alkalinity feedstock |
| [alkalinity_feedstock_processing_custom](alkalinity_feedstock_processing_custom.md) | Custom description of alkalinity feedstock processing method when 'other' is ... |
| [amount](amount.md) |  |
| [analyzing_instrument](analyzing_instrument.md) | Instrument used to analyze the water samples or measure the water body contin... |
| [analyzing_method](analyzing_method.md) | Additional information describing how the sample was analyzed |
| [appropriate_use_quality](appropriate_use_quality.md) | Climate quality is defined as measurements of quality sufficient to assess lo... |
| [approval_document](approval_document.md) | Filename(s), links and/or DOIs to access files of permitting documents, separ... |
| [arrangement](arrangement.md) | The grid arrangement of orthogonal physical quantities (e |
| [atmospheric_forcing](atmospheric_forcing.md) | Atmospheric forcing data source(s) |
| [atmospheric_pressure_sensor](atmospheric_pressure_sensor.md) | Atmospheric pressure sensor |
| [author_list_for_citation](author_list_for_citation.md) | Author list in the format of Lastname1, Firstname1 Middlename1; Lastname2, Fi... |
| [bathymetry](bathymetry.md) | Bathymetry data source(s) |
| [biological_subject](biological_subject.md) | Taxonomy (species, genus, or community) being studied (e |
| [blank_correction](blank_correction.md) | Whether the reported variables were corrected for blank, and if so, how they ... |
| [boundary_conditions](boundary_conditions.md) | Boundary condition data source(s) |
| [box](box.md) | A bounding box defined by two corner points — the southwest (lower-left) corn... |
| [calculation_method_and_parameters](calculation_method_and_parameters.md) | Information about how the variable was calculated and the parameters used in ... |
| [calculation_software_version](calculation_software_version.md) | Version of the software used to calculate reported values from raw values |
| [calibration](calibration.md) | Calibration information for this instrument |
| [calibration_certificates](calibration_certificates.md) | Information about calibration certificates |
| [calibration_files](calibration_files.md) | A list of supplementary file names containing coefficients and techniques use... |
| [calibration_location](calibration_location.md) | Factory calibration, lab calibration, or field calibration |
| [calibration_temperature](calibration_temperature.md) | Temperature at which calibration was performed |
| [changes_to_evolution_of_permit_criteria](changes_to_evolution_of_permit_criteria.md) | e |
| [codebase](codebase.md) | Link to model code repository |
| [colocated_operations](colocated_operations.md) | A description is required if any nearby operations exist that may influence t... |
| [comment_type](comment_type.md) | The kind of consultation these comments came from |
| [comments](comments.md) | Additional comments about the sensor |
| [concentration](concentration.md) | Concentrations of the CO2 standard gases that are used to calibrate the CO2 s... |
| [concentration_basis](concentration_basis.md) | Whether measurements are expressed per unit volume or per unit mass (for DIC,... |
| [correction_description](correction_description.md) | Description of how the preservative effect was corrected for |
| [correction_for_unpurified_dye](correction_for_unpurified_dye.md) | Correction method applied if dye was not purified |
| [country](country.md) | The country in which the organization belongs |
| [cpu_gpu_details](cpu_gpu_details.md) | Details about CPU/GPU hardware or link to specifications |
| [crm_batch_number](crm_batch_number.md) | Batch number of the Certified Reference Material |
| [crm_manufacturer](crm_manufacturer.md) | Manufacturer of the Certified Reference Material (e |
| [curve_fitting_method](curve_fitting_method.md) | Curve fitting method used to determine the alkalinity |
| [data_access_date](data_access_date.md) | The date by when this dataset will be openly available on a public repository |
| [data_access_link](data_access_link.md) | URL to access this dataset, if it is already archived or published elsewhere |
| [data_accessibility](data_accessibility.md) | Level of access to this dataset |
| [data_conflicts_and_unreported_data](data_conflicts_and_unreported_data.md) | If data exist that are or have been used by the project but are not provided ... |
| [data_product_type](data_product_type.md) | One of the three choices: (a) Originally collected dataset (e |
| [data_submitter](data_submitter.md) | Information about the individual submitting the dataset(s), including contact... |
| [dataset_type](dataset_type.md) | Selected controlled vocabularies for data types relevant to mCDR have been re... |
| [dataset_type_custom](dataset_type_custom.md) | Custom "data type" when an appropriate value is not found in the controlled v... |
| [dataset_variable_name](dataset_variable_name.md) | The name for the variable as it is identified in the dataset data file |
| [dataset_variable_name_qc_flag](dataset_variable_name_qc_flag.md) | If applicable, the column header name used for the quality control flag corre... |
| [dataset_variable_name_raw](dataset_variable_name_raw.md) | If applicable, the column header name used for the raw data corresponding to ... |
| [datasets](datasets.md) |  |
| [description](description.md) | A narrative description of the thing |
| [detector_type](detector_type.md) | Type of the CO2 gas detector (E |
| [dosing_delivery_type](dosing_delivery_type.md) | Type of dosing delivery method |
| [dosing_depth](dosing_depth.md) | Depth in meters |
| [dosing_description](dosing_description.md) | Please be descriptive |
| [dosing_dispersal_hydrologic_location](dosing_dispersal_hydrologic_location.md) | Descriptive dosing location |
| [dosing_location](dosing_location.md) | Provide latitude and longitude in decimal degrees |
| [dosing_location_file](dosing_location_file.md) | Exact filename, URL and/or DOI to access the location file |
| [dosing_regimen](dosing_regimen.md) | A human readable summary description of the dosing regimen / frequency |
| [drying_method](drying_method.md) | Method used to dry the gas stream for marine air measurements |
| [dye_correction_method](dye_correction_method.md) | Method used to correct for dye effects |
| [dye_purified](dye_purified.md) | Whether the dye has been purified |
| [email](email.md) | Contact email address |
| [end_date](end_date.md) |  |
| [end_datetime](end_datetime.md) | End date and time of experiment in UTC ISO-8601 |
| [equilibration](equilibration.md) | Whether the feedstock was pre-equilibrated or unequilibrated |
| [equilibrator](equilibrator.md) | Equilibrator used for CO2 measurement |
| [equilibrator_pressure_sensor](equilibrator_pressure_sensor.md) | Pressure sensor for the equilibrator |
| [equilibrator_temperature_sensor](equilibrator_temperature_sensor.md) | Temperature sensor for the equilibrator |
| [equilibrator_type](equilibrator_type.md) | Type of the equilibrator for the CO2 measurement |
| [experiment_id](experiment_id.md) | The experiment to which the data belong |
| [experiment_leads](experiment_leads.md) | Provide details for each experiment lead / principal investigator (PI) includ... |
| [experiment_types](experiment_types.md) | The type(s) of mCDR experiment conducted |
| [experiments](experiments.md) |  |
| [fair_use_data_request](fair_use_data_request.md) | A statement from the data producer regarding how this dataset should be used |
| [field_replicate_information](field_replicate_information.md) | Repetition of sample collection and measurement, e |
| [filenames](filenames.md) |  |
| [frequency](frequency.md) | How often the instrument was calibrated |
| [funder](funder.md) |  |
| [funding](funding.md) | Include the name of the funder, funder country, project title, project ID, an... |
| [genesis](genesis.md) |  |
| [geo](geo.md) | Entities that have a somewhat fixed, physical extension |
| [grid_details](grid_details.md) | Details about the model grid(s) |
| [grid_geometry](grid_geometry.md) | Descriptive structure of the grid (e |
| [grid_name](grid_name.md) | Name of the grid (e |
| [grid_type](grid_type.md) | Role of this grid in a nested or multi-grid configuration |
| [hardware_configuration](hardware_configuration.md) | Details about the computational hardware used for the simulation |
| [headspace_gas_flow_rate](headspace_gas_flow_rate.md) | Flow rate (in L/min) of the gas from the equilibrator to the CO2 analyzer |
| [headspace_volume](headspace_volume.md) | Volume (in mL) of headspace (water displaced in the flask plus volume of the ... |
| [horizontal_resolution_range](horizontal_resolution_range.md) | Description of horizontal resolution (e |
| [hplc_lab](hplc_lab.md) | The name of the lab where the HPLC analysis was run (e |
| [hplc_lab_technician](hplc_lab_technician.md) | Name and contact information for HPLC technician |
| [identifier](identifier.md) | A unique identifier for the thing |
| [identifier_type](identifier_type.md) | Type of Researcher ID (e |
| [initial_conditions](initial_conditions.md) | Initial condition data source(s) |
| [input_details](input_details.md) | Details about input data sources used to drive the model on this grid |
| [instrument_type](instrument_type.md) | Type of instrument used to analyze samples or measure continuously |
| [instrument_type_custom](instrument_type_custom.md) |  |
| [is_derived_value](is_derived_value.md) | Indicates that the field in question is a derived value as opposed to one mea... |
| [is_provided_as_a_file](is_provided_as_a_file.md) | Indicates that the field in question is provided as a file |
| [last_calibration_date](last_calibration_date.md) | Date and time of most recent calibration in UTC |
| [latitude](latitude.md) | Latitude in decimal degrees of a location |
| [license](license.md) | Link a Dataset to its license to document legal constraints by adding a schem... |
| [life_stage](life_stage.md) | Life stage of the organism at time of measurement |
| [life_stage_custom](life_stage_custom.md) | Custom life stage description when "other" is selected |
| [line](line.md) | A line is a point-to-point path consisting of two or more points |
| [location](location.md) | Location of the sensor |
| [location_and_height](location_and_height.md) | Location and height of the marine air intake |
| [long_name](long_name.md) | Full descriptive name of the variable |
| [longitude](longitude.md) | Longitude in decimal degrees of a location |
| [machine](machine.md) | Name of the machine or cluster (e |
| [manufacturer](manufacturer.md) | Manufacturer name of the instrument |
| [marine_air_measurement](marine_air_measurement.md) | Information about CO2 measurements in marine air |
| [max_depth_in_m](max_depth_in_m.md) | Maximum depth of observation in meters |
| [max_height_in_m](max_height_in_m.md) | Maximum height of observation (in meters) for above ground aerial coverage |
| [mcdr_forcing_description](mcdr_forcing_description.md) | Description of the mCDR forcing applied in the simulation (e |
| [mcdr_pathway](mcdr_pathway.md) | The Marine Carbon Dioxide Removal (MCDR) pathway being studied |
| [measured](measured.md) | Whether CO2 in marine air was measured |
| [measurement_frequency](measurement_frequency.md) | How often measurements are taken, e |
| [measurement_interval](measurement_interval.md) | How often marine air CO2 is measured, e |
| [measurement_researcher](measurement_researcher.md) | The name of the PI whose research team measured or derived this parameter |
| [measurement_temperature](measurement_temperature.md) | Temperature at which pH was measured |
| [memory](memory.md) | Memory available (e |
| [metadata_builder_git_hash](metadata_builder_git_hash.md) | Git commit hash of the metadata-builder UI |
| [meteorological_and_tidal_data](meteorological_and_tidal_data.md) | Include links to relevant open datasets if referenced in the experiment but n... |
| [method_reference](method_reference.md) | Citation or reference for the calibration method |
| [min_depth_in_m](min_depth_in_m.md) | Minimum depth of observation in meters |
| [min_height_in_m](min_height_in_m.md) | Minimum height of observation (in meters) for above ground aerial coverage |
| [missing_value_indicators](missing_value_indicators.md) | The indicator used to represent missing values in the data file, e |
| [model](model.md) | Model number or name of the instrument |
| [model_component_type](model_component_type.md) | The type of model component (physics, BGC/ecosystem, or other) |
| [model_component_type_custom](model_component_type_custom.md) |  |
| [model_components](model_components.md) | Components of the model (e |
| [model_configuration](model_configuration.md) | Links to model configuration files or documentation |
| [n_nodes](n_nodes.md) | Number of nodes in the grid (for unstructured grids) |
| [n_x](n_x.md) | Number of grid points in the x-direction |
| [n_y](n_y.md) | Number of grid points in the y-direction |
| [n_z](n_z.md) | Number of vertical coordinate levels |
| [name](name.md) | A human-readable name for the thing |
| [number_of_nonzero_standards](number_of_nonzero_standards.md) | How many non-zero gas standards were used for the calibration |
| [observation_type](observation_type.md) |  |
| [operating_system](operating_system.md) | Operating system used (e |
| [other_detailed_information](other_detailed_information.md) | Any additional information about this variable |
| [output_frequency](output_frequency.md) | Frequency of model output (e |
| [owner](owner.md) | Institution that owns the platform |
| [parallelization](parallelization.md) | Parallelization details (e |
| [pco2_reported_temperature](pco2_reported_temperature.md) | In Celsius |
| [permit_id](permit_id.md) | The unique identifier or number associated with this permit |
| [permit_type](permit_type.md) | The category of permit (E |
| [permits](permits.md) | Associated permit number(s) |
| [permitting_authority](permitting_authority.md) | The group that issued the permit |
| [ph_of_standards](ph_of_standards.md) | pH values of the calibration standards used |
| [ph_reported_temperature](ph_reported_temperature.md) | The input could be a constant temperature value, or something like, in-situ t... |
| [phone](phone.md) | Contact phone number |
| [physical_site_description](physical_site_description.md) | Provide information to help characterize the field site and provide context w... |
| [platform_id](platform_id.md) | Synonymous with glider ID, cruise ID |
| [platform_info](platform_info.md) |  |
| [platform_type](platform_type.md) | For Platform Type definitions, see: https://vocab |
| [precision](precision.md) | Precision of the instrument measurements |
| [preservative](preservative.md) | As described, e |
| [previous_or_ongoing_colocated_research](previous_or_ongoing_colocated_research.md) | This field is required for co-located operations that potentially impact the ... |
| [processing_code](processing_code.md) | If applicable, link to any code for processing of raw forcing and input data ... |
| [processing_of_input_data](processing_of_input_data.md) | Narrative description of any processing applied to input data before use in t... |
| [project](project.md) |  |
| [project_id](project_id.md) | The project to which the submitted data belong |
| [project_leads](project_leads.md) | Provide details for each project lead / principal investigator (PI) including... |
| [protocol_git_hash](protocol_git_hash.md) | Git commit hash of the oae-data-protocol |
| [public_comments](public_comments.md) | Public comment documents, each with a link or DOI and an optional description |
| [qc_flag_scheme](qc_flag_scheme.md) | Describe what the quality control flags stand for, e |
| [qc_researcher](qc_researcher.md) | The name of the PI whose research team QCed this parameter |
| [qc_researcher_institution](qc_researcher_institution.md) | The institution of the PI whose research team QCed this parameter |
| [qc_steps_taken](qc_steps_taken.md) | Describe what QC steps have been taken to improve the quality of the data (e |
| [quantitative_or_qualitative](quantitative_or_qualitative.md) | Whether this variable captures quantitative (numerical) or qualitative (categ... |
| [raw_data_calculation_method](raw_data_calculation_method.md) | The method used to calculate reported values from raw sensor data |
| [references](references.md) | Links or DOIs to any reference(s) relevant to the model components/developmen... |
| [region](region.md) | Region covered by the grid |
| [related_links](related_links.md) | Links to websites or documents related to the external research project |
| [resolution](resolution.md) | Resolution of the CO2 sensor |
| [river_sediment_flux_details](river_sediment_flux_details.md) | River and/or sediment flux data source(s) |
| [role](role.md) | Role of the investigator in the experiment (e |
| [sample_preservation](sample_preservation.md) | How the samples were preserved for analysis |
| [sampling](sampling.md) |  |
| [sampling_instrument_type](sampling_instrument_type.md) |  |
| [sampling_instrument_type_custom](sampling_instrument_type_custom.md) |  |
| [sampling_method](sampling_method.md) | Method used to collect samples |
| [schema_class](schema_class.md) | The schema class name for this variable (e |
| [sea_names](sea_names.md) | Names of the seas where the data collection takes place, See Controlled Vocab... |
| [seawater_intake_depth](seawater_intake_depth.md) | Water depth of the seawater intake |
| [seawater_intake_location](seawater_intake_location.md) | Whereabouts of the seawater intake |
| [seawater_volume](seawater_volume.md) | Volume (in mL) of seawater in the flask |
| [sediment_sampling_depth](sediment_sampling_depth.md) | Depth that sediment was collected below sediment surface |
| [sediment_sampling_water_depth](sediment_sampling_water_depth.md) | Water depth where sediment was collected |
| [sediment_type](sediment_type.md) | e |
| [serial_number](serial_number.md) | Serial number of the instrument |
| [simulation_type](simulation_type.md) | The type(s) of model simulation (e |
| [social_context_site_description](social_context_site_description.md) | Details may include: |
| [social_research_conducted_to_date](social_research_conducted_to_date.md) | A description of any social research conducted to date |
| [social_study_site_characterization](social_study_site_characterization.md) | Time period and location description for the social study (e |
| [social_study_type](social_study_type.md) | The type of social science study this variable comes from |
| [social_study_type_custom](social_study_type_custom.md) | Custom study type description when "other" is selected |
| [spatial_coverage](spatial_coverage.md) | Latitude/longitude bounds of project site (e |
| [species_identification_code](species_identification_code.md) | Species reference code from a taxonomic database (e |
| [spin_up_protocol](spin_up_protocol.md) | Description of the model spin-up process |
| [standard_gas_info](standard_gas_info.md) | Standard gases used for calibration |
| [standard_identifier](standard_identifier.md) | A term from a community vocabulary that identifies this variable |
| [standard_type_and_production](standard_type_and_production.md) | Details on the standard (e |
| [standard_used](standard_used.md) | Type of standard used to calibrate the pH measurement |
| [standard_used_custom](standard_used_custom.md) | Name of the standard used, when it is not in the list |
| [start_date](start_date.md) |  |
| [start_datetime](start_datetime.md) | Start date and time of experiment in UTC ISO-8601 |
| [storage](storage.md) | Storage available (e |
| [storage_method](storage_method.md) | How the samples were stored before the measurement |
| [taxonomic_code_system](taxonomic_code_system.md) | Which taxonomic code system the identification code refers to |
| [technique_description](technique_description.md) | Details of the calibration technique used |
| [temperature_correction_method](temperature_correction_method.md) | Method used to correct pH for temperature |
| [temporal_coverage](temporal_coverage.md) | Start date and end date (if known) of the project in ISO-8601 interval format... |
| [term](term.md) |  |
| [tidal_forcing](tidal_forcing.md) | Tidal forcing data source(s) |
| [time_period](time_period.md) | The time period during which the permit will be applicable, or expected durat... |
| [time_stepping_scheme](time_stepping_scheme.md) | Time-stepping method and time step used in the simulation |
| [titration_cell_type](titration_cell_type.md) | Whether the titration cell is open or closed |
| [titration_type](titration_type.md) | Type of the titration used to determine alkalinity |
| [traceability_to_wmo_standards](traceability_to_wmo_standards.md) | Information about traceability of standard gases to WMO standards |
| [tracer_concentration](tracer_concentration.md) | Fixed concentration or provide link/source to tracer concentration separately... |
| [tracer_details](tracer_details.md) | state the kind of tracer used (e |
| [tracer_form](tracer_form.md) | The form of tracer upon delivery to the ocean (e |
| [tracer_form_custom](tracer_form_custom.md) | If "other" was selected for Tracer Form, please specify the custom tracer for... |
| [uncertainty](uncertainty.md) | It is recommended to provide uncertainty for each data point in the data file |
| [uncertainty_definition](uncertainty_definition.md) | A description of the uncertainties involved in this method |
| [unit](unit.md) |  |
| [units](units.md) | Unit of measurement for this variable |
| [uri](uri.md) |  |
| [url](url.md) | The URL of the linked resource |
| [variable_type](variable_type.md) | High-level classification of the variable |
| [variables](variables.md) | The variables in this dataset, each with its own metadata |
| [vented](vented.md) | Is the equilibrator vented or not? |
| [version](version.md) | Version of the oae-data-protocol |
| [vertical_coordinate_type](vertical_coordinate_type.md) | The vertical grid coordinate type (e |
| [vertical_coverage](vertical_coverage.md) | Minimum and maximum depths of observation in meters |
| [vertical_resolution_range](vertical_resolution_range.md) | Description of vertical resolution (e |
| [volume](volume.md) | The total volume (in liters) of the CO2 equilibrator |
| [water_flow_rate](water_flow_rate.md) | Flow rate (in L/min) of the flow through seawater |
| [water_vapor_correction_method](water_vapor_correction_method.md) | How the water vapor pressure inside the equilibrator was determined |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AlkalinityFeedstockForm](AlkalinityFeedstockForm.md) | Physical form of the alkalinity feedstock upon ocean delivery |
| [AlkalinityFeedstockProcessing](AlkalinityFeedstockProcessing.md) | Methods used to process alkalinity feedstock |
| [AnalyzingInstrumentType](AnalyzingInstrumentType.md) |  |
| [AppropriateUseQuality](AppropriateUseQuality.md) |  |
| [CalibrationLocation](CalibrationLocation.md) | Where the calibration was performed |
| [ConcentrationBasis](ConcentrationBasis.md) | Whether concentration measurements are expressed per unit volume or per unit ... |
| [DataAccessibility](DataAccessibility.md) | Level of access to a dataset |
| [DataProductType](DataProductType.md) |  |
| [DatasetType](DatasetType.md) | Type of dataset being submitted |
| [DosingDeliveryType](DosingDeliveryType.md) | Types of dosing delivery methods |
| [EquilibrationStatus](EquilibrationStatus.md) | Equilibration status of the alkalinity feedstock |
| [ExperimentType](ExperimentType.md) | Types of mCDR experiments |
| [FeedstockType](FeedstockType.md) | Types of materials used for alkalinity addition, as sourced from NCEI's OCADS... |
| [GenesisType](GenesisType.md) |  |
| [GridType](GridType.md) | Type of grid in a multi-grid or nested model configuration |
| [HydrologicLocation](HydrologicLocation.md) | Hydrologic location types for dosing |
| [LifeStage](LifeStage.md) | Life stage of the biological subject |
| [MassConcentrationUnit](MassConcentrationUnit.md) |  |
| [MCDRPathway](MCDRPathway.md) | Type of marine Carbon Dioxide Removal (mCDR) pathways |
| [ModelComponentType](ModelComponentType.md) | Type of model component |
| [ModelVariableType](ModelVariableType.md) | Classification of a variable output by a model simulation |
| [ObservationType](ObservationType.md) |  |
| [PHCalibrationStandard](PHCalibrationStandard.md) | Standard used to calibrate a pH measurement |
| [PlatformType](PlatformType.md) |  |
| [PublicCommentType](PublicCommentType.md) |  |
| [QuantitativeQualitative](QuantitativeQualitative.md) | Whether the socioeconomic data is quantitative or qualitative |
| [ResearcherIDType](ResearcherIDType.md) |  |
| [SamplingInstrumentType](SamplingInstrumentType.md) |  |
| [SamplingType](SamplingType.md) |  |
| [SeaNames](SeaNames.md) |  |
| [SimulationType](SimulationType.md) | Type of model simulation dataset |
| [SocialStudyType](SocialStudyType.md) | Type of social study conducted |
| [TaxonomicCodeSystem](TaxonomicCodeSystem.md) | Taxonomic code system used for species identification |
| [TitrationCellType](TitrationCellType.md) |  |
| [TracerForm](TracerForm.md) | Forms of tracer used in tracer studies |
| [VariableType](VariableType.md) | High-level classification of the variable |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Doi](Doi.md) | A Digital Object Identifier (DOI) for a digital object such as a document, da... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
