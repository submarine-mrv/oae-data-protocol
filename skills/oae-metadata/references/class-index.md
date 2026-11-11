# Classes

One file per class in `classes/`. Open only the ones you are drafting.

## Project

| Class | Parent | What it is |
|---|---|---|
| [Container](classes/Container.md) |  |  |
| [Project](classes/Project.md) |  | A project conducting OAE field trials or modeling. |

## Experiments

| Class | Parent | What it is |
|---|---|---|
| [Experiment](classes/Experiment.md) |  | Abstract base class for all experiment types. |
| [InSituExperiment](classes/InSituExperiment.md) | Experiment | Experiment metadata for in-situ studies (interventions, tracer studies, etc.). |
| [Intervention](classes/Intervention.md) | InSituExperiment | Additional metadata that applies to experiments where an intervention, such as an alkalinity addition, was conducted. |
| [InterventionWithTracer](classes/InterventionWithTracer.md) | Intervention | Additional metadata that applies to hybrid experiments where an intervention was conducted simultaneously alongside a tracer study, using the same instrumentation. |
| [Model](classes/Model.md) | Experiment | A computational model experiment related to OAE. |
| [Tracer](classes/Tracer.md) | InSituExperiment | Additional metadata that applies to experiments where a tracer study was conducted |

## Datasets

| Class | Parent | What it is |
|---|---|---|
| [Dataset](classes/Dataset.md) |  | Abstract base class for all dataset types. |
| [FieldDataset](classes/FieldDataset.md) | Dataset | A field or observational dataset related to an OAE experiment. |
| [ModelOutputDataset](classes/ModelOutputDataset.md) | Dataset | A model simulation output dataset. |

## Variables

| Class | Parent | What it is |
|---|---|---|
| [CalculatedVariable](classes/CalculatedVariable.md) | InSituVariable | A variable that is calculated or derived from other measured variables rather than directly measured by an instrument (e.g., carbonate system parameters computed via CO2SYS). |
| [ContinuousCO2Variable](classes/ContinuousCO2Variable.md) | ContinuousMeasuredVariable | CO2 continuous (sensor) measured variable (xCO2/pCO2/fCO2). |
| [ContinuousDICVariable](classes/ContinuousDICVariable.md) | ContinuousMeasuredVariable | Dissolved Inorganic Carbon (DIC) measured variable from continuous autonomous sensor. |
| [ContinuousMeasuredVariable](classes/ContinuousMeasuredVariable.md) | MeasuredVariable | A variable measured in-situ by a continuous autonomous sensor (e.g., temperature, salinity, conductivity, pressure from a deployed sonde or underway system). |
| [ContinuousPHVariable](classes/ContinuousPHVariable.md) | ContinuousMeasuredVariable | pH measured variable from continuous autonomous sensor |
| [ContinuousPhysiologicalVariable](classes/ContinuousPhysiologicalVariable.md) | ContinuousMeasuredVariable | Physiological response variable from continuous autonomous field sensors (e.g., respiration rates from deployed oxygen consumption monitors, heart rate from bio-loggers). |
| [ContinuousSedimentVariable](classes/ContinuousSedimentVariable.md) | ContinuousMeasuredVariable | Measured sediment variable collected from continuous autonomous sensor |
| [ContinuousTAVariable](classes/ContinuousTAVariable.md) | ContinuousMeasuredVariable | Total Alkalinity (TA) measured variable from continuous autonomous sensor |
| [DiscreteCO2Variable](classes/DiscreteCO2Variable.md) | DiscreteMeasuredVariable | CO2 discrete (bottle) measured variable (pCO2/fCO2). |
| [DiscreteDICVariable](classes/DiscreteDICVariable.md) | DiscreteMeasuredVariable | Dissolved Inorganic Carbon (DIC) measured variable from discrete bottle samples. |
| [DiscreteMeasuredVariable](classes/DiscreteMeasuredVariable.md) | MeasuredVariable | A variable measured in-situ from discrete water samples (e.g., bottle samples analyzed in a lab or shipboard). |
| [DiscretePHVariable](classes/DiscretePHVariable.md) | DiscreteMeasuredVariable | pH measured variable with dye-based spectrophotometric measurement. |
| [DiscretePhysiologicalVariable](classes/DiscretePhysiologicalVariable.md) | DiscreteMeasuredVariable | Physiological response variable from discrete field samples (e.g., organism growth rates, calcification rates, gene expression from bottle or tissue samples collected in the field). |
| [DiscreteSedimentVariable](classes/DiscreteSedimentVariable.md) | DiscreteMeasuredVariable | Measured sediment variable collected from discrete bottle samples |
| [DiscreteTAVariable](classes/DiscreteTAVariable.md) | DiscreteMeasuredVariable | Total Alkalinity (TA) measured variable from discrete bottle samples |
| [HPLCVariable](classes/HPLCVariable.md) | DiscreteMeasuredVariable | HPLC (High-Performance Liquid Chromatography) measured variable for pigment analysis. |
| [ModelOutputVariable](classes/ModelOutputVariable.md) | Variable | A variable output by a model simulation (e.g., air-sea CO2 flux, dissolved inorganic carbon, total alkalinity, pH, temperature, salinity from an OAE model run). |
| [NonMeasuredVariable](classes/NonMeasuredVariable.md) | FieldVariable | A contextual or ancillary variable that is NOT directly measured or calculated by the project. |
| [SocioeconomicVariable](classes/SocioeconomicVariable.md) | InSituVariable | Socioeconomic variable for social and economic data such as survey responses, ecosystem service valuations, or text analysis. |

