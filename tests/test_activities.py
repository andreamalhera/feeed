import pandas as pd
import pytest

from feeed.activities import Activities as activities

def test_activities(mock_log_data):
    features = activities(feature_names=['activities']).extract(mock_log_data)
    print(features)
    assert len(features) == 12
    assert set(features.keys()) == set(['activities_iqr', 'activities_kurtosis', 'activities_max',
                                        'activities_mean', 'activities_median', 'activities_min', 'activities_q1',
                                        'activities_q3', 'activities_skewness', 'activities_std', 'activities_variance',
                                        'n_unique_activities'])

    assert features['activities_iqr']== pytest.approx(983.5)
    assert features['activities_kurtosis']== pytest.approx(1.05777753209275)
    assert features['activities_max']== pytest.approx(3383)
    assert features['activities_mean']== pytest.approx(950.875)
    assert features['activities_median']== pytest.approx(788.0)
    assert features['activities_min']== pytest.approx(6)
    assert features['activities_q1']== pytest.approx(101.75)
    assert features['activities_q3']== pytest.approx(1085.25)
    assert features['activities_skewness']== pytest.approx(1.3912385607018212)
    assert features['activities_std']== pytest.approx(1008.5815457239935)
    assert features['activities_variance']== pytest.approx(1017236.734375)
    assert features['n_unique_activities']== pytest.approx(16)
