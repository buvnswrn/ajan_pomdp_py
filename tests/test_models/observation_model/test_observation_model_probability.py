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
from tests.test_models.helpers.observation_model_queries import DATA, PROBABILITY_QUERY, SAMPLE_QUERY, ARGMAX_QUERY


class TestObservationModelProbability(unittest.TestCase):

    observation_model = AjanObservationModel(DATA, None, PROBABILITY_QUERY, SAMPLE_QUERY, ARGMAX_QUERY)
    rdflib.plugins.sparql.CUSTOM_EVALS["sample_values"] = custom_functions.sample_values
    rdflib.plugins.sparql.CUSTOM_EVALS["math_dist"] = custom_functions.distance
    rdflib.plugins.sparql.CUSTOM_EVALS["semantic_field_near"] = semantic_fields.near

    def test_probability_right_perceive(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "right"})
        action = AjanAction("perceive")
        x_values = np.random.uniform(0, 640, 17)
        y_values = np.random.uniform(0, 480, 17)
        keypoints = np.column_stack((x_values, y_values))
        observation = AjanObservation({"pose": keypoints}, ["pose"])
        probability = self.observation_model.probability(observation, state, action)
        print(probability)
        self.assertNotEqual(probability, 0.0)

    def test_probability_left_perceive(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "left"})
        action = AjanAction("perceive")
        x_values = np.random.uniform(0, 640, 17)
        y_values = np.random.uniform(0, 480, 17)
        keypoints = np.column_stack((x_values, y_values))
        observation = AjanObservation({"pose": keypoints}, ["pose"])
        probability = self.observation_model.probability(observation, state, action)
        print(probability)
        self.assertNotEqual(probability, 0.0)

    def test_probability_none_perceive(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": None})
        action = AjanAction("perceive")
        x_values = np.random.uniform(0, 640, 17)
        y_values = np.random.uniform(0, 480, 17)
        keypoints = np.column_stack((x_values, y_values))
        observation = AjanObservation({"pose": keypoints}, ["pose"])
        probability = self.observation_model.probability(observation, state, action)
        print(probability)
        self.assertEqual(probability, 0.0)

    def test_probability_left_perceive_none(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "left"})
        action = AjanAction("perceive")
        observation = AjanObservation({"pose": None}, ["pose"])
        probability = self.observation_model.probability(observation, state, action)
        print(probability)
        self.assertEqual(probability, 1.0)

    def test_probability_right_perceive_none(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "right"})
        action = AjanAction("perceive")
        observation = AjanObservation({"pose": None}, ["pose"])
        probability = self.observation_model.probability(observation, state, action)
        print(probability)
        self.assertEqual(probability, 1.0)

    def test_probability_none_perceive_none(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": None})
        action = AjanAction("perceive")
        observation = AjanObservation({"pose": None}, ["pose"])
        probability = self.observation_model.probability(observation, state, action)
        print(probability)
        self.assertEqual(probability, 1.0)

    def test_probability_right_move_right(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "right"})
        action = AjanAction("move", {"motion": "right"})
        observation = AjanObservation({"pose": None}, ["pose"])
        probability = self.observation_model.probability(observation, state, action)
        print(probability)
        self.assertEqual(probability, 1.0)

    def test_probability_left_move_right(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "left"})
        action = AjanAction("move", {"motion": "right"})
        observation = AjanObservation({"pose": None}, ["pose"])
        probability = self.observation_model.probability(observation, state, action)
        print(probability)
        self.assertEqual(probability, 1.0)

    def test_probability_none_move_right(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": None})
        action = AjanAction("move", {"motion": "right"})
        observation = AjanObservation({"pose": None}, ["pose"])
        probability = self.observation_model.probability(observation, state, action)
        print(probability)
        self.assertEqual(probability, 1.0)

    def test_probability_left_move_left(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "left"})
        action = AjanAction("move", {"motion": "left"})
        observation = AjanObservation({"pose": None}, ["pose"])
        probability = self.observation_model.probability(observation, state, action)
        print(probability)
        self.assertEqual(probability, 1.0)

    def test_probability_none_move_left(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": None})
        action = AjanAction("move", {"motion": "left"})
        observation = AjanObservation({"pose": None}, ["pose"])
        probability = self.observation_model.probability(observation, state, action)
        print(probability)
        self.assertEqual(probability, 1.0)

    def test_probability_right_move_left(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "right"})
        action = AjanAction("move", {"motion": "left"})
        observation = AjanObservation({"pose": None}, ["pose"])
        probability = self.observation_model.probability(observation, state, action)
        print(probability)
        self.assertEqual(probability, 1.0)

    def test_probability_right_move_right_wrong(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "right"})
        action = AjanAction("move", {"motion": "right"})
        x_values = np.random.uniform(0, 640, 17)
        y_values = np.random.uniform(0, 480, 17)
        keypoints = np.column_stack((x_values, y_values))
        observation = AjanObservation({"pose": keypoints}, ["pose"])
        probability = self.observation_model.probability(observation, state, action)
        print(probability)
        self.assertEqual(probability, 0.0)

    def test_probability_left_move_right_wrong(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "left"})
        action = AjanAction("move", {"motion": "right"})
        x_values = np.random.uniform(0, 640, 17)
        y_values = np.random.uniform(0, 480, 17)
        keypoints = np.column_stack((x_values, y_values))
        observation = AjanObservation({"pose": keypoints}, ["pose"])
        probability = self.observation_model.probability(observation, state, action)
        print(probability)
        self.assertEqual(probability, 0.0)

    def test_probability_none_move_right_wrong(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": None})
        action = AjanAction("move", {"motion": "right"})
        x_values = np.random.uniform(0, 640, 17)
        y_values = np.random.uniform(0, 480, 17)
        keypoints = np.column_stack((x_values, y_values))
        observation = AjanObservation({"pose": keypoints}, ["pose"])
        probability = self.observation_model.probability(observation, state, action)
        print(probability)
        self.assertEqual(probability, 0.0)

    def test_probability_left_move_left_wrong(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "left"})
        action = AjanAction("move", {"motion": "left"})
        x_values = np.random.uniform(0, 640, 17)
        y_values = np.random.uniform(0, 480, 17)
        keypoints = np.column_stack((x_values, y_values))
        observation = AjanObservation({"pose": keypoints}, ["pose"])
        probability = self.observation_model.probability(observation, state, action)
        print(probability)
        self.assertEqual(probability, 0.0)

    def test_probability_none_move_left_wrong(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": None})
        action = AjanAction("move", {"motion": "left"})
        x_values = np.random.uniform(0, 640, 17)
        y_values = np.random.uniform(0, 480, 17)
        keypoints = np.column_stack((x_values, y_values))
        observation = AjanObservation({"pose": keypoints}, ["pose"])
        probability = self.observation_model.probability(observation, state, action)
        print(probability)
        self.assertEqual(probability, 0.0)

    def test_probability_right_move_left_wrong(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "right"})
        action = AjanAction("move", {"motion": "left"})
        x_values = np.random.uniform(0, 640, 17)
        y_values = np.random.uniform(0, 480, 17)
        keypoints = np.column_stack((x_values, y_values))
        observation = AjanObservation({"pose": keypoints}, ["pose"])
        probability = self.observation_model.probability(observation, state, action)
        print(probability)
        self.assertEqual(probability, 0.0)




if __name__ == '__main__':
    unittest.main()
