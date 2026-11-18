import inspect
import math
import os
import subprocess

from collections import Counter
from Levenshtein import distance
from pm4py.algo.filtering.log.variants import variants_filter

from ..feature import Feature

class Eventropies(Feature):
    def __init__(self, feature_names='eventropies'):
        self.feature_type="eventropies"
        self.available_class_methods = dict(inspect.getmembers(Eventropies, predicate=inspect.ismethod))
        if self.feature_type in feature_names:
            self.feature_names = [*self.available_class_methods.keys()]
        else:
            self.feature_names = feature_names

    # Helper function to calculate eventropy of k_block_ratio and k_block_diff
    def eventropy_k_block(log, k=1):
        # k represents the block size
        all_k_object_substrings = [trace[i:i + k] for trace in (tuple(event["concept:name"] for event in trace) for trace in log) for i in range(len(trace) - k + 1)]

        k_sub_counts = Counter(all_k_object_substrings)
        total_k_substrings = len(all_k_object_substrings)

        k_substring_entropy = sum((count / total_k_substrings) * math.log2(count / total_k_substrings) for count in k_sub_counts.values())
        return round(-k_substring_entropy,3)

    # Helper functions for kNN eventropy
    def harmonic_sum(j):
        if j < 0:
            return None
        elif j == 0:
            return 0.0
        else:
            L_j = 0.0
            for i in range(1, j + 1):
                L_j += 1.0 / float(i)
            return L_j

    def calculate_distance_matrix(trace_list):
        n = len(trace_list)
        distance_matrix = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                dist = distance(trace_list[i], trace_list[j])
                distance_matrix[i][j] = dist
                distance_matrix[j][i] = dist

        return distance_matrix

    def find_nearest_neighbors(trace_list, k=1):
        n = len(trace_list)
        distance_matrix = Eventropies.calculate_distance_matrix(trace_list)

        def calculate_normalized_distance(i, j):
            return distance_matrix[i][j] / max(len(trace_list[i]), len(trace_list[j]))

        neighbour_list = []

        for i in range(n):
            distances = [(calculate_normalized_distance(i, j))
                        for j in range(n) if i != j]
            distances.sort(key=lambda x: x)

            filtered_distances = [d for d in distances if d != 0]
            if len(neighbour_list) >= k:
                neighbour_list.append(filtered_distances[k-1])

        return neighbour_list

    # Calculating knn eventropies
    def eventropy_flattened_knn(log, k=1,d=1):
        unique_traces = variants_filter.get_variants(log)
        unique_traces = list(unique_traces)
        local_neighbour_list = Eventropies.find_nearest_neighbors(unique_traces, k)
        n= len(unique_traces)

        knn_entropy = 0
        for neighbour in local_neighbour_list:
            normalized_lev = neighbour
            part_2 = math.log(normalized_lev)
            part_3 = math.log(math.pow(math.pi, d/ 2.0) / math.gamma(d / 2.0 + 1.0))
            part_4 = 0.5772
            part_5 = Eventropies.harmonic_sum(k-1)
            part_6 = math.log(n)
            local_sum = d/n * (part_2 + part_3 + part_4 - part_5 + part_6)
            knn_entropy += local_sum
        return round(knn_entropy,3)

    # Extractable Features
    @classmethod
    def eventropy_trace(cls, log):
        # Get unique traces and their counts
        trace_counts = Counter(tuple(event["concept:name"] for event in trace) for trace in log)

        # Calculate trace entropy
        trace_entropy = sum((count / len(log)) * math.log2(count / len(log)) for count in trace_counts.values())

        return round(-trace_entropy,3)  # Use negative sign to follow the convention of minimizing entropy

    @classmethod
    def eventropy_prefix(cls, log): # Considers prefixes amongst traces
        # Get unique traces
        unique_traces = [tuple(event["concept:name"] for event in trace) for trace in log]

        # Generate all possible prefixes
        all_possible_prefixes = [tuple(trace[:i+1]) for trace in unique_traces for i in range(len(trace))]

        # Use Counter to count occurrences of each unique prefix
        prefix_counts = Counter(all_possible_prefixes)

        # Calculate prefix entropy
        total_prefixes = len(all_possible_prefixes)
        prefix_entropy = sum((count / total_prefixes) * math.log2(count / total_prefixes) for count in prefix_counts.values())

        return round(-prefix_entropy,3)

    @classmethod
    def eventropy_prefix_flattened(cls,log): # Considers prefixes amongst variants
        unique_traces = variants_filter.get_variants(log)

        # Generate all possible prefixes
        all_possible_prefixes = [tuple(trace[:i+1]) for trace in unique_traces for i in range(len(trace))]

        # Use Counter to count occurrences of each unique prefix
        prefix_counts = Counter(all_possible_prefixes)

        # Calculate prefix entropy
        total_prefixes = len(all_possible_prefixes)
        prefix_entropy = sum((count / total_prefixes) * math.log2(count / total_prefixes) for count in prefix_counts.values())

        return round(-prefix_entropy,3)

    @classmethod
    def eventropy_global_block(cls, log):
        all_traces = [tuple(event["concept:name"] for event in trace) for trace in log]

        # Generate all possible substrings for all traces
        all_substrings = [sub for trace in all_traces for sub in (tuple(trace[i:j]) for i in range(len(trace)) for j in range(i + 1, len(trace) + 1))]

        substring_counts = Counter(all_substrings)
        total_substrings = len(all_substrings)

        # Calculate entropy
        substring_entropy = sum((count / total_substrings) * math.log2(count / total_substrings) for count in substring_counts.values())

        return round(-substring_entropy,3)

    @classmethod
    def eventropy_global_block_flattened(cls,log):
        all_traces = variants_filter.get_variants(log)

        # Generate all possible substrings for all traces
        all_substrings = [sub for trace in all_traces for sub in (tuple(trace[i:j]) for i in range(len(trace)) for j in range(i + 1, len(trace) + 1))]

        substring_counts = Counter(all_substrings)
        total_substrings = len(all_substrings)

        # Calculate entropy
        substring_entropy = sum((count / total_substrings) * math.log2(count / total_substrings) for count in substring_counts.values())

        return round(-substring_entropy,3)

    @classmethod
    def eventropy_lempel_ziv(cls,log):
        all_traces = [tuple(event["concept:name"] for event in trace) for trace in log] # List of tuples
        N, N_w, words,previous_encountered = 0, 0, set(),[]
        for trace in all_traces:
            if trace not in previous_encountered:
                previous_encountered.append(trace)
                word = ""
                for activity in trace:
                    word += activity
                    if word not in words:
                        words.add(word)
                        word = ""

            N += len(trace)

        N_w = len(words)
        return round((N_w * math.log2(N)) / N,3)

    @classmethod
    def eventropy_lempel_ziv_flattened(cls,log):
        unique_traces = list(variants_filter.get_variants(log))
        N, N_w, words,previous_encountered = 0, 0, set(),[]
        for trace in unique_traces:
            if trace not in previous_encountered:
                previous_encountered.append(trace)
                word = ""
                for activity in trace:
                    word += activity
                    if word not in words:
                        words.add(word)
                        word = ""

            N += len(trace)

        N_w = len(words)
        return round((N_w * math.log2(N)) / N,3)

    @classmethod
    def eventropy_k_block_diff_1(cls, log,k=1):
        return round(Eventropies.eventropy_k_block(log, k) - Eventropies.eventropy_k_block(log, k-1),3)

    @classmethod
    def eventropy_k_block_diff_3(cls, log,k=3):
        return round(Eventropies.eventropy_k_block(log, k) - Eventropies.eventropy_k_block(log, k-1),3)

    @classmethod
    def eventropy_k_block_diff_5(cls, log,k=5):
        return round(Eventropies.eventropy_k_block(log, k) - Eventropies.eventropy_k_block(log, k-1),3)

    @classmethod
    def eventropy_k_block_ratio_1(cls, log,k=1):
        return round(Eventropies.eventropy_k_block(log, k)/k,3)

    @classmethod
    def eventropy_k_block_ratio_3(cls, log,k=3):
        return round(Eventropies.eventropy_k_block(log, k)/k,3)

    @classmethod
    def eventropy_k_block_ratio_5(cls, log,k=5):
        return round(Eventropies.eventropy_k_block(log, k)/k,3)

    @classmethod
    def eventropy_knn_3(cls, log): # Flattened knn eventropy
        return Eventropies.eventropy_flattened_knn(log,k=3)

    @classmethod
    def eventropy_knn_5(cls, log): # Flattened knn eventropy
        return Eventropies.eventropy_flattened_knn(log,k=5)

    @classmethod
    def eventropy_knn_7(cls, log): # Flattened knn eventropy
        return Eventropies.eventropy_flattened_knn(log,k=7)
