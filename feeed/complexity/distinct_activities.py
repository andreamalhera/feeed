import inspect
import numpy as np

from ..feature import Feature
from ..trace_variant import TraceVariant
from ..simple_stats import SimpleStats
from ..trace_length import TraceLength

class DistinctActivities(Feature):
    def __init__(self, feature_names='distinct_activities'):
        self.feature_type = "distinct_activities"
        self.available_class_methods = dict(inspect.getmembers(DistinctActivities, predicate=inspect.ismethod))
        if self.feature_type in feature_names:
            self.feature_names = [*self.available_class_methods.keys()]
        else:
            self.feature_names = feature_names

    def distinct_activities_in_trace(trace):
        distinct_activities_in_trace = set()
        for event in trace:
            distinct_activities_in_trace.add(event["concept:name"])
        return distinct_activities_in_trace

    @classmethod
    def distinct_activities_min(cls, log):
        return np.min([len(DistinctActivities.distinct_activities_in_trace(trace)) for trace in log])

    @classmethod
    def distinct_activities_max(cls, log):
        return np.max([len(DistinctActivities.distinct_activities_in_trace(trace)) for trace in log])

    @classmethod
    def distinct_activities_mean(cls, log):
        return np.mean([len(DistinctActivities.distinct_activities_in_trace(trace)) for trace in log])

    @classmethod
    def distinct_activities_std(cls, log):
        return np.std([len(DistinctActivities.distinct_activities_in_trace(trace)) for trace in log])

    @classmethod
    def event_density(cls, log):
        avg_distinct_activities_per_trace = DistinctActivities.distinct_activities_mean(log)
        avg_trace_length = TraceLength.trace_len_mean(log)
        return avg_distinct_activities_per_trace / avg_trace_length

    @classmethod
    def distinct_activities_non_overlap(cls, log):
        overlap = 0
        for trace1 in log:
            events_in_trace_1 = DistinctActivities.distinct_activities_in_trace(trace1)
            for trace2 in log:
                events_in_trace_2 = DistinctActivities.distinct_activities_in_trace(trace2)
                # calculate the overlap between both sets
                intersection = events_in_trace_1.intersection(events_in_trace_2)
                union = events_in_trace_1.union(events_in_trace_2)
                overlap += len(intersection) / len(union)
        return 1 - (overlap / (len(log) ** 2))

    @classmethod
    def complexity_factor(cls, log):
        base = np.log(SimpleStats.n_variants(log))
        exponent = ((1 - TraceVariant.similarity_rate_variants(log)) + DistinctActivities.event_density(log))
        factor = DistinctActivities.distinct_activities_mean(log)
        return (base ** exponent) * factor
