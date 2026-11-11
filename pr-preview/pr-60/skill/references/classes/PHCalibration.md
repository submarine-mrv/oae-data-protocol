# PHCalibration

pH instrument calibration. Use this class directly for TRIS or other standards, and DyeCalibration when standard_used is dye.

Parent: Calibration

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| standard_used | yes | no | enum: `dye`, `tris`, `other` | Type of standard used to calibrate the pH measurement. |
| technique_description | yes | no | string | Details of the calibration technique used. |
| calibration_temperature | no | no | string | Temperature at which calibration was performed. |
| standard_used_custom | no | no | string | Name of the standard used, when it is not in the list. |
| standard_type_and_production | no | no | string | Details on the standard (e.g., type of dye used) and how or where it was produced. |
| ph_of_standards | no | no | string | pH values of the calibration standards used. |
| calibration_location | no | no | enum: `factory`, `lab`, `field` | Factory calibration, lab calibration, or field calibration. |
| method_reference | no | no | string | Citation or reference for the calibration method. |
| frequency | no | no | string | How often the instrument was calibrated. |
| last_calibration_date | no | no | datetime | Date and time of most recent calibration in UTC. |
| calibration_certificates | no | no | string | Information about calibration certificates. Ideally, the certificate should be made available in a PDF file with filename listed here. |

## Rules

- When `standard_used` is `other`, `standard_used_custom` is required.

## Vocabularies

What each value means, for the fields above.

### standard_used

- `dye`: Indicator dye, e.g., m-cresol purple.
- `tris`: TRIS buffer in synthetic seawater.
- `other`: A standard not listed here. Name it in the custom field.

### calibration_location

- `factory`: Factory calibration performed by manufacturer.
- `lab`: Laboratory calibration.
- `field`: Field calibration performed during deployment.
