import pandas as pd
import pytest

from feeed.trace_length import TraceLength as trace_length

def test_trace_length(mock_log_data):
    features = trace_length(feature_names=['trace_length']).extract(mock_log_data)
    print(features)
    assert len(features) == 29
    assert set(features.keys()) == set(['trace_len_coefficient_variation','trace_len_entropy',
                                        'trace_len_geometric_mean','trace_len_geometric_std',
                                        'trace_len_harmonic_mean','trace_len_hist1','trace_len_hist10',
                                        'trace_len_hist2','trace_len_hist3','trace_len_hist4',
                                        'trace_len_hist5','trace_len_hist6','trace_len_hist7',
                                        'trace_len_hist8','trace_len_hist9','trace_len_iqr',
                                        'trace_len_kurtosis','trace_len_kurtosis_hist','trace_len_max',
                                        'trace_len_mean','trace_len_median','trace_len_min',
                                        'trace_len_mode','trace_len_q1','trace_len_q3',
                                        'trace_len_skewness','trace_len_skewness_hist',
                                        'trace_len_std','trace_len_variance'])

    assert features['trace_len_coefficient_variation']== pytest.approx(.7916391922924689)
    assert features['trace_len_entropy']== pytest.approx(6.769403523350811)
    assert features['trace_len_geometric_mean']== pytest.approx(12.281860759040903)
    assert features['trace_len_geometric_std']== pytest.approx(1.7464004837799154)
    assert features['trace_len_harmonic_mean']== pytest.approx(10.47731701485374)
    assert features['trace_len_hist1']== pytest.approx(0.048613291470434326)
    assert features['trace_len_hist10']== pytest.approx(0.00010465724751439027)
    assert features['trace_len_hist2']== pytest.approx(0.005285190999476714)
    assert features['trace_len_hist3']== pytest.approx(0.0005756148613291472)
    assert features['trace_len_hist4']== pytest.approx(0.0002093144950287807)
    assert features['trace_len_hist5']== pytest.approx(0.00010465724751439036)
    assert features['trace_len_hist6']== pytest.approx(0.0)
    assert features['trace_len_hist7']== pytest.approx(5.232862375719522e-05)
    assert features['trace_len_hist8']== pytest.approx(0.0)
    assert features['trace_len_hist9']== pytest.approx(0.0)
    assert features['trace_len_iqr']== pytest.approx(7.0)
    assert features['trace_len_kurtosis']== pytest.approx(87.0376906898399)
    assert features['trace_len_kurtosis_hist']== pytest.approx(4.931206347805768)
    assert features['trace_len_max']== pytest.approx(185)
    assert features['trace_len_mean']== pytest.approx(14.48952380952381)
    assert features['trace_len_median']== pytest.approx(13.0)
    assert features['trace_len_min']== pytest.approx(3)
    assert features['trace_len_mode']== pytest.approx(8)
    assert features['trace_len_q1']== pytest.approx(9.0)
    assert features['trace_len_q3']== pytest.approx(16.0)
    assert features['trace_len_skewness']== pytest.approx(7.250526815880918)
    assert features['trace_len_skewness_hist']== pytest.approx(2.6128507781562513)
    assert features['trace_len_std']== pytest.approx(11.470474925273926)
    assert features['trace_len_variance']== pytest.approx(131.57179501133788)
