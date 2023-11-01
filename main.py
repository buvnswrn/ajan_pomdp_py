from fastapi import FastAPI
from POMDPService.interface.pomdp import pomdp_ns
from POMDPService.interface.state import state_ns
from POMDPService.interface.action import action_ns
from POMDPService.interface.belief import belief_ns

app = FastAPI(title="AJAN-POMDP", description="API for planning with pomdp-py through AJAN")
app.include_router(pomdp_ns, tags=['POMDP Service'])
app.include_router(state_ns, tags=['State'])
app.include_router(action_ns, tags=['Action'])
app.include_router(belief_ns, tags=['Belief'])

app1 = FastAPI(title="AJAN-POMDP-State", description="API for planning with pomdp-py through AJAN1")
app1.include_router(pomdp_ns, tags=['POMDP Service1'])


@app.on_event("startup")
def init():
    pass


@app.on_event("shutdown")
def shutdown():
    pass