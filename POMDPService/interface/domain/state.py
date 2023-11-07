from fastapi import APIRouter, HTTPException
from POMDPService.VariableModels.ResponseModels import CreateResponse
from POMDPService.VariableModels.State import StateInit, POMDPInit
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanAgent, AjanEnvObjectState, AjanOOState
from POMDPService.interface.pomdp import states, init_states

state_ns = APIRouter(prefix="/AJAN/pomdp/state")


@state_ns.post("/create/agent", summary="Create an Agent state",
               description="Create an agent state with given name and attributes", response_model=CreateResponse)
def create(state: StateInit):
    agent = get_state(state)
    print("Initialized:", agent)
    return {"name": str(agent), "message": "Agent Creation Successful", "id": id(agent)}


def get_state(state, pomdp_id=None):
    if pomdp_id is None:
        pomdp_id = state.pomdp_id
    if state.state.params is None:
        attributes = None
        to_print = None
    else:
        attributes = state.state.params.attributes
        to_print = state.state.params.to_print
    if state.state.type.lower() == "agent":
        agent = AjanAgent(state.state.id, attributes=attributes, to_print=to_print)
    elif state.state.type.lower() == "env":
        agent = AjanEnvObjectState(state.state.name, state.state.id, attributes=attributes,
                                   to_print=to_print)
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
    return {"name": str(env_obj), "message": "Environment Object Created successfully", "id": id(env_obj)}


@state_ns.post("/initialize", summary="Initialize Object States",
               description="Initializes the object oriented POMDP States from the previously created states",
               response_model=CreateResponse)
def initialize(pomdp: POMDPInit):
    if states.keys().__contains__(pomdp.pomdp_id):
        _states = states[pomdp.pomdp_id]
        init_states[pomdp.pomdp_id] = AjanOOState(_states)
        return {"name": str(states[pomdp.pomdp_id]), "message": "States Initialized successfully",
                "id": id(states[pomdp.pomdp_id])}
    else:
        raise HTTPException(status_code=406, detail="POMDP ID is invalid. "
                                                    "Initialize POMDP for ID:%s and create states before proceeding "
                                                    "with Object Oriented POMDP state initialization")