## Instruments and calibrations

| Class | Parent | What it is |
|---|---|---|
| [AnalyzingInstrument](classes/AnalyzingInstrument.md) |  | Base class for scientific instruments used in analyzing samples for measurement. |
| [CO2Calibration](classes/CO2Calibration.md) | Calibration | Base CO2 gas detector calibration with standard gas information. |
| [CO2GasDetector](classes/CO2GasDetector.md) | AnalyzingInstrument | CO2 gas detector with standard gas calibration. |
| [CRMCalibration](classes/CRMCalibration.md) | Calibration | Calibration using Certified Reference Materials, used for DIC and TA instruments. |
| [CRMInstrument](classes/CRMInstrument.md) | AnalyzingInstrument | Instrument calibrated with Certified Reference Materials, used for DIC and TA measurements. |
| [Calibration](classes/Calibration.md) |  | Base calibration information for instruments. |
| [ContinuousCO2Calibration](classes/ContinuousCO2Calibration.md) | CO2Calibration | CO2 calibration for continuous measurements, with extended standard gas details. |
| [ContinuousCO2GasDetector](classes/ContinuousCO2GasDetector.md) | CO2GasDetector | CO2 gas detector for continuous measurements, with measurement frequency. |
| [ContinuousStandardGas](classes/ContinuousStandardGas.md) | StandardGas | Standard gas used for continuous CO2 calibration, with additional traceability and count information. |
| [DiscreteCO2Calibration](classes/DiscreteCO2Calibration.md) | CO2Calibration | CO2 calibration for discrete measurements, with calibration temperature. |
| [DyeCalibration](classes/DyeCalibration.md) | PHCalibration | pH instrument calibration with an indicator dye standard. |
| [PHCalibration](classes/PHCalibration.md) | Calibration | pH instrument calibration. |
| [PHInstrument](classes/PHInstrument.md) | AnalyzingInstrument | pH measurement instrument with dye-based calibration. |
| [StandardGas](classes/StandardGas.md) |  | Standard gas used for CO2 calibration. |

## Supporting

| Class | Parent | What it is |
|---|---|---|
| [CO2Equilibrator](classes/CO2Equilibrator.md) |  | Equilibrator used for continuous CO2 measurement. |
| [DosingConcentration](classes/DosingConcentration.md) |  | Details of tracer concentration information |
| [DosingLocation](classes/DosingLocation.md) | Place | A specific location of dosing for an OAE intervention and/or tracer study. |
| [ExternalProject](classes/ExternalProject.md) |  | A research project that is not directly managed by the OAE project, but whose location is proximal to the OAE project and whose data may be relevant to understanding the context or impacts of OAE activities. |
| [GenericSensor](classes/GenericSensor.md) |  | Generic sensor base class used in continuous CO2 measurements. |
| [GeoCoordinates](classes/GeoCoordinates.md) |  | A geographic coordinate in decimal degrees. |
| [GeoShape](classes/GeoShape.md) |  | The geographic shape of a place. |
| [HardwareConfiguration](classes/HardwareConfiguration.md) |  | Details about the computational hardware used to run a model simulation. |
| [MarineAirMeasurement](classes/MarineAirMeasurement.md) |  | Information about CO2 measurements in marine air. |
| [ModelComponent](classes/ModelComponent.md) |  | A component of a model (e.g., physics, biogeochemistry/ecosystem). |
| [ModelGrid](classes/ModelGrid.md) |  | Details about a model grid. |
| [ModelInputDetails](classes/ModelInputDetails.md) |  | Details about input data sources used to drive the model. |
| [MonetaryGrant](classes/MonetaryGrant.md) |  |  |
| [NamedLink](classes/NamedLink.md) |  | A link to a resource with a name and URL. |
| [Organization](classes/Organization.md) |  |  |
| [Permit](classes/Permit.md) |  | A permit associated with the project. |
| [Person](classes/Person.md) |  | Information about a researcher or investigator involved in the experiment. |
| [Place](classes/Place.md) |  | A geospatial area of interest, defined by a bounding box, polygon/line, or a point designated as a pair of geo-coordinates. |
| [Platform](classes/Platform.md) |  |  |
| [PressureSensor](classes/PressureSensor.md) | GenericSensor | Pressure sensor used in continuous CO2 measurements. |
| [PropertyValue](classes/PropertyValue.md) |  |  |
| [PublicComment](classes/PublicComment.md) |  | A public comment document associated with a consultation for this experiment. |
| [SamplePreservation](classes/SamplePreservation.md) |  | Sample preservation information for DIC and TA measurements. |
| [SpatialCoverage](classes/SpatialCoverage.md) | Place | A bounding box defined by latitude and longitude coordinates. |
| [TemperatureSensor](classes/TemperatureSensor.md) | GenericSensor | Temperature sensor used in continuous CO2 measurements. |
| [VerticalExtent](classes/VerticalExtent.md) |  | The vertical extent of a place or structure in meters. |
| [VocabularyItemReference](classes/VocabularyItemReference.md) |  |  |
