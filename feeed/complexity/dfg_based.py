import inspect
import numpy as np
import networkx

from ..feature import Feature
from ..activities import Activities

class DFGBased(Feature):
    def __init__(self, feature_names='dfg_based'):
        self.feature_type = "dfg_based"
        self.available_class_methods = dict(inspect.getmembers(DFGBased, predicate=inspect.ismethod))
        if self.feature_type in feature_names:
            self.feature_names = [*self.available_class_methods.keys()]
        else:
            self.feature_names = feature_names

    def extract(self, log):
        Feature.check_log(log)
        dfg = DFGBased.directly_follows_graph(log)
        output = {}
        for feature_name in self.feature_names:
            feature_fn = self.available_class_methods[feature_name]
            output[feature_name] = feature_fn(log, dfg=dfg)
        return output

    def directly_follows_graph(log):
        Feature.check_log(log)
        # calculate the event log's level of detail
        directly_follows_graph = networkx.DiGraph()
        # create two special nodes marking the start and the end of the traces
        start = "START"
        end = "END"
        directly_follows_graph.add_node(start)
        directly_follows_graph.add_node(end)
        # get the set of activity names
        events = set(Activities.activities(log).keys())
        # create a node for each distinct event
        for event in events:
            directly_follows_graph.add_node(event)
        # add edges between nodes if the respective events are direct neighbors in some trace
        for trace in log:
            # add an edge from the start node to the start event of this trace
            directly_follows_graph.add_edge(start, trace[0]["concept:name"])
            for i in range(len(trace)-1):
                directly_follows_graph.add_edge(trace[i]["concept:name"], trace[i+1]["concept:name"])
            # add an edge from the end event of this trace to the end node
            directly_follows_graph.add_edge(trace[-1]["concept:name"], end)
        return directly_follows_graph

    @classmethod
    def n_nodes_dfg(cls, log, dfg=None):
        if dfg is None:
            dfg = DFGBased.directly_follows_graph(log)
        return dfg.number_of_nodes()

    @classmethod
    def n_edges_dfg(cls, log, dfg=None):
        if dfg is None:
            dfg = DFGBased.directly_follows_graph(log)
        return dfg.number_of_edges()

    @classmethod
    def coeff_of_connectivity_dfg(cls, log, dfg=None):
        if dfg is None:
            dfg = DFGBased.directly_follows_graph(log)
        return DFGBased.n_edges_dfg(log, dfg=dfg) / DFGBased.n_nodes_dfg(log, dfg=dfg)

    @classmethod
    def avg_node_degree_dfg(cls, log, dfg=None):
        if dfg is None:
            dfg = DFGBased.directly_follows_graph(log)
        return sum([dfg.degree(node) for node in dfg.nodes]) / DFGBased.n_nodes_dfg(log, dfg=dfg)

    @classmethod
    def max_node_degree_dfg(cls, log, dfg=None):
        if dfg is None:
            dfg = DFGBased.directly_follows_graph(log)
        return max([dfg.degree(node) for node in dfg.nodes])

    @classmethod
    def density_dfg(cls, log, dfg=None):
        if dfg is None:
            dfg = DFGBased.directly_follows_graph(log)
        number_of_nodes = DFGBased.n_nodes_dfg(log, dfg=dfg)
        number_of_edges = DFGBased.n_edges_dfg(log, dfg=dfg)
        max_number_of_edges = number_of_nodes * (number_of_nodes - 1)
        return number_of_edges / max_number_of_edges

    @classmethod
    def structure_dfg(cls, log, dfg=None):
        if dfg is None:
            dfg = DFGBased.directly_follows_graph(log)
        return 1 - (DFGBased.n_edges_dfg(log, dfg=dfg) / (DFGBased.n_nodes_dfg(log, dfg=dfg) ** 2))

    @classmethod
    def cyclomatic_number_dfg(cls, log, dfg=None):
        if dfg is None:
            dfg = DFGBased.directly_follows_graph(log)
        return DFGBased.n_edges_dfg(log, dfg=dfg) - DFGBased.n_nodes_dfg(log, dfg=dfg) + 1

    @classmethod
    def n_cut_vertices_dfg(cls, log, dfg=None):
        if dfg is None:
            dfg = DFGBased.directly_follows_graph(log)
        undirected_dfg = dfg.to_undirected()
        return len(list(networkx.articulation_points(undirected_dfg)))

    @classmethod
    def separability_ratio_dfg(cls, log, dfg=None):
        if dfg is None:
            dfg = DFGBased.directly_follows_graph(log)
        return DFGBased.n_cut_vertices_dfg(log, dfg=dfg) / DFGBased.n_nodes_dfg(log, dfg=dfg)

    @classmethod
    def sequentiality_ratio_dfg(cls, log, dfg=None):
        if dfg is None:
            dfg = DFGBased.directly_follows_graph(log)
        sequential_nodes = [node for node in dfg.nodes if dfg.in_degree(node) < 2 and dfg.out_degree(node) < 2]
        num_sequential_arcs = 0
        for (u, v) in dfg.edges:
            if u in sequential_nodes and v in sequential_nodes:
                num_sequential_arcs += 1
        return num_sequential_arcs / DFGBased.n_nodes_dfg(log, dfg=dfg)

    @classmethod
    def cyclicity_dfg(cls, log, dfg=None):
        if dfg is None:
            dfg = DFGBased.directly_follows_graph(log)
        nodes_on_cycles = set()
        for component in networkx.strongly_connected_components(dfg):
            if len(component) > 1:
                nodes_on_cycles.update(component)
        return len(nodes_on_cycles) / DFGBased.n_nodes_dfg(log, dfg=dfg)
