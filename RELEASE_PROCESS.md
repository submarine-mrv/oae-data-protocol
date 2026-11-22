# Release Process

`main` holds work in progress, and PRs merge into it without changing `version`. A release
publishes the docs site and the AI skill at [schema.oaedata.org](https://schema.oaedata.org).
Release when the Metadata Builder needs a schema change, just before its own release.

1. Open a PR that sets `version:` in `src/oae_data_protocol/schema/oae_data_protocol.yaml` and runs
   `just gen-all`. Title it `chore(release): vX.Y.Z` and merge it.
2. Tag the merge commit and publish the release:

   ```bash
   git fetch origin
   git tag vX.Y.Z origin/main
   git push origin vX.Y.Z
   gh release create vX.Y.Z --verify-tag --generate-notes
   ```

   Publishing the release runs `deploy-docs.yaml`. Running that workflow by hand redeploys the
   latest tag, never `main`.
3. In oae-metadata-builder, run `make schema` with this checkout on the tag.

Version numbers follow semver. Before 1.0, a change that makes existing files invalid bumps the
minor version, and anything else bumps the patch.

The Metadata Builder's `make schema` records an untagged commit as `<last release>+dev.<short hash>`,
so files exported from a development build name the exact commit they follow.
