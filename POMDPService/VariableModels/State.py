from pydantic import BaseModel
from typing import Dict, Optional, Tuple, List


class Attributes(BaseModel):
    attributes: dict = None
    to_print: list = None


class ProbabilisticModelsData(BaseModel):
    params: Attributes = None
    data: str
    probability_query: str = None
    sample_query: str = None
    argmax_query: str = None
    rollout_query: str = None
    get_all_action_query: str = None


class State(BaseModel):
    id: int
    name: str = None
    params: Attributes = None
    type: str = None


class StateInit(BaseModel):
    pomdp_id: int
    state: State


class POMDPInit(BaseModel):
    pomdp_id: int


di = {
    "prior": {
        0: {
            "name": "person",
            "attributes": {
                "pose": (0, 1),
                "gesture": True
            },
            "type": "person",
            "to_print": ["gesture"],
            "probability": 0
        },
        100: {
            "name": "drone",
            "attributes": {
                "pose": (0, 1),
                "gesture": True
            },
            "type": "drone",
            "to_print": ["gesture"],
            "probability": 0
        }
    }
}


# or use some id to get the object stored somewhere


class BeliefPrior(BaseModel):
    state: State
    probability: float


class BeliefInit(BaseModel):
    pomdp_id: int
    representation: str
    belief_dict: List[BeliefPrior]  # pomdp_id


class BeliefInitKB(BaseModel):
    pomdp_id: int
    repo_url: str
