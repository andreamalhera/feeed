import pandas as pd

class EmptyLogError(ValueError):
    """Raised for event logs without traces or events, so batch runs can skip them."""

class Feature:
    def __init__(self, feature_names=None):
        self.feature_names = feature_names

    def check_log(log, log_name=None):
        log_name = f" {log_name}" if log_name else ""
        if len(log) == 0:
            raise EmptyLogError(f"ERROR: Event log{log_name} contains no traces.")
        if not isinstance(log, pd.DataFrame) and all(len(trace) == 0 for trace in log):
            raise EmptyLogError(f"ERROR: Event log{log_name} contains no events.")

    def extract(self, log):
        Feature.check_log(log)
        feature_names=self.feature_names

        output = {}
        for feature_name in feature_names:
            feature_fn = self.available_class_methods[feature_name]
            feature_value = feature_fn(log)
            output[f"{feature_name}"] = feature_value

        return output
