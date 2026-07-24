"""OAE Data Protocol package.

The version is derived from git tags at build time via uv-dynamic-versioning
(see pyproject.toml). At runtime we read it back from the installed package
metadata; there is no committed VERSION file or generated _version.py.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("oae_data_protocol")
except PackageNotFoundError:  # package not installed (e.g. running from a source tree)
    __version__ = "0.0.0"
