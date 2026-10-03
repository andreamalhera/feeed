import pandas as pd
import pytest

from feeed.complexity.distinct_activities import DistinctActivities as distinct_activities

def test_distinct_activities(mock_log_data_sepsis):
    features = distinct_activities(feature_names=['distinct_activities']).extract(mock_log_data_sepsis)
    print(features)
    assert len(features) == 7
    assert set(features.keys()) == set(['distinct_activities_min', 'distinct_activities_max',
                                        'distinct_activities_mean', 'distinct_activities_std', 'event_density',
                                        'distinct_activities_non_overlap', 'complexity_factor'])

    assert features['distinct_activities_min']== pytest.approx(0.0)
    assert features['distinct_activities_max']== pytest.approx(12.0)
    assert features['distinct_activities_mean']== pytest.approx(9.124643196955281)
    assert features['distinct_activities_std']== pytest.approx(2.1229281030976637)
    assert features['event_density']== pytest.approx(0.6297407228081402)
    assert features['distinct_activities_non_overlap']== pytest.approx(0.2672578712477922)
    assert features['complexity_factor']== pytest.approx(89.39066539235645)
