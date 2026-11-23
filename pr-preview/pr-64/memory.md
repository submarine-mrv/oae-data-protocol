

# Slot: Memory (memory)


_Memory available (e.g., '512 GB DDR4')._





URI: [oae:memory](https://schema.oaedata.org/memory)



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
| self | oae:memory |
| native | oae:memory |




## LinkML Source

<details>
```yaml
name: memory
description: Memory available (e.g., '512 GB DDR4').
title: Memory
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: memory
owner: HardwareConfiguration
domain_of:
- HardwareConfiguration
range: string

```
</details>