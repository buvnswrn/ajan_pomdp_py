import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanAgentState, AjanEnvObjectState, AjanOOState
from POMDPService.ajan_pomdp_planning.oopomdp.models.reward_model import AjanRewardModel


class TestRewardModel(unittest.TestCase):

    reward_model = None

    sample_query = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
    SELECT ?sample
    WHERE {
        pomdp-ns:current_action rdfs:value ?action .
        pomdp-ns:RewardModel pomdp-ns:attributes ?modelAttributesNode .
        ?modelAttributesNode pomdp-ns1:_drone_id ?droneId.
        ?modelAttributesNode pomdp-ns1:_person_id ?personId.
        
        OPTIONAL {
        ?action pomdp-ns:attributes ?actionAttributeNode .
        ?actionAttributeNode pomdp-ns1:_motion ?motionType .
        }
        
        OPTIONAL {
        pomdp-ns:current_state rdfs:value ?currentOOState .
        ?currentOOState rdfs:type pomdp-ns:OOState .
        ?currentOOState rdfs:value ?currentDroneState .
        ?currentDroneState pomdp-ns:id ?droneId .
        }
        
        OPTIONAL {
        pomdp-ns:current_state rdfs:value ?currentOOState .
        ?currentOOState rdfs:type pomdp-ns:OOState .
        ?currentOOState rdfs:value ?currentPersonState .
        ?currentPersonState pomdp-ns:id ?personId .
        }
        
        OPTIONAL {
        pomdp-ns:current_state rdfs:value ?currentDroneState .}
        
        pomdp-ns:next_state rdfs:value ?nextState .
        
        BIND(0.0 as ?probability) .
        BIND(0.0 as ?temp_reward) .
        BIND(1000 AS ?bigReward) .
        
        OPTIONAL {
        ?currentDroneState pomdp-ns:attributes ?cattributeNode .
        ?cattributeNode rdfs:type pomdp-ns:current_state .
        ?cattributeNode pomdp-ns1:_gesture_found ?current_gesture_found .
        
        ?currentDroneState pomdp-ns:attributes ?nattributeNode .
        ?nattributeNode rdfs:type pomdp-ns:next_state .
        ?nattributeNode pomdp-ns1:_gesture_found ?next_gesture_found .
        }
        
        OPTIONAL {
        ?currentPersonState pomdp-ns:attributes ?cpattributeNode .
        ?cpattributeNode rdfs:type pomdp-ns:current_state .
        ?cpattributeNode pomdp-ns1:_gesture ?person_current_gesture .
        
        ?currentPersonState pomdp-ns:attributes ?npattributeNode .
        ?npattributeNode rdfs:type pomdp-ns:next_state .
        ?npattributeNode pomdp-ns1:_gesture ?person_next_gesture .
        }
        
        BIND (IF(?action = pomdp-ns1:Action_perceive &&
        (!?current_gesture_found && ?next_gesture_found), ?temp_reward+?bigReward, ?temp_reward) as ?perceiveReward) .
        
        BIND (IF(?person_current_gesture != rdfs:nil && 
        ?person_current_gesture = ?person_next_gesture &&
        ?action = pomdp-ns1:Action_move,
        IF(?person_current_gesture = ?motionType,?perceiveReward+?bigReward,?perceiveReward-?bigReward), ?perceiveReward)
        as ?perceiveReward) .
        
        BIND(?perceiveReward as ?sample) .
        
    }
    """

    probability_query = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
    SELECT ?probability
    WHERE {
        pomdp-ns:current_action rdfs:value ?action .
        pomdp-ns:RewardModel pomdp-ns:attributes ?modelAttributesNode .
        ?modelAttributesNode pomdp-ns1:_drone_id ?droneId.
        ?modelAttributesNode pomdp-ns1:_person_id ?personId.
        
        OPTIONAL {
        ?action pomdp-ns:attributes ?actionAttributeNode .
        ?actionAttributeNode pomdp-ns1:_motion ?motionType .
        }
        
        OPTIONAL {
        pomdp-ns:current_state rdfs:value ?currentOOState .
        ?currentOOState rdfs:type pomdp-ns:OOState .
        ?currentOOState rdfs:value ?currentDroneState .
        ?currentDroneState pomdp-ns:id ?droneId .
        }
        
        OPTIONAL {
        pomdp-ns:current_state rdfs:value ?currentOOState .
        ?currentOOState rdfs:type pomdp-ns:OOState .
        ?currentOOState rdfs:value ?currentPersonState .
        ?currentPersonState pomdp-ns:id ?personId .
        }
        
        OPTIONAL {
        pomdp-ns:current_state rdfs:value ?currentDroneState .}
        
        pomdp-ns:next_state rdfs:value ?nextState .
        
        BIND(0.0 as ?probability) .
        BIND(0.0 as ?temp_reward) .
        BIND(1000 AS ?bigReward) .
        
        OPTIONAL {
        ?currentDroneState pomdp-ns:attributes ?cattributeNode .
        ?cattributeNode rdfs:type pomdp-ns:current_state .
        ?cattributeNode pomdp-ns1:_gesture_found ?current_gesture_found .
        
        ?currentDroneState pomdp-ns:attributes ?nattributeNode .
        ?nattributeNode rdfs:type pomdp-ns:next_state .
        ?nattributeNode pomdp-ns1:_gesture_found ?next_gesture_found .
        }
        
        OPTIONAL {
        ?currentPersonState pomdp-ns:attributes ?cpattributeNode .
        ?cpattributeNode rdfs:type pomdp-ns:current_state .
        ?cpattributeNode pomdp-ns1:_gesture ?person_current_gesture .
        
        ?currentPersonState pomdp-ns:attributes ?npattributeNode .
        ?npattributeNode rdfs:type pomdp-ns:next_state .
        ?npattributeNode pomdp-ns1:_gesture ?person_next_gesture .
        }
        pomdp-ns:current_reward rdfs:value ?current_reward .
        BIND (IF(?action = pomdp-ns1:Action_perceive &&
        (!?current_gesture_found && ?next_gesture_found), ?temp_reward+?bigReward, ?temp_reward) as ?perceiveReward) .
        
        BIND (IF(?person_current_gesture != rdfs:nil && 
        ?person_current_gesture = ?person_next_gesture &&
        ?action = pomdp-ns1:Action_move,
        IF(?person_current_gesture = ?motionType,?perceiveReward+?bigReward,?perceiveReward-?bigReward), ?perceiveReward)
        as ?perceiveReward) .
        
        BIND(?perceiveReward as ?reward) .
        BIND(IF(?current_reward = ?reward, 1.0, ?probability) as ?probability).
        
    }
    """

    argmax_query = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
    SELECT ?argmax
    WHERE {
        pomdp-ns:current_action rdfs:value ?action .
        pomdp-ns:RewardModel pomdp-ns:attributes ?modelAttributesNode .
        ?modelAttributesNode pomdp-ns1:_drone_id ?droneId.
        ?modelAttributesNode pomdp-ns1:_person_id ?personId.
        
        OPTIONAL {
        ?action pomdp-ns:attributes ?actionAttributeNode .
        ?actionAttributeNode pomdp-ns1:_motion ?motionType .
        }
        
        OPTIONAL {
        pomdp-ns:current_state rdfs:value ?currentOOState .
        ?currentOOState rdfs:type pomdp-ns:OOState .
        ?currentOOState rdfs:value ?currentDroneState .
        ?currentDroneState pomdp-ns:id ?droneId .
        }
        
        OPTIONAL {
        pomdp-ns:current_state rdfs:value ?currentOOState .
        ?currentOOState rdfs:type pomdp-ns:OOState .
        ?currentOOState rdfs:value ?currentPersonState .
        ?currentPersonState pomdp-ns:id ?personId .
        }
        
        OPTIONAL {
        pomdp-ns:current_state rdfs:value ?currentDroneState .}
        
        pomdp-ns:next_state rdfs:value ?nextState .
        
        BIND(0.0 as ?probability) .
        BIND(0.0 as ?temp_reward) .
        BIND(1000 AS ?bigReward) .
        
        OPTIONAL {
        ?currentDroneState pomdp-ns:attributes ?cattributeNode .
        ?cattributeNode rdfs:type pomdp-ns:current_state .
        ?cattributeNode pomdp-ns1:_gesture_found ?current_gesture_found .
        
        ?currentDroneState pomdp-ns:attributes ?nattributeNode .
        ?nattributeNode rdfs:type pomdp-ns:next_state .
        ?nattributeNode pomdp-ns1:_gesture_found ?next_gesture_found .
        }
        
        OPTIONAL {
        ?currentPersonState pomdp-ns:attributes ?cpattributeNode .
        ?cpattributeNode rdfs:type pomdp-ns:current_state .
        ?cpattributeNode pomdp-ns1:_gesture ?person_current_gesture .
        
        ?currentPersonState pomdp-ns:attributes ?npattributeNode .
        ?npattributeNode rdfs:type pomdp-ns:next_state .
        ?npattributeNode pomdp-ns1:_gesture ?person_next_gesture .
        }
        
        BIND (IF(?action = pomdp-ns1:Action_perceive &&
        (!?current_gesture_found && ?next_gesture_found), ?temp_reward+?bigReward, ?temp_reward) as ?perceiveReward) .
        
        BIND (IF(?person_current_gesture != rdfs:nil && 
        ?person_current_gesture = ?person_next_gesture &&
        ?action = pomdp-ns1:Action_move,
        IF(?person_current_gesture = ?motionType,?perceiveReward+?bigReward,?perceiveReward-?bigReward), ?perceiveReward)
        as ?perceiveReward) .
        
        BIND(?perceiveReward as ?argmax) .
        
    }
    
    """

    def test_init(self):
        self.reward_model = AjanRewardModel("", {"drone_id": 101, "person_id": 102}, self.probability_query, self.sample_query, self.argmax_query)
        self.assertNotEqual(self.reward_model, None, "Should not be None")

    def test_init1(self):
        self.reward_model = AjanRewardModel("", {"drone_id": 100, "big": 1000, "person_id": None}, self.probability_query, self.sample_query, self.argmax_query)
        self.assertNotEqual(self.reward_model, None, "Should not be None")

    def test_probability_perceive(self):
        self.test_init()
        next_state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": True})
        state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": False})
        person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": None})
        action = AjanAction("perceive")

        oo_state = AjanOOState({"Drone": state, "Person": person_state})
        oo_next_state = AjanOOState({"Drone": next_state, "Person": person_state})

        probability = self.reward_model.probability(1000, oo_state, action, oo_next_state)

        self.assertEqual(probability, 1.0, "Probability mismatch in perceive action")

    def test_probability_move(self):
        self.test_init()
        state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": False})
        next_state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": True})

        person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": None})
        next_person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": "Left"})

        action = AjanAction("move", {"motion": "Left"})

        oo_state = AjanOOState({"Drone": state, "Person": person_state})
        oo_next_state = AjanOOState({"Drone": next_state, "Person": next_person_state})

        probability = self.reward_model.probability(1000, oo_state, action, oo_next_state)

        self.assertEqual(probability, 0.0, "Probability mismatch in move action")

    def test_probability_move_left_left_left(self):
        self.test_init()
        state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": False})
        next_state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": True})

        person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": "Left"})

        next_person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": "Left"})

        action = AjanAction("move", {"motion": "Left"})

        oo_state = AjanOOState({"Drone": state, "Person": person_state})
        oo_next_state = AjanOOState({"Drone": next_state, "Person": next_person_state})

        probability = self.reward_model.probability(1000, oo_state, action, oo_next_state)

        self.assertEqual(probability, 1.0, "Probability mismatch in move action")

    def test_probability_move_right_right_right(self):
        self.test_init()
        state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": False})
        next_state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": True})

        person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": "Right"})

        next_person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": "Right"})

        action = AjanAction("move", {"motion": "Right"})

        oo_state = AjanOOState({"Drone": state, "Person": person_state})
        oo_next_state = AjanOOState({"Drone": next_state, "Person": next_person_state})

        probability = self.reward_model.probability(1000, oo_state, action, oo_next_state)

        self.assertEqual(probability, 1.0, "Probability mismatch in move action")

    def test_probability_move_right_right_left(self):
        self.test_init()
        state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": False})
        next_state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": True})

        person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": "Right"})

        next_person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": "Right"})

        action = AjanAction("move", {"motion": "Left"})

        oo_state = AjanOOState({"Drone": state, "Person": person_state})
        oo_next_state = AjanOOState({"Drone": next_state, "Person": next_person_state})

        probability = self.reward_model.probability(1000, oo_state, action, oo_next_state)

        self.assertEqual(probability, 0.0, "Probability mismatch in move action")

    def test_probability_move_right_left_left(self):
        self.test_init()
        state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": False})
        next_state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": True})

        person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": "Right"})

        next_person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": "Left"})

        action = AjanAction("move", {"motion": "Left"})

        oo_state = AjanOOState({"Drone": state, "Person": person_state})
        oo_next_state = AjanOOState({"Drone": next_state, "Person": next_person_state})

        probability = self.reward_model.probability(1000, oo_state, action, oo_next_state)

        self.assertEqual(probability, 0.0, "Probability mismatch in move action")

    def test_sample_perceive(self):
        self.test_init()
        next_state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": True})
        state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": False})
        person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": None})
        action = AjanAction("perceive")

        oo_state = AjanOOState({"Drone": state, "Person": person_state})
        oo_next_state = AjanOOState({"Drone": next_state, "Person": person_state})

        sample = self.reward_model.sample(oo_state, action, oo_next_state)

        self.assertEqual(sample, 1000, "sample mismatch in perceive action")

    def test_sample_perceive_1(self):
        self.test_init1()
        current_env_state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": None})
        next_env_state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "right"})

        current_agent_state = AjanAgentState("Drone", 100, {"pose": (0, 0), "gesture_found": False})
        next_agent_state = AjanAgentState("Drone", 100, {"pose": (0, 0), "gesture_found": True})

        current_state = AjanOOState({80: current_env_state, 68: current_agent_state})

        next_state = AjanOOState({80: next_env_state, 68: next_agent_state})

        action = AjanAction("perceive")

        sample = self.reward_model.sample(current_state, action, next_state)

        self.assertEqual(sample, 1000, "sample mismatch in perceive action")

    def test_sample_perceive_2(self):
        self.test_init1()
        current_env_state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": None})
        next_env_state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": None})
        current_agent_state = AjanAgentState("Drone", 100, {"pose": (0, 0), "gesture_found": False})
        next_agent_state = AjanAgentState("Drone", 100, {"pose": (0, 0), "gesture_found": False})
        action = AjanAction("move", {"motion": "right"})
        current_state = AjanOOState({112: current_env_state, 100: current_agent_state})
        next_state = AjanOOState({112: next_env_state, 100: next_agent_state})
        sample = self.reward_model.sample(current_state, action, next_state)
        self.assertEqual(sample, 0, "sample mismatch in perceive action")


    def test_sample_perceive_no_change(self):
        self.test_init()
        state = AjanAgentState("Drone", 101, {"pose": (0, 0), "gesture_found": False})
        next_state = AjanAgentState("Drone", 101, {"pose": (0, 0), "gesture_found": True})
        person_state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": None})
        next_person_state = AjanEnvObjectState("Person", 112, {"pose": None, "gesture": "right"})
        action = AjanAction("perceive")

        oo_state = AjanOOState({"Drone": state, "Person": person_state})
        oo_next_state = AjanOOState({"Drone": next_state, "Person": next_person_state})

        sample = self.reward_model.sample(oo_state, action, oo_next_state)

        self.assertEqual(sample, 1000, "sample mismatch in perceive action")

    def test_sample_move(self):
        self.test_init()
        state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": False})
        next_state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": True})

        person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": None})
        next_person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": "Left"})

        action = AjanAction("move", {"motion": "Left"})

        oo_state = AjanOOState({"Drone": state, "Person": person_state})
        oo_next_state = AjanOOState({"Drone": next_state, "Person": next_person_state})

        sample = self.reward_model.sample(oo_state, action, oo_next_state)

        # This should actually be penalized but it is not
        self.assertEqual(sample, 0.0, "sample mismatch in move action")

    def test_sample_move_left_left_left(self):
        self.test_init()
        state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": False})
        next_state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": True})

        person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": "Left"})

        next_person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": "Left"})

        action = AjanAction("move", {"motion": "Left"})

        oo_state = AjanOOState({"Drone": state, "Person": person_state})
        oo_next_state = AjanOOState({"Drone": next_state, "Person": next_person_state})

        sample = self.reward_model.sample(oo_state, action, oo_next_state)

        self.assertEqual(sample, 1000, "sample mismatch in move action")

    def test_sample_move_right_right_right(self):
        self.test_init()
        state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": False})
        next_state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": True})

        person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": "Right"})

        next_person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": "Right"})

        action = AjanAction("move", {"motion": "Right"})

        oo_state = AjanOOState({"Drone": state, "Person": person_state})
        oo_next_state = AjanOOState({"Drone": next_state, "Person": next_person_state})

        sample = self.reward_model.sample(oo_state, action, oo_next_state)

        self.assertEqual(sample, 1000, "sample mismatch in move action")

    def test_sample_move_right_right_left(self):
        self.test_init()
        state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": False})
        next_state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": True})

        person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": "Right"})

        next_person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": "Right"})

        action = AjanAction("move", {"motion": "Left"})

        oo_state = AjanOOState({"Drone": state, "Person": person_state})
        oo_next_state = AjanOOState({"Drone": next_state, "Person": next_person_state})

        sample = self.reward_model.sample(oo_state, action, oo_next_state)

        self.assertEqual(sample, -1000, "sample mismatch in move action")

    def test_sample_move_right_left_left(self):
        self.test_init()
        state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": False})
        next_state = AjanAgentState("Drone", 101, {"pose": (10, 10), "gesture_found": True})

        person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": "Right"})

        next_person_state = AjanEnvObjectState("Person", 102, {"pose": (10, 10), "gesture": "Left"})

        action = AjanAction("move", {"motion": "Left"})

        oo_state = AjanOOState({"Drone": state, "Person": person_state})
        oo_next_state = AjanOOState({"Drone": next_state, "Person": next_person_state})

        sample = self.reward_model.sample(oo_state, action, oo_next_state)

        self.assertEqual(sample, 0.0, "sample mismatch in move action")  # Actually should be penalized



if __name__ == '__main__':
    unittest.main()
