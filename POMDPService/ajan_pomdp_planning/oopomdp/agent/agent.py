import pomdp_py
from rdflib import Graph


class AjanAgent(pomdp_py.Agent):
    def __init__(self, agent_id, data, init_belief, policy_model, transition_model, observation_model, reward_model):
        self.graph = Graph()
        self.graph.parse(data=data)
        self.agent_id = agent_id
        super().__init__(init_belief, policy_model=policy_model,
                         transition_model=transition_model,
                         observation_model=observation_model,
                         reward_model=reward_model)

    def clear_history(self):
        """Custom function; clear history"""
        self._history = None