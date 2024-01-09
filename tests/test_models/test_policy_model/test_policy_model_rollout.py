import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanEnvObjectState, AjanOOState, AjanAgentState
from POMDPService.ajan_pomdp_planning.oopomdp.models.policy_model import AjanPolicyModel
from tests.test_models.alternate_models.python_policy_model import PolicyModel
from tests.test_models.helpers.policy_model_queries import SAMPLE_QUERY_POLICY, ROLLOUT_QUERY_POLICY, \
    GET_ALL_ACTIONS_QUERY, DATA_POLICY, SAMPLE_QUERY_POLICY1, ROLLOUT_QUERY_POLICY1, GET_ALL_ACTIONS_QUERY1


def print_Action(action):
    if action.attributes is not None:
        print(str(action) + " " + action.attributes["motion"])
    else:
        print(action)


class TestPolicyModelRollout(unittest.TestCase):
    policy_model = AjanPolicyModel(DATA_POLICY, None, SAMPLE_QUERY_POLICY1, ROLLOUT_QUERY_POLICY1, GET_ALL_ACTIONS_QUERY1)
    # policy_model = PolicyModel()

    def test_rollout_false_right(self):
        state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                     {"pose": (0, 0), "gesture": "right"},
                                                     ["pose", "gesture"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"pose": (0, 0), "gesture_found": False},
                                                 ["gesture_found", "pose"])})
        action = self.policy_model.rollout(state)
        print_Action(action)
        self.assertIn(action, [AjanAction("move", {"motion": "right"}),
                               AjanAction("move", {"motion": "left"}),
                               AjanAction("perceive")])  # should only be perceive

    def test_rollout_false_left(self):
        state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                     {"pose": (0, 0), "gesture": "left"},
                                                     ["pose", "gesture"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"pose": (0, 0), "gesture_found": False},
                                                 ["gesture_found", "pose"])})
        action = self.policy_model.rollout(state)
        print_Action(action)
        self.assertIn(action, [AjanAction("move", {"motion": "right"}),
                               AjanAction("move", {"motion": "left"}),
                               AjanAction("perceive")])  # should only be perceive

    def test_rollout_false_none(self):
        state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                     {"pose": (0, 0), "gesture": None},
                                                     ["pose", "gesture"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"pose": (0, 0), "gesture_found": False},
                                                 ["gesture_found", "pose"])})
        action = self.policy_model.rollout(state)
        print_Action(action)
        self.assertIn(action, [AjanAction("move", {"motion": "right"}),
                               AjanAction("move", {"motion": "left"}),
                               AjanAction("perceive")])  # should only be perceive

    def test_rollout_true_right(self):
        state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                     {"pose": (0, 0), "gesture": "right"},
                                                     ["pose", "gesture"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"pose": (0, 0), "gesture_found": True},
                                                 ["gesture_found", "pose"])})
        action = self.policy_model.rollout(state)
        print_Action(action)
        self.assertIn(action, [AjanAction("move", {"motion": "right"}),
                               AjanAction("move", {"motion": "left"}),
                               AjanAction("perceive")])  # should only be move right

    def test_rollout_true_left(self):
        state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                     {"pose": (0, 0), "gesture": "left"},
                                                     ["pose", "gesture"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"pose": (0, 0), "gesture_found": True},
                                                 ["gesture_found", "pose"])})
        action = self.policy_model.rollout(state)
        print_Action(action)
        self.assertIn(action, [AjanAction("move", {"motion": "right"}),
                               AjanAction("move", {"motion": "left"}),
                               AjanAction("perceive")])  # should only be move left

    def test_rollout_true_none(self):
        state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                     {"pose": (0, 0), "gesture": None},
                                                     ["pose", "gesture"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"pose": (0, 0), "gesture_found": True},
                                                 ["gesture_found", "pose"])})
        action = self.policy_model.rollout(state)
        print_Action(action)
        self.assertIn(action, [AjanAction("move", {"motion": "right"}),
                               AjanAction("move", {"motion": "left"}),
                               AjanAction("perceive")])  # should only be perceive


if __name__ == '__main__':
    unittest.main()
