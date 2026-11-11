# GeoShape

The geographic shape of a place. A GeoShape can be described using several properties whose values are based on latitude/longitude pairs. Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points. (imported from schema.org)

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| box | no | no | string | A bounding box defined by two corner points — the southwest (lower-left) corner followed by the northeast (upper-right) corner. Per science-on-schema.org, each point is written as `<latitude> <longitude>` in decimal degrees (WGS 84), with all four values space-separated: `"<minLat> <minLon> <maxLat> <maxLon>"`. Example: `"39.3280 120.1633 40.445 123.7878"`. See https://github.com/ESIPFed/science-on-schema.org/blob/main/guides/Dataset.md#spatial-coverage |
| line | no | no | string | A line is a point-to-point path consisting of two or more points. A line is expressed as a series of two or more point objects separated by space. |
