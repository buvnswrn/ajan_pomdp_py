import pomdp_py
from rdflib import Graph


class AjanOOPOMDP(pomdp_py.POMDP):
    def __init__(self, data, name, agent, env):
        self.graph = Graph()
        self.graph.parse(data=data)
        super().__init__(agent, env, name)
