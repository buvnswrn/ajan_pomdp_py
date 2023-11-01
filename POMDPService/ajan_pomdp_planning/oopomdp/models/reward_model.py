import pomdp_py
from rdflib import Graph, RDF
from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import pomdp_ns


class AjanRewardModel(pomdp_py.RewardModel):
    def __init__(self, data, attributes, probability_query, sample_query, argmax_query):
        self.graph = Graph()
        self.graph.parse(data=data)
        self.attributes = attributes
        self.probability_query = probability_query
        self.argmax_query = argmax_query
        self.sample_query = sample_query

    def probability(self, reward, state, action, next_state):
        self.graph.add((pomdp_ns['reward'], RDF.value,
                        pomdp_ns[reward]))
        out = self.parse_query(self.probability_query, next_state, action)
        # Update the observation, next_state, action to the local graph
        return out.probability

    def sample(self, state, action, next_state):
        if self.sample_query == "argmax":
            return self.argmax(state, action, next_state)
        out = self.parse_query(self.sample_query, state, action, next_state)
        return out.sample

    def argmax(self, state, action, next_state):
        if self.argmax_query == "sample":
            return self.sample(state, action, next_state)
        out = self.parse_query(self.argmax_query, state, action, next_state)
        return out.argmax

    def parse_query(self, query, state, action, next_state):
        self.graph.add((pomdp_ns['state'], RDF.value,
                        pomdp_ns[state]))
        self.graph.add((pomdp_ns['next_state'], RDF.value,
                        pomdp_ns[next_state]))
        self.graph.add((pomdp_ns['action'], RDF.value,
                        pomdp_ns[action]))
        out = self.graph.query(query)
        return out
