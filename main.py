from fastapi import FastAPI
from POMDPService import POMDP_AJAN

app = FastAPI(title="AJAN-POMDP", description="API for planning with pomdp-py through AJAN")
app.include_router(POMDP_AJAN.pomdp_ns, tags=['POMDP Service'])
app.include_router(POMDP_AJAN.state_ns, tags=['State'])
app.include_router(POMDP_AJAN.action_ns, tags=['Action'])
app.include_router(POMDP_AJAN.belief_ns, tags=['Belief'])

app1 = FastAPI(title="AJAN-POMDP-State", description="API for planning with pomdp-py through AJAN1")
app1.include_router(POMDP_AJAN.pomdp_ns, tags=['POMDP Service1'])


@app.on_event("startup")
def init():
    pass


@app.on_event("shutdown")
def shutdown():
    pass