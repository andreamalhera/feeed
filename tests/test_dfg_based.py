import pandas as pd
import pytest

from feeed.complexity.dfg_based import DFGBased as dfg_based

def test_dfg_based(mock_log_data_sepsis):
    features = dfg_based(feature_names=['dfg_based']).extract(mock_log_data_sepsis)
    print(features)
    assert len(features) == 12
    assert set(features.keys()) == set(['n_nodes_dfg', 'n_edges_dfg', 'coeff_of_connectivity_dfg',
                                        'avg_node_degree_dfg', 'max_node_degree_dfg',
                                        'density_dfg', 'structure_dfg', 'cyclomatic_number_dfg',
                                        'n_cut_vertices_dfg', 'separability_ratio_dfg',
                                        'sequentiality_ratio_dfg', 'cyclicity_dfg'])

    assert features['n_nodes_dfg']== pytest.approx(18.0)
    assert features['n_edges_dfg']== pytest.approx(135.0)
    assert features['coeff_of_connectivity_dfg']== pytest.approx(7.5)
    assert features['avg_node_degree_dfg']== pytest.approx(15.0)
    assert features['max_node_degree_dfg']== pytest.approx(29)
    assert features['density_dfg']== pytest.approx(0.4411764705882353)
    assert features['structure_dfg']== pytest.approx(0.5833333333333333)
    assert features['cyclomatic_number_dfg']== pytest.approx(118.0)
    assert features['n_cut_vertices_dfg']== pytest.approx(0)
    assert features['separability_ratio_dfg']== pytest.approx(0.0)
    assert features['sequentiality_ratio_dfg']== pytest.approx(0.0)
    assert features['cyclicity_dfg']== pytest.approx(0.8888888888888888)
