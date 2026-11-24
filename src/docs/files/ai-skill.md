# Drafting Metadata with AI

Most of what a metadata file asks for is already written down somewhere: in a project plan, a
monitoring report, or the data files themselves. An AI tool such as Claude or ChatGPT can read this
project documentation and these data files and, with sufficient guidance, write a first draft of
your [metadata file](metadata-format.md). You then import the draft into the
[Metadata Builder](metadata-builder.md) to review, complete and validate it.

For AI to effectively draft OAE metadata, it needs to know how the OAE Data Protocol is structured,
which types of values each field in the metadata accepts, and when to leave a field empty. To make
this process easier for researchers, we've developed an
"[agent skill](https://github.com/submarine-mrv/oae-data-protocol/tree/main/skills/oae-metadata)"
that can be imported into your local AI workflow to ensure your AI tool is able to work effectively
with the OAE Data Protocol. For more background on agent skills, see Anthropic's documentation on
[using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude).

## Getting started

Paste this into Claude or ChatGPT:

> Help me set up the oae-metadata skill so that we can draft metadata files together that follow
> the OAE Data Protocol. See https://schema.oaedata.org/skill/install.md

Your AI tool reads the setup guide at that address, asks what you need if it cannot tell, and sets
the skill up in the way that fits the tool you are using. It may ask your permission to save the
skill for future chats. Once it is set up, attach your files and ask for a draft.

!!! warning "If your AI tool says it could not run the validator"
    The skill includes a validator that checks each draft against the protocol before you get it. If
    Claude or ChatGPT tells you it could not run the validator, the skill is not fully installed.
    Install it yourself, as described under
    [Installing the skill yourself](#installing-the-skill-yourself). A draft that was not validated
    can still be imported: the Metadata Builder will show its errors.

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

## Installing the skill yourself

### In Claude or ChatGPT

Download [oae-metadata.zip](https://schema.oaedata.org/oae-metadata.zip) and upload it in your AI
tool's skills settings. In Claude (in the browser or the desktop app), open Customize, then Skills.
In ChatGPT, open the skills page in your settings. From then on you can attach your files to any
chat and ask for a draft of OAE metadata from them.

In Claude you can also ask for the plugin file in a chat: "Download
https://schema.oaedata.org/oae-metadata.plugin and offer it to me to install", then press Install.

Saved skills depend on your plan and on code execution being turned on.

### From a plugin marketplace

The protocol's GitHub repository is a plugin marketplace for coding tools that work directly on the
files in a folder on your computer.

In [Claude Code](https://code.claude.com/docs), run these two commands in a session:

```
/plugin marketplace add submarine-mrv/oae-data-protocol
/plugin install oae-metadata@oae-data
```

To receive new versions automatically, type `/plugin`, choose Marketplaces, then `oae-data`, then
Enable auto-update. To update manually, run `claude plugin update oae-metadata@oae-data` in a
terminal.

In [Codex](https://developers.openai.com/codex), run these two commands in a terminal:

```
codex plugin marketplace add submarine-mrv/oae-data-protocol
codex plugin add oae-metadata@oae-data
```

## Staying up to date with the protocol

An installed copy of the skill holds the version of the protocol that was current when you
installed it. It checks for a newer version each time it is used, and again each time it validates a
draft. There are three outcomes:

- Your copy is current: nothing changes.
- A newer version of the protocol has been released: your AI tool tells you, drafts from the current
  files on this site instead of your copy, and asks you to install the skill again.
- The check could not be made: the report's first line says the version could not be confirmed.

In every case the Metadata Builder validates a draft against the current protocol when you import
it.

## Limitations

- An AI-drafted metadata file is a starting point. Review every value against its source before you
  publish.
- Maps and figures are not read. Locations that are only shown on a map are reported as missing.
- Importing a dataset twice creates two datasets. Delete the old one in the Metadata Builder first.
- NetCDF files are not supported yet.

## For developers

Every page of this site is also published as markdown for AI tools: add `.md` to a page's address
(for example [`/FieldDataset.md`](https://schema.oaedata.org/FieldDataset.md)), or start from
[`/llms.txt`](https://schema.oaedata.org/llms.txt). The skill's own instructions are at
[`/skill/SKILL.md`](https://schema.oaedata.org/skill/SKILL.md); an AI tool that can open web pages
can follow them from there without installing anything. The source of the skill is in the
[protocol repository](https://github.com/submarine-mrv/oae-data-protocol/tree/main/skills).
