from fastapi import APIRouter
from ..VariableModels.ResponseModels import CreateResponse
from ..VariableModels.State import Attributes
from ..ajan_pomdp_planning.oopomdp.domain.observation import AjanObservation
from .pomdp import observations

obs_ns = APIRouter(prefix="/AJAN/pomdp/observation")


@obs_ns.post("/create", summary="Create the Observation", response_model=CreateResponse)
def create_obs(pomdp_id, params: Attributes):
    pass
