import sys

import pomdp_py
from rdflib import Graph

from POMDPService.ajan_pomdp_planning.helpers.to_graph import add_attributes_to_graph
from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import createIRI, _Action

gettrace = getattr(sys, 'gettrace', None)
debug = False
if gettrace is None:
    print('No sys.gettrace')
elif gettrace():
    print('Hmm, Big Debugger is watching me')
    debug = True


class AjanAction(pomdp_py.Action):
    def __init__(self, name, attributes=None):
        self.name = name
        self.attributes = attributes
        self.graph = Graph()

        if attributes is not None:
            action_subject = createIRI(_Action, name)
            add_attributes_to_graph(self.graph, attributes, action_subject)
        if debug:
            print(self.graph.serialize(format='turtle'))
        # TODO: add attributes to graph and check them

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if isinstance(other, AjanAction):
            return self.name == other.name
        elif type(other) == str:
            return self.name == other

    def __str__(self):
        return self.name

    def __repr__(self):
        return "AjanAction(%s)" % self.name
