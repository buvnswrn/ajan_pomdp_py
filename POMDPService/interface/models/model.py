from fastapi import APIRouter

from POMDPService.VariableModels.ResponseModels import CreateResponse
from POMDPService.VariableModels.State import POMDPInit
from POMDPService.ajan_pomdp_planning.oopomdp.models.observation_model import AjanOOObservationModel
from POMDPService.ajan_pomdp_planning.oopomdp.models.transition_model import AjanOOTransitionModel
from POMDPService.interface.pomdp import models

model_ns = APIRouter(prefix="/AJAN/pomdp/oo-model")


@model_ns.post("/create", summary="Create the Object oriented Models", response_model=CreateResponse)
def init_model(pomdp: POMDPInit):
    # Agent models
    oo_observation_model = AjanOOObservationModel(models[pomdp.pomdp_id]['agent']['observation'])
    models[pomdp.pomdp_id]['agent']['observation'] = oo_observation_model

    # should be id:transition_models
    agent_oo_transition_model = AjanOOTransitionModel(models[pomdp.pomdp_id]['agent']['transition'])
    models[pomdp.pomdp_id]['agent']['transition'] = agent_oo_transition_model

    # Environment models

    env_oo_transition_model = AjanOOTransitionModel(models[pomdp.pomdp_id]['env']['transition'])

    models[pomdp.pomdp_id]['env']['transition'] = env_oo_transition_model

    return CreateResponse(name="Created", message="Observation Model Created")
