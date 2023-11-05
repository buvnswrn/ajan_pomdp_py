import ctypes

from fastapi import APIRouter
from POMDPService.VariableModels.ResponseModels import CreateResponse
from POMDPService.VariableModels.State import AgentInit
from POMDPService.ajan_pomdp_planning.oopomdp.agent.agent import AjanAgent

agent_ns = APIRouter(prefix="/AJAN/pomdp/agent")


@agent_ns.post("/create", summary="Create the agent", response_model=CreateResponse)
def create_agent(agent_init: AgentInit):
    init_belief = ctypes.cast(agent_init.init_belief, ctypes.py_object).value
    policy_model = ctypes.cast(agent_init.policy_model, ctypes.py_object).value
    transition_model = ctypes.cast(agent_init.transition_model, ctypes.py_object).value
    observation_model = ctypes.cast(agent_init.observation_model, ctypes.py_object).value
    reward_model = ctypes.cast(agent_init.reward_model, ctypes.py_object).value
    agent = AjanAgent(agent_init.data, init_belief, policy_model, transition_model, observation_model, reward_model)
    return CreateResponse(name=str(agent), message="Created the agent", id=id(agent))


@agent_ns.post("/create-from-cache", summary="Create the agent", response_model=CreateResponse)
def create_agent(pomdp_id: int):
    pass
