import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanOOState, AjanAgentState
from POMDPService.ajan_pomdp_planning.oopomdp.models.transition_model import AjanTransitionModel
from tests.test_inspection_models.helpers.drone_transition_model_queries import ARGMAX_QUERY_D_T, SAMPLE_QUERY_D_T, \
    PROBABILITY_QUERY_D_T, DATA_D_T

Perceive = AjanAction("perceive")
MoveLeft = AjanAction("move", {"motion": "left"})
MoveRight = AjanAction("move", {"motion": "right"})
MoveUp = AjanAction("move", {"motion": "up"})
MoveDown = AjanAction("move", {"motion": "down"})


class TestDroneTransitionModelProbability(unittest.TestCase):
    drone_transition_model = AjanTransitionModel(100, DATA_D_T, None, PROBABILITY_QUERY_D_T, SAMPLE_QUERY_D_T,
                                                 ARGMAX_QUERY_D_T)

    # region perceive - valid
    def test_probability_1_left_false_perceive_1_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.5)

    def test_probability_1_right_false_perceive_1_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.5)

    def test_probability_2_left_false_perceive_2_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.5)

    def test_probability_2_right_false_perceive_2_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.5)

    def test_probability_3_left_false_perceive_3_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.5)

    def test_probability_3_right_false_perceive_3_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.5)

    def test_probability_4_left_false_perceive_4_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.5)

    def test_probability_4_right_false_perceive_4_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.5)

    def test_probability_1_left_false_perceive_1_left_true(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "left",
                                                       "complete_status": True},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.5)

    def test_probability_1_right_false_perceive_1_right_true(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "right",
                                                       "complete_status": True},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.5)

    def test_probability_2_left_false_perceive_2_left_true(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "left",
                                                       "complete_status": True},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.5)

    def test_probability_2_right_false_perceive_2_right_true(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "right",
                                                       "complete_status": True},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.5)

    def test_probability_3_left_false_perceive_3_left_true(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "left",
                                                       "complete_status": True},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.5)

    def test_probability_3_right_false_perceive_3_right_true(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone",100,
                                                      {"rack_id": 3, "direction": "right",
                                                       "complete_status": True},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.5)

    def test_probability_4_left_false_perceive_4_left_true(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100:AjanAgentState("Drone", 100,
                                                     {"rack_id": 4, "direction": "left",
                                                      "complete_status": True},
                                                     ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.5)

    def test_probability_4_right_false_perceive_4_right_true(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100:AjanAgentState("Drone", 100,
                                                     {"rack_id": 4, "direction": "right",
                                                      "complete_status": True},
                                                     ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.5)

    # endregion

    # region move left - valid

    def test_probability_1_left_false_move_left_1_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state,current_state,action)
        self.assertEqual(probability, 1.0)

    def test_probability_1_right_false_move_left_1_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state,current_state,action)
        self.assertEqual(probability, 1.0)

    def test_probability_2_left_false_move_left_2_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state,current_state,action)
        self.assertEqual(probability, 1.0)

    def test_probability_2_right_false_move_left_2_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state,current_state,action)
        self.assertEqual(probability, 1.0)

    def test_probability_3_left_false_move_left_3_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state,current_state,action)
        self.assertEqual(probability, 1.0)

    def test_probability_3_right_false_move_left_3_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state,current_state,action)
        self.assertEqual(probability, 1.0)

    def test_probability_4_left_false_move_left_4_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state,current_state,action)
        self.assertEqual(probability, 1.0)

    def test_probability_4_right_false_move_left_4_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state,current_state,action)
        self.assertEqual(probability, 1.0)

    # endregion

    # region move right - valid

    def test_probability_1_left_false_move_right_1_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state,current_state,action)
        self.assertEqual(probability, 1.0)

    def test_probability_1_right_false_move_right_1_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state,current_state,action)
        self.assertEqual(probability, 1.0)

    def test_probability_2_left_false_move_right_2_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_2_right_false_move_right_2_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_3_left_false_move_right_3_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_3_right_false_move_right_3_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_4_left_false_move_right_4_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_4_right_false_move_right_4_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    # endregion

    # region move up - valid

    def test_probability_1_left_false_move_up_2_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_1_right_false_move_up_2_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_2_left_false_move_up_3_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_2_right_false_move_up_3_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_3_left_false_move_up_4_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_3_right_false_move_up_4_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_4_left_false_move_up_4_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_4_right_false_move_up_4_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    # endregion

    # region move down - valid

    def test_probability_1_left_false_move_down_1_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state,current_state,action)
        self.assertEqual(probability, 1.0)

    def test_probability_1_right_false_move_down_1_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state,current_state,action)
        self.assertEqual(probability, 1.0)

    def test_probability_2_left_false_move_down_1_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state,current_state,action)
        self.assertEqual(probability, 1.0)

    def test_probability_2_right_false_move_down_1_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state,current_state,action)
        self.assertEqual(probability, 1.0)

    def test_probability_3_left_false_move_down_2_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state,current_state,action)
        self.assertEqual(probability, 1.0)

    def test_probability_3_right_false_move_down_2_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state,current_state,action)
        self.assertEqual(probability, 1.0)

    def test_probability_4_left_false_move_down_3_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state,current_state,action)
        self.assertEqual(probability,1.0)

    def test_probability_4_right_false_move_down_3_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        probability = self.drone_transition_model.probability(next_state,current_state,action)
        self.assertEqual(probability,1.0)

    # endregion

    # def test_probability_2_left_false_move_right_2_left_false(self):
    #     current_state = AjanOOState({100: AjanAgentState("Drone", 100,
    #                                                      {"rack_id": 2, "direction": "left",
    #                                                       "complete_status": False},
    #                                                      ["rack_id", "direction", "complete_status"])})
    #     action = MoveRight
    #     next_state = AjanOOState({100: AjanAgentState("Drone", 100,
    #                                                   {"rack_id": 2, "direction": "left",
    #                                                    "complete_status": False},
    #                                                   ["rack_id", "direction", "complete_status"])})
    #     probability = self.drone_transition_model.probability(next_state, current_state, action)
    #     self.assertEqual(probability, 0.0)


if __name__ == '__main__':
    unittest.main()
