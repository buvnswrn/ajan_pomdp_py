from fastapi import APIRouter, HTTPException
from .VariableModels.State import StateInit, POMDPInit, BeliefInit, List, BeliefPrior
from .VariableModels.ResponseModels import CreateResponse
from .ajan_pomdp_planning.oopomdp.agent.belief import initialize_belief
from .ajan_pomdp_planning.oopomdp.domain.state import AjanAgent, AjanEnvObjectState, AjanOOState
from .ajan_pomdp_planning.oopomdp.domain.action import AjanAction

pomdp_ns = APIRouter(prefix="/AJAN/pomdp")
state_ns = APIRouter(prefix="/AJAN/pomdp/state")
action_ns = APIRouter(prefix="/AJAN/pomdp/action")
belief_ns = APIRouter(prefix="/AJAN/pomdp/belief")

states = {}
actions = {}
init_beliefs = {}


@pomdp_ns.post("/initialize")
def initialize(pomdp: POMDPInit):
    states[pomdp.pomdp_id] = {}
    actions[pomdp.pomdp_id] = []
    init_beliefs[pomdp.pomdp_id] = {}


@state_ns.post("/create/agent", summary="Create an Agent state",
               description="Create an agent state with given name and attributes", response_model=CreateResponse)
def create(state: StateInit):
    agent = get_state(state)
    print("Initialized:", agent)
    return {"name": str(agent), "message": "Agent Creation Successful"}


def get_state(state, pomdp_id = None):
    if pomdp_id is None:
        pomdp_id = state.pomdp_id
    if state.state.type.lower() == "agent":
        agent = AjanAgent(state.state.id, attributes=state.state.attributes, to_print=state.state.to_print)
    elif state.state.type.lower() == "env":
        agent = AjanEnvObjectState(state.state.name, state.state.id, attributes=state.state.attributes,
                                   to_print=state.state.to_print)
    else:
        agent = None
    if agent is not None:
        if not states.keys().__contains__(state.state.id):
            states[pomdp_id][state.state.id] = agent
        else:
            raise HTTPException(status_code=406, detail="State ID is already used")
    else:
        raise HTTPException(status_code=406, detail="State cannot be created, Possible types are 'agent', 'env'")
    return agent


@state_ns.post("/create/object", summary="Create a Object state",
               description="Create a Environment object state with given name and attributes",
               response_model=CreateResponse)
def create(state: StateInit):
    env_obj = AjanEnvObjectState(state.name, state.id, attributes=state.attributes, to_print=state.to_print)
    if not states[state.pomdp_id].keys().__contains__(state.id):
        states[state.pomdp_id][state.id] = env_obj
    else:
        raise HTTPException(status_code=406, detail="State ID is already used")
    print("Initialized:", env_obj)
    return {"name": str(env_obj), "message": "Environment Object Created successfully"}


@state_ns.post("/initialize", summary="Initialize Object States",
               description="Initializes the object oriented POMDP States from the previously created states",
               response_model=CreateResponse)
def initialize(pomdp: POMDPInit):
    if states.keys().__contains__(pomdp.pomdp_id):
        _states = states[pomdp.pomdp_id]
        states[pomdp.pomdp_id] = AjanOOState(_states)
        return {"name": str(states[pomdp.pomdp_id]), "message": "States Initialized successfully"}
    else:
        raise HTTPException(status_code=406, detail="POMDP ID is invalid. "
                                                    "Initialize POMDP for ID:%s and create states before proceeding "
                                                    "with Object Oriented POMDP state initialization")


@action_ns.post("/create/action", summary="Create an Action", response_model=CreateResponse)
def create(pomdp_id: int, name: str, attributes: dict):
    action = AjanAction(name, attributes)
    if not actions[pomdp_id].__contains__(name):
        actions[pomdp_id].append(action)
    else:
        raise HTTPException(status_code=406, detail="Action is already created")
    print("Created:", action.__repr__())
    return {"name": action.__repr__(), "message": "Action Successfully created"}


@belief_ns.post("/create/init-belief", summary="Create the initial belief", response_model=CreateResponse)
def init_belief(belief_dict: BeliefInit):
    belief_states = convert_to_states(belief_dict.pomdp_id, belief_dict.belief_dict)
    belief = initialize_belief(belief_dict.pomdp_id, belief_states, belief_dict.representation)
    init_beliefs[belief_dict.pomdp_id] = belief
    return {"name": str(belief), "message": "Initial Belief created successfully"}


def convert_to_states(p_id: int, belief_dict: List[BeliefPrior]):
    init_belief_dict = {}
    state_prob = {}
    for prior in belief_dict:
        agent_state = get_state(prior, p_id)
        if not init_belief_dict.keys().__contains__(p_id):
            init_belief_dict[p_id] = {}
        if not init_belief_dict[p_id].keys().__contains__(agent_state.objclass):
            init_belief_dict[p_id][agent_state.objclass] = {}
        state_prob[agent_state] = prior.probability
        init_belief_dict[p_id][agent_state.objclass].update(state_prob)
    return init_belief_dict  # { 0: {'drone': {state1:prob} } }
