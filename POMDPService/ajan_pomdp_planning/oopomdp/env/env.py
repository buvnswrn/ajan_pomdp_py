import pomdp_py
from rdflib import Graph


class AjanEnvironment(pomdp_py.Environment):
    def __init__(self, data, init_state, transition_model, reward_model):
        self.graph = Graph()
        self.graph.parse(data)
        super().__init__(init_state, transition_model, reward_model)