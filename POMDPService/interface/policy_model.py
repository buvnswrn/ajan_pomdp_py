from fastapi import APIRouter
from ..VariableModels.ResponseModels import CreateResponse
from ..VariableModels.State import Attributes, ProbabilisticModelsData
from ..ajan_pomdp_planning.oopomdp.models.policy_model import AjanPolicyModel

policy_model_ns = APIRouter(prefix="/AJAN/pomdp/policy_model")


@policy_model_ns.post("/create/init-model", summary="Create the policy model", response_model=CreateResponse)
def init_model(model_data: ProbabilisticModelsData):
    model = AjanPolicyModel(model_data.data,
                            None,
                            model_data.probability_query,
                            model_data.sample_query,
                            model_data.argmax_query)
    print(model)
    return CreateResponse(name="Created", message="Policy Model Created")
