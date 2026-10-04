import pandas as pd
import pytest

from feeed.complexity.repetitions import Repetitions as repetitions

def test_repetitions(mock_log_data_sepsis):
    features = repetitions(feature_names=['repetitions']).extract(mock_log_data_sepsis)
    print(features)
    assert len(features) == 8
    assert set(features.keys()) == set(['n_traces_with_loop', 'avg_traces_with_loop',
                                        'avg_loops_per_trace', 'max_loops_per_trace',
                                        'avg_loop_size_per_trace', 'max_loop_size_per_trace',
                                        'n_traces_with_repetition', 'avg_traces_with_repetition'])

    assert features['n_traces_with_loop']== pytest.approx(421.0)
    assert features['avg_traces_with_loop']== pytest.approx(0.40095238095238095)
    assert features['avg_loops_per_trace']== pytest.approx(0.8266666666666667)
    assert features['max_loops_per_trace']== pytest.approx(33.0)
    assert features['avg_loop_size_per_trace']== pytest.approx(2.456057007125891)
    assert features['max_loop_size_per_trace']== pytest.approx(8.0)
    assert features['n_traces_with_repetition']== pytest.approx(723.0)
    assert features['avg_traces_with_repetition']== pytest.approx(0.6885714285714286)
