import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanOOState, AjanEnvObjectState
from POMDPService.ajan_pomdp_planning.oopomdp.models.transition_model import AjanTransitionModel
from tests.test_models.helpers.person_transition_model_queries import DATA, SAMPLE_QUERY, PROBABILITY_QUERY, \
    ARGMAX_QUERY


class TestPersonTransitionModelSample(unittest.TestCase):
    person_transition_model = AjanTransitionModel(112, DATA, None, PROBABILITY_QUERY, SAMPLE_QUERY, ARGMAX_QUERY)

    def test_sample_right_perceive(self):
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {'id': 112, 'gesture': 'right', 'pose': None})})
        action = AjanAction("perceive")
        sampled_state = self.person_transition_model.sample(current_state, action)
        self.assertIn(sampled_state, [AjanEnvObjectState("Person", 112,
                                                         {"id": 112, "gesture": 'right', 'pose': None}),
                                      AjanEnvObjectState("Person", 112,
                                                         {"id": 112, "gesture": 'left', 'pose': None}),
                                      AjanEnvObjectState("Person", 112,
                                                         {"id": 112, "gesture": None, 'pose': None})])

    def test_sample_left_perceive(self):
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {'id': 112, 'gesture': 'left', 'pose': None})})
        action = AjanAction("perceive")
        sampled_state = self.person_transition_model.sample(current_state, action)
        self.assertIn(sampled_state, [AjanEnvObjectState("Person", 112,
                                                         {"id": 112, "gesture": 'right', 'pose': None}),
                                      AjanEnvObjectState("Person", 112,
                                                         {"id": 112, "gesture": 'left', 'pose': None}),
                                      AjanEnvObjectState("Person", 112,
                                                         {"id": 112, "gesture": None, 'pose': None})])

    def test_sample_none_perceive(self):
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {'id': 112, 'gesture': None, 'pose': None})})
        action = AjanAction("perceive")
        sampled_state = self.person_transition_model.sample(current_state, action)
        self.assertIn(sampled_state, [AjanEnvObjectState("Person", 112,
                                                         {"id": 112, "gesture": 'right', 'pose': None}),
                                      AjanEnvObjectState("Person", 112,
                                                         {"id": 112, "gesture": 'left', 'pose': None}),
                                      AjanEnvObjectState("Person", 112,
                                                         {"id": 112, "gesture": None, 'pose': None})])

    def test_sample_right_move_right(self):
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {'id': 112, 'gesture': 'right', 'pose': None})})
        action = AjanAction("move", {"motion": "right"})
        sampled_state = self.person_transition_model.sample(current_state, action)
        self.assertEqual(sampled_state, AjanEnvObjectState("Person", 112,
                                                           {"id": 112, "gesture": 'right', 'pose': None}))

    def test_sample_left_move_right(self):
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {'id': 112, 'gesture': 'left', 'pose': None})})
        action = AjanAction("move", {"motion": "right"})
        sampled_state = self.person_transition_model.sample(current_state, action)
        self.assertEqual(sampled_state, AjanEnvObjectState("Person", 112,
                                                           {"id": 112, "gesture": 'left', 'pose': None}))

    def test_sample_none_move_right(self):
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {'id': 112, 'gesture': None, 'pose': None})})
        action = AjanAction("move", {"motion": "right"})
        sampled_state = self.person_transition_model.sample(current_state, action)
        self.assertEqual(sampled_state, AjanEnvObjectState("Person", 112,
                                                           {"id": 112, "gesture": None, 'pose': None}))

    def test_sample_right_move_left(self):
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {'id': 112, 'gesture': 'right', 'pose': None})})
        action = AjanAction("move", {"motion": "left"})
        sampled_state = self.person_transition_model.sample(current_state, action)
        self.assertEqual(sampled_state, AjanEnvObjectState("Person", 112,
                                                           {"id": 112, "gesture": 'right', 'pose': None}))

    def test_sample_left_move_left(self):
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {'id': 112, 'gesture': 'left', 'pose': None})})
        action = AjanAction("move", {"motion": "left"})
        sampled_state = self.person_transition_model.sample(current_state, action)
        self.assertEqual(sampled_state, AjanEnvObjectState("Person", 112,
                                                           {"id": 112, "gesture": 'left', 'pose': None}))

    def test_sample_none_move_left(self):
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {'id': 112, 'gesture': None, 'pose': None})})
        action = AjanAction("move", {"motion": "left"})
        sampled_state = self.person_transition_model.sample(current_state, action)
        self.assertEqual(sampled_state, AjanEnvObjectState("Person", 112,
                                                           {"id": 112, "gesture": None, 'pose': None}))

    def test_sample_right_move_right_with_pose(self):
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {'id': 112, 'gesture': 'right', 'pose': (0, 0)})})
        action = AjanAction("move", {"motion": "right"})
        sampled_state = self.person_transition_model.sample(current_state, action)
        self.assertEqual(sampled_state, AjanEnvObjectState("Person", 112,
                                                           {"id": 112, "gesture": 'right', 'pose': (0, 0)}))

    def test_sample_left_move_right_with_pose(self):
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {'id': 112, 'gesture': 'left', 'pose': (0, 0)})})
        action = AjanAction("move", {"motion": "right"})
        sampled_state = self.person_transition_model.sample(current_state, action)
        self.assertEqual(sampled_state, AjanEnvObjectState("Person", 112,
                                                           {"id": 112, "gesture": 'left', 'pose': (0, 0)}))

    def test_sample_none_move_right_with_pose(self):
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {'id': 112, 'gesture': None, 'pose': (0, 0)})})
        action = AjanAction("move", {"motion": "right"})
        sampled_state = self.person_transition_model.sample(current_state, action)
        self.assertEqual(sampled_state, AjanEnvObjectState("Person", 112,
                                                           {"id": 112, "gesture": None, 'pose': (0, 0)}))

    def test_sample_right_move_left_with_pose(self):
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {'id': 112, 'gesture': 'right', 'pose': (0, 0)})})
        action = AjanAction("move", {"motion": "left"})
        sampled_state = self.person_transition_model.sample(current_state, action)
        self.assertEqual(sampled_state, AjanEnvObjectState("Person", 112,
                                                           {"id": 112, "gesture": 'right', 'pose': (0, 0)}))

    def test_sample_left_move_left_with_pose(self):
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {'id': 112, 'gesture': 'left', 'pose': (0, 0)})})
        action = AjanAction("move", {"motion": "left"})
        sampled_state = self.person_transition_model.sample(current_state, action)
        self.assertEqual(sampled_state, AjanEnvObjectState("Person", 112,
                                                           {"id": 112, "gesture": 'left', 'pose': (0, 0)}))

    def test_sample_none_move_left_with_pose(self):
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {'id': 112, 'gesture': None, 'pose': (0, 0)})})
        action = AjanAction("move", {"motion": "left"})
        sampled_state = self.person_transition_model.sample(current_state, action)
        self.assertEqual(sampled_state, AjanEnvObjectState("Person", 112,
                                                           {"id": 112, "gesture": None, 'pose': (0, 0)}))

    def test_sample_right_perceive_with_pose(self):
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {'id': 112,
                                                              'gesture': 'right',
                                                              'pose': (0, 0)})})
        action = AjanAction("perceive")
        sampled_state = self.person_transition_model.sample(current_state, action)
        self.assertIn(sampled_state, [AjanEnvObjectState("Person", 112,
                                                         {"id": 112, "gesture": 'right', 'pose': None}),
                                      AjanEnvObjectState("Person", 112,
                                                         {"id": 112, "gesture": 'left', 'pose': None}),
                                      AjanEnvObjectState("Person", 112,
                                                         {"id": 112, "gesture": None, 'pose': None})])

    def test_sample_left_perceive_with_pose(self):
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {'id': 112,
                                                              'gesture': 'left',
                                                              'pose': (0, 0)})})
        action = AjanAction("perceive")
        sampled_state = self.person_transition_model.sample(current_state, action)
        self.assertIn(sampled_state, [AjanEnvObjectState("Person", 112,
                                                         {"id": 112, "gesture": 'right', 'pose': None}),
                                      AjanEnvObjectState("Person", 112,
                                                         {"id": 112, "gesture": 'left', 'pose': None}),
                                      AjanEnvObjectState("Person", 112,
                                                         {"id": 112, "gesture": None, 'pose': None})])

    def test_sample_none_perceive_with_pose(self):
        current_state = AjanOOState({112: AjanEnvObjectState("Person", 112,
                                                             {'id': 112,
                                                              'gesture': None,
                                                              'pose': (0, 0)})})
        action = AjanAction("perceive")
        sampled_state = self.person_transition_model.sample(current_state, action)
        self.assertIn(sampled_state, [AjanEnvObjectState("Person", 112,
                                                         {"id": 112, "gesture": 'right', 'pose': None}),
                                      AjanEnvObjectState("Person", 112,
                                                         {"id": 112, "gesture": 'left', 'pose': None}),
                                      AjanEnvObjectState("Person", 112,
                                                         {"id": 112, "gesture": None, 'pose': None})])


if __name__ == '__main__':
    unittest.main()
