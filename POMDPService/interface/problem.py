import ctypes

from fastapi import APIRouter

from POMDPService.VariableModels.ResponseModels import CreateResponse
from POMDPService.VariableModels.State import POMDPProblemInit
from POMDPService.ajan_pomdp_planning.oopomdp.problem import AjanOOPOMDP
from POMDPService.interface.pomdp import problems, agents, envs

problem_ns = APIRouter(prefix="/AJAN/pomdp/problem")


@problem_ns.post("/create-from-pointers", summary="Create a POMDP Problem", response_model=CreateResponse)
def create_pomdp_problem(prob_init: POMDPProblemInit):
    agent = ctypes.cast(prob_init.agent, ctypes.py_object).value
    env = ctypes.cast(prob_init.env, ctypes.py_object).value
    problem = AjanOOPOMDP(prob_init.data, prob_init.name, agent, env)
    problems[prob_init.pomdp_id] = problem
    return CreateResponse(name=str(problem), message="Created the POMDP Problem", id=id(problem))


@problem_ns.post("/create", summary="Create a POMDP Problem", response_model=CreateResponse)
def create_pomdp_problem(prob_init: POMDPProblemInit):
    agent = agents[prob_init.pomdp_id]
    env = envs[prob_init.pomdp_id]
    problem = AjanOOPOMDP(prob_init.data, prob_init.name, agent, env)
    problems[prob_init.pomdp_id] = problem
    return CreateResponse(name=str(problem), message="Created the POMDP Problem", id=id(problem))
