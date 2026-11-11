# DosingConcentration

Details of tracer concentration information

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| is_derived_value | yes | no | boolean | Indicates that the field in question is a derived value as opposed to one measured directly. |
| is_provided_as_a_file | yes | no | boolean | Select ‘Variable’ if the concentration varies over time, or ‘Fixed Value’ if it is constant. Note: Variable concentrations must be provided in a data file. |
| amount | no | no | float |  |
| unit | no | no | enum: `unit:KiloGM-PER-M3`, `unit:MicroGM-PER-L`, `unit:MicroGM-PER-MilliL`, `unit:MilliGM-PER-L`, `unit:MilliGM-PER-M3`, `unit:MilliGM-PER-MilliL`, `unit:NanoGM-PER-L`, `unit:NanoGM-PER-MilliL`, `unit:PicoGM-PER-MilliL` |  |
