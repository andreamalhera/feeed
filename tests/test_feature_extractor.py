import pytest

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
                         'start_activities_variance': 134496.66666666666,
                         'rel_unique_start_activities': 0.0070921985815602835
                         }
    assert len(features) == 14
    assert features == EXPECTED_FEATURES

def test_extract_features_epa_subset_across_logs():
    epa_subset = ['epa_variant_entropy', 'epa_normalized_variant_entropy',
                  'epa_sequence_entropy', 'epa_normalized_sequence_entropy']

    first = extract_features("test_data/BPI_Challenge_2013_closed_problems.xes", epa_subset)
    sepsis = extract_features("test_data/Sepsis.xes", epa_subset)

    assert sepsis['epa_variant_entropy'] == pytest.approx(40624.49329803771, rel=1e-4)
    assert sepsis['epa_normalized_variant_entropy'] == pytest.approx(0.6957588422064969, rel=1e-4)
    assert sepsis['epa_sequence_entropy'] == pytest.approx(76528.6794749776, rel=1e-4)
    assert sepsis['epa_normalized_sequence_entropy'] == pytest.approx(0.5223430410751398, rel=1e-4)
    assert sepsis['epa_variant_entropy'] != pytest.approx(first['epa_variant_entropy'])
