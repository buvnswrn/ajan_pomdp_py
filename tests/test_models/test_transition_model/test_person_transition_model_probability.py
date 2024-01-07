# Run this model in debug mode with breakpoint in out.query of to_graph (line 156) since SELECT query is used.
# Else it will fail due to some sync issues which is automatically corrected internally in pomdp_py.

import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanAgentState, AjanOOState
from POMDPService.ajan_pomdp_planning.oopomdp.models.transition_model import AjanTransitionModel
from tests.test_models.helpers.person_transition_model_queries import PROBABILITY_QUERY, DATA, ARGMAX_QUERY, \
    SAMPLE_QUERY


class TestPersonTransitionModelProbability(unittest.TestCase):

    person_transition_model = AjanTransitionModel(112, DATA, None, PROBABILITY_QUERY, SAMPLE_QUERY, ARGMAX_QUERY)

    def test_probability_right_right_perceive(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "right"}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "right"}, ["pose", "gesture"])
        action = AjanAction("perceive")
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 0.999999999)

    def test_probability_right_left_perceive(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "left"}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "right"}, ["pose", "gesture"])
        action = AjanAction("perceive")
        # Wrong result here
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_right_none_perceive(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": None}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "right"}, ["pose", "gesture"])
        action = AjanAction("perceive")
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_left_right_perceive(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "right"}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "left"}, ["pose", "gesture"])
        action = AjanAction("perceive") # Not just equal to but have to check the attributes as well.
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_left_left_perceive(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "left"}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "left"}, ["pose", "gesture"])
        action = AjanAction("perceive")
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 0.999999999)

    def test_probability_left_none_perceive(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": None}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "left"}, ["pose", "gesture"])
        action = AjanAction("perceive")
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_none_right_perceive(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "right"}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": None}, ["pose", "gesture"])
        action = AjanAction("perceive")
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_none_left_perceive(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "left"}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": None}, ["pose", "gesture"])
        action = AjanAction("perceive")
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_none_none_perceive(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": None}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": None}, ["pose", "gesture"])
        action = AjanAction("perceive")
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 0.999999999)

    def test_probability_right_right_move_right(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "right"}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "right"}, ["pose", "gesture"])
        action = AjanAction("move", {"motion": "right"})
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 0.999999999)

    def test_probability_right_left_move_right(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "left"}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "right"}, ["pose", "gesture"])
        action = AjanAction("move", {"motion": "right"})
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_right_none_move_right(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": None}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "right"}, ["pose", "gesture"])
        action = AjanAction("move", {"motion": "right"})
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_left_right_move_right(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "right"}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "left"}, ["pose", "gesture"])
        action = AjanAction("move", {"motion": "right"})
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_left_left_move_right(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "left"}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "left"}, ["pose", "gesture"])
        action = AjanAction("move", {"motion": "right"})
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 0.999999999)

    def test_probability_left_none_move_right(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": None}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "left"}, ["pose", "gesture"])
        action = AjanAction("move", {"motion": "right"})
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_none_right_move_right(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "right"}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": None}, ["pose", "gesture"])
        action = AjanAction("move", {"motion": "right"})
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_none_left_move_right(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "left"}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": None}, ["pose", "gesture"])
        action = AjanAction("move", {"motion": "right"})
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_none_none_move_right(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": None}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": None}, ["pose", "gesture"])
        action = AjanAction("move", {"motion": "right"})
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 0.999999999)

    def test_probability_right_right_move_left(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "right"}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": (0, 0), "gesture": "right"}, ["pose", "gesture"])
        action = AjanAction("move", {"motion": "left"})
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 0.999999999)

    def test_probability_right_left_move_left(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "left"}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": (0, 0), "gesture": "right"}, ["pose", "gesture"])
        action = AjanAction("move", {"motion": "left"})
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_right_none_move_left(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": None}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": (0, 0), "gesture": "right"}, ["pose", "gesture"])
        action = AjanAction("move", {"motion": "left"})
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_left_right_move_left(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "right"}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": (0, 0), "gesture": "left"}, ["pose", "gesture"])
        action = AjanAction("move", {"motion": "left"})
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_left_left_move_left(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "left"}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": (0, 0), "gesture": "left"}, ["pose", "gesture"])
        action = AjanAction("move", {"motion": "left"})
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 0.999999999)

    def test_probability_left_none_move_left(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": None}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": (0, 0), "gesture": "left"}, ["pose", "gesture"])
        action = AjanAction("move", {"motion": "left"})
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_none_right_move_left(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "right"}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": (0, 0), "gesture": None}, ["pose", "gesture"])
        action = AjanAction("move", {"motion": "left"})
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_none_left_move_left(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": "left"}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": (0, 0), "gesture": None}, ["pose", "gesture"])
        action = AjanAction("move", {"motion": "left"})
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 1e-9)

    def test_probability_none_none_move_left(self):
        next_state = AjanAgentState("Person", 112, {"id": 112, "pose": None, "gesture": None}, ["pose", "gesture"])
        current_state = AjanAgentState("Person", 112, {"id": 112, "pose": (0, 0), "gesture": None}, ["pose", "gesture"])
        action = AjanAction("move", {"motion": "left"})
        self.assertEqual(self.person_transition_model.probability(next_state, current_state, action), 0.999999999)


if __name__ == '__main__':
    unittest.main()
