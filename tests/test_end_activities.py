import pandas as pd
import pytest

from feeed.end_activities import EndActivities as end_activities

def test_end_activities(mock_log_data):
    features = end_activities(feature_names=['end_activities']).extract(mock_log_data)
    print(features)
    assert len(features) == 12
    assert set(features.keys()) == set(['end_activities_iqr', 'end_activities_kurtosis',
                                        'end_activities_max', 'end_activities_mean', 'end_activities_median',
                                        'end_activities_min', 'end_activities_q1', 'end_activities_q3',
                                        'end_activities_skewness', 'end_activities_std',
                                        'end_activities_variance', 'n_unique_end_activities'])

    assert features['end_activities_iqr']== pytest.approx(39.5)
    assert features['end_activities_kurtosis']== pytest.approx(2.5007579343413617)
    assert features['end_activities_max']== pytest.approx(393)
    assert features['end_activities_mean']== pytest.approx(75.0)
    assert features['end_activities_median']== pytest.approx(32.5)
    assert features['end_activities_min']== pytest.approx(2)
    assert features['end_activities_q1']== pytest.approx(14.0)
    assert features['end_activities_q3']== pytest.approx(53.5)
    assert features['end_activities_skewness']== pytest.approx(2.004413358907822)
    assert features['end_activities_std']== pytest.approx(112.91400014423114)
    assert features['end_activities_variance']== pytest.approx(12749.57142857143)
    assert features['n_unique_end_activities']== pytest.approx(14)
