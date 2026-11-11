# CRMCalibration

Calibration using Certified Reference Materials, used for DIC and TA instruments.

Parent: Calibration

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| crm_manufacturer | yes | no | string | Manufacturer of the Certified Reference Material (e.g., Scripps, JAMSTEC). |
| crm_batch_number | yes | no | string | Batch number of the Certified Reference Material. |
| technique_description | yes | no | string | Details of the calibration technique used. |
| calibration_location | no | no | enum: `factory`, `lab`, `field` | Factory calibration, lab calibration, or field calibration. |
| method_reference | no | no | string | Citation or reference for the calibration method. |
| frequency | no | no | string | How often the instrument was calibrated. |
| last_calibration_date | no | no | datetime | Date and time of most recent calibration in UTC. |
| calibration_certificates | no | no | string | Information about calibration certificates. Ideally, the certificate should be made available in a PDF file with filename listed here. |

## Vocabularies

What each value means, for the fields above.

### calibration_location

- `factory`: Factory calibration performed by manufacturer.
- `lab`: Laboratory calibration.
- `field`: Field calibration performed during deployment.
