from pydantic import BaseModel
from typing import Dict, Optional, Tuple, List


class State(BaseModel):
    id: int
    name: str = None
    attributes: dict = None
    to_print: list = None
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
