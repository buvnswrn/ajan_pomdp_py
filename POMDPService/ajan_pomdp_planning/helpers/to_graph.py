import sys

from rdflib import RDF, Graph, BNode, Literal

import POMDPService.ajan_pomdp_planning.oopomdp.domain.action as _action_helper
import POMDPService.ajan_pomdp_planning.oopomdp.domain.observation as _observation_helper
from POMDPService.ajan_pomdp_planning.helpers.converters import get_data_from_graph, get_value_to_graph_literal
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanOOState, AjanEnvObjectState, AjanAgentState
from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import createIRI, _State, _CurrentAction, _Action, \
    _CurrentState, _NextState, pomdp_ns, _Attributes, _CurrentObservation, _Observation, _To_Print, _PlannedAction, \
    pomdp_ns1

gettrace = getattr(sys, 'gettrace', None)
debug = False
if gettrace is None:
    print('No sys.gettrace')
elif gettrace():
    print('Hmm, Big Debugger is watching me')
    debug = False

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


def get_observation_query(observation):
    query = """PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    SELECT ?attributes ?for_hash
    WHERE {
        {
        BIND (<""" + str(observation) + """> as ?observation)
        }
        ?observation (pomdp-ns:|!pomdp-ns:)* ?s .
        ?observation pomdp-ns:attributes ?attributes .
        ?observation pomdp-ns:for_hash ?for_hash .
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


def add_observation_to_graph(graph, observation, namespace):
    graph.add((namespace, RDF.value, observation.observation_subject))
    graph += observation.graph
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
    graph.remove((namespace, RDF.value, state.state_subject))
    graph -= state.graph
    # add the type to the attributes node so that we can query it
    if type(state) != AjanOOState:
        graph.remove((state.attributes_node, RDF.type, namespace))
    else:
        for key, value in state.object_states.items():
            graph.remove((value.attributes_node, RDF.type, namespace))
    return graph


def remove_action_from_graph(graph, action):
    graph.remove((_CurrentAction, RDF.value, createIRI(_Action, action)))
    graph -= action.graph
    return graph


def remove_observation_from_graph(graph, observation, namespace):
    graph.remove((namespace, RDF.value, observation.observation_subject))
    graph -= observation.graph
    return graph


def parse_query(graph, query, state=None, action=None, next_state=None, observation=None, remove_cache=True):
    if action is not None:
        graph = add_action_to_graph(graph, action)
    if state is not None:
        graph = add_state_to_graph(graph, state, _CurrentState)  # removed oo state since we do not need it.
    if next_state is not None:
        graph = add_state_to_graph(graph, next_state, _NextState)  # removed oo state since we do not need it.
    if observation is not None:
        graph = add_observation_to_graph(graph, observation, _CurrentObservation)
    out = graph.query(query)
    # print("out", out.bindings)
    # result_state = [a[key_value] for a in out][0]
    if remove_cache:
        if action is not None:
            remove_action_from_graph(graph, action)
        if state is not None:
            remove_state_from_graph(graph, state, _CurrentState)
        if next_state is not None:
            remove_state_from_graph(graph, next_state, _NextState)
        if observation is not None:
            remove_observation_from_graph(graph, observation, _CurrentObservation)
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


def get_observation_from_graph(graph, observation_uri):
    out = graph.query(get_observation_query(observation_uri))
    result = out.bindings[0]
    observation_attributes_node = result['attributes']
    observation_for_hash = result['for_hash']
    observation_attributes = get_attributes_from_graph(graph, observation_attributes_node)
    for_hash = get_for_hash_from_graph(graph, observation_for_hash)
    result_observation = _observation_helper.AjanObservation(observation_attributes, for_hash)
    return result_observation


def add_attributes_to_graph(graph, attributes, state_subject):
    attributes_node = add_blank_parent_node(graph, _Attributes, state_subject)
    for key, value in attributes.items():
        graph.add((attributes_node, createIRI(pomdp_ns, key), get_value_to_graph_literal(value, graph)))
    return attributes_node


def add_to_list_values_to_graph(graph, to_print, state_subject, namespace=_To_Print):
    to_print_node = add_blank_parent_node(graph, namespace, state_subject)
    for key in to_print:
        graph.add((to_print_node, RDF.value, Literal(key)))
    return to_print_node


def add_blank_parent_node(graph, namespace, state_subject):
    attributes_node = BNode()
    graph.add((state_subject, namespace, attributes_node))
    return attributes_node


def get_attributes_from_graph(graph, attributes_node):
    if attributes_node == RDF.nil:
        return None
    state_attributes = dict()
    for s, p, o in graph.triples((attributes_node, None, None)):
        if debug:
            print(s, p, o)
        key = p.split("/_")[-1]
        value = get_data_from_graph(o, graph)
        state_attributes[key] = value
    return state_attributes


def get_attributes_node_from_graph(graph, parent_node):
    for s, p, o in graph.triples((parent_node, _Attributes, None)):
        return o


def get_for_hash_from_graph(graph, for_hash_node):
    for_hash = list()
    for s, p, o in graph.triples((for_hash_node, RDF.value, None)):
        for_hash.append(str(o))
    return for_hash


def get_to_print_from_graph(subject_node, graph: Graph):
    print_node = [print_node for print_node in graph.objects(subject_node, _To_Print)][0]
    if print_node == RDF.nil:
        return None
    else:
        return get_for_hash_from_graph(graph, print_node)


def convert_to_state(graph: Graph):
    state_uri = [o for o in graph.objects(_State, RDF.value)][0]
    return get_state_from_graph(graph, state_uri)


def convert_to_action(graph: Graph):
    action_uri = [o for o in graph.objects(_Action, RDF.value)][0]
    return get_action_from_graph(graph, action_uri)


def convert_to_observation(graph: Graph):
    return get_observation_from_graph(graph, _Observation)


def convert_to_planned_action_data(graph: Graph, pomdp_id, action):
    pomdp_id_node = pomdp_ns1[str(pomdp_id)]
    action_node = createIRI(_Action, str(action))
    temp_graph = Graph()
    temp_graph.add((pomdp_id_node, _PlannedAction, action_node))
    temp_graph += graph
    if action.attributes is not None:
        attribute_node = get_attributes_node_from_graph(graph, None)
        temp_graph.add((attribute_node, RDF.type, _PlannedAction))
    return temp_graph.serialize(format="turtle")


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
