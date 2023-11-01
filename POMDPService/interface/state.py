from fastapi import APIRouter, HTTPException
from ..VariableModels.ResponseModels import CreateResponse
from ..VariableModels.State import StateInit, POMDPInit
from ..ajan_pomdp_planning.oopomdp.domain.state import AjanAgent, AjanEnvObjectState, AjanOOState
from .pomdp import states

state_ns = APIRouter(prefix="/AJAN/pomdp/state")


@state_ns.post("/create/agent", summary="Create an Agent state",
               description="Create an agent state with given name and attributes", response_model=CreateResponse)
def create(state: StateInit):
    agent = get_state(state)
    print("Initialized:", agent)
    return {"name": str(agent), "message": "Agent Creation Successful"}


def get_state(state, pomdp_id=None):
    if pomdp_id is None:
        pomdp_id = state.pomdp_id
    if state.state.type.lower() == "agent":
        agent = AjanAgent(state.state.id, attributes=state.state.params.attributes, to_print=state.state.params.to_print)
    elif state.state.type.lower() == "env":
        agent = AjanEnvObjectState(state.state.name, state.state.id, attributes=state.state.params.attributes,
                                   to_print=state.state.params.to_print)
    else:
        agent = None
    if agent is not None:
        if not states[pomdp_id].keys().__contains__(state.state.id):
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
