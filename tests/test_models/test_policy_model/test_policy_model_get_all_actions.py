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


class TestPolicyModelGetAllActions(unittest.TestCase):
    policy_model = AjanPolicyModel(DATA_POLICY, None, SAMPLE_QUERY_POLICY, ROLLOUT_QUERY_POLICY, GET_ALL_ACTIONS_QUERY)

    def test_get_all_actions_None(self):
        actions = self.policy_model.get_all_actions()
        self.assertEqual(set(actions), {Perceive, MoveRight, MoveDown, MoveLeft, MoveUp})

    def test_get_all_actions_2_left_false_2_0(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.get_all_actions(state)
        print(actions)
        self.assertEqual(actions, [Perceive])  # only perceive since that is the best action

    def test_get_all_actions_2_left_false_2_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.get_all_actions(state)
        print(actions)
        self.assertEqual(actions, [Perceive])

    def test_get_all_actions_2_left_false_2_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.get_all_actions(state)
        print(actions)
        self.assertEqual(actions, [MoveUp, MoveDown])

    def test_get_all_actions_3_left_false_3_0(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.get_all_actions(state)
        print(actions)
        self.assertEqual(actions, [Perceive])

    def test_get_all_actions_3_left_false_3_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.get_all_actions(state)
        print(actions)
        self.assertEqual(actions, [Perceive])

    def test_get_all_actions_3_left_false_3_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.get_all_actions(state)
        print(actions)
        self.assertEqual(actions, [MoveUp, MoveDown])

    def test_get_all_actions_4_left_false_4_0(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 0},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.get_all_actions(state)
        print(actions)
        self.assertEqual(actions, [Perceive])

    def test_get_all_actions_4_left_false_4_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.get_all_actions(state)
        print(actions)
        self.assertEqual(actions, [Perceive])

    def test_get_all_actions_4_left_false_4_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "left",
                                                  "complete_status": False},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.get_all_actions(state)
        print(actions)
        self.assertEqual(actions, [MoveDown])

    def test_get_all_actions_2_left_true_2_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.get_all_actions(state)
        self.assertEqual(actions, [MoveRight])

    def test_get_all_actions_2_left_true_2_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 2, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 2, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.get_all_actions(state)
        self.assertEqual(actions, [MoveUp, MoveDown])

    def test_get_all_actions_3_left_true_3_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.get_all_actions(state)
        self.assertEqual(actions, [MoveRight])

    def test_get_all_actions_3_left_true_3_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 3, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 3, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.get_all_actions(state)
        self.assertEqual(actions, [MoveUp, MoveDown])

    def test_get_all_actions_4_left_true_4_1(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 1},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.get_all_actions(state)
        self.assertEqual(actions, [MoveRight])

    def test_get_all_actions_4_left_true_4_2(self):
        state = AjanOOState({112: AjanEnvObjectState("Shelf", 115,
                                                     {"rack_id": 4, "inspection_state": 2},
                                                     ["rack_id", "inspection_state"]),
                             100: AjanAgentState("Drone", 100,
                                                 {"rack_id": 4, "direction": "left",
                                                  "complete_status": True},
                                                 ["rack_id", "direction", "complete_status"])})
        actions = self.policy_model.get_all_actions(state)
        self.assertEqual(actions, [MoveDown])



if __name__ == '__main__':
    unittest.main()
