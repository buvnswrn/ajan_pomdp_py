from fastapi import APIRouter
from POMDPService.VariableModels.State import BeliefInit, List, BeliefPrior, BeliefInitKB
from POMDPService.VariableModels.ResponseModels import CreateResponse
from POMDPService.ajan_pomdp_planning.oopomdp.agent.belief import initialize_belief
from POMDPService.interface.pomdp import init_beliefs
from POMDPService.interface.domain.state import get_state

from rdflib import Graph

belief_ns = APIRouter(prefix="/AJAN/pomdp/belief")


@belief_ns.post("/create/init-belief", summary="Create the initial belief", response_model=CreateResponse)
def init_belief(belief_dict: BeliefInit):
    belief_states = convert_to_states(belief_dict.pomdp_id, belief_dict.belief_dict)
    belief = initialize_belief(belief_dict.pomdp_id,belief_dict.agent_id, belief_states, belief_dict.representation)
    init_beliefs[belief_dict.pomdp_id] = belief
    return {"name": str(belief), "message": "Initial Belief created successfully", "id": id(belief)}


@belief_ns.post("/create/init-belief-from-knowledge-base",
                summary="Create the initial belief from agent's knowledge base", response_model=CreateResponse)
def init_belief(belief_data: BeliefInitKB):
    g = Graph()
    g.parse(belief_data.repo_url)
    return {"name": "success", "message": "Initial Belief created", "id": id(g)}


def convert_to_states(p_id: int, belief_dict: List[BeliefPrior]):
    init_belief_dict = {}
    state_prob = {}
    for prior in belief_dict:
        agent_state = get_state(prior, p_id, False)
        if not init_belief_dict.keys().__contains__(p_id):
            init_belief_dict[p_id] = {}
            state_prob = {}
        key: str = agent_state.objclass
        key = key.split("_")[1]
        if not init_belief_dict[p_id].keys().__contains__(key):
            init_belief_dict[p_id][key] = {}
            state_prob = {}
        state_prob[agent_state] = prior.probability
        init_belief_dict[p_id][key].update(state_prob)
    return init_belief_dict  # { 0: {'drone': {state1:prob} } }
