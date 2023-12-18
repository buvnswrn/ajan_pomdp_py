import sys

import pomdp_py
from rdflib import Graph

import POMDPService.ajan_pomdp_planning.helpers.to_graph as graph_helper
from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import createIRI, _Action, _For_Hash

gettrace = getattr(sys, 'gettrace', None)
debug = False
if gettrace is None:
    print('No sys.gettrace')
elif gettrace():
    print('Hmm, Big Debugger is watching me')
    debug = True


class AjanAction(pomdp_py.Action):
    def __init__(self, name, attributes=None, for_hash=None):
        self.name = name
        self.attributes = attributes
        self.for_hash = for_hash
        self.graph = Graph()
        self.action_subject = createIRI(_Action, name)
        if type(attributes) == str:
            temp_graph = Graph()
            temp_graph.parse(data=attributes, format='turtle')
            self.attributes_node = graph_helper.get_attributes_node_from_graph(temp_graph, self.action_subject)
            attributes = graph_helper.get_attributes_from_graph(temp_graph, self.attributes_node)
        if attributes is not None:
            self.attribute_node = graph_helper.add_attributes_to_graph(self.graph, attributes, self.action_subject)
            self.attributes = attributes
        if type(for_hash) == str:
            temp_graph = Graph()
            temp_graph.parse(data=for_hash, format='turtle')
            for_hash = graph_helper.get_to_print_from_graph(self.action_subject, temp_graph)
            # self.graph += temp_graph
        if for_hash is not None:
            self.for_hash = frozenset(for_hash)
            self.for_hash_node = graph_helper.add_to_list_values_to_graph(self.graph, for_hash,
                                                                       self.action_subject, _For_Hash)
        else:
            self.for_hash = None
        if debug:
            print(self.graph.serialize(format='turtle'))

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        if isinstance(other, AjanAction):
            return self.name == other.name \
                if self.attributes is None else self.attributes == other.attributes and self.name == other.name
        elif type(other) == str:
            return self.name == other

    def __str__(self):
        return self.name

    def __repr__(self):
        if self.for_hash is None or self.attributes is None:
            return "AjanAction(%s)" % self.name
        else:
            attr_to_print = self.name
            for key in self.for_hash:
                attr_to_print += ", %s" % str(self.attributes[key])
            return 'AjanAction(%s)' % (str(attr_to_print))
