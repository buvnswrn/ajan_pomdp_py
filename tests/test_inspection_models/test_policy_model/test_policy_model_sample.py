import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanEnvObjectState, AjanOOState, AjanAgentState
from POMDPService.ajan_pomdp_planning.oopomdp.models.policy_model import AjanPolicyModel
from tests.test_inspection_models.helpers.policy_model_queries import GET_ALL_ACTIONS_QUERY, ROLLOUT_QUERY_POLICY, \
    SAMPLE_QUERY_POLICY, DATA_POLICY

Perceive = AjanAction("perceive")
MoveLeft = AjanAction("move", {"motion": "left"})
MoveRight = AjanAction("move", {"motion": "right"})
MoveUp = AjanAction("move", {"motion": "up"})
MoveDown = AjanAction("move", {"motion": "down"})


class TestPolicyModelSample(unittest.TestCase):

    policy_model = AjanPolicyModel(DATA_POLICY, None, SAMPLE_QUERY_POLICY, ROLLOUT_QUERY_POLICY, GET_ALL_ACTIONS_QUERY)

    def test_sample_2_left_false_2_0(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        print(actions)
        self.assertEqual(actions, Perceive)  # only perceive since that is the best action

    def test_sample_2_left_false_2_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        print(actions)
        self.assertEqual(actions, Perceive)

    def test_sample_2_left_false_2_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        print(actions)
        self.assertIn(actions, [MoveUp, MoveDown])

    def test_sample_3_left_false_3_0(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        print(actions)
        self.assertEqual(actions, Perceive)

    def test_sample_3_left_false_3_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        print(actions)
        self.assertEqual(actions, Perceive)

    def test_sample_3_left_false_3_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        print(actions)
        self.assertIn(actions, [MoveUp, MoveDown])

    def test_sample_4_left_false_4_0(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        print(actions)
        self.assertEqual(actions, Perceive)

    def test_sample_4_left_false_4_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        print(actions)
        self.assertEqual(actions, Perceive)

    def test_sample_4_left_false_4_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        print(actions)
        self.assertEqual(actions, MoveDown)

    def test_sample_2_left_true_2_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveRight)

    def test_sample_2_left_true_2_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertIn(actions, [MoveUp, MoveDown])

    def test_sample_3_left_true_3_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveRight)

    def test_sample_3_left_true_3_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertIn(actions, [MoveUp, MoveDown])

    def test_sample_4_left_true_4_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveRight)

    def test_sample_4_left_true_4_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveDown)

    def test_sample_1_left_false_1_0(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, Perceive)

    def test_sample_1_left_false_1_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, Perceive)

    def test_sample_1_left_false_1_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveUp)

    def test_sample_1_left_true_1_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveRight)

    def test_sample_1_left_true_1_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveUp)

    # def test_sample_1_left_true_1_0(self):
    #     state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
    #                                                  {"rack_id": 1, "inspection_state": 0},
    #                                                  ["rack_id", "inspection_state"]),
    #                          100: AjanAgentState("Drone", 100,
    #                                              {"rack_id": 1, "direction": "left",
    #                                               "complete_status": True},
    #                                              ["rack_id", "direction", "complete_status"])})
    #     actions = self.policy_model.sample(state)
    #     self.assertEqual(actions, MoveRight)

    def test_sample_2_right_false_2_0(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "right",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, Perceive)

    def test_sample_2_right_false_2_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "right",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, Perceive)

    def test_sample_2_right_false_2_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "right",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertIn(actions, [MoveUp, MoveDown])

    def test_sample_3_right_false_3_0(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "right",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, Perceive)

    def test_sample_3_right_false_3_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "right",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, Perceive)

    def test_sample_3_right_false_3_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "right",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertIn(actions, [MoveUp, MoveDown])

    def test_sample_4_right_false_4_0(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "right",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, Perceive)

    def test_sample_4_right_false_4_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "right",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, Perceive)

    def test_sample_4_right_false_4_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "right",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveDown)

    def test_sample_2_right_true_2_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveLeft)

    def test_sample_2_right_true_2_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertIn(actions, [MoveUp, MoveDown])

    def test_sample_3_right_true_3_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveLeft)

    def test_sample_3_right_true_3_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertIn(actions, [MoveUp, MoveDown])

    def test_sample_4_right_true_4_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveLeft)

    def test_sample_4_right_true_4_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveDown)

    def test_sample_1_right_false_1_0(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "right",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, Perceive)

    def test_sample_1_right_false_1_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "right",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, Perceive)

    def test_sample_1_right_false_1_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "right",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveUp)

    def test_sample_1_right_true_1_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveLeft)

    def test_sample_1_right_true_1_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveUp)

    def test_sample_1_right_true_1_0(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveLeft)

    def test_sample_2_right_true_2_0(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveLeft)

    def test_sample_3_right_true_3_0(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveLeft)

    def test_sample_4_right_true_4_0(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "right",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveLeft)

    def test_sample_1_left_true_1_0(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 1, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 1, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveRight)

    def test_sample_2_left_true_2_0(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveRight)

    def test_sample_3_left_true_3_0(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveRight)

    def test_sample_4_left_true_4_0(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.sample(state)
        self.assertEqual(actions, MoveRight)


if __name__ == '__main__':
    unittest.main()
