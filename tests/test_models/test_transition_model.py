import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanAgentState, AjanEnvObjectState
from POMDPService.ajan_pomdp_planning.oopomdp.models.transition_model import AjanTransitionModel


class TestTransitionModel(unittest.TestCase):

    transition_model = None

    probability_query = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    SELECT ?probability
    WHERE{
        pomdp-ns:next_state rdf:value ?next_state .
        pomdp-ns:current_state rdf:value ?current_state .
        BIND(0.000000001 as ?epsilon) .
        BIND(IF(?next_state=?current_state, 1-?epsilon, ?epsilon) as ?probability) .
    }
    """
    sample_query = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX pomdp-data-ns:<http://www.dfki.de/pomdp-ns/POMDP/data/>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

    CONSTRUCT {
        pomdp-ns:State rdfs:value ?state .
        ?state rdfs:type pomdp-ns:State .
        ?state pomdp-ns:id ?stateId .
        ?state pomdp-ns:name "Drone" .
        ?state pomdp-ns:type "Agent" .
        ?state pomdp-ns:attributes ?attributes .
        ?attributes pomdp-ns1:_id ?stateId .

        ?attributes pomdp-ns1:_gesture_found ?gestureValue .

        ?attributes pomdp-ns1:_pose ?pose .
        ?pose rdfs:type pomdp-data-ns:2dVector .
        ?pose rdfs:x ?xValue .
        ?pose rdfs:y ?yValue .

    }
    WHERE{
        pomdp-ns:current_state rdfs:value ?state .
        pomdp-ns:current_action rdfs:value ?action .
        ?state pomdp-ns:id ?stateId .
        ?state pomdp-ns:attributes ?attributesNode .
        ?attributesNode pomdp-ns1:_pose ?poseNode .
        ?attributesNode pomdp-ns1:_gesture_found ?gesture .
        ?poseNode rdfs:x ?xPose .
        ?poseNode rdfs:y ?yPose .

        OPTIONAL{    
            ?action pomdp-ns:attributes ?actionAttributes .
            ?actionAttributes pomdp-ns1:_motion ?motionType .
        }

        BIND(BNODE() as ?attributes) .
        BIND(BNODE() as ?pose) .
        BIND(BNODE() as ?poseValue) .

        BIND(IF (?action=pomdp-ns1:Action_move && ?motionType ="Right",
                ?xPose-1,?xPose) as ?xValue) .
        BIND(IF (?action=pomdp-ns1:Action_move && ?motionType ="Left",
                ?yPose+1,?yPose) as ?yValue) .

        BIND(IF(?action=pomdp-ns1:Action_perceive, 
                IF(RAND()>0.5,"true"^^xsd:boolean,"false"^^xsd:boolean), 
            ?gesture) as ?gestureValue) .
        ?s ?p ?o  .
    }
    """
    sample_query_person = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX pomdp-data-ns:<http://www.dfki.de/pomdp-ns/POMDP/data/>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

    CONSTRUCT {
        pomdp-ns:State rdfs:value ?state .
        ?state rdfs:type pomdp-ns:State .
        ?state pomdp-ns:id ?stateId .
        ?state pomdp-ns:name ?stateName .
        ?state pomdp-ns:type ?stateType .
        ?state pomdp-ns:attributes ?attributes .
        ?attributes pomdp-ns1:_id ?stateId .

        ?attributes pomdp-ns1:_gesture ?gestureValue .

        ?attributes pomdp-ns1:_pose ?pose .
        ?pose rdfs:type ?poseType .
        ?pose rdfs:x ?xValue .
        ?pose rdfs:y ?yValue .

    }
    WHERE{
        pomdp-ns:current_state rdfs:value ?state .
        ?state pomdp-ns:name ?stateName .
        ?state pomdp-ns:type ?stateType .

        pomdp-ns:current_action rdfs:value ?action .
        ?state pomdp-ns:id ?stateId .
        ?state pomdp-ns:attributes ?attributesNode .
        ?attributesNode pomdp-ns1:_pose ?poseNode .
        ?attributesNode pomdp-ns1:_gesture ?gesture .

        OPTIONAL{    
            ?poseNode rdfs:x ?xPose .
            ?poseNode rdfs:y ?yPose .
            BIND(pomdp-data-ns:2dVector as ?poseType) .
            ?action pomdp-ns:attributes ?actionAttributes .
            ?actionAttributes pomdp-ns1:_motion ?motionType .
        }

        BIND(BNODE() as ?attributes) .
        BIND(IF(?action=pomdp-ns1:Action_perceive, rdfs:nil, BNODE()) as ?pose) .
        BIND(BNODE() as ?poseValue) .

        BIND(IF(?action=pomdp-ns1:Action_perceive, 
                IF(RAND()>0.5,
                    IF(RAND()>0.5, "left",rdfs:nil)
                    ,"right"), 
                ?gesture) as ?gestureValue) .
        ?s ?p ?o  .
    }
    """
    argmax_query = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX pomdp-data-ns:<http://www.dfki.de/pomdp-ns/POMDP/data/>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    CONSTRUCT {
        pomdp-ns:State rdfs:value ?state .
        ?state rdfs:type pomdp-ns:State .
        ?state pomdp-ns:id ?id .
        ?state pomdp-ns:name "Drone" .
        ?state pomdp-ns:type "Agent" .
        ?state pomdp-ns:attributes ?attributes .
        ?attributes pomdp-ns1:_id ?id .

        ?attributes pomdp-ns1:_gesture_found ?gestureValue .

        ?attributes pomdp-ns1:_pose ?pose .
        ?pose rdfs:type pomdp-data-ns:2dVector .
        ?pose rdfs:x ?xValue .
        ?pose rdfs:y ?yValue .

    }
    WHERE{
        pomdp-ns:current_state rdfs:value ?state .
        pomdp-ns:current_action rdfs:value ?action .
        ?state pomdp-ns:id ?stateId .
        BIND(BNODE() as ?attributes) .
        BIND(BNODE() as ?pose) .
        BIND(BNODE() as ?poseValue) .

        BIND(IF(?action=pomdp-ns1:Action_perceive,
                ?stateId,
                    ?stateId-1) as ?xValue) .
            BIND(IF(?action=pomdp-ns1:Action_perceive,
                ?stateId, 
                    ?stateId-1) as ?yValue) .
        BIND(IF (?action=pomdp-ns1:Action_MoveLeft,
                ?stateId-1,?xValue) as ?xValue) .
        BIND(IF (?action=pomdp-ns1:Action_MoveLeft,
                ?stateId+1,?xValue) as ?yValue) .

        BIND(IF(?action=pomdp-ns1:Action_perceive, 
                IF(RAND()>0.5,"True"^^xsd:boolean,"False"^^xsd:boolean), 
            "False"^^xsd:boolean) as ?gestureValue) .
        BIND(101 as ?id) .
        ?s ?p ?o  .
    }
    """
    argmax_query_person = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX pomdp-data-ns:<http://www.dfki.de/pomdp-ns/POMDP/data/>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

    CONSTRUCT {
        pomdp-ns:State rdfs:value ?state .
        ?state rdfs:type pomdp-ns:State .
        ?state pomdp-ns:id ?stateId .
        ?state pomdp-ns:name ?stateName .
        ?state pomdp-ns:type ?stateType .
        ?state pomdp-ns:attributes ?attributes .
        ?attributes pomdp-ns1:_id ?stateId .

        ?attributes pomdp-ns1:_gesture ?gestureValue .

        ?attributes pomdp-ns1:_pose ?pose .
        ?pose rdfs:type ?poseType .
        ?pose rdfs:x ?xValue .
        ?pose rdfs:y ?yValue .

    }
    WHERE{
        pomdp-ns:current_state rdfs:value ?state .
        ?state pomdp-ns:name ?stateName .
        ?state pomdp-ns:type ?stateType .

        pomdp-ns:current_action rdfs:value ?action .
        ?state pomdp-ns:id ?stateId .
        ?state pomdp-ns:attributes ?attributesNode .
        ?attributesNode pomdp-ns1:_pose ?poseNode .
        ?attributesNode pomdp-ns1:_gesture ?gesture .

        OPTIONAL{    
            ?poseNode rdfs:x ?xPose .
            ?poseNode rdfs:y ?yPose .
            BIND(pomdp-data-ns:2dVector as ?poseType) .
            ?action pomdp-ns:attributes ?actionAttributes .
            ?actionAttributes pomdp-ns1:_motion ?motionType .
        }

        BIND(BNODE() as ?attributes) .
        BIND(IF(?action=pomdp-ns1:Action_perceive, rdfs:nil, BNODE()) as ?pose) .
        BIND(BNODE() as ?poseValue) .

        BIND(IF(?action=pomdp-ns1:Action_perceive, 
                IF(RAND()>0.5,
                    IF(RAND()>0.5, "left",rdfs:nil)
                    ,"right"), 
                ?gesture) as ?gestureValue) .
        ?s ?p ?o  .
    }
    """

    def test_init(self):

        self.transition_model = AjanTransitionModel("model_id", "", [],
                                                    self.probability_query, self.sample_query, self.argmax_query)
        self.assertNotEqual(self.transition_model, None, "Should not be None")

    def test_get_probability_diff_state(self):
        self.test_init()
        next_state = AjanAgentState("Drone", 102)
        state = AjanAgentState("Drone", 102)
        action = AjanAction("perceive")

        probability = self.transition_model.probability(next_state, state, action)

        self.assertEqual(probability, 1e-09, "Probability mismatch")

    def test_get_probability_same_state(self):
        self.test_init()
        next_state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": True})
        state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": False})
        action = AjanAction("perceive", {"pose": (10, 10), "gesture_found": True})
        action = AjanAction("move", {"motion": "Left"})
        action = AjanAction("move", {"motion": "Right"})

        probability = self.transition_model.probability(next_state, state, action)

        self.assertEqual(probability, 0.999999999, "Probability mismatch")

    def test_sample(self):
        self.test_init()
        state = AjanAgentState("Drone", 101, {'gesture_found': False, 'id': 101, 'pose': (10, 10)})
        action = AjanAction("perceive")
        action = AjanAction("move", {"motion": "Left"})
        action = AjanAction("move", {"motion": "Right"})
        result_state = self.transition_model.sample(state, action)

        self.assertNotEqual(result_state, state, "States Should be equal")

    def test_sample_person_move(self):
        self.test_init()
        self.transition_model.sample_query = self.sample_query_person
        state = AjanEnvObjectState("Person", 112, {'gesture': "left", 'id': 112, 'pose': None})
        move_action = AjanAction("move", {"motion": "left"})
        result_state = self.transition_model.sample(state, move_action)
        self.assertEqual(result_state, state, "States Should be equal")



    def test_sample_perceive(self):
        self.test_init()
        state = AjanAgentState("Drone", 101, {'gesture_found': False, 'id': 101, 'pose': (10, 10)})
        action = AjanAction("perceive")
        result_state = self.transition_model.sample(state, action)

        if result_state.attributes['gesture_found']:
            self.assertNotEqual(result_state, state, "States Should be equal")
        else:
            self.assertEqual(result_state, state, "States Should be equal")

    def test_argmax(self):
        self.test_init()
        state = AjanAgentState("Drone", 101, {'gesture_found': False, 'id': 101, 'pose': (10, 10)})
        action = AjanAction("perceive")
        action = AjanAction("move", {"motion": "Left"})
        action = AjanAction("move", {"motion": "Right"})
        result_state = self.transition_model.argmax(state, action)

        self.assertNotEqual(result_state, state, "States Should be equal")

    def test_argmax_person_perceive(self):
        self.test_init()
        self.transition_model.argmax_query = self.argmax_query_person
        state = AjanEnvObjectState("Person", 101, {'gesture': None, 'id': 101, 'pose': None})
        action = AjanAction("perceive")
        result_state = self.transition_model.argmax(state, action)
        if result_state.attributes['gesture'] is not None:
            self.assertNotEqual(result_state, state, "States Should be equal")
        else:
            self.assertEqual(result_state, state, "States Should be equal")

    def test_argmax_person_move(self):
        self.test_init()
        self.transition_model.argmax_query = self.argmax_query_person
        state = AjanEnvObjectState("Person", 101, {'gesture': None, 'id': 101, 'pose': None})
        action = AjanAction("move", {"motion": "Right"})
        result_state = self.transition_model.argmax(state, action)
        self.assertEqual(result_state, state, "States Should be equal")


if __name__ == '__main__':
    unittest.main()
