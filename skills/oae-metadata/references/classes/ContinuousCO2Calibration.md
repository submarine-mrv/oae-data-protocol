# ContinuousCO2Calibration

CO2 calibration for continuous measurements, with extended standard gas details.

Parent: CO2Calibration

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| technique_description | yes | no | string | Details of the calibration technique used. |
| standard_gas_info | no | no | [ContinuousStandardGas](ContinuousStandardGas.md) | Standard gases used for calibration. |
| calibration_location | no | no | enum: `factory`, `lab`, `field` | Factory calibration, lab calibration, or field calibration. |
| method_reference | no | no | string | Citation or reference for the calibration method. |
| frequency | no | no | string | How often the instrument was calibrated. |
| last_calibration_date | no | no | datetime | Date and time of most recent calibration in UTC. |
| calibration_certificates | no | no | string | Information about calibration certificates. Ideally, the certificate should be made available in a PDF file with filename listed here. |
