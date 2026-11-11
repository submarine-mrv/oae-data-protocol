# ContinuousStandardGas

Standard gas used for continuous CO2 calibration, with additional traceability and count information.

Parent: StandardGas

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| number_of_nonzero_standards | no | no | integer | How many non-zero gas standards were used for the calibration. |
| traceability_to_wmo_standards | no | no | string | Information about traceability of standard gases to WMO standards. |
| manufacturer | no | no | string | Manufacturer of the standard gas. |
| concentration | no | no | string | Concentrations of the CO2 standard gases that are used to calibrate the CO2 sensor, e.g., 260, 350, 510ppm. |
| uncertainty | no | no | string | Uncertainties of the CO2 standard gas, e.g., 0.5%. |
