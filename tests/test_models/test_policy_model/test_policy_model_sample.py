import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanEnvObjectState, AjanAgentState, AjanOOState
from POMDPService.ajan_pomdp_planning.oopomdp.models.policy_model import AjanPolicyModel
from tests.test_models.helpers.policy_model_queries import ROLLOUT_QUERY_POLICY, SAMPLE_QUERY_POLICY, DATA_POLICY, GET_ALL_ACTIONS_QUERY


class TestPolicyModelSample(unittest.TestCase):
    policy_model = AjanPolicyModel(DATA_POLICY, None, SAMPLE_QUERY_POLICY, ROLLOUT_QUERY_POLICY, GET_ALL_ACTIONS_QUERY)

    def test_sample_false_right(self):
        state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                     {"pose": (0, 0), "gesture": "right"},
                                                     ["pose", "gesture"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"pose": (0, 0), "gesture_found": False},
                                                 ["gesture_found", "pose"])})
        action = self.policy_model.sample(state)
        print(action)
        self.assertIn(action, [AjanAction("move", {"motion": "right"}),
                               AjanAction("move", {"motion": "left"}),
                               AjanAction("perceive")])  # should only be perceive

    def test_sample_false_left(self):
        state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                     {"pose": (0, 0), "gesture": "left"},
                                                     ["pose", "gesture"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"pose": (0, 0), "gesture_found": False},
                                                 ["gesture_found", "pose"])})
        action = self.policy_model.sample(state)
        print(action)
        self.assertIn(action, [AjanAction("move", {"motion": "right"}),
                               AjanAction("move", {"motion": "left"}),
                               AjanAction("perceive")])  # should only be perceive

    def test_sample_false_none(self):
        state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                     {"pose": (0, 0), "gesture": None},
                                                     ["pose", "gesture"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"pose": (0, 0), "gesture_found": False},
                                                 ["gesture_found", "pose"])})
        action = self.policy_model.sample(state)
        print(action)
        self.assertIn(action, [AjanAction("move", {"motion": "right"}),
                               AjanAction("move", {"motion": "left"}),
                               AjanAction("perceive")])  # should only be perceive

    def test_sample_true_right(self):
        state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                     {"pose": (0, 0), "gesture": "right"},
                                                     ["pose", "gesture"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"pose": (0, 0), "gesture_found": True},
                                                 ["gesture_found", "pose"])})
        action = self.policy_model.sample(state)
        print(action)
        self.assertIn(action, [AjanAction("move", {"motion": "right"}),
                               AjanAction("move", {"motion": "left"}),
                               AjanAction("perceive")])  # should only be move right

    def test_sample_true_left(self):
        state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                     {"pose": (0, 0), "gesture": "left"},
                                                     ["pose", "gesture"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"pose": (0, 0), "gesture_found": True},
                                                 ["gesture_found", "pose"])})
        action = self.policy_model.sample(state)
        print(action)
        self.assertIn(action, [AjanAction("move", {"motion": "right"}),
                               AjanAction("move", {"motion": "left"}),
                               AjanAction("perceive")])  # should only be move left

    def test_sample_true_none(self):
        state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                     {"pose": (0, 0), "gesture": None},
                                                     ["pose", "gesture"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"pose": (0, 0), "gesture_found": True},
                                                 ["gesture_found", "pose"])})
        action = self.policy_model.sample(state)
        print(action)
        self.assertIn(action, [AjanAction("move", {"motion": "right"}),
                               AjanAction("move", {"motion": "left"}),
                               AjanAction("perceive")])  # should only be perceive

    def test_get_all_actions(self):
        state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                     {"pose": (0, 0), "gesture": None},
                                                     ["pose", "gesture"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"pose": (0, 0), "gesture_found": True},
                                                 ["gesture_found", "pose"])})
        actions = self.policy_model.get_all_actions(state)
        print(actions)
        self.assertCountEqual(actions, [AjanAction("perceive"),
                                        AjanAction("move", {"motion": "left"}),
                                        AjanAction("move", {"motion": "right"})])


if __name__ == '__main__':
    unittest.main()
