import inspect
import numpy as np
import pm4py

from .feature import Feature
from pm4py import get_end_activities
from scipy import stats

class EndActivities(Feature):
    def __init__(self, feature_names='end_activities'):
        self.feature_type="end_activities"
        self.available_class_methods = dict(inspect.getmembers(EndActivities, predicate=inspect.ismethod))
        if self.feature_type in feature_names:
            self.feature_names = [*self.available_class_methods.keys()]
        else:
            self.feature_names = feature_names

    def log_end(log):
        log_end = get_end_activities(
            pm4py.filter_event_attribute_values(
                log, "concept:name", ["END"], level="event", retain=False
            )
        )
        # log_end = get_end_activities(log)
        return log_end

    def end_activities_occurrences(log):
        log_end = EndActivities.log_end(log)
        end_activities_occurrences = list(log_end.values())
        return end_activities_occurrences

    @classmethod
    def n_unique_end_activities(cls, log):
        log_end = EndActivities.log_end(log)
        return len(log_end)

    @classmethod
    def end_activities_min(cls, log):
        end_activities_occurrences = EndActivities.end_activities_occurrences(log)
        return np.min(end_activities_occurrences)

    @classmethod
    def end_activities_max(cls, log):
        end_activities_occurrences = EndActivities.end_activities_occurrences(log)
        return np.max(end_activities_occurrences)

    @classmethod
    def end_activities_mean(cls, log):
        end_activities_occurrences = EndActivities.end_activities_occurrences(log)
        return np.mean(end_activities_occurrences)

    @classmethod
    def end_activities_median(cls, log):
        end_activities_occurrences = EndActivities.end_activities_occurrences(log)
        return np.median(end_activities_occurrences)

    @classmethod
    def end_activities_std(cls, log):
        end_activities_occurrences = EndActivities.end_activities_occurrences(log)
        return np.std(end_activities_occurrences)

    @classmethod
    def end_activities_variance(cls, log):
        end_activities_occurrences = EndActivities.end_activities_occurrences(log)
        return np.var(end_activities_occurrences)

    @classmethod
    def end_activities_q1(cls, log):
        end_activities_occurrences = EndActivities.end_activities_occurrences(log)
        return np.percentile(end_activities_occurrences, 25)

    @classmethod
    def end_activities_q3(cls, log):
        end_activities_occurrences = EndActivities.end_activities_occurrences(log)
        return np.percentile(end_activities_occurrences, 75)

    @classmethod
    def end_activities_iqr(cls, log):
        end_activities_occurrences = EndActivities.end_activities_occurrences(log)
        return stats.iqr(end_activities_occurrences)

    @classmethod
    def end_activities_skewness(cls, log):
        end_activities_occurrences = EndActivities.end_activities_occurrences(log)
        if len(end_activities_occurrences) > 1:
            return stats.skew(end_activities_occurrences)
        else:
            return None

    @classmethod
    def end_activities_kurtosis(cls, log):
        end_activities_occurrences = EndActivities.end_activities_occurrences(log)
        if len(end_activities_occurrences) > 1:
            return stats.kurtosis(end_activities_occurrences)
        else:
            return None
