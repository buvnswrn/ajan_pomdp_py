import pomdp_py
import rdflib
from pomdp_py import OOState
from rdflib import Graph, RDF, BNode

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
        out = self.parse_query(self.sample_query, state)
        action = [AjanAction(str(a.sample)) for a in out][0]
        return action

    def rollout(self, state, tuple_history=None):
        if self.rollout_query == 'sample':
            return self.sample(state)
        out = self.parse_query(self.rollout_query, state)
        action = [AjanAction(str(a.rollout)) for a in out][0]
        return action

    def get_all_actions(self, state=None, history=None, *args):
        out = self.parse_query(self.get_all_action_query, state)
        action_list = [AjanAction(str(a.allActions)) for a in out]
        return action_list

    def convert_to_action(self, sample):
        return [AjanAction(str(a.allActions)) for a in sample]

    def parse_query(self, query, next_state: OOState):
        emptyNode = BNode()
        self.graph.add((_NextState, RDF.value,
                        emptyNode))
        next_state_dict_node = BNode()
        self.graph.add((emptyNode, RDF.type, _OOState))
        self.graph.add((emptyNode, RDF.value, next_state_dict_node))

        # self.graph.add((next_state_dict_node, RDF.type, RDF.Seq))
        # list_of_states = list(next_state.object_states.items())
        # rdflib.Seq(self.graph, pomdp_ns["object_states"])  # create a sequence in the graph
        #
        # for i, (key, value) in enumerate(list_of_states):
        #     pair = BNode()
        #     self.graph.add((pair, pomdp_ns["key"], rdflib.Literal(key, datatype=rdflib.XSD.int)))
        #     self.graph.add((pair, pomdp_ns["value"], convert_state_to_rdf(self.graph, value)))
        #     self.graph.add((next_state_dict_node, RDF.li[i], pomdp_ns[key]))
        #     self.graph.add((pomdp_ns[key], RDF.value,
        #                     pomdp_ns[value]))
        #
        # self.graph.add((next_state_dict_node, RDF.first, emptyNode))
        # # convert the next_state to RDF
        # for key, value in next_state.object_states.items():
        #     self.graph.add((pomdp_ns[key], RDF.value,
        #                     pomdp_ns[value]))
        out = self.graph.query(query)
        return out
