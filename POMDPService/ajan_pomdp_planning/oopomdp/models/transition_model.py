import pomdp_py
from rdflib import Graph, RDF

from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanOOState
from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import pomdp_ns


class AjanTransitionModel(pomdp_py.TransitionModel):
    def __init__(self, data, attributes, probability_query, sample_query, argmax_query):
        self.graph = Graph()
        self.graph.parse(data=data)
        self.attributes = attributes
        self.probability_query = probability_query
        self.argmax_query = argmax_query
        self.sample_query = sample_query

    def probability(self, next_state, state, action):
        self.graph.add((pomdp_ns['state'], RDF.value,
                        pomdp_ns[state]))
        out = self.parse_query(self.probability_query, next_state, action)
        # Update the observation, next_state, action to the local graph
        return out.probability

    def sample(self, state, action):
        if self.sample_query == "argmax":
            return self.argmax(state, action)
        out = self.parse_query(self.sample_query, state, action)
        return self.convert_to_observation(out.sample)

    def argmax(self, state, action):
        if self.argmax_query == "sample":
            return self.sample(state, action)
        out = self.parse_query(self.argmax_query, state, action)
        return self.convert_to_observation(out.argmax)

    def convert_to_observation(self, sample):
        pass  # parse the node and convert it to AjanObservation

    def parse_query(self, query, next_state, action):
        self.graph.add((pomdp_ns['next_state'], RDF.value,
                        pomdp_ns[next_state]))
        self.graph.add((pomdp_ns['action'], RDF.value,
                        pomdp_ns[action]))
        out = self.graph.query(query)
        return out


class AjanOOTransitionModel(pomdp_py.OOTransitionModel):
    def __init__(self, ids, graph_datas, attributes, probability_queries, sample_queries, argmax_queries):
        transition_models = {ids[i]: AjanTransitionModel(graph_datas[i],
                                                         attributes[i],
                                                         probability_queries[i],
                                                         sample_queries[i],
                                                         argmax_queries[i]) for i in range(0, len(ids))}
        super().__init__(transition_models)

    def sample(self, state, action, argmax=False, **kwargs):
        oostate = pomdp_py.OOTransitionModel.sample(self, state, action, **kwargs)
        return AjanOOState(oostate.object_states)

    def argmax(self, state, action, **kwargs):
        oostate = pomdp_py.OOTransitionModel.argmax(self, state, action, **kwargs)
        return AjanOOState(oostate.object_states)
