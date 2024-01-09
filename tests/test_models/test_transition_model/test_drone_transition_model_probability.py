# Run this model in debug mode with breakpoint in out.query of to_graph (line 156) since SELECT query is used.
# Else it will fail due to some sync issues which is automatically corrected internally in pomdp_py.

import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanAgentState, AjanOOState
from POMDPService.ajan_pomdp_planning.oopomdp.models.transition_model import AjanTransitionModel
from tests.test_models.alternate_models.python_transition_model import TransitionModel
from tests.test_models.helpers.drone_transition_model_queries import DATA_D_T, SAMPLE_QUERY_D_T, ARGMAX_QUERY_D_T, \
    PROBABILITY_QUERY_D_T, PROBABILITY_QUERY_D_T_2


class TestDroneTransitionModelProbability(unittest.TestCase):

    drone_transition_model = AjanTransitionModel(100, DATA_D_T, None, PROBABILITY_QUERY_D_T_2, SAMPLE_QUERY_D_T, ARGMAX_QUERY_D_T)

    # drone_transition_model = TransitionModel("drone", 100)

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
