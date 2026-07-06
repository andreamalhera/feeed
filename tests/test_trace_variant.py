import pandas as pd
import pytest

from feeed.trace_variant import TraceVariant as trace_variant

def test_trace_length(mock_log_data):
    features = trace_variant(feature_names=['trace_variant']).extract(mock_log_data)
    print(features)
    assert len(features) == 1
    assert set(features.keys()) == set(['kurtosis_variant_occurrence', 'mean_variant_occurrence',
                                        'ratio_most_common_variant', 'ratio_top_10_variants', 'ratio_top_1_variants',
                                        'ratio_top_20_variants', 'ratio_top_50_variants', 'ratio_top_5_variants',
                                        'ratio_top_75_variants', 'skewness_variant_occurrence', 'std_variant_occurrence'])

    assert features['kurtosis_variant_occurrence']== pytest.approx(217.44268017168216)
    assert features['mean_variant_occurrence']== pytest.approx(1.2411347517730495)
    assert features['ratio_most_common_variant']== pytest.approx(0.03333333333333333)
    assert features['ratio_top_10_variants']== pytest.approx(0.2742857142857143)
    assert features['ratio_top_1_variants']== pytest.approx(0.12)
    assert features['ratio_top_20_variants']== pytest.approx(0.35523809523809524)
    assert features['ratio_top_50_variants']== pytest.approx(0.5971428571428572)
    assert features['ratio_top_5_variants']== pytest.approx(0.21523809523809523)
    assert features['ratio_top_75_variants']== pytest.approx(0.7980952380952381)
    assert features['skewness_variant_occurrence']== pytest.approx(13.637101374069475)
    assert features['std_variant_occurrence']== pytest.approx(1.7594085182491936)

