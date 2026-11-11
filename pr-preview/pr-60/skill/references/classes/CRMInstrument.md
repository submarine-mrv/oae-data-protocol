# CRMInstrument

Instrument calibrated with Certified Reference Materials, used for DIC and TA measurements.

Parent: AnalyzingInstrument

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| calibration | yes | no | [CRMCalibration](CRMCalibration.md) | CRM calibration information for this instrument. |
| instrument_type | yes | no | enum [AnalyzingInstrumentType](../enums/AnalyzingInstrumentType.md) | Type of instrument used to analyze samples or measure continuously. |
| accuracy | yes | no | string | Accuracy of the instrument measurements. |
| manufacturer | no | no | string | Manufacturer name of the instrument. |
| model | no | no | string | Model number or name of the instrument. |
| instrument_type_custom | no | no | string |  |
| serial_number | no | no | string | Serial number of the instrument. |
| precision | no | no | string | Precision of the instrument measurements. |
