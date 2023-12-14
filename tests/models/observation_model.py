import unittest

import numpy
import numpy as np
import rdflib
from rdflib.plugins.sparql import CUSTOM_EVALS

from CustomSPARQLFunctions.math import distance, sample_values
from CustomSPARQLFunctions.semantic_fields import near
from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.observation import AjanObservation
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanEnvObjectState
from POMDPService.ajan_pomdp_planning.oopomdp.models.observation_model import AjanObservationModel


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

    right_keypoint = numpy.array(
        [[362.2897033691406, 183.26980590820312], [366.96588134765625, 180.3370361328125],  # Nose, Left Eye
         [359.25262451171875, 179.9287872314453], [374.8979187011719, 185.27777099609375],  # Right Eye, Left Ear
         [356.7257080078125, 184.7674560546875], [387.3588562011719, 213.78274536132812],
         # Right Ear, Left Shoulder
         [345.8138732910156, 208.60122680664062], [399.6535339355469, 242.93577575683594],
         # Right Shoulder, Left Elbow
         [314.02880859375, 212.2890625], [395.7891845703125, 268.6268615722656],  # Right Elbow, Left Wrist
         [290.3717041015625, 203.26809692382812], [376.18865966796875, 275.7311096191406],  # Right Wrist, Left Hip
         [349.8257141113281, 273.4117126464844], [380.6387939453125, 323.3451232910156],  # Right Hip, Left Knee
         [344.4939270019531, 321.383544921875], [384.9736633300781, 366.05596923828125],  # Right Knee, Left Ankle
         [341.6835632324219, 363.7601318359375]])  # Right Ankle

    left_keypoint = numpy.array(
        [[363.5481262207031, 182.52304077148438], [365.7922668457031, 179.2210235595703],  # Nose, Left Eye
         [358.5639343261719, 179.872314453125], [367.997314453125, 184.44668579101562],  # Right Eye, Left Ear
         [349.0396728515625, 186.233154296875], [378.8489990234375, 206.544921875],  # Right Ear, Left Shoulder
         [339.2182922363281, 213.96359252929688], [408.90496826171875, 207.91845703125],  # Right Shoulder,
         # Left Elbow
         [327.3758544921875, 242.71759033203125], [438.9847412109375, 197.96572875976562],
         # Right Elbow, Left Wrist
         [332.4953918457031, 269.58294677734375], [378.767822265625, 273.4088439941406],  # Right Wrist, Left Hip
         [352.5574645996094, 276.4232177734375], [381.8661804199219, 321.59808349609375],  # Right Hip, Left Knee
         [346.67724609375, 322.4833068847656], [383.0187683105469, 367.87591552734375],  # Right Knee, Left Ankle
         [341.7171936035156, 367.486328125]])  # Right Ankle

    def test_init(self):
        self.observation_model = AjanObservationModel("", {"person_id": 102, "epsilon": 1e-9},
                                                      self.probability_query, self.sample_query, self.argmax_query)

        rdflib.plugins.sparql.CUSTOM_EVALS["sample_values"] = sample_values
        rdflib.plugins.sparql.CUSTOM_EVALS["math_dist"] = distance
        rdflib.plugins.sparql.CUSTOM_EVALS["semantic_field_near"] = near
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
