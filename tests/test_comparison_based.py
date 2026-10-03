import pandas as pd
import pytest

from feeed.complexity.comparison_based import ComparisonBased as comparison_based

def test_comparison_based(mock_log_data_sepsis):
    features = comparison_based(feature_names=['comparison_based']).extract(mock_log_data_sepsis)
    print(features)
    assert len(features) == 7
    assert set(features.keys()) == set(['number_of_successions', 'number_of_ties',
                                        'structure', 'average_affinity', 'lempel_ziv_complexity',
                                        'deviation_from_random', 'average_edit_distance'])

    assert features['number_of_successions']== pytest.approx(115.0)
    assert features['number_of_ties']== pytest.approx(30.0)
    assert features['structure']== pytest.approx(0.9999580839327331)
    assert features['average_affinity']== pytest.approx(0.25580040954097816)
    assert features['lempel_ziv_complexity']== pytest.approx(2769.0)
    assert features['deviation_from_random']== pytest.approx(0.7874054734233626)
    assert features['average_edit_distance']== pytest.approx(18.891374097780197)
