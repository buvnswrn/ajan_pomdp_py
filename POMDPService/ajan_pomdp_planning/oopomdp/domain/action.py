import pomdp_py
from rdflib import Graph


class AjanAction(pomdp_py.Action):
    def __init__(self, name, attributes=None):
        self.name = name
        self.attributes = attributes
        self.graph = Graph()

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
