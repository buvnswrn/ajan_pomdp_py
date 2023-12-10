import sys

import pomdp_py
from rdflib import Graph, RDF, Literal

import POMDPService.ajan_pomdp_planning.helpers.to_graph as graph_helper
from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import createIRI, _State, _Type, _Id, _OOState, _Name

gettrace = getattr(sys, 'gettrace', None)
debug = False
if gettrace is None:
    print('No sys.gettrace')
elif gettrace():
    print('Hmm, Big Debugger is watching me')
    debug = True


class AjanAgentState(pomdp_py.ObjectState):
    def __init__(self, name, agent_id, attributes: dict = None, to_print: list = None):
        if to_print is None:
            to_print = ['id']
        self.to_print = frozenset(to_print)
        self.graph = Graph()
        self.state_subject = createIRI(_State, agent_id)
        self.graph.add((self.state_subject, RDF.type, _State))
        self.graph.add((self.state_subject, _Type, Literal("Agent")))
        self.graph.add((self.state_subject, _Id, Literal(agent_id)))
        self.graph.add((self.state_subject, _Name, Literal(name)))
        if attributes is not None:
            attributes = {**attributes, **{"id": agent_id}}
        else:
            attributes = {"id": agent_id}
        self.attributes_node = graph_helper.add_attributes_to_graph(self.graph, attributes, self.state_subject)
        if debug:
            print(self.graph.serialize(format='turtle'))
        super().__init__('AjanAgent_' + name, attributes)

    def __str__(self):
        attr_to_print = str(self.attributes['id'])
        for key in self.to_print:
            if key != 'id':
                attr_to_print += ", %s" % str(self.attributes[key])
        return 'AjanAgentState(%s)' % (str(attr_to_print))

    def __repr__(self):
        return self.__str__()


class AjanEnvObjectState(pomdp_py.ObjectState):
    def __init__(self, objclass, obj_id, attributes: dict = None, to_print: list = None):
        if to_print is None:
            to_print = ['id']
        self.to_print = frozenset(to_print)
        self.graph = Graph()
        self.state_subject = createIRI(_State, obj_id)
        self.graph.add((self.state_subject, RDF.type, _State))
        self.graph.add((self.state_subject, _Type, Literal("Env")))
        self.graph.add((self.state_subject, _Id, Literal(obj_id)))
        self.graph.add((self.state_subject, _Name, Literal(objclass)))
        if attributes is not None:
            attributes = {**attributes, **{"id": obj_id}}
        else:
            attributes = {"id": obj_id}
        self.attributes_node = graph_helper.add_attributes_to_graph(self.graph, attributes, self.state_subject)
        if debug:
            print(self.graph.serialize(format='turtle'))
        super().__init__("AjanEnv_" + objclass, attributes)

    def add_attribute(self, key, value):
        pass

    def __str__(self):
        attr_to_print = str(self.attributes['id'])
        for key in self.to_print:
            if key != 'id':
                attr_to_print += ", %s" % str(self.attributes[key])
        return 'AjanEnvObjectState(%s)' % (str(attr_to_print))


class AjanOOState(pomdp_py.OOState):
    def __init__(self, object_states: dict):
        self.attributes = dict()
        self.attributes['id'] = ""
        states = list()

        self.graph = Graph()

        for key, value in object_states.items():
            _id = value.attributes['id']
            self.attributes['id'] += str(_id) + "_"
        self.attributes['id'] = self.attributes['id'][:-1]
        self.state_subject = createIRI(_OOState, self.attributes['id'])
        self.graph.add((self.state_subject, RDF.type, _OOState))
        self.graph.add((self.state_subject, _Id, Literal(self.attributes['id'])))
        for key, value in object_states.items():
            states.append(value.state_subject)
            self.graph += value.graph
            self.graph.add((self.state_subject, RDF.value, value.state_subject))

        if debug:
            print(self.graph.serialize(format='turtle'))

        super().__init__(object_states)

    def __str__(self):
        return 'AjanOOState(%s)' % (str(self.object_states))

    def __repr__(self):
        return str(self)

    def __to_rdf__(self):
        return self.object_states


def to_string(obj):
    return "new string"


if __name__ == "__main__":
    attr = {"gesture": False, "pose": (1, 0)}
    toprint = ["gesture"]
    toprint1 = ["gesture", "pose"]
    agent = AjanAgentState("Drone", 9, attr, toprint)
    agent1 = AjanEnvObjectState("Person", 120, attr, toprint1)
    agent1.attributes['pose'] = (10, 9)
    print(agent.attributes['id'])
    # AjanAgent.__str__ = to_string
    print(agent)
    print(agent1)
