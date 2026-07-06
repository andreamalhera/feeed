import pytest
import pandas as pd
from pm4py.objects.log.util import dataframe_utils
from pm4py.objects.conversion.log import converter as log_converter
from pm4py.objects.log.importer.xes import importer as xes_importer

@pytest.fixture(scope="session")
def mock_log_data():
    log = xes_importer.apply("test_data/Sepsis.xes")
    return log