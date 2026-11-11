# ExternalProject

A research project that is not directly managed by the OAE project, but whose location is proximal to the OAE project and whose data may be relevant to understanding the context or impacts of OAE activities.

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| temporal_coverage | yes | no | string | Start date and end date (if known) of the project in ISO-8601 interval format (YYYY-MM-DD/YYY-MM-DD). If the end date is not known, use open-ended format YYYY-MM-DD/.. |
| spatial_coverage | yes | no | [SpatialCoverage](SpatialCoverage.md) | Latitude/longitude bounds of project site (e.g., boundary domain of observations or relevant activities), expressed as a schema.org GeoShape bounding box. |
| name | yes | no | string | The name of the external research project. |
| description | no | no | string | A brief description of the external research project. |
| related_links | no | yes | uri | Links to websites or documents related to the external research project. |
