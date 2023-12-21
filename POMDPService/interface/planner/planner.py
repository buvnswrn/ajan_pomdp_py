import ctypes
import time

import pomdp_py
from fastapi import APIRouter

from POMDPService.VariableModels.ResponseModels import CreateResponse, CreateActionResponse
from POMDPService.VariableModels.State import PlannerInit, POMDPInit
from POMDPService.interface.pomdp import planners, problems, last_action

planner_ns = APIRouter(prefix="/AJAN/pomdp/planner")


@planner_ns.post("/create", summary="Create an instance of the planner", response_model=CreateResponse)
def create_planner(planner_init: PlannerInit):
    planner = None
    if planner_init.policy_model is not None:
        policy_model = ctypes.cast(planner_init.policy_model, ctypes.py_object).value
    else:
        policy_model = problems[planner_init.pomdp_id].agent.policy_model
    if planner_init.name == "POMCP":
        planner = pomdp_py.POMCP(max_depth=planner_init.max_depth,
                                 discount_factor=planner_init.discount_factor,
                                 num_sims=planner_init.num_sims,
                                 exploration_const=planner_init.exploration_const,
                                 rollout_policy=policy_model,
                                 show_progress=True,
                                 pbar_update_interval=planner_init.pbar_update_interval)
    elif planner_init.name == "POUCT":
        planner = pomdp_py.POUCT(max_depth=planner_init.max_depth,
                                 discount_factor=planner_init.discount_factor,
                                 planning_time=planner_init.planning_time,
                                 num_sims=planner_init.num_sims,
                                 exploration_const=planner_init.exploration_const,
                                 rollout_policy=policy_model)
    if planner is not None:
        planners[planner_init.pomdp_id] = planner
        return CreateResponse(name=str(planner), message="Created the planner", id=id(planner))
    else:
        return CreateResponse(name="Invalid name:%s. Possible values are: POMCP, POUCT" % planner_init.name,
                              message="Cannot Create the planner")


@planner_ns.post("/get-action", summary="Get the planned action", description="Get the action computed by the planner",
                 response_model=CreateActionResponse)
def get_action(pomdp: POMDPInit):
    pomdp_id = pomdp.pomdp_id
    start_time = time.time()
    action = planners[pomdp_id].plan(problems[pomdp_id].agent)
    last_action[pomdp_id] = action
    print(str(action) + " in " + str(time.time() - start_time) + " seconds")
    if action.attributes is None:
        return CreateActionResponse(name=str(action), message="Fetched the action", id=id(action))
    response = CreateActionResponse(name=str(action), message="Fetched the action", id=id(action),
                                    attributes=action.attributes, data=action.graph.serialize(format='turtle'))
    return response

