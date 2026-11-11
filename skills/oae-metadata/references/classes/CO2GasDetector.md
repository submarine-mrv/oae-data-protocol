# CO2GasDetector

CO2 gas detector with standard gas calibration.

Parent: AnalyzingInstrument

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| detector_type | yes | no | string | Type of the CO2 gas detector (E.g., Infrared) |
| calibration | yes | no | [DiscreteCO2Calibration](DiscreteCO2Calibration.md) | CO2 calibration information for this instrument. |
| manufacturer | yes | no | string | Manufacture of the CO2 sensor |
| instrument_type | yes | no | always `gas_analyzer` | Type of instrument used to analyze samples or measure continuously. |
| accuracy | yes | no | string | Accuracy of the instrument measurements. |
| resolution | no | no | string | Resolution of the CO2 sensor. |
| uncertainty | no | no | string | Uncertainty of the CO2 sensor. |
| model | no | no | string | Model number of the CO2 sensor, e.g., 6262 |
| instrument_type_custom | no | no | string |  |
| serial_number | no | no | string | Serial number of the instrument. |
| precision | no | no | string | Precision of the instrument measurements. |
