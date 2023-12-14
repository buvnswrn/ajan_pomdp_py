import pomdp_py
from rdflib import Graph
import POMDPService.ajan_pomdp_planning.helpers.to_graph as graph_helper

from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import _Observation


class AjanObservation(pomdp_py.Observation):
    def __init__(self, attributes: dict, for_hash: list):
        self.attributes = attributes
        self.for_hash = for_hash
        self.graph = Graph()
        self.observation_subject = _Observation
        if attributes is not None:
            graph_helper.add_attributes_to_graph(self.graph, attributes, self.observation_subject)

    def __hash__(self):
        hash_list = list()
        for element in self.for_hash:
            value = self.attributes[element]
            if type(value) not in [str, int, float]:
                value = str(value)
            hash_list.append(value)
        return hash(tuple(hash_list))

    def __eq__(self, other):
        equal = False
        if self.attributes is not None:
            for key in self.attributes:
                equal = self.attributes[key] == other.attributes[key]
                if not equal:
                    return False
            return equal
        return True


class AjanOOObservation(pomdp_py.OOObservation):
    def __init__(self, observations: dict):
        self._hashcode = hash(frozenset(observations.items()))
        self.observations = observations

    def __hash__(self):
        return self._hashcode

    def __eq__(self, other):
        if not isinstance(other, AjanOOObservation):
            return False
        else:
            return self.observations == other.observations

    def __str__(self):
        return "AjanOOObservation(%s)" % str(self.observations)

    def __repr__(self):
        return str(self)
