# FEEED: **Fe**ature **E**xtraction from **E**vent **D**ata [[0]](#references)

The analysis of event data is largely influenced by the effective characterization of descriptors. These descriptors serve as the building blocks of our understanding, encapsulating the behavior described within the event data. In light of these considerations, we introduce FEEED (**Fe**ature **E**xtraction for **E**vent **D**ata), an extendable tool for event data feature extraction. FEEED represents a significant advancement in event data behavior analysis, offering a range of features to empower analysts and data scientists in their pursuit of insightful, actionable, and understandable event data analysis. What sets FEEED apart is its unique capacity to act as a bridge between the worlds of data mining and process mining. In doing so, it promises to enhance the accuracy, comprehensiveness, and utility of characterizing event data for a diverse range of applications.

A video tutorial on how to use this tool can be found [here](https://www.youtube.com/watch?v=wS6n3ngRRd8).
If you'd like to learn more about how it works, see References below.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Extending Features](#extending-features)
- [References](#references)

## Installation
Requirements:
- Python > 3.9
- [Java](https://www.java.com/en/download/)

To directly use meta feature extraction methods via `import`, install directly from [PyPi](https://pypi.org/project/feeed/) with
```shell
pip install feeed
```
Run:
```shell
python -c "from feeed.feature_extractor import extract_features; print(extract_features('test_data/Sepsis.xes'))"
```

## Usage
Features extracted by this tool stem from [[2]](#references),[[3]](#references),[[4]](#references),[[5]](#references).
Output data contains at least one feature with a `feature_name` and a corresponding value obtained by that feature's specific computation. The schema looks like this:
```python
{
'log': 'Sepsis'
'feature_name': value
}
```
Every `feature_name` belongs to a `feature_type`, and a `feature_type` can comprise multiple features. The following Feature Types table presents the correspondence between `feature_type` and `feature_name`. 

### Feature types
Specific `feature_name`s and `feature_type`s can be selected as in the examples below:

| Feature Type     | Feature Names                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| simple_stats     | n_traces, n_variants, ratio_variants_per_number_of_traces                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| trace_length     | trace_len_min, trace_len_max, trace_len_mean, trace_len_median, trace_len_mode, trace_len_std, trace_len_variance, trace_len_q1, trace_len_q3, trace_len_iqr, trace_len_geometric_mean, trace_len_geometric_std, trace_len_harmonic_mean, trace_len_skewness, trace_len_kurtosis, trace_len_coefficient_variation, trace_len_entropy, trace_len_hist1, trace_len_hist2, trace_len_hist3, trace_len_hist4, trace_len_hist5, trace_len_hist6, trace_len_hist7, trace_len_hist8, trace_len_hist9, trace_len_hist10, trace_len_skewness_hist, trace_len_kurtosis_hist |
| trace_variant    | ratio_most_common_variant, ratio_top_1_variants, ratio_top_5_variants, ratio_top_10_variants, ratio_top_20_variants, ratio_top_50_variants, ratio_top_75_variants, mean_variant_occurrence, std_variant_occurrence, skewness_variant_occurrence, kurtosis_variant_occurrence                                                                                                                                                                                                                                                                                      |
| activities       | n_unique_activities, activities_min, activities_max, activities_mean, activities_median, activities_std, activities_variance, activities_q1, activities_q3, activities_iqr, activities_skewness, activities_kurtosis                                                                                                                                                                                                                                                                                                                                              |
| start_activities | n_unique_start_activities, start_activities_min, start_activities_max, start_activities_mean, start_activities_median, start_activities_std, start_activities_variance, start_activities_q1, start_activities_q3, start_activities_iqr, start_activities_skewness, start_activities_kurtosis                                                                                                                                                                                                                                                                      |
| end_activities   | n_unique_end_activities, end_activities_min, end_activities_max, end_activities_mean, end_activities_median, end_activities_std, end_activities_variance, end_activities_q1, end_activities_q3, end_activities_iqr, end_activities_skewness, end_activities_kurtosis                                                                                                                                                                                                                                                                                              |
| eventropies[[4]](#references)   | eventropy_trace, eventropy_prefix, eventropy_prefix_flattened, eventropy_global_block, eventropy_global_block_flattened, eventropy_lempel_ziv, eventropy_lempel_ziv_flattened, eventropy_k_block_diff_1, eventropy_k_block_diff_3, eventropy_k_block_diff_5, eventropy_k_block_ratio_1, eventropy_k_block_ratio_3, eventropy_k_block_ratio_5, eventropy_knn_3, eventropy_knn_5, eventropy_knn_7                                                                                                                                                                 |
| epa_based[[5]](#references)       | epa_variant_entropy, epa_normalized_variant_entropy, epa_sequence_entropy, epa_normalized_sequence_entropy, epa_sequence_entropy_linear_forgetting, epa_normalized_sequence_entropy_linear_forgetting, epa_sequence_entropy_exponential_forgetting, epa_normalized_sequence_entropy_exponential_forgetting
| time_based       | accumulated_time, execution_time, remaining_time, within_day (with each: min, max, mean, median, mode, std, variance, q1, q3, iqr, geometric_mean, geometric_std, harmonic_mean, skewness, kurtosis, coefficient_variation, entropy, skewness_hist, kurtosis_hist resulting in e.g. accumulated_time_min)|

### Examples
For the following examples we used Sepsis event data[1].
#### Example 1:
Passing sublist of feature_names, e.g. ['start_activities_min', 'end_activities_max'], to get a list of values for those features only.
```shell
python -c "from feeed.feature_extractor import extract_features; print(extract_features('test_data/Sepsis.xes',  ['start_activities_min', 'end_activities_max']))"
```
outputs
```python
SUCCESSFULLY: 2 features for SEPSIS.xes took 0:00:00.342855 sec.
{'log': 'SEPSIS', 'start_activities_min': 6, 'end_activities_max': 393}
```

#### Example 2:
Passing sublist of feature_types, e.g. ['start_activities'], to get a list of values for the feature type 'start_activities' only
```shell
python -c "from feeed.feature_extractor import extract_features; print(extract_features('test_data/Sepsis.xes',  ['start_activities']))"
```
outputs
```python
SUCCESSFULLY: 12 features for Sepsis.xes took 0:00:01.946063 sec.
{'log': 'Sepsis', 'n_unique_start_activities': 6, 'start_activities_iqr': 9.25, 'start_activities_kurtosis': 1.199106773708694, 'start_activities_max': 995, 'start_activities_mean': 175.0, 'start_activities_median': 12.0, 'start_activities_min': 6, 'start_activities_q1': 7.75, 'start_activities_q3': 17.0, 'start_activities_skewness': 1.7883562472303318, 'start_activities_std': 366.73787187399483, 'start_activities_variance': 134496.66666666666}
```

#### Example 3:
By not passing any list of feature_types to get the full list of all feature values for all feature_types,
from the shell
```shell
python -c "from feeed.feature_extractor import extract_features; print(extract_features('test_data/Sepsis.xes'))"
```
For the order of feature_names as in [Feature Type table](#feature-types):
```python
python -c "from feeed.feature_extractor import extract_features; print(extract_features('test_data/Sepsis.xes', ['n_traces', 'n_variants', 'ratio_variants_per_number_of_traces', 'trace_len_min', 'trace_len_max', 'trace_len_mean', 'trace_len_median', 'trace_len_mode', 'trace_len_std', 'trace_len_variance', 'trace_len_q1', 'trace_len_q3', 'trace_len_iqr', 'trace_len_geometric_mean', 'trace_len_geometric_std', 'trace_len_harmonic_mean', 'trace_len_skewness', 'trace_len_kurtosis', 'trace_len_coefficient_variation', 'trace_len_entropy', 'trace_len_hist1', 'trace_len_hist2', 'trace_len_hist3', 'trace_len_hist4', 'trace_len_hist5', 'trace_len_hist6', 'trace_len_hist7', 'trace_len_hist8', 'trace_len_hist9', 'trace_len_hist10', 'trace_len_skewness_hist', 'trace_len_kurtosis_hist', 'ratio_most_common_variant', 'ratio_top_1_variants', 'ratio_top_5_variants', 'ratio_top_10_variants', 'ratio_top_20_variants', 'ratio_top_50_variants', 'ratio_top_75_variants', 'mean_variant_occurrence', 'std_variant_occurrence', 'skewness_variant_occurrence', 'kurtosis_variant_occurrence', 'n_unique_activities', 'activities_min', 'activities_max', 'activities_mean', 'activities_median', 'activities_std', 'activities_variance', 'activities_q1', 'activities_q3', 'activities_iqr', 'activities_skewness', 'activities_kurtosis', 'n_unique_start_activities', 'start_activities_min', 'start_activities_max', 'start_activities_mean', 'start_activities_median', 'start_activities_std', 'start_activities_variance', 'start_activities_q1', 'start_activities_q3', 'start_activities_iqr', 'start_activities_skewness', 'start_activities_kurtosis', 'n_unique_end_activities', 'end_activities_min', 'end_activities_max', 'end_activities_mean', 'end_activities_median', 'end_activities_std', 'end_activities_variance', 'end_activities_q1', 'end_activities_q3', 'end_activities_iqr', 'end_activities_skewness', 'end_activities_kurtosis', 'eventropy_trace', 'eventropy_prefix', 'eventropy_global_block', 'eventropy_lempel_ziv', 'eventropy_k_block_diff_1', 'eventropy_k_block_diff_3', 'eventropy_k_block_diff_5', 'eventropy_k_block_ratio_1', 'eventropy_k_block_ratio_3', 'eventropy_k_block_ratio_5', 'eventropy_knn_3', 'eventropy_knn_5', 'eventropy_knn_7', 'epa_variant_entropy', 'epa_normalized_variant_entropy', 'epa_sequence_entropy', 'epa_normalized_sequence_entropy', 'epa_sequence_entropy_linear_forgetting', 'epa_normalized_sequence_entropy_linear_forgetting', 'epa_sequence_entropy_exponential_forgetting', 'epa_normalized_sequence_entropy_exponential_forgetting', 'accumulated_time', 'execution_time', 'remaining_time', 'within_day']))"
```
or in a python script
```python
from feeed.feature_extractor import extract_features

features = extract_features("test_data/Sepsis.xes")

```
outputs
```python
SUCCESSFULLY: 179 features for Sepsis.xes took 0:00:14.875727 sec.

{'log': 'Sepsis', 'n_traces': 1050, 'n_variants': 846, 'ratio_variants_per_number_of_traces': 0.8057142857142857, 'trace_len_coefficient_variation': 0.7916391922924689, 'trace_len_entropy': 6.769403523350811, 'trace_len_geometric_mean': 12.281860759040903, 'trace_len_geometric_std': 1.7464004837799154, 'trace_len_harmonic_mean': 10.47731701485374, 'trace_len_hist1': 0.048613291470434326, 'trace_len_hist10': 0.00010465724751439027, 'trace_len_hist2': 0.005285190999476714, 'trace_len_hist3': 0.0005756148613291472, 'trace_len_hist4': 0.0002093144950287807, 'trace_len_hist5': 0.00010465724751439036, 'trace_len_hist6': 0.0, 'trace_len_hist7': 5.232862375719522e-05, 'trace_len_hist8': 0.0, 'trace_len_hist9': 0.0, 'trace_len_iqr': 7.0, 'trace_len_kurtosis': 87.0376906898399, 'trace_len_kurtosis_hist': 4.931206347805768, 'trace_len_max': 185, 'trace_len_mean': 14.48952380952381, 'trace_len_median': 13.0, 'trace_len_min': 3, 'trace_len_mode': 8, 'trace_len_q1': 9.0, 'trace_len_q3': 16.0, 'trace_len_skewness': 7.250526815880918, 'trace_len_skewness_hist': 2.6128507781562513, 'trace_len_std': 11.470474925273926, 'trace_len_variance': 131.57179501133788, 'kurtosis_variant_occurrence': 217.44268017168216, 'mean_variant_occurrence': 1.2411347517730495, 'ratio_most_common_variant': 0.03333333333333333, 'ratio_top_10_variants': 0.2742857142857143, 'ratio_top_1_variants': 0.12, 'ratio_top_20_variants': 0.35523809523809524, 'ratio_top_50_variants': 0.5971428571428572, 'ratio_top_5_variants': 0.21523809523809523, 'ratio_top_75_variants': 0.7980952380952381, 'skewness_variant_occurrence': 13.637101374069475, 'std_variant_occurrence': 1.7594085182491936, 'activities_iqr': 983.5, 'activities_kurtosis': 1.05777753209275, 'activities_max': 3383, 'activities_mean': 950.875, 'activities_median': 788.0, 'activities_min': 6, 'activities_q1': 101.75, 'activities_q3': 1085.25, 'activities_skewness': 1.3912385607018212, 'activities_std': 1008.5815457239935, 'activities_variance': 1017236.734375, 'n_unique_activities': 16, 'n_unique_start_activities': 6, 'start_activities_iqr': 9.25, 'start_activities_kurtosis': 1.199106773708694, 'start_activities_max': 995, 'start_activities_mean': 175.0, 'start_activities_median': 12.0, 'start_activities_min': 6, 'start_activities_q1': 7.75, 'start_activities_q3': 17.0, 'start_activities_skewness': 1.7883562472303318, 'start_activities_std': 366.73787187399483, 'start_activities_variance': 134496.66666666666, 'end_activities_iqr': 39.5, 'end_activities_kurtosis': 2.5007579343413617, 'end_activities_max': 393, 'end_activities_mean': 75.0, 'end_activities_median': 32.5, 'end_activities_min': 2, 'end_activities_q1': 14.0, 'end_activities_q3': 53.5, 'end_activities_skewness': 2.004413358907822, 'end_activities_std': 112.91400014423114, 'end_activities_variance': 12749.57142857143, 'n_unique_end_activities': 14, 'eventropy_global_block': 14.501, 'eventropy_global_block_flattened': 14.655, 'eventropy_k_block_diff_1': 3.238, 'eventropy_k_block_diff_3': 1.712, 'eventropy_k_block_diff_5': 1.104, 'eventropy_k_block_ratio_1': 3.238, 'eventropy_k_block_ratio_3': 2.262, 'eventropy_k_block_ratio_5': 1.871, 'eventropy_knn_3': 4.956, 'eventropy_knn_5': 4.49, 'eventropy_knn_7': 4.191, 'eventropy_lempel_ziv': 1.727, 'eventropy_lempel_ziv_flattened': 1.888, 'eventropy_prefix': 10.227, 'eventropy_prefix_flattened': 10.595, 'eventropy_trace': 9.334, 'epa_normalized_sequence_entropy': 0.5223430410751398, 'epa_normalized_sequence_entropy_exponential_forgetting': 0.29950463593968696, 'epa_normalized_sequence_entropy_linear_forgetting': 0.21936523360299368, 'epa_normalized_variant_entropy': 0.6957588422064969, 'epa_sequence_entropy': 76528.6794749776, 'epa_sequence_entropy_exponential_forgetting': 43880.53919110408, 'epa_sequence_entropy_linear_forgetting': 32139.284589305265, 'epa_variant_entropy': 40624.49329803771, 'accumulated_time_min': 0.0, 'accumulated_time_max': 36488789.0, 'accumulated_time_mean': 396893.5456158801, 'accumulated_time_median': 11924.0, 'accumulated_time_mode': 0.0, 'accumulated_time_std': 1603193.2693230412, 'accumulated_time_variance': 2570228658802.701, 'accumulated_time_q1': 1138.5, 'accumulated_time_q3': 273793.5, 'accumulated_time_iqr': 272655.0, 'accumulated_time_geometric_mean': 10904.332835327954, 'accumulated_time_geometric_std': 44.90292804116573, 'accumulated_time_harmonic_mean': 0.0, 'accumulated_time_skewness': 11.401470845961647, 'accumulated_time_kurtosis': 172.5725804780399, 'accumulated_time_coefficient_variation': 4.039353340541942, 'accumulated_time_entropy': 7.7513093893416505, 'accumulated_time_skewness_hist': 2.6663623098416838, 'accumulated_time_kurtosis_hist': 5.1101603988544575, 'execution_time_min': 0.0, 'execution_time_max': 36051318.0, 'execution_time_mean': 169759.47397134217, 'execution_time_median': 188.0, 'execution_time_mode': 0.0, 'execution_time_std': 1442884.0333929851, 'execution_time_variance': 2081914333820.4087, 'execution_time_q1': 0.0, 'execution_time_q3': 18623.25, 'execution_time_iqr': 18623.25, 'execution_time_geometric_mean': 199.88320191111325, 'execution_time_geometric_std': 127.92792986844444, 'execution_time_harmonic_mean': 0.0, 'execution_time_skewness': 14.528527518337812, 'execution_time_kurtosis': 250.488253204707, 'execution_time_coefficient_variation': 8.499578843161146, 'execution_time_entropy': 6.221052534222753, 'execution_time_skewness_hist': 2.666603580180752, 'execution_time_kurtosis_hist': 5.110914600502133, 'remaining_time_min': 0.0, 'remaining_time_max': 36488789.0, 'remaining_time_mean': 2796232.825161036, 'remaining_time_median': 619470.0, 'remaining_time_mode': 0.0, 'remaining_time_std': 5281078.119895241, 'remaining_time_variance': 27889786108436.258, 'remaining_time_q1': 202862.5, 'remaining_time_q3': 2487420.0, 'remaining_time_iqr': 2284557.5, 'remaining_time_geometric_mean': 224736.22203397762, 'remaining_time_geometric_std': 70.1715364379747, 'remaining_time_harmonic_mean': 0.0, 'remaining_time_skewness': 3.1659682263680318, 'remaining_time_kurtosis': 11.666720436340661, 'remaining_time_coefficient_variation': 1.8886403422401359, 'remaining_time_entropy': 8.55331137332654, 'remaining_time_skewness_hist': 2.61693528788402, 'remaining_time_kurtosis_hist': 4.950830339077765, 'within_day_min': 0.0, 'within_day_max': 86340.0, 'within_day_mean': 44411.8630209018, 'within_day_median': 41160.0, 'within_day_mode': 28800.0, 'within_day_std': 20574.179204094926, 'within_day_variance': 423296849.9222121, 'within_day_q1': 28800.0, 'within_day_q3': 60433.5, 'within_day_iqr': 31633.5, 'within_day_geometric_mean': 37271.412987373165, 'within_day_geometric_std': 2.2119866614383827, 'within_day_harmonic_mean': 0.0, 'within_day_skewness': 0.18928976165276779, 'within_day_kurtosis': -0.7723273653451699, 'within_day_coefficient_variation': 0.46325863867525635, 'within_day_entropy': 9.513096875438656, 'within_day_skewness_hist': 0.7185535544033509, 'within_day_kurtosis_hist': 0.6172758296143384}
```

## Extending Features
This tutorial is for extending this tool to include additional features (e.g. time-based). As an example for this tutorial, we focus on the example of time-based features. The `feeed/time.py` script contains the class `TimeBased`, which extracts features from timestamps. FEEED focuses and extracts features of the whole log only (e.g., time within the day).

### Assumptions and conditions
To include new features in this repo, first consider the following:

* Clarifying whether the proposed feature is on event-log-level instead of a single event, trace, or activity level.
* Next, check for dependency and Python version compatibility with this current repo (see `setup.py`).

If both conditions apply, move on to implementation.

### Implementing any `NewFeatures` class
* Clone this repo to your local machine using `git clone git@github.com:lmu-dbs/feeed.git`
* Include the new module containing the `new_feature` computation in `feeed/`, resulting in `feeed/new_feature.py` (e.g. `feeed/time.py`).
* Import the new class `NewFeatures` in `feeed/feature_extractor.py` (e.g. `from .time import TimeBased as time_based`)
   * `NewFeatures` should inherit from [Feature](feeed/feature.py) to use `extract`.
   * Input for `NewFeatures` should support event-logs, as in [pm4py](https://pm4py.fit.fraunhofer.de/static/assets/api/2.7.5.1/api.html#input-pm4py-read).
   * Ensure output of the `NewFeatures` class is a dict of the sort: `{"new_feature_name_1": value1, "new_feature_name_2": value2}`.
* To call the new class and methods, include the new `new_feature_type` (e.g. "time_based") in the [list of `feeed/feature_extractor.py`](https://github.com/lmu-dbs/feeed/blob/688cbe290d5c434f98bc9f059da0010f81ec89f1/feeed/feature_extractor.py#L21).
    * Include the `new_feature_type` in [NEW_FEATURE_TYPE](https://github.com/lmu-dbs/feeed/blob/53d2473509d5eccb9126b7d7bd8487132afd2eb7/feeed/feature_extractor.py#L14)
* Include the new `new_feature_type` (e.g. "time_based") and its `feature_names`s (e.g. "accumulated_time_geometric_mean") in the [Feature Type table](#feature-types).

Below, see an example of pseudo-code of how to implement a new (generic) feature extraction class.
Note that `cls` is the class object of the form `<class 'feeed.new_feature_type.NewFeatures>`;
`**kwargs` points to e.g. log attributes, which can also be replaced by simply `log`, if desired;
and `summarize()` needs to be implemented depending on the feature level,
meaning if `arr_values` is on a log level, `summarize` is the identity function:

```python
import inspect

from .feature import Feature

class NewFeatures(Feature):
    def __init__(self, feature_names='new_feature_type'):
    self.feature_type="new_feature_type"
    self.available_class_methods = dict(inspect.getmembers(NewFeatures, predicate=inspect.ismethod))
    if self.feature_type in feature_names:
        self.feature_names = [*self.available_class_methods.keys()]
    else:
        self.feature_names = feature_names

    def helper_function(log):
        return len(log)*2

    @classmethod
    def new_feature_name_1(cls, **kwargs):
        double_length = NewFeatures.helper_funtion(log)
        return kwargs["event_attribute"] ** double_length

    @classmethod
    def new_feature_name_2(cls, **kwargs):
        double_length = NewFeatures.helper_funtion(log)
        return kwargs["event_attribute"] + double_length

```
### Testing the new implementation

After implementing the new feature; including it in the list of `feeed/feature_extractor.py` and importing the new method accordingly, you can quickly test it by running the:

```bash
python -c "from feeed.feature_extractor import extract_features; print(extract_features('test_data/SEPSIS.xes', ['new_feature_type']))"
```
and
```bash
python -c "from feeed.feature_extractor import extract_features; print(extract_features('test_data/SEPSIS.xes', ['new_feature_name_1', 'new_feature_name_2']))"
```

### Update documentation
When updating results and table in the documentation, please note that the features are sorted by their type and types are sorted chronologically.

Finally, consider submitting a pull request to our repository. We are looking forward to your new features! :)

## Acknowledgements
We thank [Anirudh](https://github.com/anirudh027) and [Nikolina R.](https://github.com/Niklkind) for assistance with the maintenance and automation of this repository, which greatly improved its usability.


## References
0. Maldonado, A., Tavares, G.M., Oyamada, R.S., Ceravolo, P., & Seidl, T. (2023). FEEED: Feature Extraction from Event Data. ICPM Doctoral Consortium / Demo.
1. Mannhardt, Felix (2016): Sepsis Cases - Event Log. Version 1. 4TU.ResearchData. dataset. https://doi.org/10.4121/uuid:915d2bfb-7e84-49ad-a286-dc35f063a460
2. G. M. Tavares, S. Barbon Junior, E. Damiani, and P. Ceravolo, “Selecting optimal trace clustering pipelines with meta-learning,” in Intelligent Systems, J. C. Xavier-Junior and R. A. Rios, Eds. Cham: Springer
International Publishing, 2022, pp. 150–164.
3. S. B. Jr., P. Ceravolo, R. S. Oyamada, and G. M. Tavares, “Trace encoding in process mining: a survey and benchmarking,” Engineering Applications of Artificial Intelligence, 2023.
4. C. O. Back, S. Debois, and T. Slaats, “Entropy as a measure of log variability,” Journal on Data Semantics, vol. 8, no. 2, Jun 2019.
5. A. Augusto, J. Mendling, M. Vidgof, and B. Wurm, “The connection between process complexity of event sequences and models discovered by process mining,” Information Sciences, vol. 598, pp. 196–215, 2022.
