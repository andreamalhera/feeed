import inspect
import numpy as np
import pm4py

from .feature import Feature
from pm4py import get_start_activities
from scipy import stats

class StartActivities(Feature):
    def __init__(self, feature_names='start_activities'):
        self.feature_type="start_activities"
        self.available_class_methods = dict(inspect.getmembers(StartActivities, predicate=inspect.ismethod))
        if self.feature_type in feature_names:
            self.feature_names = [*self.available_class_methods.keys()]
        else:
            self.feature_names = feature_names

    def log_start(log):
        log_start = get_start_activities(
            pm4py.filter_event_attribute_values(
                log, "concept:name", ["START"], level="event", retain=False
            )
        )
        # log_start = get_start_activities(log)
        return log_start

    def start_activities_occurrences(log):
        log_start = StartActivities.log_start(log)
        start_activities_occurrences = list(log_start.values())
        return start_activities_occurrences

    @classmethod
    def n_unique_start_activities(cls, log):
        log_start = StartActivities.log_start(log)
        return len(log_start)

    @classmethod
    def start_activities_min(cls, log):
        start_activities_occurrences = StartActivities.start_activities_occurrences(log)
        return np.min(start_activities_occurrences)

    @classmethod
    def start_activities_max(cls, log):
        start_activities_occurrences = StartActivities.start_activities_occurrences(log)
        return np.max(start_activities_occurrences)

    @classmethod
    def start_activities_mean(cls, log):
        start_activities_occurrences = StartActivities.start_activities_occurrences(log)
        return np.mean(start_activities_occurrences)

    @classmethod
    def start_activities_median(cls, log):
        start_activities_occurrences = StartActivities.start_activities_occurrences(log)
        return np.median(start_activities_occurrences)

    @classmethod
    def start_activities_std(cls, log):
        start_activities_occurrences = StartActivities.start_activities_occurrences(log)
        return np.std(start_activities_occurrences)

    @classmethod
    def start_activities_variance(cls, log):
        start_activities_occurrences = StartActivities.start_activities_occurrences(log)
        return np.var(start_activities_occurrences)

    @classmethod
    def start_activities_q1(cls, log):
        start_activities_occurrences = StartActivities.start_activities_occurrences(log)
        return np.percentile(start_activities_occurrences, 25)

    @classmethod
    def start_activities_q3(cls, log):
        start_activities_occurrences = StartActivities.start_activities_occurrences(log)
        return np.percentile(start_activities_occurrences, 75)

    @classmethod
    def start_activities_iqr(cls, log):
        start_activities_occurrences = StartActivities.start_activities_occurrences(log)
        return stats.iqr(start_activities_occurrences)

    @classmethod
    def start_activities_skewness(cls, log):
        start_activities_occurrences = StartActivities.start_activities_occurrences(log)
        return stats.skew(start_activities_occurrences)

    @classmethod
    def start_activities_kurtosis(cls, log):
        start_activities_occurrences = StartActivities.start_activities_occurrences(log)
        return stats.kurtosis(start_activities_occurrences)
