# Variables

Variables describe the individual measurements, calculations, or contextual data columns within a dataset. The OAE Data Protocol uses a class hierarchy to capture the different levels of metadata required for different kinds of variables — a directly measured pH value needs calibration and instrument details, while a calculated CO₂ variable needs the calculation method, and a contextual column like a station ID needs minimal metadata.

## Variable Hierarchy

```mermaid
graph LR
    V("`*Variable*
    (abstract)`")
    FV("`*FieldVariable*
    (abstract)`")
    ISV("`*InSituVariable*
    (abstract)`")
    MV("`*MeasuredVariable*
    (abstract)`")
    NMV["NonMeasuredVariable"]
    MOV["ModelOutputVariable"]
    SEV["SocioeconomicVariable"]
    CV["CalculatedVariable"]
    DM["DiscreteMeasuredVariable"]
    CM["ContinuousMeasuredVariable"]
    DPH["`DiscretePHVariable
    DiscreteTAVariable
    DiscreteDICVariable
    DiscretePhysiologicalVariable
    *…and others*`"]
    CPH["`ContinuousPHVariable
    ContinuousTAVariable
    ContinuousDICVariable
    ContinuousPhysiologicalVariable
    *…and others*`"]

    V --> FV
    V --> MOV
    FV --> NMV
    FV --> ISV
    ISV --> SEV
    ISV --> CV
    ISV --> MV
    MV --> DM
    MV --> CM
    DM --> DPH
    CM --> CPH

    classDef abstract fill:#f5f5f5,stroke:#999,stroke-dasharray: 4 3,color:#555
    classDef concrete fill:#e0e8f0,stroke:#4F656A
    classDef leaf fill:#d0e8d0,stroke:#4F656A
    class V,FV,ISV,MV abstract
    class DM,CM concrete
    class NMV,MOV,SEV,CV,DPH,CPH leaf
```

