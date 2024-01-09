import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanAgentState, AjanOOState
from POMDPService.ajan_pomdp_planning.oopomdp.models.transition_model import AjanTransitionModel
from tests.test_models.alternate_models.python_transition_model import TransitionModel
from tests.test_models.helpers.drone_transition_model_queries import DATA_D_T, SAMPLE_QUERY_D_T, ARGMAX_QUERY_D_T, PROBABILITY_QUERY_D_T


class TestDroneTransitionModelSample(unittest.TestCase):
    drone_transition_model = AjanTransitionModel(100, DATA_D_T, None, PROBABILITY_QUERY_D_T, SAMPLE_QUERY_D_T, ARGMAX_QUERY_D_T)
    # drone_transition_model = TransitionModel("drone", 100)

    def test_sample_true_perceive(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True}, ["pose", "gesture_found"])})
        action = AjanAction("perceive")
        sampled_state = self.drone_transition_model.sample(current_state, action)
        self.assertIn(sampled_state, [AjanAgentState("Drone", 100, {"id": 100, "pose": (0, 0), "gesture_found": True}, ["pose", "gesture_found"]),
                                      AjanAgentState("Drone", 100, {"id": 100, "pose": (0, 0), "gesture_found": False}, ["pose", "gesture_found"])])

    def test_sample_false_perceive(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False}, ["pose", "gesture_found"])})
        action = AjanAction("perceive")
        sampled_state = self.drone_transition_model.sample(current_state, action)
        self.assertIn(sampled_state, [AjanAgentState("Drone", 100, {"id": 100, "pose": (0, 0), "gesture_found": True}, ["pose", "gesture_found"]),
                                      AjanAgentState("Drone", 100, {"id": 100, "pose": (0, 0), "gesture_found": False}, ["pose", "gesture_found"])])

    def test_sample_false_perceive_without_pose(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": None, "gesture_found": False}, ["pose", "gesture_found"])})
        action = AjanAction("perceive")
        sampled_state = self.drone_transition_model.sample(current_state, action)
        self.assertIn(sampled_state, [AjanAgentState("Drone", 100, {"id": 100, "pose": None, "gesture_found": True}, ["pose", "gesture_found"]),
                                      AjanAgentState("Drone", 100, {"id": 100, "pose": None, "gesture_found": False}, ["pose", "gesture_found"])])

    def test_sample_true_perceive_without_pose(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": None, "gesture_found": True}, ["pose", "gesture_found"])})
        action = AjanAction("perceive")
        sampled_state = self.drone_transition_model.sample(current_state, action)
        self.assertIn(sampled_state, [AjanAgentState("Drone", 100, {"id": 100, "pose": None, "gesture_found": True}, ["pose", "gesture_found"]),
                                      AjanAgentState("Drone", 100, {"id": 100, "pose": None, "gesture_found": False}, ["pose", "gesture_found"])])

    def test_sample_false_move_right(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        sampled_state = self.drone_transition_model.sample(current_state, action) 
        self.assertEqual(sampled_state, AjanAgentState("Drone", 100,
                                                       {"id": 100, "pose": (1, 1), "gesture_found": False}, ["pose", "gesture_found"]))
    
    def test_sample_true_move_right(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        sampled_state = self.drone_transition_model.sample(current_state, action)
        self.assertEqual(sampled_state, AjanAgentState("Drone", 100,
                                                       {"id": 100, "pose": (1, 1), "gesture_found": False}, ["pose", "gesture_found"]))
    
    def test_sample_false_move_left(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": False}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "left"})
        sampled_state = self.drone_transition_model.sample(current_state, action)
        self.assertEqual(sampled_state, AjanAgentState("Drone", 100,
                                                       {"id": 100, "pose": (-1, 1), "gesture_found": False}, ["pose", "gesture_found"]))
    
    def test_sample_true_move_left(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": (0, 0), "gesture_found": True}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "left"})
        sampled_state = self.drone_transition_model.sample(current_state, action)
        self.assertEqual(sampled_state, AjanAgentState("Drone", 100,
                                                       {"id": 100, "pose": (-1, 1), "gesture_found": False}, ["pose", "gesture_found"]))
    
    def test_sample_false_move_right_without_pose(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": None, "gesture_found": False}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        with self.assertRaises(IndexError):
            sampled_state = self.drone_transition_model.sample(current_state, action)
    
    def test_sample_true_move_right_without_pose(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": None, "gesture_found": True}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "right"})
        with self.assertRaises(IndexError):
            sampled_state = self.drone_transition_model.sample(current_state, action)
    
    def test_sample_false_move_left_without_pose(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": None, "gesture_found": False}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "left"})
        with self.assertRaises(IndexError):
            sampled_state = self.drone_transition_model.sample(current_state, action)
    
    def test_sample_true_move_left_without_pose(self):
        current_state = AjanOOState({100: AjanAgentState("Drone", 100,
                                                         {"id": 100, "pose": None, "gesture_found": True}, ["pose", "gesture_found"])})
        action = AjanAction("move", {"motion": "left"})
        with self.assertRaises(IndexError):
            sampled_state = self.drone_transition_model.sample(current_state, action)


if __name__ == '__main__':
    unittest.main()
