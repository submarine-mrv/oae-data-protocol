"""Data test."""
import os
import glob
import unittest
import logging

from linkml_runtime.loaders import yaml_loader
from oae_data_protocol.datamodel.oae_data_protocol import Experiment

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, '*.yaml'))


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_data(self):
        """Data test."""
        logger.info("Setting up data test")
        for path in EXAMPLE_FILES:
            file_name = os.path.basename(path)
            logger.info("Running tests against file: %s", file_name)
            obj = yaml_loader.load(path, target_class=Experiment)
            assert obj
