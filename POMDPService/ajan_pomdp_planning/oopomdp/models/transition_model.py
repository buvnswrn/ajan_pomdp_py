import pomdp_py
from rdflib import Graph, Seq

from POMDPService.ajan_pomdp_planning.helpers.to_graph import check_state, \
    remove_state_from_graph, parse_query, convert_to_states
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanOOState
from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import createIRI, _State, \
    _CurrentState


class AjanTransitionModel(pomdp_py.TransitionModel):
    def __init__(self, model_id, data, attributes, probability_query, sample_query, argmax_query):
        self.model_id = model_id
        self.graph = Graph()
        self.graph.parse(data=data)
        self.attributes = attributes
        self.probability_query = probability_query
        self.argmax_query = argmax_query
        self.sample_query = sample_query
        self.prev_graphs = list()

    def probability(self, next_state, state, action):

        # check whether the passed state is OOState or not
        # Based on that load the corresponding state. Filter the needed states only
        state = check_state(self.model_id, state)
        next_state = check_state(self.model_id, next_state)

        # add the corresponding data to the graph to query them
        self.graph.add((pomdp_ns['state'], RDF.value,
                        pomdp_ns[state]))
        out = self.parse_query(self.probability_query, state, action, next_state)
        out = parse_query(self.graph, self.probability_query, state, action, next_state)
        # Update the observation, next_state, action to the local graph
        return float(out.bindings[0]['probability'])

    def sample(self, state, action):
        state = check_state(self.model_id, state)
        out = parse_query(self.graph, self.sample_query, state, action, remove_cache=False)
        result_state_uri = [a.sample for a in out][0]
        # Does not return OO State
        result_state = convert_to_states(self.graph, result_state_uri)  # this should not be barely returning a state
        return result_state  # Send some sample state

    def argmax(self, state, action):
        if self.argmax_query == "sample":
            return self.sample(state, action)
        state = self.check_state(state)
        out = self.parse_query(self.argmax_query, state, action)
        return self.convert_to_states(out.argmax)
        state = check_state(self.model_id, state)
        out = parse_query(self.graph, self.argmax_query, state, action)
        result_state_uri = [a.argmax for a in out][0]
        return convert_to_states(self.graph, result_state_uri)

    # region Helper Functions

    def remove_oo_state_from_graph(self, state):
        for key, value in state.object_states.items():
            remove_state_from_graph(self.graph, value, _CurrentState)

    def add_oo_state_to_graph(self, state, namespace):
        # Add Current State value and it's graph
        states = list()
        for key, value in state.object_states.items():
            state_subject = createIRI(_State, value.attributes['id'])
            states.append(state_subject)
            self.graph += value.graph
        Seq(self.graph, namespace, states)

    # endregion


class AjanOOTransitionModel(pomdp_py.OOTransitionModel):
    def __init__(self, ids, graph_datas, attributes, probability_queries, sample_queries, argmax_queries):
        transition_models = {ids[i]: AjanTransitionModel(graph_datas[i],
                                                         attributes[i],
                                                         probability_queries[i],
                                                         sample_queries[i],
                                                         argmax_queries[i]) for i in range(0, len(ids))}
        super().__init__(transition_models)

    def __init__(self, transition_models):
        super().__init__(transition_models)

    def sample(self, state, action, argmax=False, **kwargs):
        oostate = pomdp_py.OOTransitionModel.sample(self, state, action, **kwargs)
        return AjanOOState(oostate.object_states)  # this should be the one converting to OOState after getting a state

    def argmax(self, state, action, **kwargs):
        oostate = pomdp_py.OOTransitionModel.argmax(self, state, action, **kwargs)
        return AjanOOState(oostate.object_states)
