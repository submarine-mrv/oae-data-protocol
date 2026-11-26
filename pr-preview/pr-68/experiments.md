

# Slot: experiments



URI: [oae:experiments](https://schema.oaedata.org/experiments)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) |  |  no  |







## Properties

* Range: [Any](Any.md)&nbsp;or&nbsp;<br />[Experiment](Experiment.md)&nbsp;or&nbsp;<br />[InSituExperiment](InSituExperiment.md)&nbsp;or&nbsp;<br />[Model](Model.md)&nbsp;or&nbsp;<br />[Intervention](Intervention.md)&nbsp;or&nbsp;<br />[Tracer](Tracer.md)&nbsp;or&nbsp;<br />[InterventionWithTracer](InterventionWithTracer.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:experiments |
| native | oae:experiments |




## LinkML Source

<details>
```yaml
name: experiments
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: experiments
owner: Container
domain_of:
- Container
range: Any
multivalued: true
any_of:
- range: Experiment
- range: InSituExperiment
- range: Model
- range: Intervention
- range: Tracer
- range: InterventionWithTracer

```
</details>