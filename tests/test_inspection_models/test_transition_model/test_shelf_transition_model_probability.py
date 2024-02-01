import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanOOState, AjanEnvObjectState
from POMDPService.ajan_pomdp_planning.oopomdp.models.transition_model import AjanTransitionModel
from tests.test_inspection_models.helpers.shelf_transition_model_queries import DATA_S_T, PROBABILITY_QUERY_S_T, \
    ARGMAX_QUERY_S_T, SAMPLE_QUERY_S_T

Perceive = AjanAction("perceive")
MoveLeft = AjanAction("move", {"motion": "left"})
MoveRight = AjanAction("move", {"motion": "right"})
MoveUp = AjanAction("move", {"motion": "up"})
MoveDown = AjanAction("move", {"motion": "down"})


class TestShelfTransitionModelProbability(unittest.TestCase):
    shelf_transition_model = AjanTransitionModel(115, DATA_S_T, None, PROBABILITY_QUERY_S_T, SAMPLE_QUERY_S_T,
                                                 ARGMAX_QUERY_S_T)

    # region perceive - valid
    def test_probability_1_0_perceive_1_1(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 1, "inspection_state": 0},
                                                             ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 1, "inspection_state": 1},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.999999999)

    def test_probability_1_1_perceive_1_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 1, "inspection_state": 1},
                                                             ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 1, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.999999999)

    def test_probability_1_2_perceive_1_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 1, "inspection_state": 2},
                                                             ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 1, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.999999999)

    def test_probability_2_0_perceive_2_1(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 2, "inspection_state": 0},
                                                             ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 2, "inspection_state": 1},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.999999999)

    def test_probability_2_1_perceive_2_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 2, "inspection_state": 1},
                                                             ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 2, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.999999999)

    def test_probability_2_2_perceive_2_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 2, "inspection_state": 2},
                                                             ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 2, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.999999999)

    def test_probability_3_0_perceive_3_1(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 3, "inspection_state": 0},
                                                             ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 3, "inspection_state": 1},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.999999999)

    def test_probability_3_1_perceive_3_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 3, "inspection_state": 1},
                                                             ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 3, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.999999999)

    def test_probability_3_2_perceive_3_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 3, "inspection_state": 2},
                                                             ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 3, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.999999999)

    def test_probability_4_0_perceive_4_1(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 4, "inspection_state": 0},
                                                             ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 4, "inspection_state": 1},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.999999999)

    def test_probability_4_1_perceive_4_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 4, "inspection_state": 1},
                                                             ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 4, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.999999999)

    def test_probability_4_2_perceive_4_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 4, "inspection_state": 2},
                                                             ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 4, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 0.999999999)

    # endregion

    # region move up - valid

    def test_probability_1_0_move_up_2_0(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 1, "inspection_state": 0},
                                                             ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 2, "inspection_state": 0},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_1_1_move_up_2_1(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 1, "inspection_state": 1},
                                                             ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 2, "inspection_state": 1},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_1_2_move_up_2_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 1, "inspection_state": 2},
                                                             ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 2, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_2_0_move_up_3_0(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 2, "inspection_state": 0},
                                                             ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 3, "inspection_state": 0},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_2_1_move_up_3_1(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 2, "inspection_state": 1},
                                                             ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 3, "inspection_state": 1},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_2_2_move_up_3_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 2, "inspection_state": 2},
                                                             ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 3, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_3_0_move_up_4_0(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 3, "inspection_state": 0},
                                                             ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 4, "inspection_state": 0},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_3_1_move_up_4_1(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 3, "inspection_state": 1},
                                                             ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 4, "inspection_state": 1},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_3_2_move_up_4_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 3, "inspection_state": 2},
                                                             ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 4, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_4_0_move_up_4_0(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 4, "inspection_state": 0},
                                                             ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 4, "inspection_state": 0},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_4_1_move_up_4_1(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 4, "inspection_state": 1},
                                                             ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 4, "inspection_state": 1},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_4_2_move_up_4_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 4, "inspection_state": 2},
                                                             ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 4, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    # endregion

    # region move down - valid

    def test_probability_1_0_move_down_1_0(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 1, "inspection_state": 0},
                                                             ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 1, "inspection_state": 0},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_1_1_move_down_1_1(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 1, "inspection_state": 1},
                                                             ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 1, "inspection_state": 1},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_1_2_move_down_1_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 1, "inspection_state": 2},
                                                             ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 1, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_2_0_move_down_1_0(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 2, "inspection_state": 0},
                                                             ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 1, "inspection_state": 0},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_2_1_move_down_1_1(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 2, "inspection_state": 1},
                                                             ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 1, "inspection_state": 1},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_2_2_move_down_1_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 2, "inspection_state": 2},
                                                             ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 1, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_3_0_move_down_2_0(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 3, "inspection_state": 0},
                                                             ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 2, "inspection_state": 0},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_3_1_move_down_2_1(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 3, "inspection_state": 1},
                                                             ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 2, "inspection_state": 1},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_3_2_move_down_2_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 3, "inspection_state": 2},
                                                             ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 2, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_4_0_move_down_3_0(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 4, "inspection_state": 0},
                                                             ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 3, "inspection_state": 0},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_4_1_move_down_3_1(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 4, "inspection_state": 1},
                                                             ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 3, "inspection_state": 1},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_4_2_move_down_3_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 4, "inspection_state": 2},
                                                             ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 3, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    # endregion

    # region move left - valid

    def test_probability_1_0_move_left_1_0(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 1, "inspection_state": 0},
                                                             ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 1, "inspection_state": 0},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_1_1_move_left_1_1(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 1, "inspection_state": 1},
                                                             ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 1, "inspection_state": 1},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_1_2_move_left_1_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 1, "inspection_state": 2},
                                                             ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 1, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_2_0_move_left_2_0(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 2, "inspection_state": 0},
                                                             ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 2, "inspection_state": 0},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_2_1_move_left_2_1(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 2, "inspection_state": 1},
                                                             ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 2, "inspection_state": 1},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_2_2_move_left_2_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 2, "inspection_state": 2},
                                                             ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 2, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_3_0_move_left_3_0(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 3, "inspection_state": 0},
                                                             ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 3, "inspection_state": 0},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_3_1_move_left_3_1(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 3, "inspection_state": 1},
                                                             ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 3, "inspection_state": 1},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_3_2_move_left_3_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 3, "inspection_state": 2},
                                                             ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 3, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_4_0_move_left_4_0(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 4, "inspection_state": 0},
                                                             ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 4, "inspection_state": 0},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_4_1_move_left_4_1(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 4, "inspection_state": 1},
                                                             ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 4, "inspection_state": 1},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_4_2_move_left_4_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 4, "inspection_state": 2},
                                                             ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 4, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    # endregion

    # region move right - valid

    def test_probability_1_0_move_right_1_0(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 1, "inspection_state": 0},
                                                             ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 1, "inspection_state": 0},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_1_1_move_right_1_1(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 1, "inspection_state": 1},
                                                             ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 1, "inspection_state": 1},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_1_2_move_right_1_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 1, "inspection_state": 2},
                                                             ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 1, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_2_0_move_right_2_0(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 2, "inspection_state": 0},
                                                             ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 2, "inspection_state": 0},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_2_1_move_right_2_1(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 2, "inspection_state": 1},
                                                             ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 2, "inspection_state": 1},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_2_2_move_right_2_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 2, "inspection_state": 2},
                                                             ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 2, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_3_0_move_right_3_0(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 3, "inspection_state": 0},
                                                             ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 3, "inspection_state": 0},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_3_1_move_right_3_1(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 3, "inspection_state": 1},
                                                             ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 3, "inspection_state": 1},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_3_2_move_right_3_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 3, "inspection_state": 2},
                                                             ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 3, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_4_0_move_right_4_0(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 4, "inspection_state": 0},
                                                             ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 4, "inspection_state": 0},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_4_1_move_right_4_1(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 4, "inspection_state": 1},
                                                             ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 4, "inspection_state": 1},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    def test_probability_4_2_move_right_4_2(self):
        current_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                             {"rack_id": 4, "inspection_state": 2},
                                                             ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                          {"rack_id": 4, "inspection_state": 2},
                                                          ["rack_id", "inspection_state"])})

        probability = self.shelf_transition_model.probability(next_state, current_state, action)
        self.assertEqual(probability, 1.0)

    # endregion



if __name__ == '__main__':
    unittest.main()
