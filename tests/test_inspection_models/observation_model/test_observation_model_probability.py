import statistics
import unittest

import numpy as np
import rdflib
from rdflib.plugins.sparql import CUSTOM_EVALS
import CustomSPARQLFunctions.math as custom_functions
import CustomSPARQLFunctions.semantic_fields as semantic_fields
from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.observation import AjanObservation
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanEnvObjectState
from POMDPService.ajan_pomdp_planning.oopomdp.models.observation_model import AjanObservationModel
from tests.test_inspection_models.helpers.observation_model_queries import PROBABILITY_QUERY_OBS, SAMPLE_QUERY_OBS, \
    ARGMAX_QUERY_OBS, DATA_OBS

Perceive = AjanAction("perceive")
MoveLeft = AjanAction("move", {"motion": "left"})
MoveRight = AjanAction("move", {"motion": "right"})
MoveUp = AjanAction("move", {"motion": "up"})
MoveDown = AjanAction("move", {"motion": "down"})


class TestObservationModelProbability(unittest.TestCase):
    observation_model = AjanObservationModel(DATA_OBS, None, PROBABILITY_QUERY_OBS, SAMPLE_QUERY_OBS, ARGMAX_QUERY_OBS)
    # Initial delay is expected, so loading plugins here.
    # Without this in testcases the query fails in run mode, but succeeds in debug and ajan mode.
    rdflib.plugins.sparql.CUSTOM_EVALS["sample_values"] = custom_functions.sample_values
    rdflib.plugins.sparql.CUSTOM_EVALS["math_dist"] = custom_functions.distance
    rdflib.plugins.sparql.CUSTOM_EVALS["semantic_field_near"] = semantic_fields.near

    def test_probability_1_0_perceive_one_box(self):
        state = AjanEnvObjectState("Shelf", 115, {"rack_id": 1, "inspection_state": 0}, ["rack_id", "inspection_state"])
        action = Perceive
        observation = AjanObservation({"object_id": 0,
                                       "objects": ("Box_1",),
                                       "Box_1": (1.996646e+02, 3.677877e+02, 2.317814e+02, 2.210151e+02),
                                       "Box_1_probability": 5.637725e-01,
                                       "average_probability": 5.637725e-01,
                                       }, ["object_id", "objects"])

        probability = self.observation_model.probability(observation, state, action)
        self.assertEqual(probability, 5.637725e-01)  # add assertion here

    def test_probability_1_0_perceive_more_box(self):
        state = AjanEnvObjectState("Shelf", 115, {"rack_id": 1, "inspection_state": 0}, ["rack_id", "inspection_state"])
        action = Perceive
        observation = AjanObservation({"object_id": 0,
                                       "objects": ["Box_1", "Box_2"],
                                       "Box_1": (1.996646e+02, 3.677877e+02, 2.317814e+02, 2.210151e+02),
                                       "Box_1_probability": 5.637725e-01,
                                       "Box_2": (1.996646e+02, 3.677877e+02, 2.317814e+02, 2.210151e+02),
                                       "Box_2_probability": 4.637725e-01,
                                       "average_probability": 5.137725e-01,
                                       }, ["object_id", "objects"])

        probability = self.observation_model.probability(observation, state, action)
        self.assertEqual(probability, statistics.mean([5.637725e-01, 4.637725e-01]))

    def test_probability_1_0_perceive_no_box(self):
        state = AjanEnvObjectState("Shelf", 115, {"rack_id": 1, "inspection_state": 0}, ["rack_id", "inspection_state"])
        action = Perceive
        observation = AjanObservation({"object_id": 0,
                                       "objects": [],
                                       "average_probability": 0.0,
                                       }, ["object_id", "objects"])

        probability = self.observation_model.probability(observation, state, action)
        self.assertEqual(probability, 0.0)

    def test_probability_1_0_move_left_more_box(self):
        state = AjanEnvObjectState("Shelf", 115, {"rack_id": 1, "inspection_state": 0}, ["rack_id", "inspection_state"])
        action = MoveLeft
        observation = AjanObservation({"object_id": 0,
                                       "objects": ["Box_1", "Box_2"],
                                       "Box_1": (1.996646e+02, 3.677877e+02, 2.317814e+02, 2.210151e+02),
                                       "Box_1_probability": 5.637725e-01,
                                       "Box_2": (1.996646e+02, 3.677877e+02, 2.317814e+02, 2.210151e+02),
                                       "Box_2_probability": 4.637725e-01,
                                       "average_probability": 5.137725e-01,
                                       }, ["object_id", "objects"])

        probability = self.observation_model.probability(observation, state, action)
        self.assertEqual(probability, 0.0)

    def test_probability_1_0_move_up_no_box(self):
        state = AjanEnvObjectState("Shelf", 115, {"rack_id": 1, "inspection_state": 0}, ["rack_id", "inspection_state"])
        action = MoveUp
        observation = AjanObservation({"object_id": 0,
                                       "objects": [],
                                       "average_probability": 0.0,
                                       }, ["object_id", "objects"])

        probability = self.observation_model.probability(observation, state, action)
        self.assertEqual(probability, 0.0)

    def test_probability_1_0_move_down_more_box(self):
        state = AjanEnvObjectState("Shelf", 115, {"rack_id": 1, "inspection_state": 0}, ["rack_id", "inspection_state"])
        action = MoveDown
        observation = AjanObservation({"object_id": 0,
                                       "objects": ["Box_1", "Box_2"],
                                       "Box_1": (1.996646e+02, 3.677877e+02, 2.317814e+02, 2.210151e+02),
                                       "Box_1_probability": 5.637725e-01,
                                       "Box_2": (1.996646e+02, 3.677877e+02, 2.317814e+02, 2.210151e+02),
                                       "Box_2_probability": 4.637725e-01,
                                       "average_probability": 5.137725e-01,
                                       }, ["object_id", "objects"])

        probability = self.observation_model.probability(observation, state, action)
        self.assertEqual(probability, 0.0)

    def test_probability_1_0_move_right_no_box(self):
        state = AjanEnvObjectState("Shelf", 115, {"rack_id": 1, "inspection_state": 0}, ["rack_id", "inspection_state"])
        action = MoveRight
        observation = AjanObservation({"object_id": 0,
                                       "objects": [],
                                       "average_probability": 0.0,
                                       }, ["object_id", "objects"])

        probability = self.observation_model.probability(observation, state, action)
        self.assertEqual(probability, 0.0)

    def test_probability_1_0_move_right_more_box(self):
        state = AjanEnvObjectState("Shelf", 115, {"rack_id": 1, "inspection_state": 0}, ["rack_id", "inspection_state"])
        action = MoveRight
        observation = AjanObservation({"object_id": 0,
                                       "objects": ["Box_1", "Box_2"],
                                       "Box_1": (1.996646e+02, 3.677877e+02, 2.317814e+02, 2.210151e+02),
                                       "Box_1_probability": 5.637725e-01,
                                       "Box_2": (1.996646e+02, 3.677877e+02, 2.317814e+02, 2.210151e+02),
                                       "Box_2_probability": 4.637725e-01,
                                       "average_probability": 5.137725e-01,
                                       }, ["object_id", "objects"])

        probability = self.observation_model.probability(observation, state, action)
        self.assertEqual(probability, 0.0)

    def test_probability_1_0_move_left_no_box(self):
        state = AjanEnvObjectState("Shelf", 115, {"rack_id": 1, "inspection_state": 0}, ["rack_id", "inspection_state"])
        action = MoveLeft
        observation = AjanObservation({"object_id": 0,
                                       "objects": [],
                                       "average_probability": 0.0,
                                       }, ["object_id", "objects"])

        probability = self.observation_model.probability(observation, state, action)
        self.assertEqual(probability, 0.0)


if __name__ == '__main__':
    unittest.main()
