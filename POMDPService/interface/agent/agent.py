import ctypes

from fastapi import APIRouter
from POMDPService.VariableModels.ResponseModels import CreateResponse, BooleanResponse
from POMDPService.VariableModels.State import AgentInit
from POMDPService.ajan_pomdp_planning.oopomdp.agent.agent import AjanAgent
from POMDPService.ajan_pomdp_planning.oopomdp.problem import AjanOOPOMDP
from POMDPService.interface.pomdp import init_beliefs, models, agents, problems, last_action, last_observation

agent_ns = APIRouter(prefix="/AJAN/pomdp/agent")


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


@agent_ns.post("/clear-history", summary="Clears the agent's history", response_model=BooleanResponse)
def clear_history(pomdp_id):
    problems[pomdp_id].agent.clear_history()
    return BooleanResponse(success=True, message="History cleared successfully")


@agent_ns.post("/update-history", summary="Updates the agent's history", response_model=BooleanResponse)
def update_history(pomdp_id):
    problem: AjanOOPOMDP = problems[pomdp_id]
    problem.agent.update_history(last_action[pomdp_id], last_observation[pomdp_id])
    return BooleanResponse(success=True, message="Agent history updated successfully")