This hierarchy aims to align with [NOAA-PMEL's OAPMetadata](https://github.com/NOAA-PMEL/OAPMetadata) XSD schema to make
interoperability easier between NOAA's OCADS system, and other repositories where OAE researchers may choose to host
their data, whether they be other ocean data repositories, and generalist repositories such as Zenodo.

## Choosing a Variable Type

In a **field dataset**, three fields decide each variable's class. Variables in a **model output
dataset** use the
[ModelOutputVariable](https://schema.oaedata.org/ModelOutputVariable.md) class and are classified with the separate
[ModelVariableType](https://schema.oaedata.org/ModelVariableType.md) enum. See [Model Output Variables](#model-output-variables) below.

- **`variable_type`**: what kind of measurement it is. See [VariableType](https://schema.oaedata.org/VariableType.md) for the
  values.
- **`genesis`**: whether it was `measured` by an instrument or `calculated` from other variables. Not
  used for `non_measured` variables.
- **`sampling`**: for measured variables, `discrete` (bottle or grab samples) or `continuous`
  (sensors, underway systems).

### Selection → Schema Class Mapping

| variable_type | genesis | sampling | Schema Class |
|---------------|---------|----------|--------------|
| `pH` | `measured` | `discrete` | [DiscretePHVariable](https://schema.oaedata.org/DiscretePHVariable.md) |
| `pH` | `measured` | `continuous` | [ContinuousPHVariable](https://schema.oaedata.org/ContinuousPHVariable.md) |
| `ta` | `measured` | `discrete` | [DiscreteTAVariable](https://schema.oaedata.org/DiscreteTAVariable.md) |
| `ta` | `measured` | `continuous` | [ContinuousTAVariable](https://schema.oaedata.org/ContinuousTAVariable.md) |
| `dic` | `measured` | `discrete` | [DiscreteDICVariable](https://schema.oaedata.org/DiscreteDICVariable.md) |
| `dic` | `measured` | `continuous` | [ContinuousDICVariable](https://schema.oaedata.org/ContinuousDICVariable.md) |
| `co2` | `measured` | `discrete` | [DiscreteCO2Variable](https://schema.oaedata.org/DiscreteCO2Variable.md) |
| `co2` | `measured` | `continuous` | [ContinuousCO2Variable](https://schema.oaedata.org/ContinuousCO2Variable.md) |
| `sediment` | `measured` | `discrete` | [DiscreteSedimentVariable](https://schema.oaedata.org/DiscreteSedimentVariable.md) |
| `sediment` | `measured` | `continuous` | [ContinuousSedimentVariable](https://schema.oaedata.org/ContinuousSedimentVariable.md) |
| `hplc` | `measured` | `discrete` | [HPLCVariable](https://schema.oaedata.org/HPLCVariable.md) |
| `physiological` | `measured` | `discrete` | [DiscretePhysiologicalVariable](https://schema.oaedata.org/DiscretePhysiologicalVariable.md) |
| `physiological` | `measured` | `continuous` | [ContinuousPhysiologicalVariable](https://schema.oaedata.org/ContinuousPhysiologicalVariable.md) |
| `socioeconomic` | `measured` | — | [SocioeconomicVariable](https://schema.oaedata.org/SocioeconomicVariable.md) |
| `other` | `measured` | `discrete` | [DiscreteMeasuredVariable](https://schema.oaedata.org/DiscreteMeasuredVariable.md) |
| `other` | `measured` | `continuous` | [ContinuousMeasuredVariable](https://schema.oaedata.org/ContinuousMeasuredVariable.md) |
| Any except `non_measured` | `calculated` | — | [CalculatedVariable](https://schema.oaedata.org/CalculatedVariable.md) |
| `non_measured` | — | — | [NonMeasuredVariable](https://schema.oaedata.org/NonMeasuredVariable.md) |

## What Each Level Adds

Each class adds fields to the one above it. The class pages list them in full.

- **[Variable](https://schema.oaedata.org/Variable.md)**: what every variable has, such as its column name in the data file,
  a descriptive name and an optional reference to a community vocabulary.
- **[InSituVariable](https://schema.oaedata.org/InSituVariable.md)**: data the project collected or derived: units, how it was
  produced and who produced it.
- **[MeasuredVariable](https://schema.oaedata.org/MeasuredVariable.md)**: how samples were taken and analyzed, the analyzing
  instrument with its [calibration](https://schema.oaedata.org/instruments-calibration/index.md), and quality control.
- **[CalculatedVariable](https://schema.oaedata.org/CalculatedVariable.md)**: how the value was calculated, including software,
  inputs and constants.

## Model Output Variables

Variables in a [ModelOutputDataset](https://schema.oaedata.org/ModelOutputDataset.md) are described by a single class,
[ModelOutputVariable](https://schema.oaedata.org/ModelOutputVariable.md), which sits directly under `Variable` as a sibling of
[FieldVariable](https://schema.oaedata.org/FieldVariable.md). `ModelOutputVariable`s carry none of the
sampling, instrument, calibration or in-situ QC metadata that field-collected variables do. How the
output was produced is described by the simulation configuration on the parent dataset.

## Type-Specific Fields (Mixins)

Many measured variables (either discrete or continuous) inherit additional fields based on their `variable_type` that are
always present whether the specific variable is discrete or continuous. In these instances, we use LinkML's [mixin](https://linkml.io/linkml/schemas/inheritance.html#mixin-classes-and-slots)
feature to allow for trait-like composability of these fields into both the corresponding DiscreteVariable and
ContinuousVariable classes for that `variable_type`.

| Variable Type | Mixin                                                            |
|---------------|------------------------------------------------------------------|
| `pH` | [MeasuredPHFields](https://schema.oaedata.org/MeasuredPHFields.md)                       |
| `ta` | [MeasuredTAFields](https://schema.oaedata.org/MeasuredTAFields.md)                       |
| `dic` | [MeasuredDICFields](https://schema.oaedata.org/MeasuredDICFields.md)                     |
| `co2` | [MeasuredCO2Fields](https://schema.oaedata.org/MeasuredCO2Fields.md)                     |
| `sediment` | [MeasuredSedimentFields](https://schema.oaedata.org/MeasuredSedimentFields.md)           |
| `physiological` | [MeasuredPhysiologicalFields](https://schema.oaedata.org/MeasuredPhysiologicalFields.md) |
| `other` | —                                                                |

Leaf classes (e.g., [DiscretePHVariable](https://schema.oaedata.org/DiscretePHVariable.md), [DiscreteTAVariable](https://schema.oaedata.org/DiscreteTAVariable.md)) may
add further type-specific fields as well. For a comprehensive list of all required and optional fields please refer
to the individual class pages linked in the [mapping table](#selection-schema-class-mapping) above.
