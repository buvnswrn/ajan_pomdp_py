import pomdp_py
from rdflib import Graph, RDF

from POMDPService.ajan_pomdp_planning.oopomdp.domain.observation import AjanObservation, AjanOOObservation
from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import pomdp_ns


class AjanObservationModel(pomdp_py.ObservationModel):
    def __init__(self, data, attributes, probability_query, sample_query, argmax_query):
        self.graph = Graph()
        self.graph.parse(data=data)
        self.attributes = attributes
        self.probability_query = probability_query
        self.argmax_query = argmax_query
        self.sample_query = sample_query

    def probability(self, observation, next_state, action):
        self.graph.add((pomdp_ns['observation'], RDF.value,
                        pomdp_ns[observation]))
        out = self.parse_query(self.probability_query, next_state, action)
        # Update the observation, next_state, action to the local graph
        return out.probability

    def sample(self, next_state, action):
        if self.sample_query == "argmax":
            return self.argmax(next_state, action)
        out = self.parse_query(self.sample_query, next_state, action)
        return self.convert_to_observation(out.sample)

    def argmax(self, next_state, action):
        if self.argmax_query == "sample":
            return self.sample(next_state, action)
        out = self.parse_query(self.argmax_query, next_state, action)
        return self.convert_to_observation(out.argmax)

    def convert_to_observation(self, sample) -> AjanObservation:
        pass  # parse the node and convert it to AjanObservation

    def parse_query(self, query, next_state, action):
        self.graph.add((pomdp_ns['next_state'], RDF.value,
                        pomdp_ns[next_state]))
        self.graph.add((pomdp_ns['action'], RDF.value,
                        pomdp_ns[action]))
        out = self.graph.query(query)
        return out


class AjanOOObservationModel(pomdp_py.OOObservationModel):
    def __init__(self, ids, graph_datas, attributes, probability_queries, sample_queries, argmax_queries):
        observation_models = {ids[i]: AjanObservationModel(graph_datas[i],
                                                           attributes[i],
                                                           probability_queries[i],
                                                           sample_queries[i],
                                                           argmax_queries[i]) for i in range(0, len(ids))}
        pomdp_py.OOObservationModel.__init__(self, observation_models)

    def __init__(self, observation_models):
        pomdp_py.OOObservationModel.__init__(self, observation_models)

    def sample(self, next_state, action, argmax=False, **kwargs):
        obs = super().sample(next_state, action, argmax, **kwargs)
        return AjanOOObservation(obs)
    