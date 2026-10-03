import inspect
import numpy as np
import pandas as pd
import warnings

from .feature import Feature
from scipy import stats

"""
Implementing each time-based feature as `@classmethods` within this class allows us to scale and manage features easily. 
A current bottleneck is that each class method should accept `**kwargs` regardless of the other arguments, which
can be internally handled in the future. Each class method is accessed by inspecting the object using `inspect.getmembers`.

All the time features are currently measured in seconds, and they include:

- `execution_time`: execution time of an event w.r.t. to the previous one
- `accumulated_time`: accumulated time of an event w.r.t. to the first one from a trace
- `remaining_time`: remaining time of an event w.r.t. to the last one from a trace
- `within_day`: time within the day, in UTC unless an IANA time zone is passed as `tz` parameter (e.g. tz='Europe/Amsterdam')

Essentially, there are methods that accept `group` or `X` as arguments. The former consists of a trace (i.e., grouped by case id) since we evaluate, for instance, the event timestamp with the previous one. The latter consists of the whole event log, since some operations can be performed element-wise (e.g., extracting the weekday from a timestamp column).
"""
class TimeBased(Feature):
    def __init__(self, feature_names='time_based', tz=None):
        self.feature_type="time_based"
        self.tz = tz
        self.available_class_methods = dict(inspect.getmembers(TimeBased, predicate=inspect.ismethod))
        if self.feature_type in feature_names:
            self.feature_names = [*self.available_class_methods.keys()]
        else:
            self.feature_names = feature_names

    def extract(self, log):
        Feature.check_log(log)
        feature_names=self.feature_names

        output = {}
        for feature_name in feature_names:
            temp = {}
            feature_fn = self.available_class_methods[feature_name]
            feature_value = feature_fn(log, tz=self.tz)
            temp[f"{feature_name}"] = feature_value
            if isinstance(temp[feature_name], dict):
                output={**output, **dict(list(temp[feature_name].items()))}
            else:
                output={**output, **temp}
        return output

    def preprocess(log):
        time_column = "time:timestamp"
        if not isinstance(log, pd.DataFrame):
            import pm4py
            log = pm4py.convert_to_dataframe(log)
        else:
            log = log.copy()

        try:
            log[time_column] = pd.to_datetime(log[time_column], utc=True)
        except:
            log[time_column] = pd.to_datetime(log[time_column], format="mixed", utc=True)
        log = log.sort_values(by=[time_column]).reset_index(drop=True)
        group = log.groupby("case:concept:name", as_index=False, observed=True, group_keys=False)
        return group, log.index, time_column, log

    def postprocess(log, feature_values, feature_name):
        log[feature_name] = feature_values
        time_features = log[[feature_name]].apply(lambda x: meta(x))
        time_features = time_features.to_dict()
        result = {f"{feature_name}_{k}": v for k,v in time_features[feature_name].items()}
        return result

    """
    ref: https://github.com/raseidi/skpm/blob/main/skpm/event_feature_extraction/_time.py#L124
    """
    @classmethod
    def execution_time(cls, log, **kwargs):
        group, ix_list, time_col, log = TimeBased.preprocess(log)
        execution_times =  group[time_col].diff().loc[ix_list].dt.total_seconds().fillna(0)
        return TimeBased.postprocess(log, execution_times, "execution_time")

    @classmethod
    def accumulated_time(cls, log, **kwargs):
        group, ix_list, time_col, log = TimeBased.preprocess(log)
        accumulated_times = (group[time_col].apply(lambda x: x - x.min()).loc[ix_list].dt.total_seconds())
        return TimeBased.postprocess(log, accumulated_times, "accumulated_time")

    @classmethod
    def remaining_time(cls, log, **kwargs):
        group, ix_list, time_col, log = TimeBased.preprocess(log)
        remaining_times = group[time_col].apply(lambda x: x.max() - x).loc[ix_list].dt.total_seconds()
        return TimeBased.postprocess(log, remaining_times, "remaining_time")

    @classmethod
    def within_day(cls, log, tz=None, **kwargs):
        # pm4py (>=2.7.23.4) converts timestamps to UTC and drops their original offset,
        # so recovering local time-of-day requires the log's own IANA tz.
        # E.g. for Sepsis ("+02:00" in summer, "+01:00" in winter) pass tz="Europe/Amsterdam":
        # TimeBased(feature_names=['within_day'], tz="Europe/Amsterdam").extract(log), or
        # extract_features("test_data/Sepsis.xes", ['within_day'], tz="Europe/Amsterdam").
        _, _, time_col, log = TimeBased.preprocess(log)
        timestamps = log[time_col]
        if tz is not None:
            timestamps = timestamps.dt.tz_convert(tz)
        within_days = pd.to_timedelta(timestamps.dt.time.astype(str)).dt.total_seconds().values
        return TimeBased.postprocess(log, within_days, "within_day")

warnings.filterwarnings("ignore")

def meta(time):
    time_min = np.min(time)
    time_max = np.max(time)
    time_mean = np.mean(time)
    time_median = np.median(time)
    time_mode = stats.mode(time, keepdims=True)[0][0]
    time_std = np.std(time)
    time_variance = np.var(time)
    time_q1 = np.percentile(time, 25)
    time_q3 = np.percentile(time, 75)
    time_iqr = stats.iqr(time)
    time_geometric_mean = stats.gmean(time+1)
    time_geometric_std = stats.gstd(time+1)
    time_harmonic_mean = stats.hmean(time)
    time_skewness = stats.skew(time)
    time_kurtosis = stats.kurtosis(time)
    time_coefficient_variation = stats.variation(time)
    time_entropy = stats.entropy(time)
    time_hist, _ = np.histogram(time, density=True)
    time_skewness_hist = stats.skew(time_hist)
    time_kurtosis_hist = stats.kurtosis(time_hist)

    return {
        "min": time_min,
        "max": time_max,
        "mean": time_mean,
        "median": time_median,
        "mode": time_mode,
        "std": time_std,
        "variance": time_variance,
        "q1": time_q1,
        "q3": time_q3,
        "iqr": time_iqr,
        "geometric_mean": time_geometric_mean,
        "geometric_std": time_geometric_std,
        "harmonic_mean": time_harmonic_mean,
        "skewness": time_skewness,
        "kurtosis": time_kurtosis,
        "coefficient_variation": time_coefficient_variation,
        "entropy": time_entropy,
        # **{f"time_hist{i}": t for i, t in enumerate(time_hist)},
        "skewness_hist": time_skewness_hist,
        "kurtosis_hist": time_kurtosis_hist,
    }

