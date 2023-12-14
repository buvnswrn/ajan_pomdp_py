import pomdp_py
import rdflib.term
from rdflib import Graph, RDF, Seq

import POMDPService.ajan_pomdp_planning.helpers.to_graph as graph_helper
from POMDPService.ajan_pomdp_planning.oopomdp.domain.observation import AjanObservation, AjanOOObservation
from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import pomdp_ns, _CurrentAction, createIRI, _Action, \
    _NextState, _State, _ObservationModel


class AjanObservationModel(pomdp_py.ObservationModel):
    def __init__(self, data, attributes, probability_query, sample_query, argmax_query):
        self.graph = Graph()
        self.graph.parse(data=data)
        self.attributes = attributes
        self.attribute_node = graph_helper.add_attributes_to_graph(self.graph, attributes, _ObservationModel) \
            if attributes is not None else None
        self.probability_query = probability_query
        self.argmax_query = argmax_query
        self.sample_query = sample_query

    def probability(self, observation, next_state, action) -> float:
        # self.graph.add((pomdp_ns['observation'], RDF.value,
        #                 pomdp_ns[observation]))
        out = graph_helper.parse_query(self.graph, self.probability_query, next_state=next_state, action=action,
                                       observation=observation)
        # Update the observation, next_state, action to the local graph
        # Assign some random probability
        probability = [a.probability for a in out][0]
        return float(probability)

    def sample(self, next_state, action):
        out = graph_helper.parse_query(self.graph, self.sample_query, next_state=next_state, action=action)
        sample_graph = out.graph
        result_observation = graph_helper.convert_to_observation(sample_graph)
        return result_observation

    def argmax(self, next_state, action):
        """
        if not isinstance(action, PerceiveAction):
            return PersonObservation([self._person_id, PersonObservation.NULL])
        else send the observation with some sampled values.
        """
        out = graph_helper.parse_query(self.graph, self.argmax_query, next_state=next_state, action=action)
        argmax_graph = out.graph
        result_observation = graph_helper.convert_to_observation(argmax_graph)
        return result_observation


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
