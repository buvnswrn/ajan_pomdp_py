import pomdp_py
from rdflib import Graph, RDF
from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import pomdp_ns


class AjanPolicyModel(pomdp_py.RolloutPolicy):
    def __init__(self, data, attributes, sample_query, rollout_query, get_all_action_query):
        self.graph = Graph()
        self.graph.parse(data=data)
        self.attributes = attributes
        self.get_all_action_query = get_all_action_query
        self.sample_query = sample_query
        self.rollout_query = rollout_query

    def sample(self, state):
        out = self.parse_query(self.sample_query, state)
        return self.convert_to_action(out.sample)

    def rollout(self, state, tuple_history=None):
        if self.rollout_query == 'sample':
            return self.sample(state)
        out = self.parse_query(self.rollout_query, state)
        return self.convert_to_action(out.rollout)

    def get_all_actions(self, state=None, tuple_history=None):
        return self.convert_to_action(self.parse_query(self.get_all_action_query, state))

    def convert_to_action(self, sample):
        pass  # parse the node and convert it to AjanObservation

    def parse_query(self, query, next_state):
        self.graph.add((pomdp_ns['next_state'], RDF.value,
                        pomdp_ns[next_state]))
        out = self.graph.query(query)
        return out
