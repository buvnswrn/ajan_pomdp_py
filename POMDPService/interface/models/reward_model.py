from fastapi import APIRouter
from POMDPService.VariableModels.ResponseModels import CreateResponse
from POMDPService.VariableModels.State import Attributes, ProbabilisticModelsData
from POMDPService.ajan_pomdp_planning.oopomdp.models.reward_model import AjanRewardModel
from POMDPService.interface.pomdp import models

reward_model_ns = APIRouter(prefix="/AJAN/pomdp/reward_model")


@reward_model_ns.post("/create/init-model", summary="Create the reward model", response_model=CreateResponse)
def init_model(model_data: ProbabilisticModelsData):
    model = AjanRewardModel(model_data.data,
                            None,
                            model_data.probability_query,
                            model_data.sample_query,
                            model_data.argmax_query)
    models[model_data.pomdp_id][model_data.type]['reward'] = model
    print(model)
    return CreateResponse(name="Created", message="Reward Model Created", id=id(model))
