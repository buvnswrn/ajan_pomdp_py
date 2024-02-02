import ctypes

from fastapi import APIRouter
from rdflib import Graph, RDF

from POMDPService.VariableModels.ResponseModels import CreateResponse, BooleanResponse
from POMDPService.VariableModels.State import EnvInit, POMDPInit, EnvStateInit
from POMDPService.ajan_pomdp_planning.helpers import to_graph
from POMDPService.ajan_pomdp_planning.oopomdp.env.env import AjanEnvironment
from POMDPService.ajan_pomdp_planning.vocabulary.POMDPVocabulary import _Environment, _State
from POMDPService.interface.pomdp import envs, init_states, models, problems, last_action, last_observation, \
    last_env_next_state

env_ns = APIRouter(prefix="/AJAN/pomdp/env")


# deprecated
@env_ns.post("/create-from-pointers", summary="Create an Environment", response_model=CreateResponse)
def create_env(env_init: EnvInit):
    init_state = ctypes.cast(env_init.init_state, ctypes.py_object).value
    transition_model = ctypes.cast(env_init.transition_model, ctypes.py_object).value
    reward_model = ctypes.cast(env_init.reward_model, ctypes.py_object).value
    env = AjanEnvironment(env_init.data, init_state, transition_model, reward_model)
    envs[env_init.pomdp_id] = env
    return CreateResponse(name=str(env), message="Created the Environment", id=id(env))


@env_ns.post("/create", summary="Create an Environment", response_model=CreateResponse)
def create_env(env_init: EnvInit):
    pomdp_id = env_init.pomdp_id
    data = env_init.data
    last_env_next_state[pomdp_id] = None
    init_state = init_states[pomdp_id]
    transition_model = models[pomdp_id]['env']['transition']
    reward_model = models[pomdp_id]['env']['reward']
    env = AjanEnvironment(data, init_state, transition_model, reward_model)
    envs[pomdp_id] = env
    return CreateResponse(name=str(env), message="Created the Environment", id=id(env))


@env_ns.post("/provide-observation", summary="Provide an observation", response_model=CreateResponse)
def provide_observation(pomdp_id: POMDPInit):
    pomdp_id = pomdp_id.pomdp_id
    problem = problems[pomdp_id]
    obs = problem.env.provide_observation(problem.agent.observation_model, last_action[pomdp_id])
    last_observation[pomdp_id] = obs
    return CreateResponse(name=str(obs), message="Observation is provided", id=id(obs))


@env_ns.post("/get-env-state", summary="Get the environment state", response_model=BooleanResponse)
def get_env_state(env_state_meta_data: EnvStateInit):
    """
    Get the current or next state of the environment.
    :param env_state_meta_data: the metadata params for fetching the environment and its state.
    :return: the current or next state of the environment.
    """
    pomdp_id = env_state_meta_data.pomdp_id
    state_type = env_state_meta_data.type
    state_id = env_state_meta_data.state_id
    if state_type == "next":
        problem = problems[pomdp_id]
        next_state = problem.env.get_next_state(last_action[pomdp_id])
        # cache the computed state for future use
        last_env_next_state[pomdp_id] = next_state
        next_env_state = next_state.object_states[state_id]
    elif state_type == "last":
        next_env_state = last_env_next_state[pomdp_id].object_states[state_id]
    else:
        next_env_state = problems[pomdp_id].env.state.object_states[state_id]

    env_state_graph: Graph = next_env_state.graph
    env_state_attribute_node = next_env_state.attributes_node
    env_state_graph.add((env_state_attribute_node, RDF.type, _Environment))
    env_state_graph.add((_Environment, _State, next_env_state.state_subject))
    env_state = next_env_state.graph.serialize(format='turtle')
    return BooleanResponse(data=env_state, message="Next state is fetched", success=True)


@env_ns.post("/apply-transition", summary="Apply State Transition", response_model=BooleanResponse)
def set_next_state(env_state_meta_data: EnvStateInit):
    """
    Set the current or next state of the environment.
    :param env_state_meta_data: the metadata params for fetching the environment and its state.
    :return: the current or next state of the environment.
    """
    pomdp_id = env_state_meta_data.pomdp_id
    state_id = env_state_meta_data.state_id
    state_data = env_state_meta_data.data
    temp_graph = Graph()
    temp_graph.parse(data=state_data)
    _state = to_graph.convert_to_state(temp_graph)
    problem = problems[pomdp_id]
    env: AjanEnvironment = problem.env
    next_state = last_env_next_state[pomdp_id]
    next_state.object_states[state_id] = _state
    if env_state_meta_data.apply:  # check whether it needs to be applied or not
        env.apply_transition(next_state)
    else:
        last_env_next_state[pomdp_id] = next_state
    return BooleanResponse(success=True, message="Next state is set")
