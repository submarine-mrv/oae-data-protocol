# Permit

A permit associated with the project.

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| permit_id | yes | no | string | The unique identifier or number associated with this permit. |
| permitting_authority | yes | no | string | The group that issued the permit. |
| approval_document | yes | no | string | Filename(s), links and/or DOIs to access files of permitting documents, separated by commas |
| agency_contact | no | no | string | The point of contact at the permitting agency. |
| changes_to_evolution_of_permit_criteria | no | no | string | e.g., changes of discharge pH and basis for changes |
| permit_type | no | no | string | The category of permit (E.g., experimental permit, commercial permit) |
| time_period | no | no | string | The time period during which the permit will be applicable, or expected duration of the permit. |
