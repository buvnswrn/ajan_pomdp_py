import random

import pomdp_py

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction


class PolicyModel(pomdp_py.RolloutPolicy):

    def sample(self, state):
        if (state.object_states[100].attributes["gesture_found"]
                and state.object_states[112].attributes["gesture"] is not None):
            return random.sample([AjanAction('move', {"motion": "left"}),
                                  AjanAction('move', {"motion": "right"})], 1)[0]
        else:
            return AjanAction('perceive')

    def rollout(self, state, tuple_history=None):
        # if (state.object_states[100].attributes["gesture_found"]
        #         and state.object_states[112].attributes["gesture"] is not None):
        #     return AjanAction('move', {"motion": state.object_states[112].attributes["gesture"]})
        # else:
        #     return AjanAction('perceive')
        return self.sample(state)

    def get_all_actions(self, state=None, history=None, *args):
        if (state.object_states[100].attributes["gesture_found"]
                and state.object_states[112].attributes["gesture"] is not None):
            return [AjanAction('move', {"motion": "left"}), AjanAction('move', {"motion": "right"})]
        else:
            return [AjanAction("perceive")]
