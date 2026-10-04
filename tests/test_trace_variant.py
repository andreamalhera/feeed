import pandas as pd
import pytest

from feeed.trace_variant import TraceVariant as trace_variant

def test_trace_variant(mock_log_data_sepsis):
    features = trace_variant(feature_names=['trace_variant']).extract(mock_log_data_sepsis)
    print(features)
    assert len(features) == 15
    assert set(features.keys()) == set(['kurtosis_variant_occurrence', 'mean_variant_occurrence',
                                        'ratio_most_common_variant', 'ratio_top_10_variants', 'ratio_top_1_variants',
                                        'ratio_top_20_variants', 'ratio_top_50_variants', 'ratio_top_5_variants',
                                        'ratio_top_75_variants', 'skewness_variant_occurrence', 'std_variant_occurrence',
                                        'coverage_variants', 'rel_coverage_variants', 'heterogeneity_rate_variants',
                                        'similarity_rate_variants'])

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
    assert features['coverage_variants']== pytest.approx(840.0)
    assert features['rel_coverage_variants']== pytest.approx(0.9929078014184397)
    assert features['heterogeneity_rate_variants']== pytest.approx(0.968946356304189)
    assert features['similarity_rate_variants']== pytest.approx(0.43379017431429806)
