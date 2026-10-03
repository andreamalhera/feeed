import pandas as pd

class Feature:
    def __init__(self, feature_names=None):
        self.feature_names = feature_names

    def check_log(log, log_name=None):
        log_name = f" {log_name}" if log_name else ""
        if len(log) == 0:
            raise ValueError(f"ERROR: Event log{log_name} contains no traces.")
        # DataFrame logs have one row per event, so len(log) == 0 already covers them
        if not isinstance(log, pd.DataFrame) and all(len(trace) == 0 for trace in log):
            raise ValueError(f"ERROR: Event log{log_name} contains no events.")

    def extract(self, log):
        Feature.check_log(log)
        feature_names=self.feature_names

        output = {}
        for feature_name in feature_names:
            feature_fn = self.available_class_methods[feature_name]
            feature_value = feature_fn(log)
            output[f"{feature_name}"] = feature_value

        return output
