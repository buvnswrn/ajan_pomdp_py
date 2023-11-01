import pomdp_py
from rdflib import Graph


class AjanAgent(pomdp_py.ObjectState):
    def __init__(self, agent_id, attributes: dict = None, to_print: list = None):
        if to_print is None:
            to_print = ['id']
        self.to_print = frozenset(to_print)
        self.graph = Graph()
        if attributes is not None:
            attributes = {**attributes, **{"id": agent_id}}
        else:
            attributes = {"id": agent_id}

        super().__init__('AjanAgent', attributes)

    def __str__(self):
        attr_to_print = str(self.attributes['id'])
        for key in self.to_print:
            if key != 'id':
                attr_to_print += ", %s" % str(self.attributes[key])
        return 'AjanAgentState(%s)' % (str(attr_to_print))

    def __repr__(self):
        return self.__str__()


class AjanEnvObjectState(pomdp_py.ObjectState):
    def __init__(self, objclass, obj_id, attributes: dict = None,  to_print: list = None):
        if to_print is None:
            to_print = ['id']
        self.to_print = frozenset(to_print)
        self.graph = Graph()
        if attributes is not None:
            attributes = {**attributes, **{"id": obj_id}}
        else:
            attributes = {"id": obj_id}
        super().__init__(objclass, attributes)

    def __str__(self):
        attr_to_print = str(self.attributes['id'])
        for key in self.to_print:
            if key != 'id':
                attr_to_print += ", %s" % str(self.attributes[key])
        return 'AjanEnvObjectState(%s)' % (str(attr_to_print))


class AjanOOState(pomdp_py.OOState):
    def __init__(self, object_states):
        super().__init__(object_states)

    def __str__(self):
        return 'AjanOOState(%s)' % (str(self.object_states))

    def __repr__(self):
        return str(self)


def to_string(obj):
    return "new string"


if __name__ == "__main__":
    attr = {"gesture": False, "pose": (1, 0)}
    toprint = ["gesture"]
    toprint1 = ["gesture", "pose"]
    agent = AjanAgent(9, attr, toprint)
    agent1 = AjanEnvObjectState("Person", 120, attr, toprint1)
    agent1.attributes['pose'] = (10, 9)
    print(agent.attributes['id'])
    # AjanAgent.__str__ = to_string
    print(agent)
    print(agent1)
