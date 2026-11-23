# Drafting Metadata with AI

Most of what a metadata file asks for is already written down somewhere: in a project plan, a
monitoring report, or the data files themselves. An AI tool such as Claude or ChatGPT can read this
project documentation and these data files and, with sufficient guidance, write a first draft of
your [metadata file](metadata-format.md). You then import the draft into the
[Metadata Builder](metadata-builder.md) to review, complete and validate it.

!!! tip "Quick start"
    Paste this into Claude or ChatGPT, and it will walk you through the setup that fits you:

    > Help me set up the oae-metadata skill so that we can draft metadata files together that
    > follow the OAE Data Protocol. See https://schema.oaedata.org/skill/install.md

For AI to effectively draft OAE metadata, it needs to know how the OAE Data Protocol is structured,
which types of values each field in the metadata accepts, and when to leave a field empty. To make
this process easier for researchers, we've developed an
"[agent skill](https://github.com/submarine-mrv/oae-data-protocol/tree/main/skills/oae-metadata)"
that can be imported into your local AI workflow to ensure your AI tool is able to work effectively
with the OAE Data Protocol. For more background on agent skills, see Anthropic's documentation on
[using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude).

## What you get

With the skill, your AI tool produces two files:

- a metadata file (JSON) containing whichever of the project, experiments and datasets your
  documentation describes
- a short report listing the required fields it could not find, values it was unsure of, and places
  where your sources disagree

The skill instructs the AI tool not to guess. A required field it cannot find is left empty and
listed in the report, for you to complete in the Metadata Builder.

## What to provide

- Project documentation, e.g. project design documents, monitoring or operations reports, or methods
  descriptions (PDF or text)
- Data files (CSV or XLSX): one dataset per file, one variable per data column
- OAPMetadata XML, if you have already submitted to OCADS

Tell the AI tool whether the project is new or already exists in the Metadata Builder. For an
existing project, provide its project ID and, for each dataset, the ID of the experiment it belongs
to.

## How to use the skill

There are three ways to use the skill, depending on which AI tool you work with. If you are unsure,
start with the first.

| | Works with | Stays up to date with the protocol | Validates its own draft |
|---|---|---|---|
| [1. Share a link in a chat](#1-share-a-link-in-a-chat) | Any AI tool that can open web pages | Yes | Sometimes |
| [2. Upload the skill to Claude or ChatGPT](#2-upload-the-skill-to-claude-or-chatgpt) | Claude or ChatGPT (browser or desktop app) | No, it needs to be downloaded again for each new version | Yes |
| [3. Install the skill in Claude Code](#3-install-the-skill-in-claude-code) | Claude Code | Yes, when the skill is updated | Yes |

"Validates its own draft" means the AI tool runs the [validator](#validating-a-draft-yourself)
included with the skill, and fixes any errors it finds before handing you the files.

### 1. Share a link in a chat

This approach requires no installation. Start a new chat, attach your files and paste the following:

> Follow the instructions at https://schema.oaedata.org/skill/SKILL.md to draft OAE metadata from
> these files. The other files it mentions are in the same folder.

!!! warning "Limitations of this approach"
    - Many AI chat tools are not able to download and run the validator. The report states when it
      was not run, and any errors will then show up once you import the draft into the Metadata
      Builder.
    - The AI tool has to open each of the skill's reference files itself, and some open fewer than
      the instructions ask for.
    - If your AI tool offers to save the instructions as a skill, the saved copy may hold only the
      instructions, without the validator and the reference files. Upload the zip file instead, as
      described in the next approach.

### 2. Upload the skill to Claude or ChatGPT

Download [oae-metadata.zip](https://schema.oaedata.org/oae-metadata.zip) and upload it in your AI
tool's skills settings. In Claude (in the browser or the desktop app), open Customize, then Skills.
In ChatGPT, open the skills page in your settings, or ask ChatGPT to install the skill from the zip
file's address. From then on you can attach your files to any chat and ask for a draft of OAE
metadata from them.

Saved skills depend on your plan and on code execution being turned on. If you do not see a skills
page in your settings, use the first approach.

The zip file contains the version of the protocol that was current when you downloaded it. Download
and upload it again whenever a new version of the protocol is released.

### 3. Install the skill in Claude Code

[Claude Code](https://code.claude.com/docs) is Anthropic's tool for working with Claude directly on
the files in a folder on your computer. If you use it, run these two commands in a session:

```
/plugin marketplace add submarine-mrv/oae-data-protocol
/plugin install oae-metadata@oae-data
```

To receive new versions automatically, type `/plugin`, choose Marketplaces, then `oae-data`, then
Enable auto-update. To update manually, run `claude plugin update oae-metadata@oae-data` in a
terminal.

### Staying up to date with the protocol

An uploaded or installed copy of the skill (approaches 2 and 3) checks this site each time it is
used, and again each time it validates a draft. There are three outcomes:

- Your copy is current: nothing changes.
- A newer version of the protocol has been released: your AI tool tells you, drafts from the current
  files on this site instead of your copy, and asks you to replace your copy.
- The check could not reach this site, which is common for AI tools in the browser: the report's
  first line says the version could not be confirmed.

In every case the Metadata Builder validates a draft against the current protocol when you import
it.

## Validating a draft yourself

The skill includes a validator, a small Python script that reads a metadata file and reports:

- errors, such as a field the protocol does not define or a value outside its controlled vocabulary
- gaps, i.e. required fields that are still empty
- each bounding box written out in words, so that a swapped latitude and longitude is easy to spot

An AI tool that can run code will run the validator for you. To run it yourself, all you need is
Python 3:

```bash
curl -O https://schema.oaedata.org/skill/scripts/validate.py
curl -O https://schema.oaedata.org/skill/assets/oae_data_protocol.schema.json
python3 validate.py your-metadata.json --schema oae_data_protocol.schema.json
```

This step is optional: the Metadata Builder shows the same errors once you import a draft. A
metadata file can also be validated directly against the JSON Schema, see
[Validating a File](metadata-format.md#validating-a-file).

## Limitations

- An AI-drafted metadata file is a starting point. Review every value against its source before you
  publish.
- Maps and figures are not read. Locations that are only shown on a map are reported as missing.
- Importing a dataset twice creates two datasets. Delete the old one in the Metadata Builder first.
- NetCDF files are not supported yet.

## For developers

Every page of this site is also published as markdown for AI tools: add `.md` to a page's address
(for example [`/FieldDataset.md`](https://schema.oaedata.org/FieldDataset.md)), or start from
[`/llms.txt`](https://schema.oaedata.org/llms.txt). The source of the skill is in the
[protocol repository](https://github.com/submarine-mrv/oae-data-protocol/tree/main/skills).
