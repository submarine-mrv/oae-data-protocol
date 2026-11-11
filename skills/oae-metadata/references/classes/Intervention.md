# Intervention

Additional metadata that applies to experiments where an intervention, such as an alkalinity addition, was conducted.

Parent: InSituExperiment

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| alkalinity_feedstock_processing | yes | no | enum: `electrochemistry`, `synthetically_derived`, `mineral_mining`, `blended`, `other` | Method(s) used to process the alkalinity feedstock. See Controlled Vocabularies section for definitions. |
| alkalinity_feedstock_form | yes | no | enum: `solid`, `aqueous`, `slurry` | The phase upon delivery to the ocean. See Controlled Vocabularies section for definitions. |
| alkalinity_feedstock | yes | no | enum: `lime`, `portlandite`, `calcium_carbonate`, `anorthite`, `dolomite`, `periclase`, `brucite`, `magnesite`, `forsterite`, `mg_rich_olivine`, `sodium_hydroxide`, `natrite`, `nahcolite`, `other` | Examples may include: olivine, potassium hydroxide, magnesium hydroxide, lime, portlandite, calcium carbonate, anorthite, dolomite, periclase, brucite, magnesite, forsterite, sodium hydroxide, natrite, nahcolite, akermanite, akermanite, alunoakermanite, etc. See Controlled Vocabularies section for selected examples (this list is not exhaustive, you may need to include your unique feedstock). |
| alkalinity_feedstock_co2_removal_potential | yes | no | float | Maximum CO₂ removal potential of a feedstock material. We recommend using an adjusted version of the Steinour equation (Gunning et al., 2010), which uses bulk elemental oxide composition to estimate the maximum CO₂ removal potential of a feedstock material. The calculation output is in the form of kg of CO₂ per tonne of feedstock and represents the quantitative hypothetical potential of the material to capture CO₂ as bicarbonate or carbonate. See Isometric's CO2 removal potential module for details. |
| alkalinity_feedstock_description | yes | no | string | Information such as feedstock source, characteristics, impurities, dilution prior to dosing, and concentration. For feedstock other than NaOH: trace metal composition and particulate grain size. Any variable information must be provided in the dosing data file, in this case include the data file and column header names here provided as variables. See [Intervention Data](https://www.carbontosea.org/oae-data-protocol/1-0-0/#intervention-data) for details. |
| equilibration | yes | no | enum: `pre_equilibrated`, `unequilibrated` | Whether the feedstock was pre-equilibrated or unequilibrated |
| alkalinity_dosing_effluent_density | yes | no | [DosingConcentration](DosingConcentration.md) | Fixed density or provide link/source to effluent density data if applicable. Please include whether density is directly measured or a derived value. If this is a variable included with your data, please note so here as 'alkalinity dosing effluent density is provided as a variable' and use 'dosing_effluent_density' for your column header name. |
| dosing_delivery_type | yes | no | enum: `static_point_source`, `variable_point_source`, `static_distributed`, `variable_distributed` | Type of dosing delivery method. See Controlled Vocabularies for definitions. |
| dosing_location | yes | no | [DosingLocation](DosingLocation.md) | Provide latitude and longitude in decimal degrees. Depending on your method of dispersal, this information may be provided as a point source, vector, or bounding box. If provided as a vector, the latitude and longitude values should be included in the dosing data file. |
| dosing_dispersal_hydrologic_location | yes | no | enum: `coastal_surface`, `offshore_surface`, `river`, `wetland`, `seafloor` | Descriptive dosing location |
| dosing_depth | yes | no | string | Depth in meters. If this is variable, please include the schedule of depth changes and depths, or as a vector in meters with the data. |
| dosing_regimen | yes | no | string | A human readable summary description of the dosing regimen / frequency. Exact details must be provided in the corresponding dosing file with exact timestamps for dosing on/off schedule. |
| dosing_description | yes | no | string | Please be descriptive. Information about the dosing mechanism must be included (outflow from pipe, diffuser, doser, manual placement) E.g., outflow from existing facility pipe directly to ocean, manual riverine introduction, coastal distribution at three separate 30 meter long sections, pier-based diffuser to intercoastal bay, distributed from stationary barge 10 miles offshore. |
| name | yes | no | string | Common name for experiment. |
| description | yes | no | string | A narrative description of the experiment. For example, what part of the project do these data represent (e.g., baseline, intervention, control) and what do they contribute to the overall project? Are all project research questions listed in Project description relevant? What were the processes to achieve these goals and answer these questions? Data submitters are encouraged to note any significant changes to the original experimental plan due to unforeseen circumstances here. |
| spatial_coverage | yes | no | [SpatialCoverage](SpatialCoverage.md) | Latitude/longitude bounds of observed data in experiment, expressed as a schema.org GeoShape bounding box. |
| project_id | yes | no | string | The project to which the submitted data belong. A unique project identifier that can be used to link project data across data submissions, and link baseline data to intervention data, for example. If no Project ID has been assigned, one may be generated by combining: lead organizer surname and first initial or company, a unique date, and location. Any method that creates a unique ID that will link all project data is acceptable. |
| experiment_id | yes | no | string | The experiment to which the data belong. Any naming convention that produces a unique ID is usable. The recommended naming convention is: Project ID + Experiment type + Optional numerical indicator to differentiate between various experiments of the same type for a project. A two digit consecutive number beginning with 01 |
| experiment_types | yes | yes | enum: `baseline`, `control`, `intervention`, `tracer_study`, `model`, `other` | The type(s) of mCDR experiment conducted. See Controlled Vocabularies section for definitions. |
| experiment_leads | yes | yes | [Person](Person.md) | Provide details for each experiment lead / principal investigator (PI) including: Name, institutional information (name, address), phone, email, ID type (e.g., ORCID, etc), researcher ID, and role. |
| start_datetime | yes | no | datetime | Start date and time of experiment in UTC ISO-8601 |
| alkalinity_feedstock_processing_custom | no | no | string | Custom description of alkalinity feedstock processing method when 'other' is selected in alkalinity_feedstock_processing. |
| alkalinity_feedstock_custom | no | no | string | Custom description of alkalinity feedstock when using a feedstock type not listed in the controlled vocabulary. |
| vertical_coverage | no | no | [VerticalExtent](VerticalExtent.md) | Minimum and maximum depths of observations in meters. |
| permits | no | yes | [Permit](Permit.md) | Associated permit number(s). |
| data_conflicts_and_unreported_data | no | no | string | If data exist that are or have been used by the project but are not provided due to conflicts (e.g., geopolitical or other), data availability (e.g., a dataset is no longer available), it may be noted here. |
| meteorological_and_tidal_data | no | yes | [NamedLink](NamedLink.md) | Include links to relevant open datasets if referenced in the experiment but not provided in the submission. |
| additional_details | no | no | string | Open text area to include additional information. These may include information for sediment processes data, biological data, or any other required information if not included in the main metadata or data files; see General Guidelines for Your Data for relevant sections of your data. Additional informational files, such as digitized laboratory notebooks, blogs, etc., may be linked here. |
| public_comments | no | yes | [PublicComment](PublicComment.md) | Public comment documents, each with a link or DOI and an optional description. Please group/concatenate all public comments associated with a specific consultation (e.g., for permitting, non-mandated consultations on a specific topic, or informal public input such as unsolicited comments and media attention) into a single document if possible, and link to it here. |
| end_datetime | no | no | datetime | End date and time of experiment in UTC ISO-8601 |

## Rules

- When `alkalinity_feedstock` is `other`, `alkalinity_feedstock_custom` is required.
- When `alkalinity_feedstock_processing` is `other`, `alkalinity_feedstock_processing_custom` is required.

## Vocabularies

What each value means, for the fields above.

### alkalinity_feedstock_processing

- `electrochemistry`: Alkalinity generated via electrochemical processes (e.g., seawater electrolysis).
- `synthetically_derived`: Intentionally industrially manufactured chemical compounds (e.g., Ca(OH)2 via lime kilns).
- `mineral_mining`: Mined geological material, including purified mineral or natural rock.
- `blended`: A mix of multiple sources.
- `other`: Unclassified or novel; include a description in Experiment Description.

### alkalinity_feedstock_form

- `solid`: Involves adding alkaline minerals or particulate slurry (such as MgOH2, MgO, or CaO) to seawater or river systems either directly, through coastal outfalls (such as wastewater), or at breaking shorelines to increase its alkalinity.
- `aqueous`: Aqueous alkalinity addition may use electrochemistry or fully dissolved mineral feedstock to increase seawater alkalinity.
- `slurry`: Slurry alkalinity additions include a mix of solid and aqueous alkalinity forms, where the solid alkaline particulates are suspended in a solution.

### alkalinity_feedstock

- `lime`: Lime (CaO) used as an alkalinity source.
- `portlandite`: Portlandite (Ca(OH)₂) used as an alkalinity source.
- `calcium_carbonate`: Calcium carbonate (CaCO₃) used as an alkalinity source.
- `anorthite`: Anorthite (CaAl₂Si₂O₈) used as an alkalinity source.
- `dolomite`: Dolomite (CaMg(CO₃)₂) used as an alkalinity source.
- `periclase`: Periclase (MgO) used as an alkalinity source.
- `brucite`: Brucite (Mg(OH)₂) used as an alkalinity source.
- `magnesite`: Magnesite (MgCO₃) used as an alkalinity source.
- `forsterite`: Forsterite (Mg₂SiO₄) used as an alkalinity source.
- `mg_rich_olivine`: Magnesium-rich olivine used as an alkalinity source.
- `sodium_hydroxide`: NaOH used as an alkalinity source.
- `natrite`: Natrite (Na₂CO₃) used as an alkalinity source.
- `nahcolite`: Nahcolite (NaHCO₃) used as an alkalinity source.
- `other`: Enter a custom value in the field provided

### equilibration

- `pre_equilibrated`: Pre-equilibrated with atmosphere before dosing
- `unequilibrated`: Not pre-equilibrated before dosing

### dosing_delivery_type

- `static_point_source`: A single dosing location such as an outflow from a static platform with a pipe
- `variable_point_source`: A mobile dosing regimen described by a single location at each time step, such as an outflow from a mobile platform such as a ship or surface vessel.
- `static_distributed`: A set location or locations of dosing that is not a point source, such as a distributed area over the seafloor or a diffusor.
- `variable_distributed`: A distributed dosing area that varies in time, such as manually placed alkaline material over different areas at different times.

### dosing_dispersal_hydrologic_location

- `coastal_surface`: Surface waters in coastal areas
- `offshore_surface`: Surface waters in offshore areas
- `river`: River systems
- `wetland`: Wetland areas
- `seafloor`: Seafloor or benthic zone

### experiment_types

- `baseline`: Baseline measurements taken before any intervention
- `control`: Control experiment without intervention for comparison
- `intervention`: Experiment with active OAE intervention
- `tracer_study`: Tracer study experiment (eg- dye or gas tracer study)
- `model`: Model-based experiment or simulation
- `other`: Other experiment type not covered by standard categories
