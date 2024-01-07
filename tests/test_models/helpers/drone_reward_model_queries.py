
SAMPLE_QUERY = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
    SELECT ?sample
    WHERE {
        pomdp-ns:current_action rdfs:value ?action .
        pomdp-ns:RewardModel pomdp-ns:attributes ?modelAttributesNode .
        
        OPTIONAL {
        ?action pomdp-ns:attributes ?actionAttributeNode .
        ?actionAttributeNode pomdp-ns1:_motion ?motionType .
        }
        
        OPTIONAL {
        ?modelAttributesNode pomdp-ns1:_drone_id ?droneId.
        pomdp-ns:current_state rdfs:value ?currentOOState .
        ?currentOOState rdfs:type pomdp-ns:OOState .
        ?currentOOState rdfs:value ?currentDroneState .
        ?currentDroneState pomdp-ns:id ?droneId .
        }
        
        OPTIONAL {
        ?modelAttributesNode pomdp-ns1:_person_id ?personId.
        pomdp-ns:current_state rdfs:value ?currentOOState .
        ?currentOOState rdfs:type pomdp-ns:OOState .
        ?currentOOState rdfs:value ?currentPersonState .
        ?currentPersonState pomdp-ns:id ?personId .
        }
        
        OPTIONAL {
        pomdp-ns:current_state rdfs:value ?currentDroneState .}
        
        pomdp-ns:next_state rdfs:value ?nextState .
        
        ?modelAttributesNode pomdp-ns1:_big ?bigReward .
        BIND(0.0 as ?probability) .
        BIND(0.0 as ?temp_reward) .
        
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

ARGMAX_QUERY = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
    SELECT ?argmax
    WHERE {
        pomdp-ns:current_action rdfs:value ?action .
        pomdp-ns:RewardModel pomdp-ns:attributes ?modelAttributesNode .
        
        OPTIONAL {
        ?action pomdp-ns:attributes ?actionAttributeNode .
        ?actionAttributeNode pomdp-ns1:_motion ?motionType .
        }
        
        OPTIONAL {
        ?modelAttributesNode pomdp-ns1:_drone_id ?droneId.
        pomdp-ns:current_state rdfs:value ?currentOOState .
        ?currentOOState rdfs:type pomdp-ns:OOState .
        ?currentOOState rdfs:value ?currentDroneState .
        ?currentDroneState pomdp-ns:id ?droneId .
        }
        
        OPTIONAL {
        ?modelAttributesNode pomdp-ns1:_person_id ?personId.
        pomdp-ns:current_state rdfs:value ?currentOOState .
        ?currentOOState rdfs:type pomdp-ns:OOState .
        ?currentOOState rdfs:value ?currentPersonState .
        ?currentPersonState pomdp-ns:id ?personId .
        }
        
        OPTIONAL {
        pomdp-ns:current_state rdfs:value ?currentDroneState .}
        
        pomdp-ns:next_state rdfs:value ?nextState .
        
        ?modelAttributesNode pomdp-ns1:_big ?bigReward .
        BIND(0.0 as ?probability) .
        BIND(0.0 as ?temp_reward) .
        
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

PROBABILITY_QUERY = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
    SELECT ?probability
    WHERE {
        pomdp-ns:current_action rdfs:value ?action .
        pomdp-ns:RewardModel pomdp-ns:attributes ?modelAttributesNode .
        
        OPTIONAL {
        ?action pomdp-ns:attributes ?actionAttributeNode .
        ?actionAttributeNode pomdp-ns1:_motion ?motionType .
        }
        
        OPTIONAL {
        ?modelAttributesNode pomdp-ns1:_drone_id ?droneId.
        pomdp-ns:current_state rdfs:value ?currentOOState .
        ?currentOOState rdfs:type pomdp-ns:OOState .
        ?currentOOState rdfs:value ?currentDroneState .
        ?currentDroneState pomdp-ns:id ?droneId .
        }
        
        OPTIONAL {
        ?modelAttributesNode pomdp-ns1:_person_id ?personId.
        pomdp-ns:current_state rdfs:value ?currentOOState .
        ?currentOOState rdfs:type pomdp-ns:OOState .
        ?currentOOState rdfs:value ?currentPersonState .
        ?currentPersonState pomdp-ns:id ?personId .
        }
        
        OPTIONAL {
        pomdp-ns:current_state rdfs:value ?currentDroneState .}
        
        pomdp-ns:next_state rdfs:value ?nextState .
        
        ?modelAttributesNode pomdp-ns1:_big ?bigReward .
        BIND(0.0 as ?probability) .
        BIND(0.0 as ?temp_reward) .
        
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
        
        BIND(?perceiveReward as ?probability) .
        
    }
"""

DATA = """
<http://www.dfki.de/pomdp-ns#RewardModel> <http://www.dfki.de/pomdp-ns#attributes>
    _:node1hjhkjqjrx22 .

_:node1hjhkjqjrx22 <http://www.dfki.de/pomdp-ns/_drone_id> 100;
  <http://www.dfki.de/pomdp-ns/_person_id> <http://www.w3.org/1999/02/22-rdf-syntax-ns#nil>;
  <http://www.dfki.de/pomdp-ns/_big> 1000;
  <http://www.dfki.de/pomdp-ns/_small> 1 .
"""