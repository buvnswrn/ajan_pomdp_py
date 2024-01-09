import unittest

import numpy
import numpy as np
import rdflib
from rdflib.plugins.sparql import CUSTOM_EVALS

import CustomSPARQLFunctions.math as custom_functions
import CustomSPARQLFunctions.semantic_fields as semantic_fields
from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.observation import AjanObservation
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanEnvObjectState
from POMDPService.ajan_pomdp_planning.oopomdp.models.observation_model import AjanObservationModel
from tests.test_models.helpers.drone_agent_data import LEFT_KEYPOINT, RIGHT_KEYPOINT


class TestObservationModel(unittest.TestCase):
    observation_model = None

    sample_query = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX pomdp-ns-data:<http://www.dfki.de/pomdp-ns/POMDP/data/>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX ajan-math-ns:<http://www.ajan.de/ajan/functions/math-ns#>
    
    CONSTRUCT {
        pomdp-ns:Observation pomdp-ns:attributes ?attributes .
        pomdp-ns:Observation pomdp-ns:for_hash ?for_hash .
        ?attributes pomdp-ns1:_person_id ?person_id .
        ?attributes pomdp-ns1:_pose ?poseNode .
        
        ?for_hash rdfs:value "person_id" .
        ?for_hash rdfs:value "pose" .
        
        
        ?poseNode rdfs:type ?poseType .
        
        ?poseNode rdfs:value ?keypoint9.
        ?poseNode rdfs:value ?keypoint10 .
        ?poseNode rdfs:value ?keypoint11 .
        ?poseNode rdfs:value ?keypoint12 .
    
        
        ?keypoint9 rdfs:x ?xValue9 .
        ?keypoint10 rdfs:x ?xValue10 .
        ?keypoint11 rdfs:x ?xValue11 .
        ?keypoint12 rdfs:x ?xValue12 .
        
        ?keypoint9 rdfs:y ?yValue9 .
        ?keypoint10 rdfs:y ?yValue10 .
        ?keypoint11 rdfs:y ?yValue11 .
        ?keypoint12 rdfs:y ?yValue12 .
    
    }
    WHERE{
        pomdp-ns:ObservationModel pomdp-ns:attributes ?attributesNode .
        ?attributesNode pomdp-ns1:_person_id ?person_id .
        pomdp-ns:current_action rdfs:value ?action .
        
        BIND(BNODE() as ?attributes) .
        BIND(BNODE() as ?for_hash) .
        BIND(IF(?action = pomdp-ns1:Action_perceive, BNODE(), rdfs:nil) as ?poseNode) .
        BIND(pomdp-ns-data:Point_9  as ?keypoint9) .
        BIND(pomdp-ns-data:Point_10 as ?keypoint10) .
        BIND(pomdp-ns-data:Point_11 as ?keypoint11) .
        BIND(pomdp-ns-data:Point_12 as ?keypoint12) .
        BIND(pomdp-ns-data:pandasDataFrame as ?poseType)
        BIND(ajan-math-ns:sample(0, 640) as ?xValue9) .
        BIND(ajan-math-ns:sample(0, 480) as ?yValue9) .
        BIND(ajan-math-ns:sample(0, 640) as ?xValue10) .
        BIND(ajan-math-ns:sample(0, 480) as ?yValue10) .
        BIND(ajan-math-ns:sample(0, 640) as ?xValue11) .
        BIND(ajan-math-ns:sample(0, 480) as ?yValue11) .
        BIND(ajan-math-ns:sample(0, 640) as ?xValue12) .
        BIND(ajan-math-ns:sample(0, 480) as ?yValue12) .
    }
    """

    probability_query = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX pomdp-ns-data:<http://www.dfki.de/pomdp-ns/POMDP/data/>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX ajan-math-ns:<http://www.ajan.de/ajan/functions/math-ns#>
    
    SELECT ?probability ?dist ?leftDistance ?rightDistance ?expProb
    WHERE {
        pomdp-ns:current_action rdfs:value ?action .
        pomdp-ns:Observation pomdp-ns:attributes ?attributesNode .
        ?attributesNode pomdp-ns1:_pose ?pose .
        pomdp-ns:next_state rdfs:value ?next_state .
        ?next_state pomdp-ns:attributes ?stateAttributesNode .
        ?stateAttributesNode pomdp-ns1:_gesture ?next_gesture .
    
        BIND(IF(?action != pomdp-ns1:Action_perceive && ?pose = rdfs:nil, 1.0,0.0) as ?probability) .
        
        BIND(5 as ?sigma) .
        
        BIND(ajan-math-ns:distance(10, 11) as ?testDistance) .
        BIND(pomdp-ns-data:Point_9 as ?lwrist) .
        BIND(pomdp-ns-data:Point_11 as ?lhip) .
        BIND(pomdp-ns-data:Point_10 as ?rhip) .
        BIND(pomdp-ns-data:Point_12 as ?rwrist) .
        BIND(ajan-math-ns:distance(?lhip, ?lwrist) as ?leftDistance) .
        BIND(ajan-math-ns:distance(?rhip, ?rwrist) as ?rightDistance) .
        BIND(ajan-math-ns:calculate_near_probability(?leftDistance, ?sigma) as ?leftProbability) .
        BIND(ajan-math-ns:calculate_near_probability(?rightDistance, ?sigma) as ?rightProbability) .
        
        BIND(IF(?action = pomdp-ns1:Action_perceive,
                    IF(?pose = rdfs:nil, 1.0,
                                            IF(?next_gesture = "Left", ?leftProbability,
                                            IF(?next_gesture = "Right", ?rightProbability, 1.0))),?probability) 
        as ?probability) .
        
        # BIND(IF(?action == pomdp-ns1:Action_perceive && ?pose != rdfs:nil, 
        #     IF(?next_gesture = "Left", ajan-math-ns:calculate_near_probability(?leftDistance, ?sigma), 
        #     IF(?next_gesture = "Right", ajan-math-ns:calculate_near_probability(?rightDistance, ?sigma), 
        #     IF(?next_gesture = rdfs:nil && ?pose = rdfs:nil, 1.0,?probability))), 1.0) 
        # as ?probability) .
        
        # BIND(IF(?next_gesture!=rdfs:nil, 
        #    ?expProb
        # ,?probability) as ?probability) .
    }
    """

    argmax_query = """
    
    """

    right_keypoint = RIGHT_KEYPOINT

    left_keypoint = LEFT_KEYPOINT

    def test_init(self):
        self.observation_model = AjanObservationModel("", {"person_id": 102, "epsilon": 1e-9},
                                                      self.probability_query, self.sample_query, self.argmax_query)

        rdflib.plugins.sparql.CUSTOM_EVALS["sample_values"] = custom_functions.sample_values
        rdflib.plugins.sparql.CUSTOM_EVALS["math_dist"] = custom_functions.distance
        rdflib.plugins.sparql.CUSTOM_EVALS["semantic_field_near"] = semantic_fields.near
        self.assertNotEqual(self.observation_model, None, "Observation model should not be none")

    def test_probability_perceive(self):
        self.test_init()
        observation = AjanObservation({"pose": None, "id": 102}, ['id', 'pose'])
        action = AjanAction("perceive")
        next_state = AjanEnvObjectState("person", 102, {"id": 102, "gesture": None}, ['id', 'gesture'])
        probability = self.observation_model.probability(observation, next_state, action)
        self.assertEqual(probability, 1.0, "Perceive with no pose should be 1.0")

    def test_probability_perceive_with_right_pose_gesture_right(self):
        self.test_init()

        observation = AjanObservation({"pose": self.right_keypoint, "id": 102}, ['id', 'pose'])
        action = AjanAction("perceive")
        next_state = AjanEnvObjectState("person", 102, {"id": 102, "gesture": "Right"}, ['id', 'gesture'])
        probability = self.observation_model.probability(observation, next_state, action)
        self.assertGreater(probability, 0.5, "Perceive with some keypoints should not have probability 0.0")

    def test_probability_perceive_with_left_pose_gesture_right(self):
        self.test_init()

        observation = AjanObservation({"pose": self.left_keypoint, "id": 102}, ['id', 'pose'])
        action = AjanAction("perceive")
        next_state = AjanEnvObjectState("person", 102, {"id": 102, "gesture": "Right"}, ['id', 'gesture'])
        probability = self.observation_model.probability(observation, next_state, action)
        self.assertLess(probability, 0.5, "Perceive with some keypoints should not have probability 0.0")

    def test_probability_perceive_with_left_pose_gesture_left(self):
        self.test_init()

        observation = AjanObservation({"pose": self.left_keypoint, "id": 102}, ['id', 'pose'])
        action = AjanAction("perceive")
        next_state = AjanEnvObjectState("person", 102, {"id": 102, "gesture": "Left"}, ['id', 'gesture'])
        probability = self.observation_model.probability(observation, next_state, action)
        self.assertGreater(probability, 0.5, "Perceive with some keypoints should not have probability 0.0")

    def test_probability_perceive_with_right_pose_gesture_left(self):
        self.test_init()

        observation = AjanObservation({"pose": self.right_keypoint, "id": 102}, ['id', 'pose'])
        action = AjanAction("perceive")
        next_state = AjanEnvObjectState("person", 102, {"id": 102, "gesture": "Left"}, ['id', 'gesture'])
        probability = self.observation_model.probability(observation, next_state, action)
        self.assertLess(probability, 0.5, "Perceive with some keypoints should not have probability 0.0")

    def test_probability_move(self):
        self.test_init()
        num_points = 17
        observation = AjanObservation({"pose": None, "id": 102}, ['id', 'pose'])
        move_left_action = AjanAction("move", {"motion": "Left"})
        next_state = AjanEnvObjectState("person", 102, {"id": 102, "gesture": None}, ['id', 'gesture'])
        probability = self.observation_model.probability(observation, next_state, move_left_action)
        self.assertEqual(1.0, probability, "Probability should be 0.0")

    def test_probability_move_with_pose(self):
        self.test_init()
        num_points = 17
        x_values = np.random.uniform(0, 640, num_points)
        y_values = np.random.uniform(0, 480, num_points)
        keypoints = np.column_stack((x_values, y_values))
        observation = AjanObservation({"pose": keypoints, "id": 102}, ['id', 'pose'])
        move_left_action = AjanAction("move", {"motion": "Right"})
        next_state = AjanEnvObjectState("person", 102, {"id": 102, "gesture": "Left"}, ['id', 'gesture'])
        probability = self.observation_model.probability(observation, next_state, move_left_action)
        self.assertEqual(0.0, probability, "Probability should be 0.0")

    def test_sample_perceive(self):
        self.test_init()
        observation = AjanObservation({"pose": None, "id": 102}, ['id', 'pose'])
        action = AjanAction("perceive")
        next_state = AjanEnvObjectState("person", 102, {"id": 102, "gesture": None}, ['id', 'gesture'])
        sample = self.observation_model.sample(next_state, action)
        is_empty = True

        if not sample.attributes['pose'] is None and not sample.attributes['pose'].empty:
            is_empty = False
        self.assertNotEqual(is_empty, True, "Pose should not be none")

    def test_sample_move(self):
        self.test_init()
        observation = AjanObservation({"pose": None, "id": 102}, ['id', 'pose'])
        action = AjanAction("move", {"motion": "Left"})
        next_state = AjanEnvObjectState("person", 102, {"id": 102, "gesture": None}, ['id', 'gesture'])
        sample = self.observation_model.sample(next_state, action)
        self.assertEqual(sample.attributes['pose'], None, "Sample should be none")


if __name__ == '__main__':
    unittest.main()
