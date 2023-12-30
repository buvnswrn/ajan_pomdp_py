import pomdp_py
from rdflib import Graph, RDF, Seq, Literal

import POMDPService.ajan_pomdp_planning.helpers.to_graph as graph_helper
from POMDPService.ajan_pomdp_planning.helpers.to_graph import parse_query
from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import _CurrentState, _NextState, createIRI, \
    _State, _CurrentAction, _Action, _CurrentReward, _RewardModel


class AjanRewardModel(pomdp_py.RewardModel):
    def __init__(self, data, attributes, probability_query, sample_query, argmax_query):
        self.graph = Graph()
        self.graph.parse(data=data)
        if attributes is not None:
            self.attributes = attributes
            self.attribute_node = graph_helper.add_attributes_to_graph(self.graph, attributes, _RewardModel)
        self.probability_query = probability_query
        self.argmax_query = argmax_query
        self.sample_query = sample_query

    def probability(self, reward, state, action, next_state):
        # Add the variables to the current graph
        self.graph.add((_CurrentReward, RDF.value, Literal(reward)))
        out = parse_query(self.graph, self.probability_query, state, action, next_state)

        # Remove the variables from the current graph
        self.graph.remove((_CurrentReward, RDF.value, Literal(reward)))
        # Update the observation, next_state, action to the local graph
        return float(out.bindings[0]['probability'])

    def sample(self, state, action, next_state):
        out = parse_query(self.graph, self.sample_query, state, action, next_state)
        return float(out.bindings[0]['sample'])

    def argmax(self, state, action, next_state):
        out = parse_query(self.graph, self.argmax_query, state, action, next_state)
        return float(out.bindings[0]['argmax'])


    # endregion
