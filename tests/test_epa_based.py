import pandas as pd
import pytest

from feeed.complexity.epa_based import Epa_based as epa_based

def test_epa_based(mock_log_data_sepsis):
    features = epa_based(feature_names=['epa_based']).extract(mock_log_data_sepsis)
    print(features)
    assert len(features) == 8
    assert set(features.keys()) == set(['epa_normalized_sequence_entropy',
                                        'epa_normalized_sequence_entropy_exponential_forgetting',
                                        'epa_normalized_sequence_entropy_linear_forgetting',
                                        'epa_normalized_variant_entropy',
                                        'epa_sequence_entropy',
                                        'epa_sequence_entropy_exponential_forgetting',
                                        'epa_sequence_entropy_linear_forgetting',
                                        'epa_variant_entropy'
                                        ])

    assert features['epa_normalized_sequence_entropy']== pytest.approx(0.5223430410751398)
    assert features['epa_normalized_sequence_entropy_exponential_forgetting']== pytest.approx(0.29950463, rel=1e-4)
    assert features['epa_normalized_sequence_entropy_linear_forgetting']== pytest.approx(0.219365233, rel=1e-4)
    assert features['epa_normalized_variant_entropy']== pytest.approx(0.6957588422064969, rel=1e-4)
    assert features['epa_sequence_entropy']== pytest.approx(76528.6794749776, rel=1e-4)
    assert features['epa_sequence_entropy_exponential_forgetting']== pytest.approx(43880.53919110408, rel=1e-4)
    assert features['epa_sequence_entropy_linear_forgetting']== pytest.approx(32139.284589305265, rel=1e-4)
    assert features['epa_variant_entropy']== pytest.approx(40624.49329803771, rel=1e-4)


def test_epa_based_cache_not_reused_across_logs(mock_log_data_sepsis, mock_log_data_bpi2013):
    # Regression: the EPA cache was only reset by the last feature method, so
    # extracting a subset of features leaked the first log's EPA into later logs.
    subset = ['epa_variant_entropy', 'epa_normalized_variant_entropy',
              'epa_sequence_entropy', 'epa_normalized_sequence_entropy']
    other_log = mock_log_data_bpi2013

    sepsis = epa_based(feature_names=subset).extract(mock_log_data_sepsis)
    other = epa_based(feature_names=subset).extract(other_log)

    other_epa = epa_based.log_to_epa(other_log)
    expected_graph = epa_based.graph_complexity(other_epa)
    expected_log = epa_based.log_complexity(other_epa)

    assert sepsis['epa_variant_entropy'] == pytest.approx(40624.49329803771, rel=1e-4)
    assert other['epa_variant_entropy'] == pytest.approx(expected_graph[0])
    assert other['epa_normalized_variant_entropy'] == pytest.approx(expected_graph[1])
    assert other['epa_sequence_entropy'] == pytest.approx(expected_log[0])
    assert other['epa_normalized_sequence_entropy'] == pytest.approx(expected_log[1])

    # Switching back must not return the other log's values either.
    sepsis_again = epa_based(feature_names=subset).extract(mock_log_data_sepsis)
    assert sepsis_again == pytest.approx(sepsis)
