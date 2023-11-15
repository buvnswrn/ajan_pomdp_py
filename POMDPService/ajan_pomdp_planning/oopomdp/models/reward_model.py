import pomdp_py
from rdflib import Graph, RDF, Seq
from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import pomdp_ns, _CurrentState, _NextState, createIRI, \
    _State, _CurrentAction, _Action


class AjanRewardModel(pomdp_py.RewardModel):
    def __init__(self, data, attributes, probability_query, sample_query, argmax_query):
        self.graph = Graph()
        self.graph.parse(data=data)
        self.attributes = attributes
        self.probability_query = probability_query
        self.argmax_query = argmax_query
        self.sample_query = sample_query

    def probability(self, reward, state, action, next_state):
        self.graph.add((pomdp_ns['reward'], RDF.value,
                        pomdp_ns[reward]))
        out = self.parse_query(self.probability_query, next_state, action)
        # Update the observation, next_state, action to the local graph
        return out.probability

    def sample(self, state, action, next_state):
        if self.sample_query == "argmax":
            return self.argmax(state, action, next_state)
        out = self.parse_query(self.sample_query, state, action, next_state)
        return float([a.sample for a in out][0])

    def argmax(self, state, action, next_state):
        if self.argmax_query == "sample":
            return self.sample(state, action, next_state)
        out = self.parse_query(self.argmax_query, state, action, next_state)
        return float([a.argmax for a in out][0])

    def remove_oo_state_from_graph(self, state):
        for key, value in state.object_states.items():
            self.graph -= value.graph

    def remove_action_from_graph(self, action):
        self.graph -= action.graph

    def add_action_to_graph(self, action):
        # Add Current Action value and it's graph
        self.graph.add((_CurrentAction, RDF.value, createIRI(_Action, action)))
        self.graph += action.graph

    def add_oo_state_to_graph(self, state, namespace):
        # Add Current State value and it's graph
        states = list()
        for key, value in state.object_states.items():
            state_subject = createIRI(_State, value.attributes['id'])
            states.append(state_subject)
            self.graph += value.graph
        Seq(self.graph, namespace, states)

    def parse_query(self, query, state, action, next_state=None, remove_cache=True):
        self.add_action_to_graph(action)
        self.add_oo_state_to_graph(state, _CurrentState)
        if next_state is not None:
            self.add_oo_state_to_graph(next_state, _NextState)
        out = self.graph.query(query)
        if remove_cache:
            self.remove_action_from_graph(action)
            self.remove_oo_state_from_graph(state)
            if next_state is not None:
                self.remove_oo_state_from_graph(next_state)
        return out
