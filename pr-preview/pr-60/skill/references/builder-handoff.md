# Handing a draft to the Metadata Builder

The researcher finishes the draft in the Metadata Builder at https://metadata.oaedata.org. Load this file before you write the JSON and again when you tell them how to import it.

## What a file may contain

A metadata file is one JSON object. Every key is optional:

- `project`: one project object
- `experiments`: a list of experiments
- `datasets`: a list of datasets, each with its `variables`
- `version`: the protocol version you drafted against (the `version` at the top of `assets/oae_data_protocol.schema.json`)

Use `[]` or leave a key out when there is nothing for it. Never write `null`.

## The two import modes

The Builder's Import button previews the file and offers:

- **Add as a new project.** Everything in the file becomes a new project.
- **Merge into current project.** Shown only when a project is open.

What merge does decides what you put in the file:

| In the file | What merge does | So |
|---|---|---|
| `project` | Its fields overwrite the open project's fields | For an existing project, leave `project` out |
| An experiment whose `experiment_id` matches one in the project | Replaces that experiment whole | Give a new experiment an id no existing experiment uses. If the researcher wants a replacement, tell them the old one is overwritten |
| An experiment with a new or missing `experiment_id` | Added as new | |
| A dataset | Always added, never replaced | Importing a second draft of the same dataset makes a duplicate. Tell the researcher to delete the old one first |
| A dataset's `experiment_id` | Links the dataset to the experiment with that id, in the file or in the project | Ask for the id of the experiment the dataset belongs to. The preview also lets the researcher pick the experiment by hand |
| `project_id` on anything | Ignored; the Builder stamps the open project's id | Still write it, so the file validates |

There is no way to update part of an existing experiment or dataset by import. Say so if the researcher asks for that.

## What the Builder drops on import

The Builder keeps only what its forms can show. These pass validation and are then removed:

- **Empty values.** Empty strings, empty objects and nulls. Leave a field out instead.
- **Fields from another class.** An experiment keeps only the fields of the class its `experiment_types` selects; a dataset only those of its `dataset_type`; a variable only those of its `schema_class`.
- **Mixed model and field experiment types.** If `experiment_types` contains `model`, the Builder reduces it to `["model"]` and drops the in-situ fields. Draft field work and modeling as separate experiments.
- **Conditional fields whose condition isn't met.** `data_access_date` unless `data_accessibility` is `scheduled_access`; `mcdr_forcing_description` unless `simulation_type` contains `perturbation`; each `*_custom` field unless its partner field is `other`.
- **Field variables in a model dataset.** They are converted to `ModelOutputVariable` and lose their sampling, instrument and calibration details.

## What to tell the researcher

1. Open https://metadata.oaedata.org and, for an existing project, open that project first.
2. Click Import and choose the JSON file. Pick "Add as a new project" or "Merge into current project".
3. In the preview, check each dataset's experiment link.
4. Work through the report: fill each gap in the form, and check each value marked uncertain against its source.
5. Export from the Builder when the forms show no errors. That export is the file to publish.
