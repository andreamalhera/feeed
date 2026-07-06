import pandas as pd
import pytest

from feeed.eventropies import Eventropies as eventropies

def test_eventropies(mock_log_data):
    features = eventropies(feature_names=['eventropies']).extract(mock_log_data)
    print(features)
    assert len(features) == 16
    assert set(features.keys()) == set(['eventropy_global_block', 'eventropy_global_block_flattened',
                                        'eventropy_k_block_diff_1', 'eventropy_k_block_diff_3',
                                        'eventropy_k_block_diff_5', 'eventropy_k_block_ratio_1',
                                        'eventropy_k_block_ratio_3', 'eventropy_k_block_ratio_5',
                                        'eventropy_knn_3', 'eventropy_knn_5', 'eventropy_knn_7',
                                        'eventropy_lempel_ziv', 'eventropy_lempel_ziv_flattened',
                                        'eventropy_prefix', 'eventropy_prefix_flattened', 'eventropy_trace'
                                        ])

    assert features['eventropy_global_block']== pytest.approx(14.501)
    assert features['eventropy_global_block_flattened']== pytest.approx(14.655)
    assert features['eventropy_k_block_diff_1']== pytest.approx(3.238)
    assert features['eventropy_k_block_diff_3']== pytest.approx(1.712)
    assert features['eventropy_k_block_diff_5']== pytest.approx(1.104)
    assert features['eventropy_k_block_ratio_1']== pytest.approx(3.238)
    assert features['eventropy_k_block_ratio_3']== pytest.approx(2.262)
    assert features['eventropy_k_block_ratio_5']== pytest.approx(1.871)
    assert features['eventropy_knn_3']== pytest.approx(4.956)
    assert features['eventropy_knn_5']== pytest.approx(4.49)
    assert features['eventropy_knn_7']== pytest.approx(4.191)
    assert features['eventropy_lempel_ziv']== pytest.approx(1.727)
    assert features['eventropy_lempel_ziv_flattened']== pytest.approx(1.888)
    assert features['eventropy_prefix']== pytest.approx(10.227)
    assert features['eventropy_prefix_flattened']== pytest.approx(10.595)
    assert features['eventropy_trace']== pytest.approx(9.334)


