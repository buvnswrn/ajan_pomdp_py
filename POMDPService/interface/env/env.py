import ctypes

from fastapi import APIRouter
from POMDPService.VariableModels.ResponseModels import CreateResponse
from POMDPService.VariableModels.State import EnvInit, POMDPInit
from POMDPService.ajan_pomdp_planning.oopomdp.env.env import AjanEnvironment
from POMDPService.interface.pomdp import envs, init_states, models, problems, last_action, last_observation

env_ns = APIRouter(prefix="/AJAN/pomdp/env")


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
    data =env_init.data
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
