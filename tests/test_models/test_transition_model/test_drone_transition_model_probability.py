# Run this model in debug mode with breakpoint in out.query of to_graph (line 156) since SELECT query is used.
# Else it will fail due to some sync issues which is automatically corrected internally in pomdp_py.

import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanAgentState, AjanOOState
from POMDPService.ajan_pomdp_planning.oopomdp.models.transition_model import AjanTransitionModel
from tests.test_models.helpers.drone_transition_model_queries import DATA, SAMPLE_QUERY, ARGMAX_QUERY, PROBABILITY_QUERY


class TestDroneTransitionModelProbability(unittest.TestCase):

    drone_transition_model = AjanTransitionModel(100, DATA, None, PROBABILITY_QUERY, SAMPLE_QUERY, ARGMAX_QUERY)


    def test_probability_true_true_perceive(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True}, ["pose", "gesture_found"])})
        action = AjanAction("perceive")
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 0.999999999)

    def test_probability_true_false_perceive(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True}, ["pose", "gesture_found"])})
        action = AjanAction("perceive")
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 1e-09)

    def test_probability_false_true_perceive(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False}, ["pose", "gesture_found"])})
        action = AjanAction("perceive")
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 1e-09)

    def test_probability_false_false_perceive(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False}, ["pose", "gesture_found"])})
        action = AjanAction("perceive")
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 0.999999999)

    def test_probability_none_true_perceive(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": None}, ["pose", "gesture_found"])})
        action = AjanAction("perceive")
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 1e-09)

    def test_probability_none_false_perceive(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": None}, ["pose", "gesture_found"])})
        action = AjanAction("perceive")
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 1e-09)

    def test_probability_none_none_perceive(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": None}, ["pose", "gesture_found"])})
        action = AjanAction("perceive")
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": None}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 0.999999999)

    def test_probability_true_none_move_right(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": None}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_false_none_move_right(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": None}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_true_true_move_right(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 0.999999999)

    def test_probability_true_false_move_right(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_false_true_move_right(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_false_false_move_right(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 0.999999999)

    def test_probability_none_true_move_right(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": None}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_none_false_move_right(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": None}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_none_none_move_right(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": None}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": None}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 0.999999999)

    def test_probability_true_true_move_left(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "left"})
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 0.999999999)

    def test_probability_false_true_move_left(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "left"})
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_true_false_move_left(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "left"})
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_false_false_move_left(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "left"})
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 0.999999999)

    def test_probability_none_true_move_left(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": None}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "left"})
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_none_false_move_left(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": None}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "left"})
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_none_none_move_left(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": None}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "left"})
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": None}, ["pose", "gesture_found"])})
        self.assertEqual(self.drone_transition_model.probability(next_state, current_state, action), 0.999999999)


if __name__ == '__main__':
    unittest.main()
