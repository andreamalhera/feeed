import pytest
from pm4py.objects.log.obj import EventLog, Trace

from feeed import EmptyLogError
from feeed.feature_extractor import *
from feeed.complexity.dfg_based import DFGBased

EMPTY_LOGS = {"no_traces": EventLog(), "no_events": EventLog([Trace(), Trace()])}

@pytest.mark.parametrize("log_kind", EMPTY_LOGS)
@pytest.mark.parametrize("ft_name", FEATURE_TYPES)
def test_extract_raises_empty_log_error(ft_name, log_kind):
    feature_class = eval(feature_type(ft_name))
    with pytest.raises(EmptyLogError):
        feature_class(feature_names=[ft_name]).extract(EMPTY_LOGS[log_kind])

@pytest.mark.parametrize("log_kind", EMPTY_LOGS)
def test_dfg_direct_call_raises_empty_log_error(log_kind):
    with pytest.raises(EmptyLogError):
        DFGBased.n_nodes_dfg(EMPTY_LOGS[log_kind])
