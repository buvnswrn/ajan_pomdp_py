import pomdp_py
from rdflib import Graph

from POMDPService.ajan_pomdp_planning.oopomdp.agent.agent import AjanAgent


class AjanOOPOMDP(pomdp_py.POMDP):
    def __init__(self, data, name, agent, env):
        self.graph = Graph()
        self.graph.parse(data=data)
        super().__init__(agent, env, name)


# def update_belief(agent: AjanAgent, real_action, real_observation, planner, obj_id=None, state_id=None):
def update_belief(agent: AjanAgent, real_action, real_observation, planner, obj_id=None, state_id=None):
    planner.update(agent, real_action, real_observation)
    if not isinstance(planner, pomdp_py.POMCP):
        if obj_id is not None:  # Change: obj_id is None
            # TODO: check here for correct belief update. The obj_id doesn't match. We need the right belief object.
            belief_obj = agent.cur_belief.object_beliefs[obj_id][state_id]
            new_belief = pomdp_py.update_histogram_belief(belief_obj,
                                                          real_action,
                                                          real_observation,
                                                          agent.observation_model[obj_id],
                                                          agent.transition_model[obj_id],
                                                          static_transition=True)
            agent.cur_belief.set_object_belief(obj_id, new_belief)
