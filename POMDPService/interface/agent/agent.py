import ctypes

import rdflib.term
import rdfpandas
from fastapi import APIRouter
from rdflib import Graph, RDF, XSD

from POMDPService.VariableModels.ResponseModels import CreateResponse, BooleanResponse
from POMDPService.VariableModels.State import AgentInit, POMDPInit
from POMDPService.ajan_pomdp_planning.oopomdp.agent.agent import AjanAgent
from POMDPService.ajan_pomdp_planning.oopomdp.domain.observation import AjanObservation
from POMDPService.ajan_pomdp_planning.oopomdp.problem import AjanOOPOMDP, update_belief
from POMDPService.interface.pomdp import init_beliefs, models, agents, problems, last_action, last_observation, planners
from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import _CurrentObservation, pomdp_ns1, pomdp_ns, _Type

agent_ns = APIRouter(prefix="/AJAN/pomdp/agent")


# Deprecated
@agent_ns.post("/create-from-pointers", summary="Create the agent", response_model=CreateResponse)
def create_agent(agent_init: AgentInit, pointers: bool):
    init_belief = ctypes.cast(agent_init.init_belief, ctypes.py_object).value
    policy_model = ctypes.cast(agent_init.policy_model, ctypes.py_object).value
    transition_model = ctypes.cast(agent_init.transition_model, ctypes.py_object).value
    observation_model = ctypes.cast(agent_init.observation_model, ctypes.py_object).value
    reward_model = ctypes.cast(agent_init.reward_model, ctypes.py_object).value
    agent = AjanAgent(agent_init.data, init_belief, policy_model, transition_model, observation_model, reward_model)
    agents[agent_init.pomdp_id] = agent
    return CreateResponse(name=str(agent), message="Created the agent", id=id(agent))


@agent_ns.post("/create", summary="Create the agent", response_model=CreateResponse)
def create_agent(agent_init: AgentInit):
    pomdp_id = agent_init.pomdp_id
    init_belief = init_beliefs[pomdp_id]
    policy_model = models[pomdp_id]['agent']['policy']
    transition_model = models[pomdp_id]['agent']['transition']
    observation_model = models[pomdp_id]['agent']['observation']
    reward_model = models[pomdp_id]['agent']['reward']
    agent = AjanAgent(agent_init.data, init_belief, policy_model, transition_model, observation_model, reward_model)
    agents[pomdp_id] = agent
    return CreateResponse(name=str(agent), message="Created the agent", id=id(agent))


@agent_ns.post("/update-belief", summary="Get the agent's action", response_model=CreateResponse)
def belief_update(agent_init: AgentInit):
    pomdp_id = agent_init.pomdp_id
    # Create an observation
    observation = create_observation(agent_init.data)
    # Update the belief
    problem: AjanOOPOMDP = problems[pomdp_id]
    update_belief(agents[pomdp_id], last_action[pomdp_id], observation, planners[pomdp_id],
                  obj_id=ord(agent_init.state_name[0].lower()), state_id=agent_init.state_id)
    # update_belief(agents[pomdp_id],last_action[pomdp_id], observation, planners[pomdp_id],
    #               obj_id=ord(agent_init.state_name[0]), state_id=agent_init.state_id)
    return CreateResponse(name=str(problem.agent.cur_belief), message="Updated the agent's belief",
                          id=id(problem.agent.cur_belief))


@agent_ns.post("/clear-history", summary="Clears the agent's history", response_model=BooleanResponse)
def clear_history(pomdp: POMDPInit):
    problems[pomdp.pomdp_id].agent.clear_history()
    return BooleanResponse(success=True, message="History cleared successfully")


@agent_ns.post("/update-history", summary="Updates the agent's history", response_model=BooleanResponse)
def update_history(pomdp: AgentInit):
    pomdp_id = pomdp.pomdp_id
    # Create and observation and then update the history
    observation = create_observation(pomdp.data)
    problem: AjanOOPOMDP = problems[pomdp_id]
    problem.agent.update_history(last_action[pomdp_id], observation)
    return BooleanResponse(success=True, message="Agent history updated successfully")


g = Graph()


def create_observation(data):
    # Create an observation
    g.parse(data=data)
    keys = [o for s, p, o in g.triples((_CurrentObservation, RDF.value, None))]
    convert_function = {}
    attributes = {}
    for key in keys:
        for s, p, o in g.triples((key, _Type, None)):
            convert_function[get_key_value(str(key))] = get_parse_function(s, o)
        for s, p, value_node in g.triples((key, RDF.value, None)):
            attributes[get_key_value(str(key))] = convert_function[get_key_value(str(key))](value_node)
    return AjanObservation(attributes, ['id'])


def get_key_value(key: str):
    return key.replace(str(pomdp_ns1['data']) + "/", "")


def get_parse_function(s, datatype: rdflib.term.Node):
    if datatype == pomdp_ns1['data/pandasDataFrame']:
        return get_dataframe_from_observation
    func = rdflib.term.XSDToPython[datatype]
    if func is None:
        return str
    return func


def get_dataframe_from_observation(observation):
    df_graph = Graph()
    for s, p, o in g.triples((observation, RDF.value, None)):
        for s1, p1, o1 in g.triples((o, None, None)):
            df_graph.add((s1, p1, o1))
    return rdfpandas.to_dataframe(df_graph)
