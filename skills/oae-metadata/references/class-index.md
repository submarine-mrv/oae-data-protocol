# Classes

Every class a metadata file can use. Each is defined in `assets/oae_data_protocol.schema.json` under
`$defs`, with its fields (`properties`), which are `required`, and its conditional rules (`if`/`then`).

## Project

| Class | Parent | What it is |
|---|---|---|
| Container |  |  |
| Project |  | A project conducting OAE field trials or modeling. |

## Experiments

| Class | Parent | What it is |
|---|---|---|
| Experiment |  | Abstract base class for all experiment types. |
| InSituExperiment | Experiment | Experiment metadata for in-situ studies (interventions, tracer studies, etc.). |
| Intervention | InSituExperiment | Additional metadata that applies to experiments where an intervention, such as an alkalinity addition, was conducted. |
| InterventionWithTracer | Intervention | Additional metadata that applies to hybrid experiments where an intervention was conducted simultaneously alongside a tracer study, using the same instrumentation. |
| Model | Experiment | A computational model experiment related to OAE. |
| Tracer | InSituExperiment | Additional metadata that applies to experiments where a tracer study was conducted |

## Datasets

| Class | Parent | What it is |
|---|---|---|
| Dataset |  | Abstract base class for all dataset types. |
| FieldDataset | Dataset | A field or observational dataset related to an OAE experiment. |
| ModelOutputDataset | Dataset | A model simulation output dataset. |

## Variables

| Class | Parent | What it is |
|---|---|---|
| CalculatedVariable | InSituVariable | A variable that is calculated or derived from other measured variables rather than directly measured by an instrument (e.g., carbonate system parameters computed via CO2SYS). |
| ContinuousCO2Variable | ContinuousMeasuredVariable | CO2 continuous (sensor) measured variable (xCO2/pCO2/fCO2). |
| ContinuousDICVariable | ContinuousMeasuredVariable | Dissolved Inorganic Carbon (DIC) measured variable from continuous autonomous sensor. |
| ContinuousMeasuredVariable | MeasuredVariable | A variable measured in-situ by a continuous autonomous sensor (e.g., temperature, salinity, conductivity, pressure from a deployed sonde or underway system). |
| ContinuousPHVariable | ContinuousMeasuredVariable | pH measured variable from continuous autonomous sensor |
| ContinuousPhysiologicalVariable | ContinuousMeasuredVariable | Physiological response variable from continuous autonomous field sensors (e.g., respiration rates from deployed oxygen consumption monitors, heart rate from bio-loggers). |
| ContinuousSedimentVariable | ContinuousMeasuredVariable | Measured sediment variable collected from continuous autonomous sensor |
| ContinuousTAVariable | ContinuousMeasuredVariable | Total Alkalinity (TA) measured variable from continuous autonomous sensor |
| DiscreteCO2Variable | DiscreteMeasuredVariable | CO2 discrete (bottle) measured variable (pCO2/fCO2). |
| DiscreteDICVariable | DiscreteMeasuredVariable | Dissolved Inorganic Carbon (DIC) measured variable from discrete bottle samples. |
| DiscreteMeasuredVariable | MeasuredVariable | A variable measured in-situ from discrete water samples (e.g., bottle samples analyzed in a lab or shipboard). |
| DiscretePHVariable | DiscreteMeasuredVariable | pH measured variable with dye-based spectrophotometric measurement. |
| DiscretePhysiologicalVariable | DiscreteMeasuredVariable | Physiological response variable from discrete field samples (e.g., organism growth rates, calcification rates, gene expression from bottle or tissue samples collected in the field). |
| DiscreteSedimentVariable | DiscreteMeasuredVariable | Measured sediment variable collected from discrete bottle samples |
| DiscreteTAVariable | DiscreteMeasuredVariable | Total Alkalinity (TA) measured variable from discrete bottle samples |
| HPLCVariable | DiscreteMeasuredVariable | HPLC (High-Performance Liquid Chromatography) measured variable for pigment analysis. |
| ModelOutputVariable | Variable | A variable output by a model simulation (e.g., air-sea CO2 flux, dissolved inorganic carbon, total alkalinity, pH, temperature, salinity from an OAE model run). |
| NonMeasuredVariable | FieldVariable | A contextual or ancillary variable that is NOT directly measured or calculated by the project. |
| SocioeconomicVariable | InSituVariable | Socioeconomic variable for social and economic data such as survey responses, ecosystem service valuations, or text analysis. |

