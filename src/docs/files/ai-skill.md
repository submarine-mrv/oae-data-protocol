# Drafting Metadata with an AI Assistant

Most of what a metadata file asks for is already written down in your project plan, your reports and
your data files. An AI assistant such as Claude or ChatGPT can read those files and write a first
draft of your [metadata file](metadata-format.md). You import the draft into the
[Metadata Builder](metadata-builder.md), check it, fill in what is missing and export the final file.

An assistant does this well only when it knows how the OAE Data Protocol is organised, which values
each field accepts, and when to leave a field empty. We publish that as a
[folder of instructions and reference files](https://github.com/submarine-mrv/oae-data-protocol/tree/main/skills/oae-metadata)
written for assistants to follow. Claude calls a folder like this a
[skill](https://support.claude.com/en/articles/12512180-using-skills-in-claude), and this page uses
the same word.

## What you get

The assistant writes two files:

- a metadata file (JSON) holding whichever of project, experiments and datasets your files describe
- a short report listing required fields it could not find, values it was unsure of, and places
  where your sources disagree

It does not guess. A required field it cannot find stays empty and goes in the report, for you to
complete in the Builder.

## What to give it

- Project design documents, monitoring or operations reports, methods descriptions (PDF or text)
- Data files (CSV or XLSX): one dataset per file, one variable per data column
- OAPMetadata XML, if you have submitted to OCADS

Say whether the project is new or already exists in the Metadata Builder. For an existing project,
give its project ID and, for each dataset, the ID of the experiment it belongs to.

## How to use it

There are three ways. If you are unsure, start with the first.

| | You need | Follows the latest protocol | Checks its own draft |
|---|---|---|---|
| [1. Paste a link into a chat](#1-paste-a-link-into-a-chat) | Any assistant that can open web pages | Yes | Sometimes |
| [2. Add the skill to Claude](#2-add-the-skill-to-claude) | A Claude account | Until a new version comes out; then download it again | Yes |
| [3. Install it in Claude Code](#3-install-it-in-claude-code) | Claude Code | Yes, when you update it | Yes |

"Checks its own draft" means the assistant runs the [checker](#checking-the-draft-yourself) that
comes with the skill and fixes what it finds before handing you the files.

### 1. Paste a link into a chat

Nothing to install. Start a chat, attach your files and paste:

> Follow the instructions at https://schema.oaedata.org/skill/SKILL.md to draft OAE metadata from
> these files. The other files it mentions are in the same folder.

!!! warning "What this way cannot promise"
    - Many chat assistants cannot download and run the checker. The report says when it was not run.
      Errors then show up when you import the draft into the Builder.
    - The assistant has to open each reference file itself, and some open fewer than the
      instructions ask for.
    - If your assistant offers to save the instructions as a skill, the saved copy no longer follows
      new protocol versions. It behaves like the zip file below.

### 2. Add the skill to Claude

Download [oae-metadata.zip](https://schema.oaedata.org/oae-metadata.zip). In Claude, in the browser
or the desktop app, open Customize, then Skills, and upload the zip. After that, attach your files to
any chat and ask Claude to draft OAE metadata from them.

The zip holds the protocol version that was current when you downloaded it. Download and upload it
again after a new version comes out.

### 3. Install it in Claude Code

[Claude Code](https://code.claude.com/docs) is Anthropic's tool for working with Claude on the files
in a folder on your computer. If you use it, type these two commands in a session:

```
/plugin marketplace add submarine-mrv/oae-data-protocol
/plugin install oae-metadata@oae-data
```

To receive new versions without asking, type `/plugin`, choose Marketplaces, then `oae-data`, then
Enable auto-update. To update by hand, run `claude plugin update oae-metadata@oae-data` in a terminal.

### When a new protocol version comes out

A copy you added or installed (ways 2 and 3) checks this site when it starts. If a newer protocol
version is published, the assistant tells you and still drafts with the copy it has. Claude in the
browser usually cannot reach this site from where it runs code, so there the check is skipped.

## Checking the draft yourself

The skill comes with a checker, a small Python script. It reads a metadata file and lists:

- errors, such as a field the protocol does not have or a value outside its vocabulary
- gaps, meaning required fields that are still empty
- each bounding box in words, so a swapped latitude and longitude is easy to spot

An assistant that can run code runs it for you. To run it yourself you need Python 3 and nothing
else:

```bash
curl -O https://schema.oaedata.org/skill/scripts/validate.py
curl -O https://schema.oaedata.org/skill/assets/oae_data_protocol.schema.json
python3 validate.py your-metadata.json --schema oae_data_protocol.schema.json
```

The Metadata Builder shows the same errors after you import a draft, so this step is optional.

## Limits

- The draft is a starting point. Review every value against its source before you publish.
- Maps and figures are not read. Locations shown only on a map are reported as missing.
- Importing a dataset twice creates two datasets. Delete the old one in the Builder first.
- NetCDF files are not supported yet.

## For developers

Every page of this site is also published as markdown for assistants: add `.md` to a page's address
(for example [`/FieldDataset.md`](https://schema.oaedata.org/FieldDataset.md)), or start from
[`/llms.txt`](https://schema.oaedata.org/llms.txt). The skill's source is in the
[protocol repository](https://github.com/submarine-mrv/oae-data-protocol/tree/main/skills).
