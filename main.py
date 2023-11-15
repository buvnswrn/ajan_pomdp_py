from fastapi import FastAPI

from POMDPService.interface.agent.agent import agent_ns
from POMDPService.interface.domain.observation import obs_ns
from POMDPService.interface.models.model import model_ns
from POMDPService.interface.models.observation_model import obs_model_ns
from POMDPService.interface.models.policy_model import policy_model_ns
from POMDPService.interface.models.reward_model import reward_model_ns
from POMDPService.interface.models.transition_model import transition_model_ns
from POMDPService.interface.planner.planner import planner_ns
from POMDPService.interface.pomdp import pomdp_ns
from POMDPService.interface.domain.state import state_ns
from POMDPService.interface.domain.action import action_ns
from POMDPService.interface.agent.belief import belief_ns
from POMDPService.interface.env.env import env_ns
from POMDPService.interface.problem import problem_ns

app = FastAPI(title="AJAN-POMDP", description="API for planning with pomdp-py through AJAN")
app.include_router(pomdp_ns, tags=['POMDP Service'])
app.include_router(state_ns, tags=['State'])
app.include_router(action_ns, tags=['Action'])
app.include_router(obs_ns, tags=['Observation'])
app.include_router(obs_model_ns, tags=['Models'])
app.include_router(model_ns, tags=['Models'])
app.include_router(transition_model_ns, tags=['Models'])
app.include_router(reward_model_ns, tags=['Models'])
app.include_router(policy_model_ns, tags=['Models'])
app.include_router(belief_ns, tags=['Belief'])
app.include_router(agent_ns, tags=['Agent'])
app.include_router(env_ns, tags=['Environment'])
app.include_router(problem_ns, tags=['Problem'])
app.include_router(planner_ns, tags=['Planner'])

app1 = FastAPI(title="AJAN-POMDP-State", description="API for planning with pomdp-py through AJAN1")
app1.include_router(pomdp_ns, tags=['POMDP Service1'])


@app.on_event("startup")
def init():
    pass


@app.on_event("shutdown")
def shutdown():
    pass