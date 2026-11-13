

# Class: InterventionWithTracer


_Additional metadata that applies to hybrid experiments where an intervention was conducted simultaneously alongside a tracer study, using the same instrumentation._





URI: [oae:InterventionWithTracer](https://schema.oaedata.org/InterventionWithTracer)






```mermaid
 classDiagram
    class InterventionWithTracer
    click InterventionWithTracer href "../InterventionWithTracer"
      TracerDetails <|-- InterventionWithTracer
        click TracerDetails href "../TracerDetails"
      Intervention <|-- InterventionWithTracer
        click Intervention href "../Intervention"
      
      InterventionWithTracer : additional_details
        
      InterventionWithTracer : alkalinity_dosing_effluent_density
        
          
    
    
    InterventionWithTracer --> "1" DosingConcentration : alkalinity_dosing_effluent_density
    click DosingConcentration href "../DosingConcentration"

        
      InterventionWithTracer : alkalinity_feedstock
        
          
    
    
    InterventionWithTracer --> "1" FeedstockType : alkalinity_feedstock
    click FeedstockType href "../FeedstockType"

        
      InterventionWithTracer : alkalinity_feedstock_co2_removal_potential
        
      InterventionWithTracer : alkalinity_feedstock_custom
        
      InterventionWithTracer : alkalinity_feedstock_description
        
      InterventionWithTracer : alkalinity_feedstock_form
        
          
    
    
    InterventionWithTracer --> "1" AlkalinityFeedstockForm : alkalinity_feedstock_form
    click AlkalinityFeedstockForm href "../AlkalinityFeedstockForm"

        
      InterventionWithTracer : alkalinity_feedstock_processing
        
          
    
    
    InterventionWithTracer --> "1" AlkalinityFeedstockProcessing : alkalinity_feedstock_processing
    click AlkalinityFeedstockProcessing href "../AlkalinityFeedstockProcessing"

        
      InterventionWithTracer : alkalinity_feedstock_processing_custom
        
      InterventionWithTracer : data_conflicts_and_unreported_data
        
      InterventionWithTracer : description
        
      InterventionWithTracer : dosing_delivery_type
        
          
    
    
    InterventionWithTracer --> "1" DosingDeliveryType : dosing_delivery_type
    click DosingDeliveryType href "../DosingDeliveryType"

        
      InterventionWithTracer : dosing_depth
        
      InterventionWithTracer : dosing_description
        
      InterventionWithTracer : dosing_dispersal_hydrologic_location
        
          
    
    
    InterventionWithTracer --> "1" HydrologicLocation : dosing_dispersal_hydrologic_location
    click HydrologicLocation href "../HydrologicLocation"

        
      InterventionWithTracer : dosing_location
        
          
    
    
    InterventionWithTracer --> "1" DosingLocation : dosing_location
    click DosingLocation href "../DosingLocation"

        
      InterventionWithTracer : dosing_regimen
        
      InterventionWithTracer : end_datetime
        
      InterventionWithTracer : equilibration
        
          
    
    
    InterventionWithTracer --> "1" EquilibrationStatus : equilibration
    click EquilibrationStatus href "../EquilibrationStatus"

        
      InterventionWithTracer : experiment_id
        
      InterventionWithTracer : experiment_leads
        
          
    
    
    InterventionWithTracer --> "1..*" Person : experiment_leads
    click Person href "../Person"

        
      InterventionWithTracer : experiment_types
        
          
    
    
    InterventionWithTracer --> "1..*" ExperimentType : experiment_types
    click ExperimentType href "../ExperimentType"

        
      InterventionWithTracer : meteorological_and_tidal_data
        
          
    
    
    InterventionWithTracer --> "*" NamedLink : meteorological_and_tidal_data
    click NamedLink href "../NamedLink"

        
      InterventionWithTracer : name
        
      InterventionWithTracer : permits
        
          
    
    
    InterventionWithTracer --> "*" Permit : permits
    click Permit href "../Permit"

        
      InterventionWithTracer : project_id
        
      InterventionWithTracer : public_comments
        
          
    
    
    InterventionWithTracer --> "* _recommended_" PublicComment : public_comments
    click PublicComment href "../PublicComment"

        
      InterventionWithTracer : spatial_coverage
        
          
    
    
    InterventionWithTracer --> "1" SpatialCoverage : spatial_coverage
    click SpatialCoverage href "../SpatialCoverage"

        
      InterventionWithTracer : start_datetime
        
      InterventionWithTracer : tracer_concentration
        
          
    
    
    InterventionWithTracer --> "1" DosingConcentration : tracer_concentration
    click DosingConcentration href "../DosingConcentration"

        
      InterventionWithTracer : tracer_details
        
      InterventionWithTracer : tracer_form
        
          
    
    
    InterventionWithTracer --> "1" TracerForm : tracer_form
    click TracerForm href "../TracerForm"

        
      InterventionWithTracer : tracer_form_custom
        
      InterventionWithTracer : vertical_coverage
        
          
    
    
    InterventionWithTracer --> "0..1" VerticalExtent : vertical_coverage
    click VerticalExtent href "../VerticalExtent"

        
      
```





## Inheritance
* [Experiment](Experiment.md)
    * [InSituExperiment](InSituExperiment.md)
        * [Intervention](Intervention.md) [ [InterventionDetails](InterventionDetails.md) [DosingDetails](DosingDetails.md)]
            * **InterventionWithTracer** [ [TracerDetails](TracerDetails.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [tracer_form](tracer_form.md) | 1 <br/> [TracerForm](TracerForm.md) | The form of tracer upon delivery to the ocean (e | [TracerDetails](TracerDetails.md) |
| [tracer_form_custom](tracer_form_custom.md) | 0..1 <br/> [String](String.md) | If "other" was selected for Tracer Form, please specify the custom tracer for... | [TracerDetails](TracerDetails.md) |
| [tracer_details](tracer_details.md) | 1 <br/> [String](String.md) | state the kind of tracer used (e | [TracerDetails](TracerDetails.md) |
| [tracer_concentration](tracer_concentration.md) | 1 <br/> [DosingConcentration](DosingConcentration.md) | Fixed concentration or provide link/source to tracer concentration separately... | [TracerDetails](TracerDetails.md) |
| [alkalinity_feedstock_processing](alkalinity_feedstock_processing.md) | 1 <br/> [AlkalinityFeedstockProcessing](AlkalinityFeedstockProcessing.md) | Method(s) used to process the alkalinity feedstock | [InterventionDetails](InterventionDetails.md) |
| [alkalinity_feedstock_processing_custom](alkalinity_feedstock_processing_custom.md) | 0..1 <br/> [String](String.md) | Custom description of alkalinity feedstock processing method when 'other' is ... | [InterventionDetails](InterventionDetails.md) |
| [alkalinity_feedstock_form](alkalinity_feedstock_form.md) | 1 <br/> [AlkalinityFeedstockForm](AlkalinityFeedstockForm.md) | The phase upon delivery to the ocean | [InterventionDetails](InterventionDetails.md) |
| [alkalinity_feedstock](alkalinity_feedstock.md) | 1 <br/> [FeedstockType](FeedstockType.md) | Examples may include: olivine, potassium hydroxide, magnesium hydroxide, lime... | [InterventionDetails](InterventionDetails.md) |
| [alkalinity_feedstock_custom](alkalinity_feedstock_custom.md) | 0..1 <br/> [String](String.md) | Custom description of alkalinity feedstock when using a feedstock type not li... | [InterventionDetails](InterventionDetails.md) |
| [alkalinity_feedstock_co2_removal_potential](alkalinity_feedstock_co2_removal_potential.md) | 1 <br/> [Float](Float.md) | Maximum CO₂ removal potential of a feedstock material | [InterventionDetails](InterventionDetails.md) |
| [alkalinity_feedstock_description](alkalinity_feedstock_description.md) | 1 <br/> [String](String.md) | Information such as feedstock source, characteristics, impurities, dilution p... | [InterventionDetails](InterventionDetails.md) |
| [equilibration](equilibration.md) | 1 <br/> [EquilibrationStatus](EquilibrationStatus.md) | Whether the feedstock was pre-equilibrated or unequilibrated | [InterventionDetails](InterventionDetails.md) |
| [alkalinity_dosing_effluent_density](alkalinity_dosing_effluent_density.md) | 1 <br/> [DosingConcentration](DosingConcentration.md) | Fixed density or provide link/source to effluent density data if applicable | [InterventionDetails](InterventionDetails.md) |
| [dosing_delivery_type](dosing_delivery_type.md) | 1 <br/> [DosingDeliveryType](DosingDeliveryType.md) | Type of dosing delivery method | [DosingDetails](DosingDetails.md) |
| [dosing_location](dosing_location.md) | 1 <br/> [DosingLocation](DosingLocation.md) | Provide latitude and longitude in decimal degrees | [DosingDetails](DosingDetails.md) |
| [dosing_dispersal_hydrologic_location](dosing_dispersal_hydrologic_location.md) | 1 <br/> [HydrologicLocation](HydrologicLocation.md) | Descriptive dosing location | [DosingDetails](DosingDetails.md) |
| [dosing_depth](dosing_depth.md) | 1 <br/> [String](String.md) | Depth in meters | [DosingDetails](DosingDetails.md) |
| [dosing_regimen](dosing_regimen.md) | 1 <br/> [String](String.md) | A human readable summary description of the dosing regimen / frequency | [DosingDetails](DosingDetails.md) |
| [dosing_description](dosing_description.md) | 1 <br/> [String](String.md) | Please be descriptive | [DosingDetails](DosingDetails.md) |
| [vertical_coverage](vertical_coverage.md) | 0..1 <br/> [VerticalExtent](VerticalExtent.md) | Minimum and maximum depths of observations in meters | [InSituExperiment](InSituExperiment.md) |
| [permits](permits.md) | * <br/> [Permit](Permit.md) | Associated permit number(s) | [InSituExperiment](InSituExperiment.md) |
| [data_conflicts_and_unreported_data](data_conflicts_and_unreported_data.md) | 0..1 <br/> [String](String.md) | If data exist that are or have been used by the project but are not provided ... | [InSituExperiment](InSituExperiment.md) |
| [meteorological_and_tidal_data](meteorological_and_tidal_data.md) | * <br/> [NamedLink](NamedLink.md) | Include links to relevant open datasets if referenced in the experiment but n... | [InSituExperiment](InSituExperiment.md) |
| [additional_details](additional_details.md) | 0..1 <br/> [String](String.md) | Open text area to include additional information | [InSituExperiment](InSituExperiment.md) |
| [name](name.md) | 1 <br/> [String](String.md) | Common name for experiment | [Experiment](Experiment.md) |
| [description](description.md) | 1 <br/> [String](String.md) | A narrative description of the experiment | [Experiment](Experiment.md) |
| [spatial_coverage](spatial_coverage.md) | 1 <br/> [SpatialCoverage](SpatialCoverage.md) | Latitude/longitude bounds of observed data in experiment, expressed as a sche... | [Experiment](Experiment.md) |
| [project_id](project_id.md) | 1 <br/> [String](String.md) | The project to which the submitted data belong | [Experiment](Experiment.md) |
| [experiment_id](experiment_id.md) | 1 <br/> [String](String.md) | The experiment to which the data belong | [Experiment](Experiment.md) |
| [experiment_types](experiment_types.md) | 1..* <br/> [ExperimentType](ExperimentType.md) | The type(s) of mCDR experiment conducted | [Experiment](Experiment.md) |
| [public_comments](public_comments.md) | * _recommended_ <br/> [PublicComment](PublicComment.md) | Public comment documents, each with a link or DOI and an optional description | [Experiment](Experiment.md) |
| [experiment_leads](experiment_leads.md) | 1..* <br/> [Person](Person.md) | Provide details for each experiment lead / principal investigator (PI) includ... | [Experiment](Experiment.md) |
| [start_datetime](start_datetime.md) | 1 <br/> [Datetime](Datetime.md) | Start date and time of experiment in UTC ISO-8601 | [Experiment](Experiment.md) |
| [end_datetime](end_datetime.md) | 0..1 <br/> [Datetime](Datetime.md) | End date and time of experiment in UTC ISO-8601 | [Experiment](Experiment.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [experiments](experiments.md) | any_of[range] | [InterventionWithTracer](InterventionWithTracer.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:InterventionWithTracer |
| native | oae:InterventionWithTracer |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InterventionWithTracer
description: Additional metadata that applies to hybrid experiments where an intervention
  was conducted simultaneously alongside a tracer study, using the same instrumentation.
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: Intervention
mixins:
- TracerDetails
rules:
- preconditions:
    slot_conditions:
      tracer_form:
        name: tracer_form
        equals_string: other
  postconditions:
    slot_conditions:
      tracer_form_custom:
        name: tracer_form_custom
        required: true

```
</details>

### Induced

<details>
```yaml
name: InterventionWithTracer
description: Additional metadata that applies to hybrid experiments where an intervention
  was conducted simultaneously alongside a tracer study, using the same instrumentation.
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: Intervention
mixins:
- TracerDetails
attributes:
  tracer_form:
    name: tracer_form
    description: The form of tracer upon delivery to the ocean (e.g. gas or dye-release)
    title: Tracer Form
    from_schema: Experiment
    rank: 1000
    alias: tracer_form
    owner: InterventionWithTracer
    domain_of:
    - TracerDetails
    range: TracerForm
    required: true
  tracer_form_custom:
    name: tracer_form_custom
    description: If "other" was selected for Tracer Form, please specify the custom
      tracer form here.
    title: Tracer Form (Custom)
    from_schema: Experiment
    rank: 1000
    alias: tracer_form_custom
    owner: InterventionWithTracer
    domain_of:
    - TracerDetails
    range: string
  tracer_details:
    name: tracer_details
    description: state the kind of tracer used (e.g. rhodamine, or a specific gas)
    title: Tracer Details
    from_schema: Experiment
    rank: 1000
    alias: tracer_details
    owner: InterventionWithTracer
    domain_of:
    - TracerDetails
    range: string
    required: true
  tracer_concentration:
    name: tracer_concentration
    description: Fixed concentration or provide link/source to tracer concentration
      separately in the dosing file. Please include whether concentration is directly
      measured or a derived value. If this is a variable included with your data,
      please note so here as 'tracer concentration provided as a variable' and use
      'tracer_concentration' for your column header name.
    title: Tracer Concentration
    from_schema: Experiment
    rank: 1000
    alias: tracer_concentration
    owner: InterventionWithTracer
    domain_of:
    - TracerDetails
    range: DosingConcentration
    required: true
  alkalinity_feedstock_processing:
    name: alkalinity_feedstock_processing
    description: Method(s) used to process the alkalinity feedstock. See Controlled
      Vocabularies section for definitions.
    title: Alkalinity Feedstock Processing
    from_schema: Experiment
    rank: 1000
    alias: alkalinity_feedstock_processing
    owner: InterventionWithTracer
    domain_of:
    - InterventionDetails
    range: AlkalinityFeedstockProcessing
    required: true
  alkalinity_feedstock_processing_custom:
    name: alkalinity_feedstock_processing_custom
    description: Custom description of alkalinity feedstock processing method when
      'other' is selected in alkalinity_feedstock_processing.
    title: Alkalinity Feedstock Processing (Custom)
    from_schema: Experiment
    rank: 1000
    alias: alkalinity_feedstock_processing_custom
    owner: InterventionWithTracer
    domain_of:
    - InterventionDetails
    range: string
  alkalinity_feedstock_form:
    name: alkalinity_feedstock_form
    description: The phase upon delivery to the ocean. See Controlled Vocabularies
      section for definitions.
    title: Alkalinity Feedstock Form
    from_schema: Experiment
    rank: 1000
    alias: alkalinity_feedstock_form
    owner: InterventionWithTracer
    domain_of:
    - InterventionDetails
    range: AlkalinityFeedstockForm
    required: true
  alkalinity_feedstock:
    name: alkalinity_feedstock
    description: 'Examples may include: olivine, potassium hydroxide, magnesium hydroxide,
      lime, portlandite, calcium carbonate, anorthite, dolomite, periclase, brucite,
      magnesite, forsterite, sodium hydroxide, natrite, nahcolite, akermanite, akermanite,
      alunoakermanite, etc.

      See Controlled Vocabularies section for selected examples (this list is not
      exhaustive, you may need to include your unique feedstock).'
    title: Alkalinity Feedstock
    from_schema: Experiment
    rank: 1000
    alias: alkalinity_feedstock
    owner: InterventionWithTracer
    domain_of:
    - InterventionDetails
    range: FeedstockType
    required: true
  alkalinity_feedstock_custom:
    name: alkalinity_feedstock_custom
    description: Custom description of alkalinity feedstock when using a feedstock
      type not listed in the controlled vocabulary.
    title: Alkalinity Feedstock (Custom)
    from_schema: Experiment
    rank: 1000
    alias: alkalinity_feedstock_custom
    owner: InterventionWithTracer
    domain_of:
    - InterventionDetails
    range: string
  alkalinity_feedstock_co2_removal_potential:
    name: alkalinity_feedstock_co2_removal_potential
    description: Maximum CO₂ removal potential of a feedstock material. We recommend
      using an adjusted version of the Steinour equation (Gunning et al., 2010), which
      uses bulk elemental oxide composition to estimate the maximum CO₂ removal potential
      of a feedstock material. The calculation output is in the form of kg of CO₂
      per tonne of feedstock and represents the quantitative hypothetical potential
      of the material to capture CO₂ as bicarbonate or carbonate. See Isometric's
      CO2 removal potential module for details.
    title: Alkalinity Feedstock CO₂ Removal Potential
    from_schema: Experiment
    rank: 1000
    alias: alkalinity_feedstock_co2_removal_potential
    owner: InterventionWithTracer
    domain_of:
    - InterventionDetails
    range: float
    required: true
  alkalinity_feedstock_description:
    name: alkalinity_feedstock_description
    description: 'Information such as feedstock source, characteristics, impurities,
      dilution prior to dosing, and concentration. For feedstock other than NaOH:
      trace metal composition and particulate grain size. Any variable information
      must be provided in the dosing data file, in this case include the data file
      and column header names here provided as variables. See [Intervention Data](https://www.carbontosea.org/oae-data-protocol/1-0-0/#intervention-data)
      for details.'
    title: Alkalinity Feedstock Description
    from_schema: Experiment
    rank: 1000
    alias: alkalinity_feedstock_description
    owner: InterventionWithTracer
    domain_of:
    - InterventionDetails
    range: string
    required: true
  equilibration:
    name: equilibration
    description: Whether the feedstock was pre-equilibrated or unequilibrated
    title: Equilibration
    from_schema: Experiment
    rank: 1000
    alias: equilibration
    owner: InterventionWithTracer
    domain_of:
    - InterventionDetails
    range: EquilibrationStatus
    required: true
  alkalinity_dosing_effluent_density:
    name: alkalinity_dosing_effluent_density
    description: Fixed density or provide link/source to effluent density data if
      applicable. Please include whether density is directly measured or a derived
      value. If this is a variable included with your data, please note so here as
      'alkalinity dosing effluent density is provided as a variable' and use 'dosing_effluent_density'
      for your column header name.
    title: Alkalinity Dosing Effluent Density
    from_schema: Experiment
    rank: 1000
    alias: alkalinity_dosing_effluent_density
    owner: InterventionWithTracer
    domain_of:
    - InterventionDetails
    range: DosingConcentration
    required: true
  dosing_delivery_type:
    name: dosing_delivery_type
    description: Type of dosing delivery method. See Controlled Vocabularies for definitions.
    title: Dosing Delivery Type
    from_schema: Experiment
    rank: 1000
    alias: dosing_delivery_type
    owner: InterventionWithTracer
    domain_of:
    - DosingDetails
    range: DosingDeliveryType
    required: true
  dosing_location:
    name: dosing_location
    description: Provide latitude and longitude in decimal degrees. Depending on your
      method of dispersal, this information may be provided as a point source, vector,
      or bounding box. If provided as a vector, the latitude and longitude values
      should be included in the dosing data file.
    title: Dosing Location
    from_schema: Experiment
    rank: 1000
    alias: dosing_location
    owner: InterventionWithTracer
    domain_of:
    - DosingDetails
    range: DosingLocation
    required: true
  dosing_dispersal_hydrologic_location:
    name: dosing_dispersal_hydrologic_location
    description: Descriptive dosing location
    title: Dosing Dispersal Hydrologic Location
    from_schema: Experiment
    rank: 1000
    alias: dosing_dispersal_hydrologic_location
    owner: InterventionWithTracer
    domain_of:
    - DosingDetails
    range: HydrologicLocation
    required: true
  dosing_depth:
    name: dosing_depth
    description: Depth in meters. If this is variable, please include the schedule
      of depth changes and depths, or as a vector in meters with the data.
    title: Dosing Depth
    from_schema: Experiment
    rank: 1000
    alias: dosing_depth
    owner: InterventionWithTracer
    domain_of:
    - DosingDetails
    range: string
    required: true
  dosing_regimen:
    name: dosing_regimen
    description: A human readable summary description of the dosing regimen / frequency.
      Exact details must be provided in the corresponding dosing file with exact timestamps
      for dosing on/off schedule.
    title: Dosing Regimen
    from_schema: Experiment
    rank: 1000
    alias: dosing_regimen
    owner: InterventionWithTracer
    domain_of:
    - DosingDetails
    range: string
    required: true
  dosing_description:
    name: dosing_description
    description: 'Please be descriptive. Information about the dosing mechanism must
      be included (outflow from pipe, diffuser, doser, manual placement)

      E.g., outflow from existing facility pipe directly to ocean, manual riverine
      introduction, coastal distribution at three separate 30 meter long sections,
      pier-based diffuser to intercoastal bay, distributed from stationary barge 10
      miles offshore.'
    title: Dosing Description
    from_schema: Experiment
    rank: 1000
    alias: dosing_description
    owner: InterventionWithTracer
    domain_of:
    - DosingDetails
    range: string
    required: true
  vertical_coverage:
    name: vertical_coverage
    description: Minimum and maximum depths of observations in meters.
    title: Vertical Coverage
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: vertical_coverage
    owner: InterventionWithTracer
    domain_of:
    - InSituExperiment
    range: VerticalExtent
  permits:
    name: permits
    description: Associated permit number(s).
    title: Permits
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: permits
    owner: InterventionWithTracer
    domain_of:
    - InSituExperiment
    range: Permit
    multivalued: true
    inlined: true
    inlined_as_list: true
  data_conflicts_and_unreported_data:
    name: data_conflicts_and_unreported_data
    description: If data exist that are or have been used by the project but are not
      provided due to conflicts (e.g., geopolitical or other), data availability (e.g.,
      a dataset is no longer available), it may be noted here.
    title: Data Conflicts and Unreported Data
    from_schema: Experiment
    rank: 1000
    alias: data_conflicts_and_unreported_data
    owner: InterventionWithTracer
    domain_of:
    - InSituExperiment
    range: string
  meteorological_and_tidal_data:
    name: meteorological_and_tidal_data
    description: Include links to relevant open datasets if referenced in the experiment
      but not provided in the submission.
    title: Meteorological and Tidal Data
    from_schema: Experiment
    rank: 1000
    alias: meteorological_and_tidal_data
    owner: InterventionWithTracer
    domain_of:
    - InSituExperiment
    range: NamedLink
    multivalued: true
    inlined: true
    inlined_as_list: true
  additional_details:
    name: additional_details
    description: Open text area to include additional information. These may include
      information for sediment processes data, biological data, or any other required
      information if not included in the main metadata or data files; see General
      Guidelines for Your Data for relevant sections of your data. Additional informational
      files, such as digitized laboratory notebooks, blogs, etc., may be linked here.
    title: Additional Details
    from_schema: Experiment
    alias: additional_details
    owner: InterventionWithTracer
    domain_of:
    - Project
    - InSituExperiment
    range: string
  name:
    name: name
    description: Common name for experiment.
    title: Name
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    slot_uri: schema:name
    alias: name
    owner: InterventionWithTracer
    domain_of:
    - Organization
    - Project
    - NamedLink
    - ExternalProject
    - MonetaryGrant
    - Experiment
    - Person
    - Dataset
    - Platform
    - ModelComponent
    range: string
    required: true
  description:
    name: description
    description: A narrative description of the experiment. For example, what part
      of the project do these data represent (e.g., baseline, intervention, control)
      and what do they contribute to the overall project? Are all project research
      questions listed in Project description relevant? What were the processes to
      achieve these goals and answer these questions? Data submitters are encouraged
      to note any significant changes to the original experimental plan due to unforeseen
      circumstances here.
    title: Experiment Description
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    slot_uri: schema:description
    alias: description
    owner: InterventionWithTracer
    domain_of:
    - Project
    - ExternalProject
    - Experiment
    - PublicComment
    - VocabularyItemReference
    - Dataset
    - ModelComponent
    range: string
    required: true
  spatial_coverage:
    name: spatial_coverage
    description: Latitude/longitude bounds of observed data in experiment, expressed
      as a schema.org GeoShape bounding box.
    title: Spatial Coverage
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    slot_uri: schema:spatialCoverage
    alias: spatial_coverage
    owner: InterventionWithTracer
    domain_of:
    - Project
    - ExternalProject
    - Experiment
    - ModelGrid
    range: SpatialCoverage
    required: true
  project_id:
    name: project_id
    description: 'The project to which the submitted data belong. A unique project
      identifier that can be used to link project data across data submissions, and
      link baseline data to intervention data, for example.

      If no Project ID has been assigned, one may be generated by combining: lead
      organizer surname and first initial or company, a unique date, and location.

      Any method that creates a unique ID that will link all project data is acceptable.'
    title: Project ID
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: project_id
    owner: InterventionWithTracer
    domain_of:
    - Project
    - Experiment
    - Dataset
    range: string
    required: true
  experiment_id:
    name: experiment_id
    description: 'The experiment to which the data belong. Any naming convention that
      produces a unique ID is usable. The recommended naming convention is:

      Project ID + Experiment type + Optional numerical indicator to differentiate
      between various experiments of the same type for a project. A two digit consecutive
      number beginning with 01'
    title: Experiment ID
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: experiment_id
    owner: InterventionWithTracer
    domain_of:
    - Experiment
    - Dataset
    range: string
    required: true
  experiment_types:
    name: experiment_types
    description: The type(s) of mCDR experiment conducted. See Controlled Vocabularies
      section for definitions.
    title: mCDR Experiment Type(s)
    from_schema: Experiment
    rank: 1000
    alias: experiment_types
    owner: InterventionWithTracer
    domain_of:
    - Experiment
    range: ExperimentType
    required: true
    multivalued: true
  public_comments:
    name: public_comments
    description: 'Public comment documents, each with a link or DOI and an optional
      description.

      Please group/concatenate all public comments associated with a specific consultation
      (e.g., for permitting, non-mandated consultations on a specific topic, or informal
      public input such as unsolicited comments and media attention) into a single
      document if possible, and link to it here.'
    title: Public Comments
    from_schema: Experiment
    rank: 1000
    alias: public_comments
    owner: InterventionWithTracer
    domain_of:
    - Experiment
    range: PublicComment
    recommended: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  experiment_leads:
    name: experiment_leads
    description: 'Provide details for each experiment lead / principal investigator
      (PI) including: Name, institutional information (name, address), phone, email,
      ID type (e.g., ORCID, etc), researcher ID, and role.'
    title: Experiment Lead(s)
    from_schema: Experiment
    rank: 1000
    alias: experiment_leads
    owner: InterventionWithTracer
    domain_of:
    - Experiment
    range: Person
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  start_datetime:
    name: start_datetime
    description: Start date and time of experiment in UTC ISO-8601
    title: Start Date and Time (UTC)
    from_schema: Experiment
    rank: 1000
    alias: start_datetime
    owner: InterventionWithTracer
    domain_of:
    - Experiment
    - ModelOutputDataset
    range: datetime
    required: true
  end_datetime:
    name: end_datetime
    description: End date and time of experiment in UTC ISO-8601
    title: End Date and Time (UTC)
    from_schema: Experiment
    rank: 1000
    alias: end_datetime
    owner: InterventionWithTracer
    domain_of:
    - Experiment
    - ModelOutputDataset
    range: datetime
rules:
- preconditions:
    slot_conditions:
      tracer_form:
        name: tracer_form
        equals_string: other
  postconditions:
    slot_conditions:
      tracer_form_custom:
        name: tracer_form_custom
        required: true

```
</details>