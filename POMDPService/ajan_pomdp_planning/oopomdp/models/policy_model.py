import pomdp_py
import rdflib
from pomdp_py import OOState
from rdflib import Graph, RDF, BNode

from POMDPService.ajan_pomdp_planning.helpers.to_graph import convert_to_action, convert_to_actions, parse_query
from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import pomdp_ns, _OOState, _NextState


def convert_state_to_rdf(graph, state: pomdp_py.State):
    pass


class AjanPolicyModel(pomdp_py.RolloutPolicy):
    def __init__(self, data, attributes, sample_query, rollout_query, get_all_action_query):
        self.graph = Graph()
        self.graph.parse(data=data)
        self.attributes = attributes
        self.get_all_action_query = get_all_action_query
        self.sample_query = sample_query
        self.rollout_query = rollout_query

    def sample(self, state):
        out = parse_query(self.graph, self.sample_query, state)  # construct query result
        sample_graph = out.graph  # graph from the construct query
        result_action = convert_to_action(sample_graph)  # this should not be barely returning a state
        return result_action  # Send some sample action

    def rollout(self, state, tuple_history=None):
        out = parse_query(self.graph, self.rollout_query, state)
        # TODO: have to add history to the graph. But for now it is not needed.
        rollout_graph = out.graph
        result_action = convert_to_action(rollout_graph)
        return result_action

    def get_all_actions(self, state=None, history=None, *args):
        out = parse_query(self.graph, self.get_all_action_query, state)
        get_all_action_graph = out.graph
        result_actions = convert_to_actions(get_all_action_graph)
        return result_actions
