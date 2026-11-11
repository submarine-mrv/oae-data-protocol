

# Slot: Experiment Lead(s) (experiment_leads)


_Provide details for each experiment lead / principal investigator (PI) including: Name, institutional information (name, address), phone, email, ID type (e.g., ORCID, etc), researcher ID, and role._





URI: [oae:experiment_leads](https://schema.oaedata.org/experiment_leads)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [Model](Model.md) | A computational model experiment related to OAE |  no  |
| [Experiment](Experiment.md) | Abstract base class for all experiment types |  no  |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |
| [Tracer](Tracer.md) | Additional metadata that applies to experiments where a tracer study was cond... |  no  |
| [InSituExperiment](InSituExperiment.md) | Experiment metadata for in-situ studies (interventions, tracer studies, etc |  no  |







## Properties

* Range: [Person](Person.md)

* Multivalued: True

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:experiment_leads |
| native | oae:experiment_leads |




## LinkML Source

<details>
```yaml
name: experiment_leads
description: 'Provide details for each experiment lead / principal investigator (PI)
  including: Name, institutional information (name, address), phone, email, ID type
  (e.g., ORCID, etc), researcher ID, and role.'
title: Experiment Lead(s)
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: experiment_leads
owner: Experiment
domain_of:
- Experiment
range: Person
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>