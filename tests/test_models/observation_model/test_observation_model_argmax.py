import unittest


import unittest
import rdflib
from rdflib.plugins.sparql import CUSTOM_EVALS

import CustomSPARQLFunctions.math as custom_functions
import CustomSPARQLFunctions.semantic_fields as semantic_fields
from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanEnvObjectState
from POMDPService.ajan_pomdp_planning.oopomdp.models.observation_model import AjanObservationModel
from tests.test_models.helpers.observation_model_queries import DATA, PROBABILITY_QUERY, SAMPLE_QUERY, ARGMAX_QUERY


class TestObservationModelArgmax(unittest.TestCase):
    observation_model = AjanObservationModel(DATA, None, PROBABILITY_QUERY, SAMPLE_QUERY, ARGMAX_QUERY)
    rdflib.plugins.sparql.CUSTOM_EVALS["sample_values"] = custom_functions.sample_values
    rdflib.plugins.sparql.CUSTOM_EVALS["math_dist"] = custom_functions.distance
    rdflib.plugins.sparql.CUSTOM_EVALS["semantic_field_near"] = semantic_fields.near

    def test_sample_right_perceive(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "right"})
        action = AjanAction("perceive")
        observation = self.observation_model.argmax(state, action)
        print(observation.attributes["pose"])

    def test_sample_left_perceive(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "left"})
        action = AjanAction("perceive")
        observation = self.observation_model.argmax(state, action)
        print(observation.attributes["pose"])

    def test_sample_none_perceive(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": None})
        action = AjanAction("perceive")
        observation = self.observation_model.argmax(state, action)
        print(observation.attributes["pose"])

    def test_sample_right_move_right(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "right"})
        action = AjanAction("move", {"motion": "right"})
        observation = self.observation_model.argmax(state, action)
        print(observation.attributes["pose"])
        self.assertEqual(observation.attributes["pose"], None)

    def test_sample_left_move_right(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "left"})
        action = AjanAction("move", {"motion": "right"})
        observation = self.observation_model.argmax(state, action)
        print(observation.attributes["pose"])
        self.assertEqual(observation.attributes["pose"], None)

    def test_sample_none_move_right(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": None})
        action = AjanAction("move", {"motion": "right"})
        observation = self.observation_model.argmax(state, action)
        print(observation.attributes["pose"])
        self.assertEqual(observation.attributes["pose"], None)

    def test_sample_left_move_left(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "left"})
        action = AjanAction("move", {"motion": "left"})
        observation = self.observation_model.argmax(state, action)
        print(observation.attributes["pose"])
        self.assertEqual(observation.attributes["pose"], None)

    def test_sample_none_move_left(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": None})
        action = AjanAction("move", {"motion": "left"})
        observation = self.observation_model.argmax(state, action)
        print(observation.attributes["pose"])
        self.assertEqual(observation.attributes["pose"], None)

    def test_sample_right_move_left(self):
        state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "right"})
        action = AjanAction("move", {"motion": "left"})
        observation = self.observation_model.argmax(state, action)
        print(observation.attributes["pose"])
        self.assertEqual(observation.attributes["pose"], None)


if __name__ == '__main__':
    unittest.main()
