from feeed.simple_stats import SimpleStats as simple_stats

def test_simple_stats(mock_log_data_sepsis):
    features = simple_stats(feature_names=['simple_stats']).extract(mock_log_data_sepsis)
    print(features)
    assert len(features) == 4
    assert features['n_events'] == 15214
    assert features['n_traces'] == 1050
    assert features['n_variants'] == 846
    assert features['ratio_variants_per_number_of_traces'] == 0.8057142857142857
