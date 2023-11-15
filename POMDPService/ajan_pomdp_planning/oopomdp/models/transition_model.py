import pomdp_py
import rdflib.term
from rdflib import Graph, RDF, Seq

from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanOOState, AjanEnvObjectState, AjanAgent
from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import pomdp_ns, createIRI, _State, \
    _CurrentState, _CurrentAction, _Action, _NextState


def get_state_query(state):
    # query = """PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    # PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    #
    # SELECT ?s ?p ?o
    # WHERE {
    #     {
    #
    #     BIND (<"""+str(state)+"""> as ?state)
    #
    #     }
    #     ?state (pomdp-ns:|!pomdp-ns:)* ?s .
    #     ?s ?p ?o .
    #     }"""
    query = """PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
        PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
        PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        
        SELECT DISTINCT ?id ?type ?attributes
        WHERE {
            {
            
            BIND (<"""+str(state)+"""> as ?state)
            
            }
            ?state (pomdp-ns:|!pomdp-ns:)* ?s .
            ?state pomdp-ns:id ?id .
            ?state pomdp-ns:type ?type .
            ?state pomdp-ns:attributes ?attributes .
            ?s ?p ?o .
        }"""
    return query


class AjanTransitionModel(pomdp_py.TransitionModel):
    def __init__(self, data, attributes, probability_query, sample_query, argmax_query):
        self.graph = Graph()
        self.graph.parse(data=data)
        self.attributes = attributes
        self.probability_query = probability_query
        self.argmax_query = argmax_query
        self.sample_query = sample_query
        self.prev_graphs = list()

    def probability(self, next_state, state, action):
        self.graph.add((pomdp_ns['state'], RDF.value,
                        pomdp_ns[state]))
        out = self.parse_query(self.probability_query, state, action, next_state)
        # Update the observation, next_state, action to the local graph
        return out.probability

    def sample(self, state, action):
        if self.sample_query == "argmax":
            return self.argmax(state, action)
        out = self.parse_query(self.sample_query, state, action, remove_cache=False)
        result_state_uri = [a.sample for a in out][0]
        result_state = self.convert_to_states(result_state_uri)
        return result_state  # Send some sample state

    def argmax(self, state, action):
        if self.argmax_query == "sample":
            return self.sample(state, action)
        out = self.parse_query(self.argmax_query, state, action)
        return self.convert_to_states(out.argmax)

    def convert_to_states(self, state_uri):
        out = self.graph.query(get_state_query(state_uri))
        result = out.bindings[0]
        state_id = int(result['id'])
        state_type = str(result['type'])
        state_attributes_node = result['attributes']
        state_attributes = dict()
        for s, p, o in self.graph.triples((state_attributes_node, None, None)):
            print(s, p, o)
            key = p.split("_")[-1]
            dt = rdflib.term.XSDToPython[o.datatype] # watchout for string value
            value = str(o)
            if dt is not None:
                value = dt(value)
            state_attributes[key] = value
        if state_type == "Env":
            result_state = AjanEnvObjectState("", state_id, attributes=state_attributes)
        elif state_type == "Agent":
            result_state = AjanAgent(state_id, state_attributes)
        return result_state

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
        # result_state = [a[key_value] for a in out][0]
        if remove_cache:
            self.remove_action_from_graph(action)
            self.remove_oo_state_from_graph(state)
            if next_state is not None:
                self.remove_oo_state_from_graph(next_state)
        return out


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
        return AjanOOState(oostate.object_states)

    def argmax(self, state, action, **kwargs):
        oostate = pomdp_py.OOTransitionModel.argmax(self, state, action, **kwargs)
        return AjanOOState(oostate.object_states)
