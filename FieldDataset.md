

# Class: FieldDataset


_A field or observational dataset related to an OAE experiment. Contains fields specific to in-situ data collection such as platform information, calibration files, QC flags, and measured variables._





URI: [oae:FieldDataset](https://schema.oaedata.org/FieldDataset)






```mermaid
 classDiagram
    class FieldDataset
    click FieldDataset href "../FieldDataset"
      Dataset <|-- FieldDataset
        click Dataset href "../Dataset"
      
      FieldDataset : author_list_for_citation
        
      FieldDataset : calibration_files
        
      FieldDataset : data_access_date
        
      FieldDataset : data_access_link
        
      FieldDataset : data_accessibility
        
          
    
    
    FieldDataset --> "1" DataAccessibility : data_accessibility
    click DataAccessibility href "../DataAccessibility"

        
      FieldDataset : data_product_type
        
          
    
    
    FieldDataset --> "1" DataProductType : data_product_type
    click DataProductType href "../DataProductType"

        
      FieldDataset : data_submitter
        
          
    
    
    FieldDataset --> "1" Person : data_submitter
    click Person href "../Person"

        
      FieldDataset : dataset_type
        
          
    
    
    FieldDataset --> "1" DatasetType : dataset_type
    click DatasetType href "../DatasetType"

        
      FieldDataset : dataset_type_custom
        
      FieldDataset : description
        
      FieldDataset : experiment_id
        
      FieldDataset : fair_use_data_request
        
      FieldDataset : filenames
        
      FieldDataset : license
        
      FieldDataset : name
        
      FieldDataset : platform_info
        
          
    
    
    FieldDataset --> "1" Platform : platform_info
    click Platform href "../Platform"

        
      FieldDataset : project_id
        
      FieldDataset : qc_flag_scheme
        
      FieldDataset : temporal_coverage
        
      FieldDataset : variables
        
          
    
    
    FieldDataset --> "*" FieldVariable : variables
    click FieldVariable href "../FieldVariable"

        
      
```





## Inheritance
* [Dataset](Dataset.md)
    * **FieldDataset**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [temporal_coverage](temporal_coverage.md) | 1 <br/> [String](String.md) | Start date and end date (if known) of the project in ISO-8601 interval format... | direct |
| [variables](variables.md) | * <br/> [FieldVariable](FieldVariable.md) | The variables in this dataset, each with its own metadata | direct |
| [data_product_type](data_product_type.md) | 1 <br/> [DataProductType](DataProductType.md) | One of the three choices: (a) Originally collected dataset (e | direct |
| [qc_flag_scheme](qc_flag_scheme.md) | 0..1 <br/> [String](String.md) | Describe what the quality control flags stand for, e | direct |
| [platform_info](platform_info.md) | 1 <br/> [Platform](Platform.md) |  | direct |
| [calibration_files](calibration_files.md) | * <br/> [String](String.md) | A list of supplementary file names containing coefficients and techniques use... | direct |
| [name](name.md) | 1 <br/> [String](String.md) | A brief descriptive sentence that summarizes the content of a dataset | [Dataset](Dataset.md) |
| [description](description.md) | 1 <br/> [String](String.md) | The abstract of a dataset is a brief summary that provides an overview of the... | [Dataset](Dataset.md) |
| [project_id](project_id.md) | 1 <br/> [String](String.md) | The project to which the submitted data belong | [Dataset](Dataset.md) |
| [experiment_id](experiment_id.md) | 1 <br/> [String](String.md) | The experiment to which the data belong | [Dataset](Dataset.md) |
| [filenames](filenames.md) | 1..* <br/> [String](String.md) |  | [Dataset](Dataset.md) |
| [dataset_type](dataset_type.md) | 1 <br/> [DatasetType](DatasetType.md) | Selected controlled vocabularies for data types relevant to mCDR have been re... | [Dataset](Dataset.md) |
| [dataset_type_custom](dataset_type_custom.md) | 0..1 <br/> [String](String.md) | Custom "data type" when an appropriate value is not found in the controlled v... | [Dataset](Dataset.md) |
| [data_submitter](data_submitter.md) | 1 <br/> [Person](Person.md) | Information about the individual submitting the dataset(s), including contact... | [Dataset](Dataset.md) |
| [author_list_for_citation](author_list_for_citation.md) | 0..1 <br/> [String](String.md) | Author list in the format of Lastname1, Firstname1 Middlename1; Lastname2, Fi... | [Dataset](Dataset.md) |
| [license](license.md) | 0..1 <br/> [uri](uri.md) | Link a Dataset to its license to document legal constraints by adding a schem... | [Dataset](Dataset.md) |
| [fair_use_data_request](fair_use_data_request.md) | 0..1 <br/> [String](String.md) | A statement from the data producer regarding how this dataset should be used | [Dataset](Dataset.md) |
| [data_accessibility](data_accessibility.md) | 1 <br/> [DataAccessibility](DataAccessibility.md) | Level of access to this dataset | [Dataset](Dataset.md) |
| [data_access_link](data_access_link.md) | 0..1 <br/> [uri](uri.md) | URL to access this dataset, if it is already archived or published elsewhere | [Dataset](Dataset.md) |
| [data_access_date](data_access_date.md) | 0..1 <br/> [Date](Date.md) | The date by when this dataset will be openly available on a public repository | [Dataset](Dataset.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Container](Container.md) | [datasets](datasets.md) | any_of[range] | [FieldDataset](FieldDataset.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:FieldDataset |
| native | oae:FieldDataset |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FieldDataset
description: A field or observational dataset related to an OAE experiment. Contains
  fields specific to in-situ data collection such as platform information, calibration
  files, QC flags, and measured variables.
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: Dataset
slots:
- temporal_coverage
- variables
slot_usage:
  variables:
    name: variables
    range: FieldVariable
attributes:
  data_product_type:
    name: data_product_type
    description: 'One of the three choices: (a) Originally collected dataset (e.g.,
      a dataset collected from a research cruise or laboratory experiment), (b) Data
      compilation product (e.g., SOCAT, GLODAP), or (c) Derived product (e.g., gridded
      products, or model output).'
    title: Data Product Type
    from_schema: Dataset
    rank: 1000
    domain_of:
    - FieldDataset
    range: DataProductType
    required: true
  qc_flag_scheme:
    name: qc_flag_scheme
    description: "Describe what the quality control flags stand for, e.g.,\n  0 =\
      \ interpolated or calculated data\n  1 = not evaluated/quality unknown\n  2\
      \ = acceptable\n  3 = questionable\n  4 = known bad\n  6 = median of replicates\n\
      \  9 = missing value\""
    title: QC Flag Scheme
    from_schema: Dataset
    rank: 1000
    domain_of:
    - FieldDataset
    range: string
  platform_info:
    name: platform_info
    title: Platform Information
    from_schema: Dataset
    rank: 1000
    domain_of:
    - FieldDataset
    range: Platform
    required: true
  calibration_files:
    name: calibration_files
    description: A list of supplementary file names containing coefficients and techniques
      used to calibrate the instruments used in data collection. The named files can
      be found within the relevant documents folder accompanying the submitted data
      files.
    title: Calibration Files (required if providing sensor data)
    from_schema: Dataset
    rank: 1000
    domain_of:
    - FieldDataset
    range: string
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: FieldDataset
description: A field or observational dataset related to an OAE experiment. Contains
  fields specific to in-situ data collection such as platform information, calibration
  files, QC flags, and measured variables.
from_schema: https://schema.oaedata.org/OAEDataSchema
is_a: Dataset
slot_usage:
  variables:
    name: variables
    range: FieldVariable
attributes:
  data_product_type:
    name: data_product_type
    description: 'One of the three choices: (a) Originally collected dataset (e.g.,
      a dataset collected from a research cruise or laboratory experiment), (b) Data
      compilation product (e.g., SOCAT, GLODAP), or (c) Derived product (e.g., gridded
      products, or model output).'
    title: Data Product Type
    from_schema: Dataset
    rank: 1000
    alias: data_product_type
    owner: FieldDataset
    domain_of:
    - FieldDataset
    range: DataProductType
    required: true
  qc_flag_scheme:
    name: qc_flag_scheme
    description: "Describe what the quality control flags stand for, e.g.,\n  0 =\
      \ interpolated or calculated data\n  1 = not evaluated/quality unknown\n  2\
      \ = acceptable\n  3 = questionable\n  4 = known bad\n  6 = median of replicates\n\
      \  9 = missing value\""
    title: QC Flag Scheme
    from_schema: Dataset
    rank: 1000
    alias: qc_flag_scheme
    owner: FieldDataset
    domain_of:
    - FieldDataset
    range: string
  platform_info:
    name: platform_info
    title: Platform Information
    from_schema: Dataset
    rank: 1000
    alias: platform_info
    owner: FieldDataset
    domain_of:
    - FieldDataset
    range: Platform
    required: true
  calibration_files:
    name: calibration_files
    description: A list of supplementary file names containing coefficients and techniques
      used to calibrate the instruments used in data collection. The named files can
      be found within the relevant documents folder accompanying the submitted data
      files.
    title: Calibration Files (required if providing sensor data)
    from_schema: Dataset
    rank: 1000
    alias: calibration_files
    owner: FieldDataset
    domain_of:
    - FieldDataset
    range: string
    multivalued: true
  temporal_coverage:
    name: temporal_coverage
    description: Start date and end date (if known) of the project in ISO-8601 interval
      format (YYYY-MM-DD/YYY-MM-DD). If the end date is not known, use open-ended
      format YYYY-MM-DD/..
    title: Temporal Coverage
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    slot_uri: schema:temporalCoverage
    alias: temporal_coverage
    owner: FieldDataset
    domain_of:
    - Project
    - ExternalProject
    - FieldDataset
    range: string
    required: true
    pattern: ^\d{4}-\d{2}-\d{2}/(\d{4}-\d{2}-\d{2}|\.\.)$
  variables:
    name: variables
    description: The variables in this dataset, each with its own metadata.
    title: Variables
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    slot_uri: schema:variableMeasured
    alias: variables
    owner: FieldDataset
    domain_of:
    - FieldDataset
    - ModelOutputDataset
    range: FieldVariable
    multivalued: true
  name:
    name: name
    description: 'A brief descriptive sentence that summarizes the content of a dataset.
      Here is one example:

      "Dissolved inorganic carbon, total alkalinity, pH, temperature, salinity and
      other variables collected from profile and discrete sample observations using
      CTD, Niskin bottle, and other instruments from R/V Wecoma in the U.S. West Coast
      California Current System during the 2011 West Coast Ocean Acidification Cruise
      (WCOA2011) from 2011-08-12 to 2011-08-30"'
    title: Dataset Title
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    slot_uri: schema:name
    alias: name
    owner: FieldDataset
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
    description: The abstract of a dataset is a brief summary that provides an overview
      of the dataset's content, purpose, and scope. It is used to provide context
      and background information to users who are interested in using the dataset.
      An abstract may include information such as the dataset's source, how the data
      was collected or generated, the variables or attributes included in the dataset,
      and any limitations or restrictions on the use of the data. It may also include
      information on how the data can be accessed or used.
    title: Description
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    slot_uri: schema:description
    alias: description
    owner: FieldDataset
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
    owner: FieldDataset
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
    owner: FieldDataset
    domain_of:
    - Experiment
    - Dataset
    range: string
    required: true
  filenames:
    name: filenames
    title: Filenames
    from_schema: https://schema.oaedata.org/OAEDataSchema
    rank: 1000
    alias: filenames
    owner: FieldDataset
    domain_of:
    - Dataset
    range: string
    required: true
    multivalued: true
    minimum_cardinality: 1
  dataset_type:
    name: dataset_type
    description: Selected controlled vocabularies for data types relevant to mCDR
      have been referenced from NASA's SeaBASS metadata system and are provided below,
      for additional data types of optical characteristics see the [SeaBASS controlled
      definitions list](https://seabass.gsfc.nasa.gov/wiki/metadataheaders#data_type).
      Additional data types have been included to meet the needs of mCDR field projects.
    title: Dataset Type
    from_schema: Dataset
    rank: 1000
    alias: dataset_type
    owner: FieldDataset
    domain_of:
    - Dataset
    range: DatasetType
    required: true
  dataset_type_custom:
    name: dataset_type_custom
    description: Custom "data type" when an appropriate value is not found in the
      controlled vocabulary list for mCDR Data Type and the corresponding `data_type`
      field is set to "other".
    title: Dataset Type (Custom)
    from_schema: Dataset
    rank: 1000
    alias: dataset_type_custom
    owner: FieldDataset
    domain_of:
    - Dataset
    range: string
  data_submitter:
    name: data_submitter
    description: Information about the individual submitting the dataset(s), including
      contact information
    title: Data Submitter
    from_schema: Dataset
    rank: 1000
    alias: data_submitter
    owner: FieldDataset
    domain_of:
    - Dataset
    range: Person
    required: true
  author_list_for_citation:
    name: author_list_for_citation
    description: Author list in the format of Lastname1, Firstname1 Middlename1; Lastname2,
      Firstname2 Middlename2; ...
    title: Author List (for citation)
    from_schema: Dataset
    rank: 1000
    alias: author_list_for_citation
    owner: FieldDataset
    domain_of:
    - Dataset
    range: string
  license:
    name: license
    description: Link a Dataset to its license to document legal constraints by adding
      a schema:license property. The guide recommends providing a URL that unambiguously
      identifies a specific version of the license used, but for many licenses it
      is hard to determine what that URL should be. Thus, we recommend that the license
      URL be drawn from the [SPDX license list](https://spdx.org/licenses/), which
      provides a curated list of licenses and their properties that is well maintained.
      For each SPDX entry, SPDX provides a canonical URL for the license (e.g., http://spdx.org/licenses/CC0-1.0),
      a unique licenseId (e.g., CC0-1.0), and other metadata about the license.
    title: License
    from_schema: Dataset
    rank: 1000
    slot_uri: schema:license
    alias: license
    owner: FieldDataset
    domain_of:
    - Dataset
    range: uri
  fair_use_data_request:
    name: fair_use_data_request
    description: A statement from the data producer regarding how this dataset should
      be used.
    title: Fair Use Data Request
    from_schema: Dataset
    rank: 1000
    alias: fair_use_data_request
    owner: FieldDataset
    domain_of:
    - Dataset
    range: string
  data_accessibility:
    name: data_accessibility
    description: Level of access to this dataset. Open Access data are freely available
      now, without restriction. Conditional Access data are available upon request,
      subject to review. Scheduled Access data will become openly available after
      a specified date; choose it for any data that are not openly available yet.
    title: Data Accessibility
    from_schema: Dataset
    rank: 1000
    alias: data_accessibility
    owner: FieldDataset
    domain_of:
    - Dataset
    range: DataAccessibility
    required: true
  data_access_link:
    name: data_access_link
    description: URL to access this dataset, if it is already archived or published
      elsewhere. DOIs are preferred if available (e.g., https://doi.org/10.25921/xxxx-xxx).
      Required for open access, optional otherwise.
    title: Data Access Link
    from_schema: Dataset
    rank: 1000
    alias: data_access_link
    owner: FieldDataset
    domain_of:
    - Dataset
    range: uri
    pattern: ^https?://.+
  data_access_date:
    name: data_access_date
    description: The date by when this dataset will be openly available on a public
      repository. Only used when data_accessibility is scheduled_access; leave empty
      otherwise.
    title: Data Access Date
    from_schema: Dataset
    rank: 1000
    alias: data_access_date
    owner: FieldDataset
    domain_of:
    - Dataset
    range: date

```
</details>