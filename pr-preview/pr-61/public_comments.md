

# Slot: Public Comments (public_comments)


_Public comment documents, each with a link or DOI and an optional description._

_Please group/concatenate all public comments associated with a specific consultation (e.g., for permitting, non-mandated consultations on a specific topic, or informal public input such as unsolicited comments and media attention) into a single document if possible, and link to it here._





URI: [oae:public_comments](https://schema.oaedata.org/public_comments)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Tracer](Tracer.md) | Additional metadata that applies to experiments where a tracer study was cond... |  no  |
| [Model](Model.md) | A computational model experiment related to OAE |  no  |
| [Intervention](Intervention.md) | Additional metadata that applies to experiments where an intervention, such a... |  no  |
| [InterventionWithTracer](InterventionWithTracer.md) | Additional metadata that applies to hybrid experiments where an intervention ... |  no  |
| [InSituExperiment](InSituExperiment.md) | Experiment metadata for in-situ studies (interventions, tracer studies, etc |  no  |
| [Experiment](Experiment.md) | Abstract base class for all experiment types |  no  |







## Properties

* Range: [PublicComment](PublicComment.md)

* Multivalued: True

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:public_comments |
| native | oae:public_comments |




## LinkML Source

<details>
```yaml
name: public_comments
description: 'Public comment documents, each with a link or DOI and an optional description.

  Please group/concatenate all public comments associated with a specific consultation
  (e.g., for permitting, non-mandated consultations on a specific topic, or informal
  public input such as unsolicited comments and media attention) into a single document
  if possible, and link to it here.'
title: Public Comments
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: public_comments
owner: Experiment
domain_of:
- Experiment
range: PublicComment
recommended: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>