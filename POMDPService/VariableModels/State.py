from pydantic import BaseModel
from typing import Dict, Optional, Tuple, List


class Attributes(BaseModel):
    attributes: dict = None
    attributes_data: str = None
    to_print: list = None
    to_print_data: str = None


class ProbabilisticModelsData(BaseModel):
    pomdp_id: int
    type: str = None
    params: Attributes = None
    data: str
    associated_object_name: str = None
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


class EnvStateInit(BaseModel):
    pomdp_id: int
    state_id: int
    type: str = None
    data: str = None  # for update


class ActionInit(BaseModel):
    pomdp_id: int
    action_name: str
    attributes: dict = None
    attributes_data: str = None
    to_print: list = None
    to_print_data: str = None


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


class AgentInit(BaseModel):
    pomdp_id: int
    data: str
    state_id: int = None
    state_name: str = None
    init_belief: int = None
    policy_model: int = None
    transition_model: int = None
    observation_model: int = None
    reward_model: int = None


class EnvInit(BaseModel):
    pomdp_id: int
    data: str
    init_state: int = None
    transition_model: int = None
    reward_model: int = None


class POMDPProblemInit(BaseModel):
    pomdp_id: int
    name: str
    data: str
    agent: int = None
    env: int = None


class PlannerInit(BaseModel):
    pomdp_id: int
    name: str
    policy_model: int = None
    max_depth: int = 10
    planning_time: float = -1.
    num_sims: int = -1
    exploration_const: int = 1000
    max_steps: int = 500
    discount_factor: float = 0.95
    pbar_update_interval: int = 500


class BeliefInitKB(BaseModel):
    pomdp_id: int
    repo_url: str
