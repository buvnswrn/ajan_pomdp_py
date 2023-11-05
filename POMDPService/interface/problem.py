import ctypes

from fastapi import APIRouter
from POMDPService.VariableModels.ResponseModels import CreateResponse
from POMDPService.VariableModels.State import EnvInit, POMDPProblemInit
from POMDPService.ajan_pomdp_planning.oopomdp.env.env import AjanEnvironment
from POMDPService.ajan_pomdp_planning.oopomdp.problem import AjanOOPOMDP

problem_ns = APIRouter(prefix="/AJAN/pomdp/problem")


@problem_ns.post("/create", summary="Create a POMDP Problem", response_model=CreateResponse)
def create_pomdp_problem(env_init: POMDPProblemInit):
    init_state = ctypes.cast(env_init.init_state, ctypes.py_object).value
    agent = ctypes.cast(env_init.agent, ctypes.py_object).value
    env = ctypes.cast(env_init.env, ctypes.py_object).value
    problem = AjanOOPOMDP(env_init.data, env_init.name, init_state, agent, env)
    return CreateResponse(name=str(problem), message="Created the Environment", id=id(problem))
