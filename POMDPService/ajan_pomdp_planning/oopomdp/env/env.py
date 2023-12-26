import pomdp_py
from rdflib import Graph


class AjanEnvironment(pomdp_py.Environment):
    def __init__(self, data, init_state, transition_model, reward_model):
        """
        Initialize the environment with the data and the models.
        :param data: turtle string representing the graph data.
        :param init_state: initial state of the environment.
        :param transition_model: transition model of the environment.
        :param reward_model: reward model of the environment.
        """
        self.graph = Graph()
        self.graph.parse(data=data)
        super().__init__(init_state, transition_model, reward_model)

    def get_next_state(self, action):
        """
        Returns the next state sampled from the transition model.
        Is can then be used by AJAN to be modified and sent back for state_transition.
        :param action: the action computed by the planner.
        :return: the state sampled from the transition model.
        """
        return self.transition_model.sample(self.state, action)  # need to be converted to a ttl string

