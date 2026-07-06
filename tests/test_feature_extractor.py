from feeed.feature_extractor import extract_features

def test_extract_features():
    features = extract_features("test_data/Sepsis.xes", ['n_unique_start_activities'])

    assert len(features) == 2
    assert features['n_unique_start_activities'] == 6

def test_extract_features_select_group():
    features = extract_features("test_data/Sepsis.xes",  ['start_activities'])
    EXPECTED_FEATURES = {'log': 'Sepsis',
                         'n_unique_start_activities': 6,
                         'start_activities_iqr': 9.25,
                         'start_activities_kurtosis': 1.199106773708694,
                         'start_activities_max': 995,
                         'start_activities_mean': 175.0,
                         'start_activities_median': 12.0,
                         'start_activities_min': 6,
                         'start_activities_q1': 7.75,
                         'start_activities_q3': 17.0,
                         'start_activities_skewness': 1.7883562472303318,
                         'start_activities_std': 366.73787187399483,
                         'start_activities_variance': 134496.66666666666
                         }
    assert len(features) == 13
    assert features == EXPECTED_FEATURES
