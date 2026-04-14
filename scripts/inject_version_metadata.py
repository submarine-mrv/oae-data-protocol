#!/usr/bin/env python3
"""
Inject version metadata into generated JSON schema files.

This script reads the VERSION file and injects it as a custom metadata field
at the root of the JSON schema. Git hashes should be obtained at runtime by
consuming applications to avoid version control conflicts.
"""

import json
import sys
from pathlib import Path


def get_version(version_file: Path) -> str:
    """Read version from VERSION file."""
    try:
        return version_file.read_text().strip()
    except FileNotFoundError:
        return "unknown"


def inject_metadata(schema_file: Path, version: str) -> None:
    """Inject version metadata into JSON schema."""
    with open(schema_file, "r") as f:
        schema = json.load(f)

    # Add custom metadata field at the root
    # Using 'x-' prefix for custom JSON Schema fields
    schema["x-protocol-version"] = version

    # Write back with pretty formatting
    with open(schema_file, "w") as f:
        json.dump(schema, f, indent=4)

    print(f"✓ Injected version into {schema_file.name}")
    print(f"  Version: {version}")


def main():
    # Determine repo root (parent of scripts directory)
    repo_root = Path(__file__).parent.parent
    version_file = repo_root / "VERSION"
    schema_file = repo_root / "project" / "jsonschema" / "oae_data_protocol.schema.json"

    # Allow override via command line
    if len(sys.argv) > 1:
        schema_file = Path(sys.argv[1])

    if not schema_file.exists():
        print(f"Error: Schema file not found: {schema_file}", file=sys.stderr)
        sys.exit(1)

    version = get_version(version_file)
    inject_metadata(schema_file, version)


if __name__ == "__main__":
    main()
