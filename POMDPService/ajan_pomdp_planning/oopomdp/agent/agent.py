import pomdp_py
from rdflib import Graph


class AjanAgent(pomdp_py.Agent):
    def __init__(self, data, init_belief, policy_model, transition_model, observation_model, reward_model):
        self.graph = Graph()
        self.graph.parse(data=data)
        super().__init__(init_belief, policy_model=policy_model,
                         transition_model=transition_model,
                         observation_model=observation_model,
                         reward_model=reward_model)
