import random

import pomdp_py

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction


class PolicyModel(pomdp_py.RolloutPolicy):

    def sample(self, state):
        return random.sample(self.get_all_actions(), 1)[0]

    def rollout(self, state, tuple_history=None):
        return self.sample(state)

    def get_all_actions(self, state=None, history=None, *args):
        return [AjanAction('move', {"motion": "left"}),
                AjanAction('move', {"motion": "right"}),
                AjanAction('perceive')]
