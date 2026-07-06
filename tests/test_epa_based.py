import pandas as pd
import pytest

from feeed.epa_based import Epa_based as epa_based

def test_epa_based(mock_log_data):
    features = epa_based(feature_names=['epa_based']).extract(mock_log_data)
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
