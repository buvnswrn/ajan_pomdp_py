from sys import gettrace

import rdflib
from rdflib import RDF

from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanOOState, AjanEnvObjectState, AjanAgentState
from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import createIRI, _State, _CurrentAction, _Action, \
    _CurrentState, _NextState


def add_state_to_graph(graph, state, namespace):
    state_subject = createIRI(_State, state.attributes['id'])
    graph.add((namespace, RDF.value, state_subject))
    graph += state.graph


def add_action_to_graph(graph, action):
    # Add Current Action value and it's graph
    graph.add((_CurrentAction, RDF.value, createIRI(_Action, action)))
    graph += action.graph


def check_state(model_id, state):
    if isinstance(state, AjanOOState):
        state = state.object_states[model_id]
    return state


def remove_state_from_graph(graph, state, namespace):
    graph.remove((namespace, RDF.value, createIRI(_State, state.attributes['id'])))
    graph -= state.graph


def remove_action_from_graph(graph, action):
    graph.remove((_CurrentAction, RDF.value, createIRI(_Action, action)))
    graph -= action.graph


def parse_query(graph, query, state, action, next_state=None, remove_cache=True):
    add_action_to_graph(graph, action)
    add_state_to_graph(graph, state, _CurrentState)  # removed oo state since we do not need it.
    if next_state is not None:
        add_state_to_graph(graph, next_state, _NextState)  # removed oo state since we do not need it.
    out = graph.query(query)
    # result_state = [a[key_value] for a in out][0]
    if remove_cache:
        remove_action_from_graph(graph, action)
        remove_state_from_graph(graph, state, _CurrentState)
        if next_state is not None:
            remove_state_from_graph(graph, next_state, _NextState)
    return out


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
    # Change: Add ?name
    query = """PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
        PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
        PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>

        SELECT DISTINCT ?id 
         ?name 
        ?type ?attributes
        WHERE {
            {

            BIND (<""" + str(state) + """> as ?state)

            }
            ?state (pomdp-ns:|!pomdp-ns:)* ?s .
            ?state pomdp-ns:id ?id .
            ?state pomdp-ns:type ?type .
            ?state pomdp-ns:name ?name .
            ?state pomdp-ns:attributes ?attributes .
            ?s ?p ?o .
        }"""
    return query


def convert_to_states(graph, state_uri):
        out = graph.query(get_state_query(state_uri))
        result = out.bindings[0]
        state_id = int(result['id'])
        state_type = str(result['type'])
        state_name = str(result['name'])
        state_attributes_node = result['attributes']
        state_attributes = dict()
        for s, p, o in graph.triples((state_attributes_node, None, None)):
            if gettrace():
                print(s, p, o)
            key = p.split("_")[-1]
            dt = rdflib.term.XSDToPython[o.datatype]  # watchout for string value
            value = str(o)
            if dt is not None:
                value = dt(value)
            state_attributes[key] = value
        if state_type.lower() == "env":
            result_state = AjanEnvObjectState(state_name, state_id, attributes=state_attributes)
        elif state_type.lower() == "agent":
            result_state = AjanAgentState(state_name, state_id, state_attributes)
        # Change: Add name to the state
        # result_oo_state = AjanOOState({ord(state_name[0]): result_state})  # This should not convert to OOState
        # result_state = result_oo_state
        return result_state