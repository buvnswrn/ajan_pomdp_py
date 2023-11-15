from fastapi import APIRouter
from POMDPService.VariableModels.ResponseModels import CreateResponse
from POMDPService.VariableModels.State import Attributes, ProbabilisticModelsData
from POMDPService.ajan_pomdp_planning.oopomdp.models.policy_model import AjanPolicyModel
from POMDPService.interface.pomdp import models

policy_model_ns = APIRouter(prefix="/AJAN/pomdp/policy_model")


@policy_model_ns.post("/create/init-model", summary="Create the policy model", response_model=CreateResponse)
def init_model(model_data: ProbabilisticModelsData):
    model = AjanPolicyModel(model_data.data,
                            None,
                            model_data.sample_query,
                            model_data.rollout_query,
                            model_data.get_all_action_query)
    models[model_data.pomdp_id]['agent']['policy'] = model
    print(model)
    return CreateResponse(name="Created", message="Policy Model Created", id=id(model))
