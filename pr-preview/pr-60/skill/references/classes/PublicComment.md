# PublicComment

A public comment document associated with a consultation for this experiment.

| Field | Required | Many | Type | Description |
|---|---|---|---|---|
| url | yes | no | uri | Link or DOI to access the public comment document. |
| comment_type | yes | no | enum: `permitting`, `non_mandated_consultation`, `informal_public_input`, `other` | The kind of consultation these comments came from. |
| description | no | no | string | A narrative description of what this public comment contains. |
