import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanOOState, AjanAgentState
from POMDPService.ajan_pomdp_planning.oopomdp.models.reward_model import AjanRewardModel
from tests.test_inspection_models.helpers.drone_reward_model_queries import SAMPLE_QUERY_D_R, ARGMAX_QUERY_D_R, \
    PROBABILITY_QUERY_D_R, DATA_D_R

Perceive = AjanAction("perceive")
MoveLeft = AjanAction("move", {"motion": "left"})
MoveRight = AjanAction("move", {"motion": "right"})
MoveUp = AjanAction("move", {"motion": "up"})
MoveDown = AjanAction("move", {"motion": "down"})


class TestDroneRewardModelSample(unittest.TestCase):
    reward_model = AjanRewardModel(DATA_D_R, None, PROBABILITY_QUERY_D_R, SAMPLE_QUERY_D_R, ARGMAX_QUERY_D_R)

    # region perceive - valid

    def test_sample_1_left_false_perceive_1_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, 10)

    def test_sample_1_right_false_perceive_1_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, 10)

    def test_sample_2_left_false_perceive_2_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, 10)

    def test_sample_2_right_false_perceive_2_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, 10)

    def test_sample_3_left_false_perceive_3_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, 10)

    def test_sample_3_right_false_perceive_3_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, 10)

    def test_sample_4_left_false_perceive_4_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, 10)

    def test_sample_4_right_false_perceive_4_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, 10)

    def test_sample_1_left_false_perceive_1_left_true(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "left",
                                                       "complete_status": True},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, 1000)

    def test_sample_1_right_false_perceive_1_right_true(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "right",
                                                       "complete_status": True},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, 1000)

    def test_sample_2_left_false_perceive_2_left_true(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "left",
                                                       "complete_status": True},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, 1000)

    def test_sample_2_right_false_perceive_2_right_true(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "right",
                                                       "complete_status": True},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, 1000)

    def test_sample_3_left_false_perceive_3_left_true(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "left",
                                                       "complete_status": True},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, 1000)

    def test_sample_3_right_false_perceive_3_right_true(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "right",
                                                       "complete_status": True},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, 1000)

    def test_sample_4_left_false_perceive_4_left_true(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "left",
                                                       "complete_status": True},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, 1000)

    def test_sample_4_right_false_perceive_4_right_true(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = Perceive
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "right",
                                                       "complete_status": True},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, 1000)

    # endregion

    # region move left - valid

    def test_sample_1_left_false_move_left_1_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, -1000)

    def test_sample_1_right_false_move_left_1_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, 0)

    def test_sample_2_left_false_move_left_2_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, -1000)

    def test_sample_2_right_false_move_left_2_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, 0)

    def test_sample_3_left_false_move_left_3_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, -1000)

    def test_sample_3_right_false_move_left_3_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, 0)

    def test_sample_4_left_false_move_left_4_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)

        self.assertEqual(reward, -1000)

    def test_sample_4_right_false_move_left_4_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveLeft
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)

        self.assertEqual(reward, 0)

    # endregion

    # region move right - valid

    def test_sample_1_left_false_move_right_1_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)

        self.assertEqual(reward, 0)

    def test_sample_1_right_false_move_right_1_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)

        self.assertEqual(reward, -1000)

    def test_sample_2_left_false_move_right_2_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)

        self.assertEqual(reward, 0)

    def test_sample_2_right_false_move_right_2_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)

        self.assertEqual(reward, -1000)

    def test_sample_3_left_false_move_right_3_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)

        self.assertEqual(reward, 0)

    def test_sample_3_right_false_move_right_3_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)

        self.assertEqual(reward, -1000)

    def test_sample_4_left_false_move_right_4_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)

        self.assertEqual(reward, 0)

    def test_sample_4_right_false_move_right_4_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveRight
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)

        self.assertEqual(reward, -1000)

    # endregion

    # region move up - valid

    def test_sample_1_left_false_move_up_2_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)

        self.assertEqual(reward, -10)

    def test_sample_1_right_false_move_up_2_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)

        self.assertEqual(reward, -10)

    def test_sample_2_left_false_move_up_3_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)

        self.assertEqual(reward, -10)

    def test_sample_2_right_false_move_up_3_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)

        self.assertEqual(reward, -10)

    def test_sample_3_left_false_move_up_4_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)

        self.assertEqual(reward, -10)

    def test_sample_3_right_false_move_up_4_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)

        self.assertEqual(reward, -10)

    def test_sample_4_left_false_move_up_4_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)

        self.assertEqual(reward, -1010)  # -1000 (for moving in boundary) - 10 (for moving up while not complete)

    def test_sample_4_right_false_move_up_4_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveUp
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 4, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)

        self.assertEqual(reward, -1010)

    # endregion

    # region move down - valid

    def test_sample_1_left_false_move_down_1_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, -1010)

    def test_sample_1_right_false_move_down_1_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 1, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, -1010)

    def test_sample_2_left_false_move_down_1_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, -10)

    def test_sample_2_right_false_move_down_1_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 2, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 1, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, -10)

    def test_sample_3_left_false_move_down_2_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, -10)

    def test_sample_3_right_false_move_down_2_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 3, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 2, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, -10)

    def test_sample_4_left_false_move_down_3_left_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "left",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "left",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, -10)

    def test_sample_4_right_false_move_down_3_right_false(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"rack_id": 4, "direction": "right",
                                                          "complete_status": False},
                                                         ["rack_id", "direction", "complete_status"])})
        action = MoveDown
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"rack_id": 3, "direction": "right",
                                                       "complete_status": False},
                                                      ["rack_id", "direction", "complete_status"])})
        reward = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(reward, -10)

    # endregion


if __name__ == '__main__':
    unittest.main()
