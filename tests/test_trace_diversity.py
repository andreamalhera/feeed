import pandas as pd
import pytest

from feeed.complexity.trace_diversity import TraceDiversity as trace_diversity

def test_trace_diversity(mock_log_data_sepsis):
    features = trace_diversity(feature_names=['trace_diversity']).extract(mock_log_data_sepsis)
    print(features)
    assert len(features) == 2
    assert set(features.keys()) == set(['simple_trace_diversity', 'advanced_trace_diversity'])

    assert features['simple_trace_diversity']== pytest.approx(0.4297098001902949)
    assert features['advanced_trace_diversity']== pytest.approx(0.869360548361305)
