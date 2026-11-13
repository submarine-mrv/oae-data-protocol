

# Slot: Machine (machine)


_Name of the machine or cluster (e.g., 'Perlmutter')._





URI: [oae:machine](https://schema.oaedata.org/machine)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HardwareConfiguration](HardwareConfiguration.md) | Details about the computational hardware used to run a model simulation |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:machine |
| native | oae:machine |




## LinkML Source

<details>
```yaml
name: machine
description: Name of the machine or cluster (e.g., 'Perlmutter').
title: Machine
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: machine
owner: HardwareConfiguration
domain_of:
- HardwareConfiguration
range: string

```
</details>