# Run this model in debug mode with breakpoint in out.query of to_graph (line 156) since SELECT query is used.
# Else it will fail due to some sync issues which is automatically corrected internally in pomdp_py.

import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanOOState, AjanAgentState
from POMDPService.ajan_pomdp_planning.oopomdp.models.reward_model import AjanRewardModel
from tests.test_models.helpers.drone_reward_model_queries import ARGMAX_QUERY, SAMPLE_QUERY, PROBABILITY_QUERY, DATA


class TestDroneRewardModelSample(unittest.TestCase):

    reward_model = AjanRewardModel(DATA, None, PROBABILITY_QUERY, SAMPLE_QUERY, ARGMAX_QUERY)

    def test_sample_true_true_perceive(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("perceive")
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_true_false_perceive(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("perceive")
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_false_true_perceive(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("perceive")
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 1000)

    def test_sample_false_false_perceive(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("perceive")
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_false_false_move_left(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (-1, 1), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "left"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_true_false_move_left(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (-1, 1), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "left"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_true_true_move_left(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (-1, 1), "gesture_found": True},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "left"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_false_true_move_left(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (-1, 1), "gesture_found": True},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "left"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_false_false_move_right(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (1, 1), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_true_false_move_right(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (1, 1), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_true_true_move_right(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (1, 1), "gesture_found": True},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)

    def test_sample_false_true_move_right(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (1, 1), "gesture_found": True},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.reward_model.sample(current_state, action, next_state), 0)


if __name__ == '__main__':
    unittest.main()
