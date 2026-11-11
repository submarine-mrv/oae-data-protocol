# Container

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| project | no | no | [Project](Project.md) |  |
| experiments | no | yes | one of [Experiment](Experiment.md), [InSituExperiment](InSituExperiment.md), [Model](Model.md), [Intervention](Intervention.md), [Tracer](Tracer.md), [InterventionWithTracer](InterventionWithTracer.md) |  |
| datasets | no | yes | one of [Dataset](Dataset.md), [FieldDataset](FieldDataset.md), [ModelOutputDataset](ModelOutputDataset.md) |  |
| version | no | no | string | Version of the oae-data-protocol |
| protocol_git_hash | no | no | string | Git commit hash of the oae-data-protocol |
| metadata_builder_git_hash | no | no | string | Git commit hash of the metadata-builder UI |
