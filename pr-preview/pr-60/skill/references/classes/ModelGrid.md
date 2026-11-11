# ModelGrid

Details about a model grid. Use multiple ModelGrid entries to describe nested or multi-grid configurations.

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| grid_type | yes | no | enum: `inner_grid`, `outer_grid`, `single_grid` | Role of this grid in a nested or multi-grid configuration. |
| grid_name | no | no | string | Name of the grid (e.g., 'inner grid', 'L1', 'global'). |
| grid_geometry | no | no | string | Descriptive structure of the grid (e.g., latitude-longitude, unstructured triangular, tripolar). |
| region | no | no | string | Region covered by the grid. |
| spatial_coverage | no | no | [SpatialCoverage](SpatialCoverage.md) | Bounding box for this grid, expressed as a schema.org GeoShape bounding box. |
| arrangement | no | no | string | The grid arrangement of orthogonal physical quantities (e.g., Arakawa A, Arakawa B, Arakawa C). |
| vertical_coordinate_type | no | no | string | The vertical grid coordinate type (e.g. z-coordinate, z*-coordinate, terrain-following coordinate, isopycnal coordinate) |
| n_x | no | no | integer | Number of grid points in the x-direction. |
| n_y | no | no | integer | Number of grid points in the y-direction. |
| n_z | no | no | integer | Number of vertical coordinate levels. |
| n_nodes | no | no | integer | Number of nodes in the grid (for unstructured grids). |
| horizontal_resolution_range | no | no | string | Description of horizontal resolution (e.g., '3.3 km', '1/12 degree'). |
| vertical_resolution_range | no | no | string | Description of vertical resolution (e.g., 'Max. 4 m near surface, stretching to 500 m at depth'). |
| input_details | no | no | [ModelInputDetails](ModelInputDetails.md) | Details about input data sources used to drive the model on this grid. |

## Vocabularies

What each value means, for the fields above.

### grid_type

- `inner_grid`: Inner (nested, higher-resolution) grid
- `outer_grid`: Outer (coarser-resolution) grid
- `single_grid`: Single grid (no nesting)
