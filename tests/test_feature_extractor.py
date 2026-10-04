import pytest

from feeed import EmptyLogError
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

def test_extract_features_skips_empty_logs_in_batch(tmp_path):
    no_traces = tmp_path / "no_traces.xes"
    no_traces.write_text('<?xml version="1.0" encoding="UTF-8"?>\n<log xes.version="1.0"></log>\n')
    no_events = tmp_path / "no_events.xes"
    no_events.write_text('<?xml version="1.0" encoding="UTF-8"?>\n<log xes.version="1.0">\n'
                         '<trace><string key="concept:name" value="c1"/></trace>\n'
                         '<trace><string key="concept:name" value="c2"/></trace>\n'
                         '</log>\n')
    subset = ['n_traces', 'n_events', 'distinct_activities_min']
    log_paths = ["test_data/Sepsis.xes", str(no_traces), str(no_events),
                 "test_data/BPI_Challenge_2013_closed_problems.xes"]

    results, skipped = [], []
    for log_path in log_paths:
        try:
            results.append(extract_features(log_path, subset))
        except EmptyLogError as e:
            skipped.append(str(e))

    assert skipped == ["ERROR: Event log no_traces.xes contains no traces.",
                       "ERROR: Event log no_events.xes contains no events."]
    assert [r['log'] for r in results] == ['Sepsis', 'BPI_Challenge_2013_closed_problems']
    assert results[0] == {'log': 'Sepsis', 'n_traces': 1050, 'n_events': 15214, 'distinct_activities_min': 3}
    # Logs after the skipped ones must match a standalone run
    assert results[1] == extract_features("test_data/BPI_Challenge_2013_closed_problems.xes", subset)

def test_extract_features_typo_is_not_empty_log_error():
    with pytest.raises(ValueError) as e:
        extract_features("test_data/Sepsis.xes", ['n_traces_typo'])
    assert not isinstance(e.value, EmptyLogError)

def test_extract_features_within_day_tz():
    utc = extract_features("test_data/Sepsis.xes", ['n_events', 'within_day'])
    local = extract_features("test_data/Sepsis.xes", ['n_events', 'within_day'], tz='Europe/Amsterdam')

    assert utc['within_day_mode'] == pytest.approx(21600.0)
    assert utc['within_day_mean'] == pytest.approx(41330.543183909555, rel=1e-2)
    assert local['within_day_mode'] == pytest.approx(28800.0)
    assert local['within_day_mean'] == pytest.approx(44411.8630209018, rel=1e-2)
    assert utc['n_events'] == local['n_events'] == 15214

def test_extract_features_time_statistics():
    features = extract_features("test_data/Sepsis.xes", ['n_events', 'within_day_min', 'execution_time_max'])

    assert set(features) == {'log', 'n_events', 'within_day_min', 'execution_time_max'}
    assert features['within_day_min'] == pytest.approx(0.0)
    assert features['execution_time_max'] == pytest.approx(36051318.0)

    with pytest.raises(ValueError):
        extract_features("test_data/Sepsis.xes", ['within_day_foo'])
