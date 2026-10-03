import pytest
import pandas as pd
from pm4py.objects.log.util import dataframe_utils
from pm4py.objects.conversion.log import converter as log_converter
from pm4py.objects.log.importer.xes import importer as xes_importer

@pytest.fixture(scope="session")
def mock_log_data_sepsis():
    log = xes_importer.apply("test_data/Sepsis.xes")
    return log

@pytest.fixture(scope="session")
def mock_log_data_bpi2013():
    log = xes_importer.apply("test_data/BPI_Challenge_2013_closed_problems.xes")
    return log
