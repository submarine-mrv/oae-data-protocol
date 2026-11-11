# Person

Information about a researcher or investigator involved in the experiment.

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| name | yes | no | string | Full name of the person. |
| email | yes | no | string | Contact email address. |
| affiliation | no | no | [Organization](Organization.md) | Institutional affiliation of the investigator. |
| phone | no | no | string | Contact phone number. |
| identifier_type | no | no | enum: `orcid`, `researcher_id`, `ocean_expert` | Type of Researcher ID (e.g., ORCID, ResearcherID). |
| identifier | no | no | string | Unique researcher identifier value. |
| role | no | no | string | Role of the investigator in the experiment (e.g., chief scientist, data submitter). |
