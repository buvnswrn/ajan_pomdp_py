from fastapi import APIRouter

from ..VariableModels.State import POMDPInit

pomdp_ns = APIRouter(prefix="/AJAN/pomdp")

states = {}
actions = {}
observations = {}
init_beliefs = {}
models = {}  # {0:{'agent':{'obs':Observation Model, 'trans':Transition Model},'env':{'trans':TransitionModel}}}
init_states = {}
problems = {}
planners = {}
agents = {}
envs = {}
last_action = {}
last_observation = {}


@pomdp_ns.post("/initialize")
def initialize(pomdp: POMDPInit):
    states[pomdp.pomdp_id] = {}
    actions[pomdp.pomdp_id] = []
    init_beliefs[pomdp.pomdp_id] = {}
    models[pomdp.pomdp_id] = {'agent': {}, 'env': {}}
