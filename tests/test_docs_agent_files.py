"""Tests for the docs build hook that publishes files for AI agents."""

import importlib.util
from pathlib import Path

ROOT = Path(__file__).parent.parent
spec = importlib.util.spec_from_file_location("mkdocs_hooks", ROOT / "scripts" / "mkdocs_hooks.py")
hooks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hooks)


def build(tmp_path):
    docs, site = tmp_path / "docs", tmp_path / "site"
    (docs / "Datasets").mkdir(parents=True)
    site.mkdir()
    (docs / "index.md").write_text("# Home\n")
    (docs / "FieldDataset.md").write_text("# Class: FieldDataset\n")
    (docs / "Datasets" / "index.md").write_text("# Datasets\n")
    (docs / "img.png").write_bytes(b"x")
    config = {
        "docs_dir": str(docs),
        "site_dir": str(site),
        "site_url": "https://schema.example.org/",
        "site_name": "Example Schema",
        "nav": [{"Home": "index.md"}, {"Datasets": ["Datasets/index.md", {"FieldDataset": "FieldDataset.md"}]}],
    }
    hooks.on_post_build(config)
    return site


def test_every_page_is_published_as_markdown(tmp_path):
    site = build(tmp_path)
    assert (site / "FieldDataset.md").read_text() == "# Class: FieldDataset\n"
    assert (site / "Datasets" / "index.md").exists()
    assert not (site / "img.png").exists()


def test_skill_folder_is_published_as_plain_files(tmp_path):
    site = build(tmp_path)
    skill = site / "skill"
    assert (skill / "SKILL.md").read_text() == (ROOT / "skills" / "oae-metadata" / "SKILL.md").read_text()
    assert (skill / "scripts" / "validate.py").exists()
    assert (skill / "assets" / "oae_data_protocol.schema.json").exists()
    assert (skill / "references" / "docs" / "variables.md").exists()
    assert (site / "oae-metadata.zip").exists()


def test_llms_txt_lists_the_skill_and_the_nav_pages(tmp_path):
    text = (build(tmp_path) / "llms.txt").read_text()
    assert text.startswith("# Example Schema\n")
    assert "https://schema.example.org/skill/SKILL.md" in text
    assert "[FieldDataset](https://schema.example.org/FieldDataset.md)" in text
    assert "[Datasets](https://schema.example.org/Datasets/index.md)" in text


def test_skill_folder_has_an_index_and_llms_txt_lists_its_files(tmp_path):
    site = build(tmp_path)
    index = (site / "skill" / "index.html").read_text()
    llms = (site / "llms.txt").read_text()
    for path in ("SKILL.md", "references/builder-handoff.md", "references/docs/variables.md", "scripts/validate.py"):
        assert f'href="{path}"' in index
        assert f"https://schema.example.org/skill/{path}" in llms
