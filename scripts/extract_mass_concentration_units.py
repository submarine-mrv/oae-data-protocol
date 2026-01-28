#!/usr/bin/env python3
"""
Extract QUDT units with hasQuantityKind quantitykind:MassConcentration from local ontology file.
This is a lightweight replacement for vskit for the specific MassConcentration use case.
"""

import yaml
from pathlib import Path
import re

def load_vskit_config(config_path="vskit-config.yaml"):
    """Load vskit config to find the local unit.ttl path."""
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    # Get the path for qudt:unit
    unit_path = config['resource_resolvers']['qudt:unit']['shorthand']
    return unit_path

def extract_mass_concentration_units(ttl_path):
    """
    Extract all units that have qudt:hasQuantityKind quantitykind:MassConcentration.
    Returns a list of unit identifiers in the format "unit:____".
    """
    units = []
    current_unit = None

    with open(ttl_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            # Look for unit definitions (e.g., "unit:KiloGM-PER-M3")
            if line.startswith('unit:'):
                # Extract the unit identifier
                match = re.match(r'^(unit:\S+)', line)
                if match:
                    current_unit = match.group(1)

            # Look for hasQuantityKind quantitykind:MassConcentration
            elif 'hasQuantityKind quantitykind:MassConcentration' in line and current_unit:
                # Add the unit if we haven't already (avoid duplicates)
                if current_unit not in units:
                    units.append(current_unit)

    return sorted(set(units))

def main():
    # Load the vskit config to find the local ontology path
    unit_path = load_vskit_config()

    # Extract units
    units = extract_mass_concentration_units(unit_path)

    # Print results (one per line, ready for LinkML enum)
    print("# Mass Concentration Units from QUDT")
    print(f"# Found {len(units)} units with hasQuantityKind quantitykind:MassConcentration")
    print()
    for unit in units:
        print(unit)

if __name__ == "__main__":
    main()
