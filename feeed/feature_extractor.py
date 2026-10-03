import pandas as pd
import subprocess
from .feature import Feature
from .simple_stats import SimpleStats as simple_stats
from .trace_length import TraceLength as trace_length
from .trace_variant import TraceVariant as trace_variant
from .complexity.trace_diversity import TraceDiversity as trace_diversity
from .activities import Activities as activities
from .complexity.distinct_activities import DistinctActivities as distinct_activities
from .start_activities import StartActivities as start_activities
from .end_activities import EndActivities as end_activities
from .complexity.repetitions import Repetitions as repetitions
from .complexity.comparison_based import ComparisonBased as comparison_based
from .complexity.dfg_based import DFGBased as dfg_based
from .complexity.eventropies import Eventropies as eventropies
from .complexity.epa_based import Epa_based as epa_based
from .time import TimeBased as time_based

from datetime import datetime as dt
from pm4py.objects.log.importer.xes import importer as xes_importer

FEATURE_TYPES = [
    "simple_stats",
    "trace_length",
    "trace_variant",
    "trace_diversity",
    "activities",
    "distinct_activities",
    "start_activities",
    "end_activities",
    "repetitions",
    "comparison_based",
    "dfg_based",
    "eventropies",
    "epa_based",
    "time_based",
    ]


def feature_type(feature_name):
    available_features = []
    for feature_type in FEATURE_TYPES:
        available_features.extend([*eval(feature_type)().available_class_methods])
        available_features.append(str(feature_type))
        if feature_name in available_features:
            return feature_type
    raise ValueError(f"ERROR: Invalid value for feature_key argument: {feature_name}. See README.md for " +
                     f"supported feature_names or use a sublist of the following: {FEATURE_TYPES} or None")

def read_pm4py_log(filename=None, verbose=False):
    if filename == None:
        raise Exception("No file specified")

    if filename.split(".")[-1] == "xes":
        input_file = filename
        from pm4py.objects.log.importer.xes import importer as xes_importer

        pm4py_log = xes_importer.apply(input_file)

    elif filename.split(".")[-1] == "csv":
        subprocess.call(["head", filename])
        i_h = input("Does the file have a header? [y/N]:") or "n"
        h = 0 if i_h != "n" else None
        i_d = input("What is the delimiter? [,]:") or ","
        i_c = input("What is the column number of case ID? [0]:")
        i_c = 0 if i_c == "" else int(i_c)
        i_a = input("What is the column number of activity name? [1]:")
        i_a = 1 if i_a == "" else int(i_a)
        i_t = input("What is the column number of timestamp? [2]:")
        i_t = 2 if i_t == "" else int(i_t)

        from pm4py.objects.conversion.log import converter as log_converter
        from pm4py.objects.log.util import dataframe_utils

        log_csv = pd.read_csv(filename, sep=i_d, header=h)
        log_csv.rename(
            columns={
                log_csv.columns[i_c]: "case",
                log_csv.columns[i_a]: "concept:name",
                log_csv.columns[i_t]: "time:timestamp",
            },
            inplace=True,
        )
        for col in log_csv.columns:
            if isinstance(col, int):
                log_csv.rename(columns={col: "column" + str(col)}, inplace=True)
        log_csv = dataframe_utils.convert_timestamp_columns_in_df(log_csv)
        log_csv = log_csv.sort_values("time:timestamp")
        parameters = {
            log_converter.Variants.TO_EVENT_LOG.value.Parameters.CASE_ID_KEY: "case"
        }
        if verbose:
            print(log_csv)
        pm4py_log = log_converter.apply(
            log_csv, parameters=parameters, variant=log_converter.Variants.TO_EVENT_LOG
        )
    else:
        raise Exception("File type not recognized, should be xes or csv")

    return pm4py_log

def extract_features(event_logs_path, feature_types=None):
    log_name = event_logs_path.rsplit("/", 1)[-1]
    log = read_pm4py_log(event_logs_path)
    Feature.check_log(log, log_name)

    if feature_types is None:
        feature_types = FEATURE_TYPES

    features = {"log": log_name.split(".xes")[0]}
    start_log = dt.now()

    for i, ft_name in enumerate(feature_types):
        start_feat = dt.now()
        ft_type = feature_type(ft_name)

        feature_values = eval(f"{ft_type}(feature_names=['{ft_name}']).extract(log)")
        features = {**features, **feature_values}

        log_info =  f"     INFO: {log_name} starting at {len(features)}, {ft_name} from {ft_type} took {dt.now()-start_feat} sec, "
        if i == len(feature_types) - 1:
            print(log_info + "last feature.")
        else:
            print(log_info + f"next {feature_types[(i+1)%len(feature_types)]}...")
    print(
        f"SUCCESSFULLY: {len(features)-1} features for {log_name} took {dt.now() - start_log} sec."
    )
    return features
