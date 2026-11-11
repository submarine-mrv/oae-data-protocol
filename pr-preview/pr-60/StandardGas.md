

# Class: StandardGas


_Standard gas used for CO2 calibration._





URI: [oae:StandardGas](https://schema.oaedata.org/StandardGas)






```mermaid
 classDiagram
    class StandardGas
    click StandardGas href "../StandardGas"
      StandardGas <|-- ContinuousStandardGas
        click ContinuousStandardGas href "../ContinuousStandardGas"
      
      StandardGas : concentration
        
      StandardGas : manufacturer
        
      StandardGas : uncertainty
        
      
```





## Inheritance
* **StandardGas**
    * [ContinuousStandardGas](ContinuousStandardGas.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [manufacturer](manufacturer.md) | 0..1 <br/> [String](String.md) | Manufacturer of the standard gas | direct |
| [concentration](concentration.md) | 0..1 <br/> [String](String.md) | Concentrations of the CO2 standard gases that are used to calibrate the CO2 s... | direct |
| [uncertainty](uncertainty.md) | 0..1 <br/> [String](String.md) | Uncertainties of the CO2 standard gas, e | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CO2Calibration](CO2Calibration.md) | [standard_gas_info](standard_gas_info.md) | range | [StandardGas](StandardGas.md) |
| [DiscreteCO2Calibration](DiscreteCO2Calibration.md) | [standard_gas_info](standard_gas_info.md) | range | [StandardGas](StandardGas.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://schema.oaedata.org/OAEDataSchema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oae:StandardGas |
| native | oae:StandardGas |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: StandardGas
description: Standard gas used for CO2 calibration.
from_schema: https://schema.oaedata.org/OAEDataSchema
attributes:
  manufacturer:
    name: manufacturer
    description: Manufacturer of the standard gas.
    title: Standard Gas Manufacturer
    from_schema: Calibration
    domain_of:
    - StandardGas
    - AnalyzingInstrument
    - GenericSensor
    range: string
  concentration:
    name: concentration
    description: Concentrations of the CO2 standard gases that are used to calibrate
      the CO2 sensor, e.g., 260, 350, 510ppm.
    title: Standard Gas Concentration
    from_schema: Calibration
    rank: 1000
    domain_of:
    - StandardGas
    range: string
  uncertainty:
    name: uncertainty
    description: Uncertainties of the CO2 standard gas, e.g., 0.5%.
    title: Standard Gas Uncertainty
    from_schema: Calibration
    domain_of:
    - StandardGas
    - CO2GasDetector
    - QCFields
    range: string

```
</details>

### Induced

<details>
```yaml
name: StandardGas
description: Standard gas used for CO2 calibration.
from_schema: https://schema.oaedata.org/OAEDataSchema
attributes:
  manufacturer:
    name: manufacturer
    description: Manufacturer of the standard gas.
    title: Standard Gas Manufacturer
    from_schema: Calibration
    alias: manufacturer
    owner: StandardGas
    domain_of:
    - StandardGas
    - AnalyzingInstrument
    - GenericSensor
    range: string
  concentration:
    name: concentration
    description: Concentrations of the CO2 standard gases that are used to calibrate
      the CO2 sensor, e.g., 260, 350, 510ppm.
    title: Standard Gas Concentration
    from_schema: Calibration
    rank: 1000
    alias: concentration
    owner: StandardGas
    domain_of:
    - StandardGas
    range: string
  uncertainty:
    name: uncertainty
    description: Uncertainties of the CO2 standard gas, e.g., 0.5%.
    title: Standard Gas Uncertainty
    from_schema: Calibration
    alias: uncertainty
    owner: StandardGas
    domain_of:
    - StandardGas
    - CO2GasDetector
    - QCFields
    range: string

```
</details>