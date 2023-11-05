import ctypes

from fastapi import APIRouter
from POMDPService.VariableModels.ResponseModels import CreateResponse
from POMDPService.VariableModels.State import EnvInit
from POMDPService.ajan_pomdp_planning.oopomdp.env.env import AjanEnvironment

env_ns = APIRouter(prefix="/AJAN/pomdp/env")


@env_ns.post("/create", summary="Create an Environment", response_model=CreateResponse)
def create_env(env_init: EnvInit):
    init_state = ctypes.cast(env_init.init_state, ctypes.py_object).value
    transition_model = ctypes.cast(env_init.transition_model, ctypes.py_object).value
    reward_model = ctypes.cast(env_init.reward_model, ctypes.py_object).value
    env = AjanEnvironment(env_init.data, init_state, transition_model, reward_model)
    return CreateResponse(name=str(env), message="Created the Environment", id=id(env))