## Instruments and calibrations

| Class | Parent | What it is |
|---|---|---|
| AnalyzingInstrument |  | Base class for scientific instruments used in analyzing samples for measurement. |
| CO2Calibration | Calibration | Base CO2 gas detector calibration with standard gas information. |
| CO2GasDetector | AnalyzingInstrument | CO2 gas detector with standard gas calibration. |
| CRMCalibration | Calibration | Calibration using Certified Reference Materials, used for DIC and TA instruments. |
| CRMInstrument | AnalyzingInstrument | Instrument calibrated with Certified Reference Materials, used for DIC and TA measurements. |
| Calibration |  | Base calibration information for instruments. |
| ContinuousCO2Calibration | CO2Calibration | CO2 calibration for continuous measurements, with extended standard gas details. |
| ContinuousCO2GasDetector | CO2GasDetector | CO2 gas detector for continuous measurements, with measurement frequency. |
| ContinuousStandardGas | StandardGas | Standard gas used for continuous CO2 calibration, with additional traceability and count information. |
| DiscreteCO2Calibration | CO2Calibration | CO2 calibration for discrete measurements, with calibration temperature. |
| DyeCalibration | PHCalibration | pH instrument calibration with an indicator dye standard. |
| PHCalibration | Calibration | pH instrument calibration. |
| PHInstrument | AnalyzingInstrument | pH measurement instrument with dye-based calibration. |
| StandardGas |  | Standard gas used for CO2 calibration. |

## Supporting

| Class | Parent | What it is |
|---|---|---|
| CO2Equilibrator |  | Equilibrator used for continuous CO2 measurement. |
| DosingConcentration |  | Details of tracer concentration information |
| DosingLocation | Place | A specific location of dosing for an OAE intervention and/or tracer study. |
| ExternalProject |  | A research project that is not directly managed by the OAE project, but whose location is proximal to the OAE project and whose data may be relevant to understanding the context or impacts of OAE activities. |
| GenericSensor |  | Generic sensor base class used in continuous CO2 measurements. |
| GeoCoordinates |  | A geographic coordinate in decimal degrees. |
| GeoShape |  | The geographic shape of a place. |
| HardwareConfiguration |  | Details about the computational hardware used to run a model simulation. |
| MarineAirMeasurement |  | Information about CO2 measurements in marine air. |
| ModelComponent |  | A component of a model (e.g., physics, biogeochemistry/ecosystem). |
| ModelGrid |  | Details about a model grid. |
| ModelInputDetails |  | Details about input data sources used to drive the model. |
| MonetaryGrant |  |  |
| NamedLink |  | A link to a resource with a name and URL. |
| Organization |  |  |
| Permit |  | A permit associated with the project. |
| Person |  | Information about a researcher or investigator involved in the experiment. |
| Place |  | A geospatial area of interest, defined by a bounding box, polygon/line, or a point designated as a pair of geo-coordinates. |
| Platform |  |  |
| PressureSensor | GenericSensor | Pressure sensor used in continuous CO2 measurements. |
| PropertyValue |  |  |
| PublicComment |  | A public comment document associated with a consultation for this experiment. |
| SamplePreservation |  | Sample preservation information for DIC and TA measurements. |
| SpatialCoverage | Place | A bounding box defined by latitude and longitude coordinates. |
| TemperatureSensor | GenericSensor | Temperature sensor used in continuous CO2 measurements. |
| VerticalExtent |  | The vertical extent of a place or structure in meters. |
| VocabularyItemReference |  |  |
