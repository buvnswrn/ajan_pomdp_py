import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanEnvObjectState
from POMDPService.ajan_pomdp_planning.oopomdp.models.observation_model import AjanObservationModel
from tests.test_inspection_models.helpers.observation_model_queries import ARGMAX_QUERY_OBS, SAMPLE_QUERY_OBS, \
    PROBABILITY_QUERY_OBS, DATA_OBS

Perceive = AjanAction("perceive")
MoveLeft = AjanAction("move", {"motion": "left"})
MoveRight = AjanAction("move", {"motion": "right"})
MoveUp = AjanAction("move", {"motion": "up"})
MoveDown = AjanAction("move", {"motion": "down"})

class TestObservationModelSample(unittest.TestCase):

    observation_model = AjanObservationModel(DATA_OBS, None, PROBABILITY_QUERY_OBS, SAMPLE_QUERY_OBS, ARGMAX_QUERY_OBS)

    def test_sample_1_0_perceive(self):

        state = AjanEnvObjectState("Shelf", 115, {"rack_id": 1, "inspection_state": 0}, ["rack_id", "inspection_state"])
        action = Perceive
        observation = self.observation_model.sample(state, action)
        print(observation.attributes["objects"])
        self.assertNotEqual(observation.attributes["objects"], None)  # add assertion here


if __name__ == '__main__':
    unittest.main()
