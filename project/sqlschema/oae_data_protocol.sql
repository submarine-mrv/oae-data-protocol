-- # Class: "PropertyValue" Description: ""
--     * Slot: id Description: 
-- # Class: "Any" Description: ""
--     * Slot: id Description: 
-- # Class: "OAEProject" Description: "A project conducting OAE field trials or modeling."
--     * Slot: description Description: A narrative description of the thing.
--     * Slot: project_id Description: Unique identifier for an OAE project.
--     * Slot: mcdr_pathway Description: The Marine Carbon Dioxide Removal (MCDR) pathway being studied.
--     * Slot: site_description Description: Details about the project site, including location and conditions.
--     * Slot: permit_info Description: Regulatory details for the project.
-- # Class: "Dataset" Description: "A dataset related to an OAE experiment. Generally following guidelines & best practices as outlined in [science-on-schema.org](https://github.com/ESIPFed/science-on-schema.org/blob/main/guides/Dataset.md)"
--     * Slot: id Description: 
--     * Slot: description Description: A narrative description of the thing.
--     * Slot: name Description: A human-readable name for the thing.
--     * Slot: identifier Description: A unique identifier for the thing
--     * Slot: url Description: Location of a page describing the dataset.
--     * Slot: temporal_coverage Description: The temporal coverage of the dataset.
--     * Slot: spatial_coverage Description: The spatial coverage of the dataset.
--     * Slot: Experiment_experiment_id Description: Autocreated FK slot
--     * Slot: Intervention_experiment_id Description: Autocreated FK slot
--     * Slot: ModelSimulation_experiment_id Description: Autocreated FK slot
-- # Class: "Experiment" Description: "A single experiment conducted within an OAE project."
--     * Slot: description Description: A narrative description of the thing.
--     * Slot: experiment_type Description: The type of experiment being conducted.
--     * Slot: experiment_id Description: Unique identifier for an OAE experiment.
--     * Slot: start_date Description: Date when the experiment began.
--     * Slot: end_date Description: Date when the experiment ended.
--     * Slot: project_project_id Description: The OAE project to which the experiment belongs.
-- # Class: "Intervention" Description: "Details about an OAE intervention."
--     * Slot: treatment_type Description: Type of OAE intervention.
--     * Slot: alkalinity_feedstock_type Description: Material used for alkalinity addition.
--     * Slot: alkalinity_feedstock_description Description: Information such as feedstock source, characteristics, concentration, impurities, dilution prior to dosing, and for feedstock other than NaOH; trace metal composition and particulate grain size.
--     * Slot: dosing_depth_in_m Description: Depth at which alkalinity is added.
--     * Slot: dosing_regimen Description: Schedule and amount of added alkalinity.
--     * Slot: dosing_location Description: Geospatial coordinates of dosing activity.
--     * Slot: description Description: A narrative description of the thing.
--     * Slot: experiment_type Description: The type of experiment being conducted.
--     * Slot: experiment_id Description: Unique identifier for an OAE experiment.
--     * Slot: start_date Description: Date when the experiment began.
--     * Slot: end_date Description: Date when the experiment ended.
--     * Slot: project_project_id Description: The OAE project to which the experiment belongs.
-- # Class: "ModelSimulation" Description: "A computational model run related to OAE."
--     * Slot: model_type Description: Type of model simulation.
--     * Slot: model_configurations Description: Details about the model configuration.
--     * Slot: description Description: Foobar description
--     * Slot: experiment_type Description: The type of experiment being conducted (must be 'model_output' for ModelSimulation class).
--     * Slot: experiment_id Description: Unique identifier for an OAE experiment.
--     * Slot: start_date Description: Date when the experiment began.
--     * Slot: end_date Description: Date when the experiment ended.
--     * Slot: grid_details_id Description: Details about the model grid.
--     * Slot: project_project_id Description: The OAE project to which the experiment belongs.
-- # Class: "ModelGrid" Description: "Details about the model grid."
--     * Slot: id Description: 
--     * Slot: grid_type Description: Descriptive structure of grid (e.g. latitude-longitude grid, unstructured triangular, tripolar)
--     * Slot: region Description: Region covered by the grid. LOOK FOR IMPORTS
--     * Slot: arrangement Description: The grid arrangement of orthogonal physical quantities (e.g. Arakawa A, Arakawa B, Arakawa C)
--     * Slot: n_x Description: Number of grid points in the x-direction.
--     * Slot: n_y Description: Number of grid points in the y-direction.
--     * Slot: n_z Description: Number of vertical coordinate levels.
--     * Slot: n_nodes Description: Number of nodes in the grid if using an unstructured grids
--     * Slot: horizontal_resolution_in_m Description: Horizontal resolution of the grid.
--     * Slot: vertical_resolution_in_m Description: Vertical resolution of the grid.
-- # Class: "ModelComponent" Description: "A component of a model."
--     * Slot: id Description: 
--     * Slot: description Description: A description of the physical model characteristics, including version of equations being solved (hydrostatic vs non-hydrostatic), tracer advection scheme, how bottom drag is represented, mixed layer parameterizations, sub-grid mixing parameterizations if applicable, etc. Associated links to data, DOIs, or publications can be noted here, but should be supplemental.
--     * Slot: name Description: Name of the model (e.g. ROMS, Oceanaigans)
--     * Slot: version Description: Version of the model component.
--     * Slot: codebase Description: Link to model code repository.
-- # Class: "ModelPhysicsComponent" Description: "A physical component of a model."
--     * Slot: id Description: 
--     * Slot: description Description: A description of the physical model characteristics, including version of equations being solved (hydrostatic vs non-hydrostatic), tracer advection scheme, how bottom drag is represented, mixed layer parameterizations, sub-grid mixing parameterizations if applicable, etc. Associated links to data, DOIs, or publications can be noted here, but should be supplemental.
--     * Slot: name Description: Name of the model (e.g. ROMS, Oceanaigans)
--     * Slot: version Description: Version of the model component.
--     * Slot: codebase Description: Link to model code repository.
-- # Class: "ModelBGCComponent" Description: "A biogeochemical / ecosystem component of a model"
--     * Slot: id Description: 
--     * Slot: air_sea_co2_flux_parameterization Description: Description and/or references of air-sea CO2 flux parameterization used, gas transfer velocity formulation and atmospheric CO2 details (e.g., fixed or time varying, and if time varying which data were used).
--     * Slot: description Description: A description of the physical model characteristics, including version of equations being solved (hydrostatic vs non-hydrostatic), tracer advection scheme, how bottom drag is represented, mixed layer parameterizations, sub-grid mixing parameterizations if applicable, etc. Associated links to data, DOIs, or publications can be noted here, but should be supplemental.
--     * Slot: name Description: Name of the model (e.g. ROMS, Oceanaigans)
--     * Slot: version Description: Version of the model component.
--     * Slot: codebase Description: Link to model code repository.
-- # Class: "Experiment_observation_type" Description: ""
--     * Slot: Experiment_experiment_id Description: Autocreated FK slot
--     * Slot: observation_type Description: The type of observation / data submitted, multiple values are allowed of mulitple datasets are being submitted for this experiment.
-- # Class: "Experiment_previous_research" Description: ""
--     * Slot: Experiment_experiment_id Description: Autocreated FK slot
--     * Slot: previous_research Description: Previous research related to the experiment.
-- # Class: "Intervention_observation_type" Description: ""
--     * Slot: Intervention_experiment_id Description: Autocreated FK slot
--     * Slot: observation_type Description: The type of observation / data submitted, multiple values are allowed of mulitple datasets are being submitted for this experiment.
-- # Class: "Intervention_previous_research" Description: ""
--     * Slot: Intervention_experiment_id Description: Autocreated FK slot
--     * Slot: previous_research Description: Previous research related to the experiment.
-- # Class: "ModelSimulation_model_components" Description: ""
--     * Slot: ModelSimulation_experiment_id Description: Autocreated FK slot
--     * Slot: model_components_id Description: Components of the model.
-- # Class: "ModelSimulation_observation_type" Description: ""
--     * Slot: ModelSimulation_experiment_id Description: Autocreated FK slot
--     * Slot: observation_type Description: The type of observation / data submitted, multiple values are allowed of mulitple datasets are being submitted for this experiment.
-- # Class: "ModelSimulation_previous_research" Description: ""
--     * Slot: ModelSimulation_experiment_id Description: Autocreated FK slot
--     * Slot: previous_research Description: Previous research related to the experiment.
-- # Class: "ModelComponent_references" Description: ""
--     * Slot: ModelComponent_id Description: Autocreated FK slot
--     * Slot: references Description: Reference for model physics.
-- # Class: "ModelPhysicsComponent_references" Description: ""
--     * Slot: ModelPhysicsComponent_id Description: Autocreated FK slot
--     * Slot: references Description: Reference for model physics.
-- # Class: "ModelBGCComponent_references" Description: ""
--     * Slot: ModelBGCComponent_id Description: Autocreated FK slot
--     * Slot: references Description: Reference for model physics.

