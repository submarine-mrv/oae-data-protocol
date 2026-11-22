

# Slot: Platform ID (platform_id)


_Synonymous with glider ID, cruise ID. A unique name assigned to oceanographic assets such as buoys, moorings, floats, drifters, towed vehicles like the Scanfish or StingRay. This is synonymous with the BCO-DMO “platform” parameter (https://www.bco-dmo.org/parameter/932), NERC “platform type” term (https://vocab.nerc.ac.uk/collection/W06/current/CLSS0001/), and the “platform_id” term within the Climate and Forecast (CF) metadata conventions (https://cfconventions.org/Data/cf-standard-names/current/build/cf-standard-name-table.html). e.g., ICES platform code (e.g., 33RO)._





URI: [oae:platform_id](https://schema.oaedata.org/platform_id)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Platform](Platform.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:platform_id |
| native | oae:platform_id |




## LinkML Source

<details>
```yaml
name: platform_id
description: Synonymous with glider ID, cruise ID. A unique name assigned to oceanographic
  assets such as buoys, moorings, floats, drifters, towed vehicles like the Scanfish
  or StingRay. This is synonymous with the BCO-DMO “platform” parameter (https://www.bco-dmo.org/parameter/932),
  NERC “platform type” term (https://vocab.nerc.ac.uk/collection/W06/current/CLSS0001/),
  and the “platform_id” term within the Climate and Forecast (CF) metadata conventions
  (https://cfconventions.org/Data/cf-standard-names/current/build/cf-standard-name-table.html).
  e.g., ICES platform code (e.g., 33RO).
title: Platform ID
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: platform_id
owner: Platform
domain_of:
- Platform
range: string

```
</details>