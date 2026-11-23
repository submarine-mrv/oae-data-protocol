# Setting up the oae-metadata skill

You are helping a researcher get set up to draft OAE Data Protocol metadata with you. The
`oae-metadata` skill is a set of instructions, reference files and a validator. It turns project
documentation and data files into a metadata file (JSON) and a short report of what is missing. The
researcher imports the JSON into the Metadata Builder at https://metadata.oaedata.org and finishes
it there.

Your job here is to work out which setup fits this researcher and walk them through it. Write
plainly and briefly. Most researchers have not heard of skills or plugins, so do not assume those
words mean anything to them.

## 1. Work out what you can from where you are running

Before asking anything, note what you already know:

- which tool you are (Claude Code or another coding tool in a terminal, the Claude app, ChatGPT, or
  something else)
- whether you can run Python code in this conversation
- whether the researcher has already attached files

## 2. Ask at most two questions

Ask only what you could not work out, in one message:

1. Do they want to try a draft now, or set things up to draft metadata regularly?
2. Do they want the draft checked against the protocol before they get it? The validator does this.
   Without it, the Metadata Builder shows the same errors after import.

## 3. Recommend one setup

Pick one and say why in a sentence. Mention another only if they ask.

**Try it now, nothing to install.** Best for a first attempt, and for any tool not listed below.
Ask them to attach their project documentation and data files to this chat. Then follow the
instructions at https://schema.oaedata.org/skill/SKILL.md; the other files it names are in the same
folder. For next time, give them this to paste into a new chat along with their files:

> Follow the instructions at https://schema.oaedata.org/skill/SKILL.md to draft OAE metadata from
> these files. The other files it mentions are in the same folder.

Tell them the limit: if you cannot run code here, the draft is not validated before they get it.

**Save the skill in the Claude or ChatGPT app.** Best for regular use in the browser or desktop app,
and when they want each draft validated. The package is https://schema.oaedata.org/oae-metadata.zip.

- If you can install a skill package from a web address yourself, install that zip file. Then
  confirm the installed skill contains `scripts/validate.py` and
  `assets/oae_data_protocol.schema.json`, and tell the researcher it is ready.
- If you can only save a single instructions file as a skill, do not. That copy leaves out the
  validator and the reference files. Give the researcher these steps instead:
    1. Download https://schema.oaedata.org/oae-metadata.zip
    2. Open the app's skills settings (in Claude: Customize, then Skills) and upload the zip file.
    3. In any new chat, attach files and ask for an OAE metadata draft.

Tell them the limit: the saved copy holds the protocol version from the day it was installed. When a
new version is released, the zip file has to be installed again.

**Install the plugin in Claude Code.** Best for someone who already works in Claude Code. They run:

```
/plugin marketplace add submarine-mrv/oae-data-protocol
/plugin install oae-metadata@oae-data
```

To get new versions automatically: `/plugin`, then Marketplaces, `oae-data`, Enable auto-update.

## 4. Finish

If they attached files and chose to try it now, start the draft. Otherwise end with the one thing
they should do next. The full guide for people is at https://schema.oaedata.org/ai-skill/.
