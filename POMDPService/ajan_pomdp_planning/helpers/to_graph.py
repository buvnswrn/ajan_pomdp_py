from sys import gettrace

from rdflib import RDF, Graph, BNode

from POMDPService.ajan_pomdp_planning.helpers.converters import get_data_from_graph, get_value_to_graph_literal
import POMDPService.ajan_pomdp_planning.oopomdp.domain.action as _action_helper
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanOOState, AjanEnvObjectState, AjanAgentState
from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import createIRI, _State, _CurrentAction, _Action, \
    _CurrentState, _NextState, pomdp_ns, _Attributes


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


def get_action_query(action):
    query = """PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    SELECT ?attributes
    WHERE {
        {
        BIND (<""" + str(action) + """> as ?action)
        }
        ?action (pomdp-ns:|!pomdp-ns:)* ?s .
        ?action pomdp-ns:attributes ?attributes .
        ?s ?p ?o .
        }"""
    return query


def add_state_to_graph(graph, state, namespace):
    graph.add((namespace, RDF.value, state.state_subject))
    graph += state.graph
    # add the type to the attributes node so that we can query it
    if not type(state) == AjanOOState:
        graph.add((state.attributes_node, RDF.type, namespace))
    else:
        for key, value in state.object_states.items():
            graph.add((value.attributes_node, RDF.type, namespace))
    return graph


def add_action_to_graph(graph, action, namespace=_CurrentAction):
    # Add Current Action value and it's graph
    graph.add((namespace, RDF.value, createIRI(_Action, action)))
    graph += action.graph
    return graph


def check_state(model_id, state):
    if isinstance(state, AjanOOState):
        state = state.object_states[model_id]
    return state


def remove_state_from_graph(graph, state, namespace):
    graph.remove((namespace, RDF.value, createIRI(_State, state.attributes['id'])))
    graph -= state.graph
    # add the type to the attributes node so that we can query it
    if type(state) != AjanOOState:
        graph.remove((state.attributes_node, RDF.type, namespace))
    return graph


def remove_action_from_graph(graph, action):
    graph.remove((_CurrentAction, RDF.value, createIRI(_Action, action)))
    graph -= action.graph
    return graph


def parse_query(graph, query, state, action=None, next_state=None, remove_cache=True):
    if action is not None:
        graph = add_action_to_graph(graph, action)
    if state is not None:
        graph = add_state_to_graph(graph, state, _CurrentState)  # removed oo state since we do not need it.
    if next_state is not None:
        graph = add_state_to_graph(graph, next_state, _NextState)  # removed oo state since we do not need it.
    out = graph.query(query)
    print("out", out.bindings)
    # result_state = [a[key_value] for a in out][0]
    if remove_cache:
        if action is not None:
            remove_action_from_graph(graph, action)
        if state is not None:
            remove_state_from_graph(graph, state, _CurrentState)
        if next_state is not None:
            remove_state_from_graph(graph, next_state, _NextState)
    return out


def get_state_from_graph(graph, state_uri):
    out = graph.query(get_state_query(state_uri))
    result = out.bindings[0]
    state_id = int(result['id'])
    state_type = str(result['type'])
    state_name = str(result['name'])
    state_attributes_node = result['attributes']
    state_attributes = get_attributes_from_graph(graph, state_attributes_node)
    if state_type.lower() == "env":
        result_state = AjanEnvObjectState(state_name, state_id, attributes=state_attributes)
    elif state_type.lower() == "agent":
        result_state = AjanAgentState(state_name, state_id, state_attributes)
    else:
        raise ValueError("Unknown state type: %s" % state_type)
    return result_state


def get_action_from_graph(graph, action_uri, fetch_multiple=False):
    out = graph.query(get_action_query(action_uri))
    action_name = action_uri.split("/Action_")[-1]
    if len(out.bindings) == 0:
        return _action_helper.AjanAction(action_name)
    if fetch_multiple:
        results = list(set(out.bindings))
    else:
        results = list(set(out.bindings))[0:]
    result_actions = list()
    for result in results:
        action_attributes_node = result['attributes']
        action_attributes = get_attributes_from_graph(graph, action_attributes_node)
        action = _action_helper.AjanAction(action_name, action_attributes if len(action_attributes) > 0 else None)
        result_actions.append(action)
    action = result_actions[0] if not fetch_multiple else result_actions
    return action


def add_attributes_to_graph(graph, attributes, state_subject):
    attributes_node = BNode()
    graph.add((state_subject, _Attributes, attributes_node))
    for key, value in attributes.items():
        graph.add((attributes_node, createIRI(pomdp_ns, key), get_value_to_graph_literal(value, graph)))
    return attributes_node


def get_attributes_from_graph(graph, attributes_node):
    state_attributes = dict()
    for s, p, o in graph.triples((attributes_node, None, None)):
        if gettrace():
            print(s, p, o)
        key = p.split("/_")[-1]
        value = get_data_from_graph(o, graph)
        state_attributes[key] = value
    return state_attributes


def convert_to_state(graph: Graph):
    state_uri = [o for o in graph.objects(_State, RDF.value)][0]
    return get_state_from_graph(graph, state_uri)


def convert_to_action(graph: Graph):
    action_uri = [o for o in graph.objects(_Action, RDF.value)][0]
    return get_action_from_graph(graph, action_uri)


def convert_to_actions(graph: Graph):
    action_uris = [o for o in graph.objects(_Action, RDF.value)]
    actions = list()
    for action_uri in action_uris:
        action_or_action_list = get_action_from_graph(graph, action_uri, True)
        if isinstance(action_or_action_list, list):
            actions += action_or_action_list
        else:
            actions.append(action_or_action_list)
    return actions
