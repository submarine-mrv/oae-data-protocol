# DiscreteCO2Calibration

CO2 calibration for discrete measurements, with calibration temperature.

Parent: CO2Calibration

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| technique_description | yes | no | string | Details of the calibration technique used. |
| calibration_temperature | no | no | string | Temperature at which calibration was performed. |
| standard_gas_info | no | no | [StandardGas](StandardGas.md) | Standard gases used for calibration. |
| calibration_location | no | no | enum: `factory`, `lab`, `field` | Factory calibration, lab calibration, or field calibration. |
| method_reference | no | no | string | Citation or reference for the calibration method. |
| frequency | no | no | string | How often the instrument was calibrated. |
| last_calibration_date | no | no | datetime | Date and time of most recent calibration in UTC. |
| calibration_certificates | no | no | string | Information about calibration certificates. Ideally, the certificate should be made available in a PDF file with filename listed here. |
