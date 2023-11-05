import pomdp_py
from rdflib import Graph

from POMDPService.ajan_pomdp_planning.oopomdp.env.env import AjanEnvironment


class AjanOOPOMDP(pomdp_py.POMDP):
    def __init__(self, data, name, init_state, agent, env, transition_model, reward_model):
        self.graph = Graph()
        self.graph.parse(data)
        super.__init__(agent, env, name)
