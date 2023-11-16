import pomdp_py
import rdflib.term
from rdflib import Graph, RDF, Seq

from POMDPService.ajan_pomdp_planning.oopomdp.domain.observation import AjanObservation, AjanOOObservation
from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import pomdp_ns, _CurrentAction, createIRI, _Action, \
    _NextState, _State


def get_observation_query(observation):
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

        SELECT DISTINCT ?attributes ?forhash
        WHERE {
            {

            BIND (<""" + str(observation) + """> as ?state)

            }
            ?state (pomdp-ns:|!pomdp-ns:)* ?s .
            ?state pomdp-ns1:attributes ?attributes .
            ?state pomdp-ns1:for_hash ?forhash .
            ?s ?p ?o .
        }"""
    return query


def get_list(graph: Graph, observation_for_hash):
    l_ = []
    i = 1
    while True:
        elem_uri = str(RDF) + "_" + str(i)
        if (observation_for_hash, rdflib.URIRef(elem_uri), None) in graph:
            for s, p, o in graph.triples((observation_for_hash, rdflib.URIRef(elem_uri), None)):
                dt = rdflib.term.XSDToPython[o.datatype]
                value = str(o)
                if dt is not None:
                    value = dt(value)
                l_.append(value)
            i += 1
        else:
            break
    return l_


class AjanObservationModel(pomdp_py.ObservationModel):
    def __init__(self, data, attributes, probability_query, sample_query, argmax_query):
        self.graph = Graph()
        self.graph.parse(data=data)
        self.attributes = attributes
        self.probability_query = probability_query
        self.argmax_query = argmax_query
        self.sample_query = sample_query

    def probability(self, observation, next_state, action):
        self.graph.add((pomdp_ns['observation'], RDF.value,
                        pomdp_ns[observation]))
        out = self.parse_query(self.probability_query, next_state, action)
        # Update the observation, next_state, action to the local graph
        # Assign some random probability
        return out.probability

    def sample(self, next_state, action):
        if self.sample_query == "argmax":
            return self.argmax(next_state, action)
        out = self.parse_query(self.sample_query, next_state, action)
        observation_uri = [a.sample for a in out][0]
        # AjanObservation(out.attributes, out.for_hash)
        return self.convert_to_observation(observation_uri)

    def argmax(self, next_state, action):
        if self.argmax_query == "sample":
            return self.sample(next_state, action)
        out = self.parse_query(self.argmax_query, next_state, action)
        return self.convert_to_observation(out.argmax)

    def convert_to_observation(self, observation_uri) -> AjanObservation:
        out = self.graph.query(get_observation_query(observation_uri))
        result = out.bindings[0]
        observation_attributes_node = result['attributes']
        observation_attributes = dict()
        for s, p, o in self.graph.triples((observation_attributes_node, None, None)):
            key = p.split('_')[1]
            dt = rdflib.term.XSDToPython[o.datatype]
            value = str(o)
            if dt is not None:
                value = dt(value)
            observation_attributes[key] = value
        observation_for_hash = result['forhash']
        for_hash = get_list(self.graph, observation_for_hash)
        return AjanObservation(observation_attributes, for_hash)

    def remove_oo_state_from_graph(self, state):
        for key, value in state.object_states.items():
            self.graph -= value.graph

    def remove_action_from_graph(self, action):
        self.graph -= action.graph

    def add_action_to_graph(self, action):
        # Add Current Action value and it's graph
        self.graph.add((_CurrentAction, RDF.value, createIRI(_Action, action)))
        self.graph += action.graph

    def add_next_state_to_graph(self, state):
        # Add Current State value and it's graph
        states = list()
        for key, value in state.object_states.items():
            state_subject = createIRI(_State, value.attributes['id'])
            states.append(state_subject)
            self.graph += value.graph
        Seq(self.graph, _NextState, states)

    def parse_query(self, query, next_state, action):
        self.add_action_to_graph(action)
        self.add_next_state_to_graph(next_state)
        out = self.graph.query(query)
        return out


class AjanOOObservationModel(pomdp_py.OOObservationModel):
    def __init__(self, ids, graph_datas, attributes, probability_queries, sample_queries, argmax_queries):
        observation_models = {ids[i]: AjanObservationModel(graph_datas[i],
                                                           attributes[i],
                                                           probability_queries[i],
                                                           sample_queries[i],
                                                           argmax_queries[i]) for i in range(0, len(ids))}
        pomdp_py.OOObservationModel.__init__(self, observation_models)

    def __init__(self, observation_models):
        pomdp_py.OOObservationModel.__init__(self, observation_models)

    def sample(self, next_state, action, argmax=False, **kwargs):
        obs = super().sample(next_state, action, argmax, **kwargs)
        return AjanOOObservation(obs)
