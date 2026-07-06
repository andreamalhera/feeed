import pandas as pd
import pytest

from feeed.start_activities import StartActivities as start_activities

def test_start_activities(mock_log_data):
    features = start_activities(feature_names=['start_activities']).extract(mock_log_data)
    print(features)
    assert len(features) == 12
    assert set(features.keys()) == set(['n_unique_start_activities', 'start_activities_iqr',
                                        'start_activities_kurtosis', 'start_activities_max',
                                        'start_activities_mean', 'start_activities_median',
                                        'start_activities_min', 'start_activities_q1', 'start_activities_q3',
                                        'start_activities_skewness', 'start_activities_std',
                                        'start_activities_variance'])

    assert features['n_unique_start_activities']== pytest.approx(6)
    assert features['start_activities_iqr']== pytest.approx(9.25)
    assert features['start_activities_kurtosis']== pytest.approx(1.199106773708694)
    assert features['start_activities_max']== pytest.approx(995)
    assert features['start_activities_mean']== pytest.approx(175.0)
    assert features['start_activities_median']== pytest.approx(12.0)
    assert features['start_activities_min']== pytest.approx(6)
    assert features['start_activities_q1']== pytest.approx(7.75)
    assert features['start_activities_q3']== pytest.approx(17.0)
    assert features['start_activities_skewness']== pytest.approx(1.7883562472303318)
    assert features['start_activities_std']== pytest.approx(366.73787187399483)
    assert features['start_activities_variance']== pytest.approx(134496.66666666666)

