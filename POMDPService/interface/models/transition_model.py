from fastapi import APIRouter
from POMDPService.VariableModels.ResponseModels import CreateResponse
from POMDPService.VariableModels.State import Attributes, ProbabilisticModelsData
from POMDPService.ajan_pomdp_planning.oopomdp.models.transition_model import AjanTransitionModel
from POMDPService.interface.pomdp import models

transition_model_ns = APIRouter(prefix="/AJAN/pomdp/transition_model")


@transition_model_ns.post("/create/init-model", summary="Create the transition model", response_model=CreateResponse)
def init_model(model_data: ProbabilisticModelsData):
    model = AjanTransitionModel(model_data.data, None,
                                model_data.probability_query,
                                model_data.sample_query,
                                model_data.argmax_query)
    models[model_data.pomdp_id][model_data.type]['transition'][ord(model_data.associated_object_name[0])] = model
    print(model)
    return CreateResponse(name="Created", message="Transition Model Created", id=id(model))
