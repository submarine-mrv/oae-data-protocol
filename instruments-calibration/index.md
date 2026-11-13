# Instruments & Calibration

Measured variables describe the instrument that analyzed them, in `analyzing_instrument`, and how that
instrument was calibrated. Some variable classes require a specific instrument type, and each
instrument type requires its own calibration type, so the right calibration fields come with the
variable.

## Instrument Hierarchy

```mermaid
graph TD
    AI["AnalyzingInstrument"]
    AI --> PHI["PHInstrument"]
    AI --> CRMI["CRMInstrument"]
    AI --> CO2D["CO2GasDetector"]
    CO2D --> CCO2D["ContinuousCO2GasDetector"]

    AI -->|calibration| C["Calibration"]
    PHI -->|calibration| PHC["PHCalibration"]
    PHC --> DYEC["DyeCalibration"]
    CRMI -->|calibration| CRMC["CRMCalibration"]
    CO2D -->|calibration| DCO2C["DiscreteCO2Calibration"]
    CCO2D -->|calibration| CCO2C["ContinuousCO2Calibration"]

    style AI fill:#e0e8f0
    style PHI fill:#d0d8e0
    style CRMI fill:#d0d8e0
    style CO2D fill:#d0d8e0
    style CCO2D fill:#d0d8e0
    style C fill:#f0e8d0
    style PHC fill:#f0e8d0
    style DYEC fill:#f0e8d0
    style CRMC fill:#f0e8d0
    style DCO2C fill:#f0e8d0
    style CCO2C fill:#f0e8d0
```

## Which Instrument Each Variable Uses

| Variable class | Instrument | Calibration |
|----------------|------------|-------------|
| [DiscretePHVariable](../DiscretePHVariable.md) | [PHInstrument](../PHInstrument.md) | [DyeCalibration](../DyeCalibration.md) when `standard_used` is dye, otherwise [PHCalibration](../PHCalibration.md) for TRIS or other standards |
| [DiscreteTAVariable](../DiscreteTAVariable.md), [DiscreteDICVariable](../DiscreteDICVariable.md) | [CRMInstrument](../CRMInstrument.md) | [CRMCalibration](../CRMCalibration.md): certified reference material |
| [DiscreteCO2Variable](../DiscreteCO2Variable.md) | [CO2GasDetector](../CO2GasDetector.md) | [DiscreteCO2Calibration](../DiscreteCO2Calibration.md): standard gases |
| [ContinuousCO2Variable](../ContinuousCO2Variable.md) | [ContinuousCO2GasDetector](../ContinuousCO2GasDetector.md) | [ContinuousCO2Calibration](../ContinuousCO2Calibration.md): standard gases |
| All other measured variables, including continuous pH, TA and DIC | [AnalyzingInstrument](../AnalyzingInstrument.md) | [Calibration](../Calibration.md) |

## Example

A discrete pH variable's `analyzing_instrument`:

<!-- validate: PHInstrument -->
```json
{
  "instrument_type": "spectrophotometer",
  "manufacturer": "Agilent",
  "accuracy": "0.001 pH units",
  "calibration": {
    "technique_description": "Spectrophotometric pH with purified m-cresol purple",
    "calibration_location": "lab",
    "standard_used": "dye",
    "standard_type_and_production": "Purified m-cresol purple, MCR Inc.",
    "dye_purified": true
  }
}
```
