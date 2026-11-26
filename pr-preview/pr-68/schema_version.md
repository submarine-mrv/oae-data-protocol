

# Slot: schema_version


_Version of the OAE Data Schema the file follows, such as 0.7.0, numbered separately from protocol_version. A file built from an unreleased commit reads 0.7.0+dev.3c014f73: the last release, then the commit._





URI: [oae:schema_version](https://schema.oaedata.org/schema_version)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Container](Container.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^\d+\.\d+\.\d+(\+dev\.[0-9a-f]{7,40})?$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:schema_version |
| native | oae:schema_version |




## LinkML Source

<details>
```yaml
name: schema_version
description: 'Version of the OAE Data Schema the file follows, such as 0.7.0, numbered
  separately from protocol_version. A file built from an unreleased commit reads 0.7.0+dev.3c014f73:
  the last release, then the commit.'
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
alias: schema_version
owner: Container
domain_of:
- Container
range: string
required: true
pattern: ^\d+\.\d+\.\d+(\+dev\.[0-9a-f]{7,40})?$

```
</details>