CREATE TABLE "PropertyValue" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Any" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "OAEProject" (
	description TEXT, 
	project_id TEXT NOT NULL, 
	mcdr_pathway VARCHAR(32), 
	site_description TEXT, 
	permit_info TEXT, 
	PRIMARY KEY (project_id)
);
CREATE TABLE "ModelGrid" (
	id INTEGER NOT NULL, 
	grid_type TEXT, 
	region TEXT, 
	arrangement TEXT, 
	n_x INTEGER, 
	n_y INTEGER, 
	n_z INTEGER, 
	n_nodes INTEGER, 
	horizontal_resolution_in_m INTEGER, 
	vertical_resolution_in_m INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "ModelComponent" (
	id INTEGER NOT NULL, 
	description TEXT, 
	name TEXT, 
	version TEXT, 
	codebase TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ModelPhysicsComponent" (
	id INTEGER NOT NULL, 
	description TEXT, 
	name TEXT, 
	version TEXT, 
	codebase TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ModelBGCComponent" (
	id INTEGER NOT NULL, 
	air_sea_co2_flux_parameterization TEXT, 
	description TEXT, 
	name TEXT, 
	version TEXT, 
	codebase TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Experiment" (
	description TEXT, 
	experiment_type VARCHAR(12), 
	experiment_id TEXT NOT NULL, 
	start_date DATETIME, 
	end_date DATETIME, 
	project_project_id TEXT, 
	PRIMARY KEY (experiment_id), 
	FOREIGN KEY(project_project_id) REFERENCES "OAEProject" (project_id)
);
CREATE TABLE "Intervention" (
	treatment_type VARCHAR(15), 
	alkalinity_feedstock_type VARCHAR(17), 
	alkalinity_feedstock_description TEXT, 
	dosing_depth_in_m INTEGER, 
	dosing_regimen TEXT, 
	dosing_location TEXT, 
	description TEXT, 
	experiment_type VARCHAR(12), 
	experiment_id TEXT NOT NULL, 
	start_date DATETIME, 
	end_date DATETIME, 
	project_project_id TEXT, 
	PRIMARY KEY (experiment_id), 
	FOREIGN KEY(project_project_id) REFERENCES "OAEProject" (project_id)
);
CREATE TABLE "ModelSimulation" (
	model_type VARCHAR(14), 
	model_configurations TEXT, 
	description TEXT, 
	experiment_type VARCHAR(12), 
	experiment_id TEXT NOT NULL, 
	start_date DATETIME, 
	end_date DATETIME, 
	grid_details_id INTEGER, 
	project_project_id TEXT, 
	PRIMARY KEY (experiment_id), 
	FOREIGN KEY(grid_details_id) REFERENCES "ModelGrid" (id), 
	FOREIGN KEY(project_project_id) REFERENCES "OAEProject" (project_id)
);
CREATE TABLE "ModelComponent_references" (
	"ModelComponent_id" INTEGER, 
	"references" TEXT, 
	PRIMARY KEY ("ModelComponent_id", "references"), 
	FOREIGN KEY("ModelComponent_id") REFERENCES "ModelComponent" (id)
);
CREATE TABLE "ModelPhysicsComponent_references" (
	"ModelPhysicsComponent_id" INTEGER, 
	"references" TEXT, 
	PRIMARY KEY ("ModelPhysicsComponent_id", "references"), 
	FOREIGN KEY("ModelPhysicsComponent_id") REFERENCES "ModelPhysicsComponent" (id)
);
CREATE TABLE "ModelBGCComponent_references" (
	"ModelBGCComponent_id" INTEGER, 
	"references" TEXT, 
	PRIMARY KEY ("ModelBGCComponent_id", "references"), 
	FOREIGN KEY("ModelBGCComponent_id") REFERENCES "ModelBGCComponent" (id)
);
CREATE TABLE "Dataset" (
	id INTEGER NOT NULL, 
	description TEXT, 
	name TEXT, 
	identifier TEXT, 
	url TEXT, 
	temporal_coverage TEXT, 
	spatial_coverage TEXT, 
	"Experiment_experiment_id" TEXT, 
	"Intervention_experiment_id" TEXT, 
	"ModelSimulation_experiment_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Experiment_experiment_id") REFERENCES "Experiment" (experiment_id), 
	FOREIGN KEY("Intervention_experiment_id") REFERENCES "Intervention" (experiment_id), 
	FOREIGN KEY("ModelSimulation_experiment_id") REFERENCES "ModelSimulation" (experiment_id)
);
CREATE TABLE "Experiment_observation_type" (
	"Experiment_experiment_id" TEXT, 
	observation_type VARCHAR(22), 
	PRIMARY KEY ("Experiment_experiment_id", observation_type), 
	FOREIGN KEY("Experiment_experiment_id") REFERENCES "Experiment" (experiment_id)
);
CREATE TABLE "Experiment_previous_research" (
	"Experiment_experiment_id" TEXT, 
	previous_research TEXT, 
	PRIMARY KEY ("Experiment_experiment_id", previous_research), 
	FOREIGN KEY("Experiment_experiment_id") REFERENCES "Experiment" (experiment_id)
);
CREATE TABLE "Intervention_observation_type" (
	"Intervention_experiment_id" TEXT, 
	observation_type VARCHAR(22), 
	PRIMARY KEY ("Intervention_experiment_id", observation_type), 
	FOREIGN KEY("Intervention_experiment_id") REFERENCES "Intervention" (experiment_id)
);
CREATE TABLE "Intervention_previous_research" (
	"Intervention_experiment_id" TEXT, 
	previous_research TEXT, 
	PRIMARY KEY ("Intervention_experiment_id", previous_research), 
	FOREIGN KEY("Intervention_experiment_id") REFERENCES "Intervention" (experiment_id)
);
CREATE TABLE "ModelSimulation_model_components" (
	"ModelSimulation_experiment_id" TEXT, 
	model_components_id INTEGER, 
	PRIMARY KEY ("ModelSimulation_experiment_id", model_components_id), 
	FOREIGN KEY("ModelSimulation_experiment_id") REFERENCES "ModelSimulation" (experiment_id), 
	FOREIGN KEY(model_components_id) REFERENCES "ModelComponent" (id)
);
CREATE TABLE "ModelSimulation_observation_type" (
	"ModelSimulation_experiment_id" TEXT, 
	observation_type VARCHAR(22), 
	PRIMARY KEY ("ModelSimulation_experiment_id", observation_type), 
	FOREIGN KEY("ModelSimulation_experiment_id") REFERENCES "ModelSimulation" (experiment_id)
);
CREATE TABLE "ModelSimulation_previous_research" (
	"ModelSimulation_experiment_id" TEXT, 
	previous_research TEXT, 
	PRIMARY KEY ("ModelSimulation_experiment_id", previous_research), 
	FOREIGN KEY("ModelSimulation_experiment_id") REFERENCES "ModelSimulation" (experiment_id)
);