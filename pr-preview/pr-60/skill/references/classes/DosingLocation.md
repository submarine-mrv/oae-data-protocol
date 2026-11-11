# DosingLocation

A specific location of dosing for an OAE intervention and/or tracer study. Can be a point, line, or bounding box

Parent: Place

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| dosing_location_file | no | no | string | Exact filename, URL and/or DOI to access the location file. Format should be one of GeoJSON or Shapefile. |
| geo | no | no | one of [GeoShape](GeoShape.md), [GeoCoordinates](GeoCoordinates.md) | Entities that have a somewhat fixed, physical extension. (imported from schema.org) |
