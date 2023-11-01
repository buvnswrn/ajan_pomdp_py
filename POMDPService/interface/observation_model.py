from fastapi import APIRouter
from ..VariableModels.ResponseModels import CreateResponse
from ..VariableModels.State import Attributes, ProbabilisticModelsData
from ..ajan_pomdp_planning.oopomdp.models.observation_model import AjanObservationModel

obs_model_ns = APIRouter(prefix="/AJAN/pomdp/observation_model")


@obs_model_ns.post("/create/init-model", summary="Create the observation model", response_model=CreateResponse)
def init_model(model_data: ProbabilisticModelsData):
    model = AjanObservationModel(model_data.data, None, model_data.probability_query, model_data.sample_query, model_data.argmax_query)
    print(model)
    return CreateResponse(name="Created", message="Observation Model Created")