import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanAgentState, AjanEnvObjectState, AjanOOState
from POMDPService.ajan_pomdp_planning.oopomdp.models.transition_model import AjanTransitionModel
from tests.test_inspection_models.helpers.drone_transition_model_queries import ARGMAX_QUERY_D_T, SAMPLE_QUERY_D_T, \
    PROBABILITY_QUERY_D_T, DATA_D_T

Perceive = AjanAction("perceive")
MoveLeft = AjanAction("move", {"motion": "left"})
MoveRight = AjanAction("move", {"motion": "right"})
MoveUp = AjanAction("move", {"motion": "up"})
MoveDown = AjanAction("move", {"motion": "down"})


class TestDroneTransitionModelSample(unittest.TestCase):
    drone_transition_model = AjanTransitionModel(100, DATA_D_T, None, PROBABILITY_QUERY_D_T, SAMPLE_QUERY_D_T,
                                                 ARGMAX_QUERY_D_T)

    # region perceive action
    def test_sample_2_left_false_perceive(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = self.drone_transition_model.sample(state, action)
        self.assertIn(next_state,
                      [AjanAgentState("Drone", 100, {"rack_id": 2, "direction": "left", "complete_status": True},
                                      ["rack_id", "direction", "complete_status"]),
                       AjanAgentState("Drone", 100,
                                      {"rack_id": 2, "direction": "left", "complete_status": False},
                                      ["rack_id", "direction", "complete_status"])])

    def test_sample_2_left_true_move_right(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 2, "direction": "right", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_2_left_true_move_up(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 3, "direction": "left", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_2_left_true_move_down(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 1, "direction": "left", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_2_left_true_move_left(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 2, "direction": "left", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_2_left_true_perceive(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = self.drone_transition_model.sample(state, action)
        self.assertIn(next_state,
                      [AjanAgentState("Drone", 100, {"rack_id": 2, "direction": "left", "complete_status": True},
                                      ["rack_id", "direction", "complete_status"]),
                       AjanAgentState("Drone", 100,
                                      {"rack_id": 2, "direction": "left", "complete_status": False},
                                      ["rack_id", "direction", "complete_status"])])

    def test_sample_2_left_false_move_right(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 2, "direction": "right", "complete_status": False},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_2_left_false_move_up(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 3, "direction": "left", "complete_status": False},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_2_left_false_move_down(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 1, "direction": "left", "complete_status": False},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_2_left_false_move_left(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 2, "direction": "left", "complete_status": False},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_1_left_false_perceive(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = self.drone_transition_model.sample(state, action)
        self.assertIn(next_state,
                      [AjanAgentState("Drone", 100, {"rack_id": 1, "direction": "left", "complete_status": True},
                                      ["rack_id", "direction", "complete_status"]),
                       AjanAgentState("Drone", 100,
                                      {"rack_id": 1, "direction": "left", "complete_status": False},
                                      ["rack_id", "direction", "complete_status"])])

    def test_sample_1_left_true_move_right(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 1, "direction": "right", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_1_left_true_move_up(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 2, "direction": "left", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_1_left_true_move_down(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 1, "direction": "left", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_1_left_true_move_left(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 1, "direction": "left", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_1_left_true_perceive(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = self.drone_transition_model.sample(state, action)
        self.assertIn(next_state,
                      [AjanAgentState("Drone", 100, {"rack_id": 1, "direction": "left", "complete_status": True},
                                      ["rack_id", "direction", "complete_status"]),
                       AjanAgentState("Drone", 100,
                                      {"rack_id": 1, "direction": "left", "complete_status": False},
                                      ["rack_id", "direction", "complete_status"])])

    def test_sample_1_left_false_move_right(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 1, "direction": "right", "complete_status": False},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_1_left_false_move_up(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 2, "direction": "left", "complete_status": False},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_1_left_false_move_down(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 1, "direction": "left", "complete_status": False},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_1_left_false_move_left(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 1, "direction": "left", "complete_status": False},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_4_left_false_perceive(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = self.drone_transition_model.sample(state, action)
        self.assertIn(next_state,
                      [AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "left", "complete_status": True},
                                      ["rack_id", "direction", "complete_status"]),
                       AjanAgentState("Drone", 100,
                                      {"rack_id": 4, "direction": "left", "complete_status": False},
                                      ["rack_id", "direction", "complete_status"])])

    def test_sample_4_left_true_move_right(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 4, "direction": "right", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_4_left_true_move_up(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 4, "direction": "left", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_4_left_true_move_down(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 3, "direction": "left", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_4_left_true_move_left(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 4, "direction": "left", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_4_left_true_perceive(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = self.drone_transition_model.sample(state, action)
        self.assertIn(next_state,
                      [AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "left", "complete_status": True},
                                      ["rack_id", "direction", "complete_status"]),
                       AjanAgentState("Drone", 100,
                                      {"rack_id": 4, "direction": "left", "complete_status": False},
                                      ["rack_id", "direction", "complete_status"])])

    def test_sample_4_left_false_move_right(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 4, "direction": "right", "complete_status": False},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_4_left_false_move_up(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 4, "direction": "left", "complete_status": False},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_4_left_false_move_down(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 3, "direction": "left", "complete_status": False},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_4_left_false_move_left(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 4, "direction": "left", "complete_status": False},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_3_left_false_perceive(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = self.drone_transition_model.sample(state, action)
        self.assertIn(next_state,
                      [AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "left", "complete_status": True},
                                      ["rack_id", "direction", "complete_status"]),
                       AjanAgentState("Drone", 100,
                                      {"rack_id": 3, "direction": "left", "complete_status": False},
                                      ["rack_id", "direction", "complete_status"])])

    def test_sample_3_left_true_move_right(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 3, "direction": "right", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_3_left_true_move_up(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 4, "direction": "left", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_3_left_true_move_down(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 2, "direction": "left", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_3_left_true_move_left(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 3, "direction": "left", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_3_left_true_perceive(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = self.drone_transition_model.sample(state, action)
        self.assertIn(next_state,
                      [AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "left", "complete_status": True},
                                      ["rack_id", "direction", "complete_status"]),
                       AjanAgentState("Drone", 100,
                                      {"rack_id": 3, "direction": "left", "complete_status": False},
                                      ["rack_id", "direction", "complete_status"])])

    def test_sample_3_left_false_move_right(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 3, "direction": "right", "complete_status": False},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_3_left_false_move_up(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 4, "direction": "left", "complete_status": False},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_3_left_false_move_down(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 2, "direction": "left", "complete_status": False},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_3_left_false_move_left(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 3, "direction": "left", "complete_status": False},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_1_right_false_perceive(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "right",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = self.drone_transition_model.sample(state, action)
        self.assertIn(next_state,
                      [AjanAgentState("Drone", 100, {"rack_id": 1, "direction": "right", "complete_status": True},
                                      ["rack_id", "direction", "complete_status"]),
                       AjanAgentState("Drone", 100,
                                      {"rack_id": 1, "direction": "right", "complete_status": False},
                                      ["rack_id", "direction", "complete_status"])])

    def test_sample_1_right_true_move_right(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 1, "direction": "right", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_1_right_true_move_up(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 2, "direction": "right", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_1_right_true_move_down(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 1, "direction": "right", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_1_right_true_move_left(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 1, "direction": "left", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_1_right_true_perceive(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = self.drone_transition_model.sample(state, action)
        self.assertIn(next_state,
                      [AjanAgentState("Drone", 100, {"rack_id": 1, "direction": "right", "complete_status": True},
                                      ["rack_id", "direction", "complete_status"]),
                       AjanAgentState("Drone", 100,
                                      {"rack_id": 1, "direction": "right", "complete_status": False},
                                      ["rack_id", "direction", "complete_status"])])

    def test_sample_1_right_false_move_right(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "right",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 1, "direction": "right", "complete_status": False},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_1_right_false_move_up(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "right",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 2, "direction": "right", "complete_status": False},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_1_right_false_move_down(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "right",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 1, "direction": "right", "complete_status": False},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_1_right_false_move_left(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "right",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 1, "direction": "left", "complete_status": False},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_2_right_false_perceive(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "right",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = self.drone_transition_model.sample(state, action)
        self.assertIn(next_state,
                      [AjanAgentState("Drone", 100, {"rack_id": 2, "direction": "right", "complete_status": True},
                                      ["rack_id", "direction", "complete_status"]),
                       AjanAgentState("Drone", 100,
                                      {"rack_id": 2, "direction": "right", "complete_status": False},
                                      ["rack_id", "direction", "complete_status"])])

    def test_sample_2_right_true_move_right(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 2, "direction": "right", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_2_right_true_move_up(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 3, "direction": "right", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_2_right_true_move_down(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 1, "direction": "right", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_2_right_true_move_left(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 2, "direction": "left", "complete_status": True},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_2_right_true_perceive(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = self.drone_transition_model.sample(state, action)
        self.assertIn(next_state,
                      [AjanAgentState("Drone", 100, {"rack_id": 2, "direction": "right", "complete_status": True},
                                      ["rack_id", "direction", "complete_status"]),
                       AjanAgentState("Drone", 100,
                                      {"rack_id": 2, "direction": "right", "complete_status": False},
                                      ["rack_id", "direction", "complete_status"])])

    def test_sample_2_right_false_move_right(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "right",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state, AjanAgentState("Drone", 100,
                                                    {"rack_id": 2, "direction": "right", "complete_status": False},
                                                    ["rack_id", "direction", "complete_status"]))

    def test_sample_2_right_false_move_up(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "right",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state,
                         AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "right", "complete_status": False},
                                        ["rack_id", "direction", "complete_status"]))

    def test_sample_2_right_false_move_down(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "right",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state,
                         AjanAgentState("Drone", 100, {"rack_id": 1, "direction": "right", "complete_status": False},
                                        ["rack_id", "direction", "complete_status"]))

    def test_sample_2_right_false_move_left(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100, {"rack_id": 2, "direction": "right",
                                                                "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state,
                         AjanAgentState("Drone", 100, {"rack_id": 2, "direction": "left", "complete_status": False},
                                        ["rack_id", "direction", "complete_status"]))

    def test_sample_4_right_false_perceive(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "right",
                                                                "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = self.drone_transition_model.sample(state, action)
        self.assertIn(next_state,
                      [AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "right", "complete_status": True},
                                      ["rack_id", "direction", "complete_status"]),
                       AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "right", "complete_status": False},
                                      ["rack_id", "direction", "complete_status"])])

    def test_sample_4_right_true_move_right(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "right",
                                                                "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state,
                         AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "right", "complete_status": True},
                                        ["rack_id", "direction", "complete_status"]))

    def test_sample_4_right_true_move_up(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "right",
                                                                "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state,
                         AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "right", "complete_status": True},
                                        ["rack_id", "direction", "complete_status"]))

    def test_sample_4_right_true_move_down(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "right",
                                                                "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state,
                         AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "right", "complete_status": True},
                                        ["rack_id", "direction", "complete_status"]))

    def test_sample_4_right_true_move_left(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "right",
                                                                "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state,
                         AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "left", "complete_status": True},
                                        ["rack_id", "direction", "complete_status"]))

    def test_sample_4_right_true_perceive(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "right",
                                                                "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = self.drone_transition_model.sample(state, action)
        self.assertIn(next_state,
                      [AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "right", "complete_status": True},
                                      ["rack_id", "direction", "complete_status"]),
                       AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "right", "complete_status": False},
                                      ["rack_id", "direction", "complete_status"])])

    def test_sample_4_right_false_move_right(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "right",
                                                                "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state,
                         AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "right", "complete_status": False},
                                        ["rack_id", "direction", "complete_status"]))

    def test_sample_4_right_false_move_up(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "right",
                                                                "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state,
                         AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "right", "complete_status": False},
                                        ["rack_id", "direction", "complete_status"]))

    def test_sample_4_right_false_move_down(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "right",
                                                                "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state,
                         AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "right", "complete_status": False},
                                        ["rack_id", "direction", "complete_status"]))

    def test_sample_4_right_false_move_left(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "right",
                                                                "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state,
                         AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "left", "complete_status": False},
                                        ["rack_id", "direction", "complete_status"]))

    def test_sample_3_right_false_perceive(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "right",
                                                                "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = self.drone_transition_model.sample(state, action)
        self.assertIn(next_state,
                      [AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "right", "complete_status": True},
                                      ["rack_id", "direction", "complete_status"]),
                       AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "right", "complete_status": False},
                                      ["rack_id", "direction", "complete_status"])])

    def test_sample_3_right_true_move_right(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "right",
                                                                "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state,
                         AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "right", "complete_status": True},
                                        ["rack_id", "direction", "complete_status"]))

    def test_sample_3_right_true_move_up(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "right",
                                                                "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state,
                         AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "right", "complete_status": True},
                                        ["rack_id", "direction", "complete_status"]))

    def test_sample_3_right_true_move_down(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "right",
                                                                "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state,
                         AjanAgentState("Drone", 100, {"rack_id": 2, "direction": "right", "complete_status": True},
                                        ["rack_id", "direction", "complete_status"]))

    def test_sample_3_right_true_move_left(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "right",
                                                                "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state,
                         AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "left", "complete_status": True},
                                        ["rack_id", "direction", "complete_status"]))

    def test_sample_3_right_true_perceive(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "right",
                                                                "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = self.drone_transition_model.sample(state, action)
        self.assertIn(next_state,
                      [AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "right", "complete_status": True},
                                      ["rack_id", "direction", "complete_status"]),
                       AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "right", "complete_status": False},
                                      ["rack_id", "direction", "complete_status"])])

    def test_sample_3_right_false_move_right(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "right",
                                                                "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state,
                         AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "right", "complete_status": False},
                                        ["rack_id", "direction", "complete_status"]))

    def test_sample_3_right_false_move_up(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "right",
                                                                "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state,
                         AjanAgentState("Drone", 100, {"rack_id": 4, "direction": "right", "complete_status": False},
                                        ["rack_id", "direction", "complete_status"]))

    def test_sample_3_right_false_move_down(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "right",
                                                                "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state,
                         AjanAgentState("Drone", 100, {"rack_id": 2, "direction": "right", "complete_status": False},
                                        ["rack_id", "direction", "complete_status"]))

    def test_sample_3_right_false_move_left(self):
        state = AjanOOState({100: AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "right",
                                                                "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = self.drone_transition_model.sample(state, action)
        self.assertEqual(next_state,
                         AjanAgentState("Drone", 100, {"rack_id": 3, "direction": "left", "complete_status": False},
                                        ["rack_id", "direction", "complete_status"]))

    # endregion


if __name__ == '__main__':
    unittest.main()
