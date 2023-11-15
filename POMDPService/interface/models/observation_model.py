from fastapi import APIRouter

from POMDPService.VariableModels.ResponseModels import CreateResponse
from POMDPService.VariableModels.State import ProbabilisticModelsData
from POMDPService.ajan_pomdp_planning.oopomdp.models.observation_model import AjanObservationModel
from POMDPService.interface.pomdp import models

obs_model_ns = APIRouter(prefix="/AJAN/pomdp/observation_model")


@obs_model_ns.post("/create/init-model", summary="Create the observation model", response_model=CreateResponse)
def init_model(model_data: ProbabilisticModelsData):
    model = AjanObservationModel(model_data.data, None, model_data.probability_query, model_data.sample_query,
                                 model_data.argmax_query)
    models[model_data.pomdp_id]['agent']['observation'][ord(model_data.associated_object_name[0])] = model
    return CreateResponse(name="Created", message="Observation Model Created", id=id(model))
