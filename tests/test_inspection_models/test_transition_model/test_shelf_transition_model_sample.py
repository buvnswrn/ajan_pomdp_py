import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanOOState, AjanEnvObjectState
from POMDPService.ajan_pomdp_planning.oopomdp.models.transition_model import AjanTransitionModel
from tests.test_inspection_models.helpers.shelf_transition_model_queries import DATA_S_T, ARGMAX_QUERY_S_T, \
    PROBABILITY_QUERY_S_T, SAMPLE_QUERY_S_T

Perceive = AjanAction("perceive")
MoveLeft = AjanAction("move", {"motion": "left"})
MoveRight = AjanAction("move", {"motion": "right"})
MoveUp = AjanAction("move", {"motion": "up"})
MoveDown = AjanAction("move", {"motion": "down"})


class TestShelfTransitionModelSample(unittest.TestCase):

    shelf_transition_model = AjanTransitionModel(115, DATA_S_T, None, PROBABILITY_QUERY_S_T, SAMPLE_QUERY_S_T,
                                                 ARGMAX_QUERY_S_T)

    def test_sample_1_0_perceive(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 1, "inspection_state": 1},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_1_1_perceive(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 1, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_1_2_perceive(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 1, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_1_0_move_left(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 1, "inspection_state": 0},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_1_0_move_right(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 1, "inspection_state": 0},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_1_0_move_up(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 2, "inspection_state": 0},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_1_0_move_down(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 1, "inspection_state": 0},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_1_1_move_left(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 1, "inspection_state": 1},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_1_1_move_right(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 1, "inspection_state": 1},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_1_1_move_up(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 2, "inspection_state": 1},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_1_1_move_down(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 1, "inspection_state": 1},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_1_2_move_left(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 1, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_1_2_move_right(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 1, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_1_2_move_up(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 2, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_1_2_move_down(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 1, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_2_0_perceive(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 2, "inspection_state": 1},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_2_1_perceive(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 2, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_2_2_perceive(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 2, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_2_0_move_left(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 2, "inspection_state": 0},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_2_0_move_right(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 2, "inspection_state": 0},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_2_0_move_up(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 3, "inspection_state": 0},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_2_0_move_down(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 1, "inspection_state": 0},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_2_1_move_left(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 2, "inspection_state": 1},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_2_1_move_right(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 2, "inspection_state": 1},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_2_1_move_up(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 3, "inspection_state": 1},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_2_1_move_down(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 1, "inspection_state": 1},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_2_2_move_left(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 2, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_2_2_move_right(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 2, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_2_2_move_up(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 3, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_2_2_move_down(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 1, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_3_0_perceive(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 3, "inspection_state": 1},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_3_1_perceive(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 3, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_3_2_perceive(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 3, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_3_0_move_left(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 3, "inspection_state": 0},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_3_0_move_right(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 3, "inspection_state": 0},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_3_0_move_up(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 4, "inspection_state": 0},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_3_0_move_down(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 2, "inspection_state": 0},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_3_1_move_left(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf", 115,
                                                        {"rack_id": 3, "inspection_state": 1},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_3_1_move_right(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 3, "inspection_state": 1},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_3_1_move_up(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 4, "inspection_state": 1},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_3_1_move_down(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 2, "inspection_state": 1},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_3_2_move_left(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 3, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_3_2_move_right(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 3, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_3_2_move_up(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 4, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_3_2_move_down(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 2, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_4_0_perceive(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 4, "inspection_state": 1},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_4_1_perceive(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 4, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_4_2_perceive(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"])})
        action = Perceive
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 4, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_4_0_move_left(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 4, "inspection_state": 0},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_4_0_move_right(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 4, "inspection_state": 0},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_4_0_move_up(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 4, "inspection_state": 0},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_4_0_move_down(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 3, "inspection_state": 0},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_4_1_move_left(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 4, "inspection_state": 1},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_4_1_move_right(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 4, "inspection_state": 1},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_4_1_move_up(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 4, "inspection_state": 1},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_4_1_move_down(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 3, "inspection_state": 1},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_4_2_move_left(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"])})
        action = MoveLeft
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 4, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_4_2_move_right(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"])})
        action = MoveRight
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 4, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_4_2_move_up(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"])})
        action = MoveUp
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 4, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))

    def test_sample_4_2_move_down(self):
        state = AjanOOState({115: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"])})
        action = MoveDown
        next_state = self.shelf_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanEnvObjectState("Shelf",115,
                                                        {"rack_id": 3, "inspection_state": 2},
                                                        ["rack_id", "inspection_state"]))


if __name__ == '__main__':
    unittest.main()
