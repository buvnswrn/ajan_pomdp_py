from fastapi import APIRouter, HTTPException
from POMDPService.interface.pomdp import actions
from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.VariableModels.ResponseModels import CreateResponse

action_ns = APIRouter(prefix="/AJAN/pomdp/action")


@action_ns.post("/create/action", summary="Create an Action", response_model=CreateResponse)
def create(pomdp_id: int, name: str, attributes: dict):
    action = AjanAction(name, attributes)
    if not actions[pomdp_id].__contains__(name):
        actions[pomdp_id].append(action)
    else:
        raise HTTPException(status_code=406, detail="Action is already created")
    print("Created:", action.__repr__())
    return {"name": action.__repr__(), "message": "Action Successfully created", "id": id(action)}
