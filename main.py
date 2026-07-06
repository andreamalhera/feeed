from datetime import datetime as dt
from feeed.feature_extractor import extract_features

import json
import numpy as np

def test_extract_features(expected_output_path, log_path="test_data/Sepsis.xes", by=None):
    print(f"RUNNING TEST: test_extract_features(expected_output_path={expected_output_path}, log_path={log_path}, by={by}")
    f = open(expected_output_path, 'r')
    expected_features = json.loads(f.read())

    features = extract_features(log_path, by)

    assert len(expected_features.keys()) == len(features.keys()), f"Difference: {len(expected_features.keys())-len(features.keys())}"
    assert expected_features.keys() == features.keys(), f"Difference: {set(expected_features.keys())-set(features.keys())}"
    return features

def default_handler(obj):
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    elif isinstance(obj, np.integer):
        return int(obj)
    else:
        raise TypeError('Object of type %s is not JSON serializable' % type(obj))

if __name__=='__main__':
    BY_TYPE = ["simple_stats","trace_length","trace_variant","activities","start_activities",
               "end_activities","eventropies","epa_based"]
    BY_NAME =['n_traces', 'n_variants', 'ratio_variants_per_number_of_traces',
              'trace_len_min', 'trace_len_max', 'trace_len_mean', 'trace_len_median',
              'trace_len_mode', 'trace_len_std', 'trace_len_variance', 'trace_len_q1',
              'trace_len_q3', 'trace_len_iqr', 'trace_len_geometric_mean', 'trace_len_geometric_std',
              'trace_len_harmonic_mean', 'trace_len_skewness', 'trace_len_kurtosis',
              'trace_len_coefficient_variation', 'trace_len_entropy', 'trace_len_hist1',
              'trace_len_hist2', 'trace_len_hist3', 'trace_len_hist4', 'trace_len_hist5',
              'trace_len_hist6', 'trace_len_hist7', 'trace_len_hist8', 'trace_len_hist9',
              'trace_len_hist10', 'trace_len_skewness_hist', 'trace_len_kurtosis_hist',
              'ratio_most_common_variant', 'ratio_top_1_variants', 'ratio_top_5_variants',
              'ratio_top_10_variants', 'ratio_top_20_variants', 'ratio_top_50_variants',
              'ratio_top_75_variants', 'mean_variant_occurrence', 'std_variant_occurrence',
              'skewness_variant_occurrence', 'kurtosis_variant_occurrence', 'n_unique_activities',
              'activities_min', 'activities_max', 'activities_mean', 'activities_median',
              'activities_std', 'activities_variance', 'activities_q1', 'activities_q3',
              'activities_iqr', 'activities_skewness', 'activities_kurtosis',
              'n_unique_start_activities', 'start_activities_min', 'start_activities_max',
              'start_activities_mean', 'start_activities_median', 'start_activities_std',
              'start_activities_variance', 'start_activities_q1', 'start_activities_q3',
              'start_activities_iqr', 'start_activities_skewness', 'start_activities_kurtosis',
              'n_unique_end_activities', 'end_activities_min', 'end_activities_max',
              'end_activities_mean', 'end_activities_median', 'end_activities_std',
              'end_activities_variance', 'end_activities_q1', 'end_activities_q3',
              'end_activities_iqr', 'end_activities_skewness', 'end_activities_kurtosis',
              'eventropy_trace', 'eventropy_prefix', 'eventropy_prefix_flattened',
              'eventropy_global_block',  'eventropy_global_block_flattened',
              'eventropy_lempel_ziv','eventropy_lempel_ziv_flattened',
              'eventropy_k_block_diff_1', 'eventropy_k_block_diff_3', 'eventropy_k_block_diff_5',
              'eventropy_k_block_ratio_1', 'eventropy_k_block_ratio_3', 'eventropy_k_block_ratio_5',
              'eventropy_knn_3', 'eventropy_knn_5', 'eventropy_knn_7', 'epa_variant_entropy',
              'epa_normalized_variant_entropy', 'epa_sequence_entropy', 'epa_normalized_sequence_entropy',
              'epa_sequence_entropy_linear_forgetting', 'epa_normalized_sequence_entropy_linear_forgetting',
              'epa_sequence_entropy_exponential_forgetting', 'epa_normalized_sequence_entropy_exponential_forgetting',
              'accumulated_time', 'execution_time', 'remaining_time', 'within_day']
    start_log = dt.now()

    features = test_extract_features('test_data/expected_output.json', by=BY_TYPE)
    test_extract_features('test_data/expected_output_by_name.json', by=BY_NAME)
    test_extract_features('test_data/expected_output_by_name.json')

    # Write the dictionary to a JSON file
    with open("output.json", "w") as json_file:
        json.dump(features, json_file, default=default_handler)

    print(f"SUCCESSFULLY: Running tests took {dt.now() - start_log} sec.")
