from fastapi import APIRouter
from POMDPService.VariableModels.ResponseModels import CreateResponse
from POMDPService.VariableModels.State import Attributes, POMDPInit
from POMDPService.ajan_pomdp_planning.oopomdp.domain.observation import AjanObservation
from POMDPService.interface.pomdp import observations

obs_ns = APIRouter(prefix="/AJAN/pomdp/observation")


@obs_ns.post("/create", summary="Create the Observation", response_model=CreateResponse)
def create_obs(pomdp_id: POMDPInit):
    return CreateResponse(name="Created Observation",
                          message="Created the observation")
