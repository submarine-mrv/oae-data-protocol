# Platform

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| platform_type | yes | no | enum [PlatformType](../enums/PlatformType.md) | For Platform Type definitions, see: https://vocab.nerc.ac.uk/collection/L06/current/ |
| name | no | no | string | Name of the observing platform, e.g., RV Ronald Brown, Saildrone#0132, Mooring_First_Landing, etc. |
| platform_id | no | no | string | Synonymous with glider ID, cruise ID. A unique name assigned to oceanographic assets such as buoys, moorings, floats, drifters, towed vehicles like the Scanfish or StingRay. This is synonymous with the BCO-DMO “platform” parameter (https://www.bco-dmo.org/parameter/932), NERC “platform type” term (https://vocab.nerc.ac.uk/collection/W06/current/CLSS0001/), and the “platform_id” term within the Climate and Forecast (CF) metadata conventions (https://cfconventions.org/Data/cf-standard-names/current/build/cf-standard-name-table.html). e.g., ICES platform code (e.g., 33RO). |
| owner | no | no | string | Institution that owns the platform. |
| country | no | no | string | Country to which the platform belongs. |
