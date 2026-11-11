

# Slot: License (license)


_Link a Dataset to its license to document legal constraints by adding a schema:license property. The guide recommends providing a URL that unambiguously identifies a specific version of the license used, but for many licenses it is hard to determine what that URL should be. Thus, we recommend that the license URL be drawn from the [SPDX license list](https://spdx.org/licenses/), which provides a curated list of licenses and their properties that is well maintained. For each SPDX entry, SPDX provides a canonical URL for the license (e.g., http://spdx.org/licenses/CC0-1.0), a unique licenseId (e.g., CC0-1.0), and other metadata about the license._





URI: [schema:license](http://schema.org/license)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) | Abstract base class for all dataset types |  no  |
| [FieldDataset](FieldDataset.md) | A field or observational dataset related to an OAE experiment |  no  |
| [ModelOutputDataset](ModelOutputDataset.md) | A model simulation output dataset |  no  |







## Properties

* Range: [uri](uri.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:license |
| native | oae:license |




## LinkML Source

<details>
```yaml
name: license
description: Link a Dataset to its license to document legal constraints by adding
  a schema:license property. The guide recommends providing a URL that unambiguously
  identifies a specific version of the license used, but for many licenses it is hard
  to determine what that URL should be. Thus, we recommend that the license URL be
  drawn from the [SPDX license list](https://spdx.org/licenses/), which provides a
  curated list of licenses and their properties that is well maintained. For each
  SPDX entry, SPDX provides a canonical URL for the license (e.g., http://spdx.org/licenses/CC0-1.0),
  a unique licenseId (e.g., CC0-1.0), and other metadata about the license.
title: License
from_schema: https://schema.oaedata.org/OAEDataSchema
rank: 1000
slot_uri: schema:license
alias: license
owner: Dataset
domain_of:
- Dataset
range: uri

```
</details>