# ModelComponent

A component of a model (e.g., physics, biogeochemistry/ecosystem).

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| model_component_type | yes | no | enum: `physics`, `bgc_ecosystem`, `sea_ice`, `atmosphere`, `other` | The type of model component (physics, BGC/ecosystem, or other). |
| name | yes | no | string | Name of the model component (e.g., ROMS, MARBL, Oceananigans). |
| description | no | no | string | A description of the model component characteristics. For physics components, this should include the version of equations being solved (hydrostatic vs non-hydrostatic), tracer advection scheme, how bottom drag is represented, mixed layer parameterizations, sub-grid mixing parameterizations if applicable, etc. For BGC components, this should include details of which parameters are modeled explicitly, derived carbonate system parameters, advection scheme for biological tracers, CO₂ solver protocol (e.g., CO₂SYS), links to data/code with biological model parameters (e.g., growth and mortality rates), etc. Equations for each explicitly modeled parameter should be provided (can be links to publications), and it should be noted if any equations or parameter values (e.g. growth rates) were modified. Description and/or references of air-sea CO₂ flux parameterization used, gas transfer velocity formulation and atmospheric CO₂ details (e.g., fixed or time varying, and if time varying which data were used). Also include details on whether dissolution and precipitation of calcium carbonate are considered, how exchanges between sediment and overlying water are represented (if applicable), and whether active feedbacks between biological processes and the carbonate system are represented. Associated links to data, DOIs, or publications can be noted here, but should be supplemental. |
| model_component_type_custom | no | no | string |  |
| version | no | no | string | Release version of the model component. |
| codebase | no | no | uri | Link to model code repository. |
| references | no | yes | uri | Links or DOIs to any reference(s) relevant to the model components/development, specific model configuration, model validation etc. |

## Rules

- When `model_component_type` is `other`, `model_component_type_custom` is required.
