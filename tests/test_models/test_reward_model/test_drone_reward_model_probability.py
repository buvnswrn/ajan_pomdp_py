import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanAgentState, AjanOOState
from POMDPService.ajan_pomdp_planning.oopomdp.models.reward_model import AjanRewardModel
from tests.test_models.helpers.drone_reward_model_queries import DATA, PROBABILITY_QUERY, SAMPLE_QUERY, ARGMAX_QUERY


class TestDroneRewardModelProbability(unittest.TestCase):
    drone_reward_model = AjanRewardModel(DATA, None, PROBABILITY_QUERY,
                                         SAMPLE_QUERY, ARGMAX_QUERY)

    def test_probability_true_true_perceive(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("perceive")
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(0, current_state, action, next_state), 1.0)

    def test_probability_true_true_perceive_wrong(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("perceive")
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(1000, current_state, action, next_state), 0.0)

    def test_probability_true_false_perceive(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("perceive")
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(0, current_state, action, next_state), 1.0)

    def test_probability_true_false_perceive_wrong(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("perceive")
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(1000, current_state, action, next_state), 0.0)

    def test_probability_false_true_perceive(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("perceive")
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(1000, current_state, action, next_state), 1.0)

    def test_probability_false_true_perceive_wrong(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("perceive")
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(0, current_state, action, next_state), 0.0)

    def test_probability_false_false_perceive(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("perceive")
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(0, current_state, action, next_state), 1.0)

    def test_probability_false_false_perceive_wrong(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("perceive")
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(1000, current_state, action, next_state), 0.0)

    def test_probability_false_false_move_left(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "left"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(0, current_state, action, next_state), 1.0)

    def test_probability_false_false_move_left_wrong(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "left"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(1000, current_state, action, next_state), 0.0)

    def test_probability_true_false_move_left(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "left"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(0, current_state, action, next_state), 1.0)

    def test_probability_true_false_move_left_wrong(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "left"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(1000, current_state, action, next_state), 0.0)

    def test_probability_true_true_move_left(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "left"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(0, current_state, action, next_state), 1.0)

    def test_probability_true_true_move_left_wrong(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "left"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(1000, current_state, action, next_state), 0.0)

    def test_probability_false_true_move_left(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "left"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(0, current_state, action, next_state), 1.0)

    def test_probability_false_true_move_left_wrong(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "left"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(1000, current_state, action, next_state), 0.0)

    def test_probability_false_false_move_right(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(0, current_state, action, next_state), 1.0)

    def test_probability_false_false_move_right_wrong(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(1000, current_state, action, next_state), 0.0)

    def test_probability_true_false_move_right(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(0, current_state, action, next_state), 1.0)

    def test_probability_true_false_move_right_wrong(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(1000, current_state, action, next_state), 0.0)

    def test_probability_true_true_move_right(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(0, current_state, action, next_state), 1.0)

    def test_probability_true_true_move_right_wrong(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(1000, current_state, action, next_state), 0.0)

    def test_probability_false_true_move_right(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(0, current_state, action, next_state), 1.0)

    def test_probability_false_true_move_right_wrong(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                      ["gesture_found", "pose"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found", "pose"])})
        self.assertEqual(self.drone_reward_model.probability(1000, current_state, action, next_state), 0.0)

    def test_probability_true_none_move_right(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": None},
                                                      ["gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                         ["gesture_found"])})
        self.assertEqual(self.drone_reward_model.probability(0, current_state, action, next_state), 1.0)

    def test_probability_true_none_move_right_wrong(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": None},
                                                      ["gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True},
                                                         ["gesture_found"])})
        self.assertEqual(self.drone_reward_model.probability(1000, current_state, action, next_state), 0.0)

    def test_probability_false_none_move_right(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": None},
                                                      ["gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found"])})
        self.assertEqual(self.drone_reward_model.probability(0, current_state, action, next_state), 1.0)

    def test_probability_false_none_move_right_wrong(self):
        next_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                      {"id": 100, "pose": (0, 0), "gesture_found": None},
                                                      ["gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False},
                                                         ["gesture_found"])})
        self.assertEqual(self.drone_reward_model.probability(1000, current_state, action, next_state), 0.0)


if __name__ == '__main__':
    unittest.main()
