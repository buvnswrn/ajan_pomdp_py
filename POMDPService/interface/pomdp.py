from fastapi import APIRouter

from ..VariableModels.State import POMDPInit

pomdp_ns = APIRouter(prefix="/AJAN/pomdp")

states = {}
actions = {}
init_beliefs = {}


@pomdp_ns.post("/initialize")
def initialize(pomdp: POMDPInit):
    states[pomdp.pomdp_id] = {}
    actions[pomdp.pomdp_id] = []
    init_beliefs[pomdp.pomdp_id] = {}