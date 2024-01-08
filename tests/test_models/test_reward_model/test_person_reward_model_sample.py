import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanOOState, AjanAgentState, AjanEnvObjectState
from POMDPService.ajan_pomdp_planning.oopomdp.models.reward_model import AjanRewardModel
from tests.test_models.helpers.person_reward_model_queries import DATA_P_R, PROBABILITY_QUERY_P_R, SAMPLE_QUERY_P_R, ARGMAX_QUERY_P_R


class TestPersonRewardModelSample(unittest.TestCase):
    reward_model = AjanRewardModel(DATA_P_R, None, PROBABILITY_QUERY_P_R, SAMPLE_QUERY_P_R, ARGMAX_QUERY_P_R)

    def test_sample_right_right_perceive(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "pose": None, "gesture": "right"},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["pose", "gesture_found"])})
        action = AjanAction("perceive")
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "pose": None, "gesture": "right"},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["pose", "gesture_found"])})

        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_right_left_perceive(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "pose": None, "gesture": "left"},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["pose", "gesture_found"])})
        action = AjanAction("perceive")
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "pose": None, "gesture": "right"},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["pose", "gesture_found"])})

        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_left_right_perceive(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "pose": None, "gesture": "right"},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["pose", "gesture_found"])})
        action = AjanAction("perceive")
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "pose": None, "gesture": "left"},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["pose", "gesture_found"])})

        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_left_left_perceive(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "pose": None, "gesture": "left"},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["pose", "gesture_found"])})
        action = AjanAction("perceive")
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "pose": None, "gesture": "left"},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["pose", "gesture_found"])})

        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_right_none_perceive(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "pose": None, "gesture": None},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["pose", "gesture_found"])})
        action = AjanAction("perceive")
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "pose": None, "gesture": "right"},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["pose", "gesture_found"])})

        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_left_none_perceive(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "pose": None, "gesture": None},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["pose", "gesture_found"])})
        action = AjanAction("perceive")
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "pose": None, "gesture": "left"},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["pose", "gesture_found"])})

        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_none_right_perceive(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "pose": None, "gesture": "right"},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": None, "gesture_found": False},
                                                      ["pose", "gesture_found"])})
        action = AjanAction("perceive")
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "pose": None, "gesture": None},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": None, "gesture_found": False},
                                                         ["pose", "gesture_found"])})

        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_none_left_perceive(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "pose": None, "gesture": "left"},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": None, "gesture_found": False},
                                                      ["pose", "gesture_found"])})
        action = AjanAction("perceive")
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "pose": None, "gesture": None},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": None, "gesture_found": False},
                                                         ["pose", "gesture_found"])})

        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_none_none_perceive(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "pose": None, "gesture": None},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": None, "gesture_found": False},
                                                      ["pose", "gesture_found"])})
        action = AjanAction("perceive")
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "pose": None, "gesture": None},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": None, "gesture_found": False},
                                                         ["pose", "gesture_found"])})

        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_right_right_move_right(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "pose": None, "gesture": "right"},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "pose": None, "gesture": "right"},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["pose", "gesture_found"])})

        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 1000)

    def test_sample_right_left_move_right(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "pose": None, "gesture": "left"},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "pose": None, "gesture": "right"},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["pose", "gesture_found"])})

        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_left_right_move_right(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "pose": None, "gesture": "right"},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "pose": None, "gesture": "left"},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["pose", "gesture_found"])})

        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_left_left_move_right(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "pose": None, "gesture": "left"},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "pose": None, "gesture": "left"},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["pose", "gesture_found"])})

        # self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0) # should not be 0
        self.assertEqual(self.reward_model.sample(current_state, action, next_state), -1000)

    def test_sample_right_none_move_right(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "pose": None, "gesture": None},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "pose": None, "gesture": "right"},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["pose", "gesture_found"])})

        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_left_none_move_right(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "pose": None, "gesture": None},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "pose": None, "gesture": "left"},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["pose", "gesture_found"])})

        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_none_right_move_right(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "pose": None, "gesture": "right"},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "pose": None, "gesture": None},
                                                             ["gesture"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})

        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_none_left_move_right(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "pose": None, "gesture": "left"},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "pose": None, "gesture": None},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_none_none_move_right(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "pose": None, "gesture": None},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "pose": None, "gesture": None},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        # self.assertEqual(self.reward_model.sample(current_state, action, next_state), -1000) # should not be -1000
        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_right_right_move_left(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "gesture": "right", "pose": None},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "left"})
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "gesture": "right", "pose": None},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        # self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)  # reward should not be zero
        self.assertEqual(self.reward_model.sample(current_state, action, next_state), -1000)

    def test_sample_right_left_move_left(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "gesture": "left", "pose": None},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "left"})
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "gesture": "right", "pose": None},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_left_right_move_left(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "gesture": "right", "pose": None},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "left"})
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "gesture": "left", "pose": None},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_left_left_move_left(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "gesture": "left", "pose": None},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "left"})
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "gesture": "left", "pose": None},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 1000)

    def test_sample_right_none_move_left(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "gesture": None, "pose": None},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})

        action = AjanAction("move", {"motion": "left"})
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "gesture": "right", "pose": None},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})

        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_left_none_move_left(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "gesture": None, "pose": None},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})

        action = AjanAction("move", {"motion": "left"})
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "gesture": "left", "pose": None},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": None, "gesture_found": False},
                                                         ["gesture_found", "pose"])})

        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_none_right_move_left(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "gesture": "right", "pose": None},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": None, "gesture_found": False},
                                                      ["gesture_found", "pose"])})

        action = AjanAction("move", {"motion": "left"})
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "gesture": None, "pose": None},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": None, "gesture_found": False},
                                                         ["gesture_found", "pose"])})

        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_none_left_move_left(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "gesture": "left", "pose": None},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": None, "gesture_found": False},
                                                      ["gesture_found", "pose"])})

        action = AjanAction("move", {"motion": "left"})
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "gesture": None, "pose": None},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": None, "gesture_found": False},
                                                         ["gesture_found", "pose"])})

        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_none_none_move_left(self):
        next_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                          {"id": 112, "gesture": None, "pose": None},
                                                          ["gesture", "pose"]),
                                  100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})

        action = AjanAction("move", {"motion": "left"})
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {"id": 112, "gesture": None, "pose": None},
                                                             ["gesture", "pose"]),
                                     100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})

        # self.assertEqual(self.reward_model.sample(current_state, action, next_state), -1000) # should not be -1000
        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)


if __name__ == '__main__':
    unittest.main()
