SAMPLE_QUERY_D_R = """
   PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
    SELECT ?sample
    WHERE {
        BIND(0 as ?sample).
        
        OPTIONAL {
        pomdp-ns:current_action rdfs:value pomdp-ns1:Action_perceive .
        
        [rdfs:type pomdp-ns:current_state;
        pomdp-ns1:_complete_status ?current_status].
        
        [rdfs:type pomdp-ns:next_state;
        pomdp-ns1:_complete_status ?next_status].
        
        BIND(IF(!?current_status && ?next_status, 1000, 
        IF(?current_status && ?next_status,?sample-10,10)) as ?sample) .
        }
        
        OPTIONAL {
        pomdp-ns:current_action rdfs:value pomdp-ns1:Action_move .
        [pomdp-ns1:_motion ?motion] .
        FILTER(?motion="left" || ?motion = "right") .
        
        [rdfs:type pomdp-ns:current_state;
        pomdp-ns1:_direction ?current_direction] .
        
        BIND(IF(?motion = ?current_direction, ?sample-1000, ?sample) as ?sample) .
        }
        
        OPTIONAL {
        pomdp-ns:current_action rdfs:value pomdp-ns1:Action_move .
        [pomdp-ns1:_motion ?motion] .
        FILTER(?motion="up" || ?motion = "down") .
        
        [rdfs:type pomdp-ns:current_state;
        pomdp-ns1:_rack_id ?current_rack_id;
        pomdp-ns1:_complete_status ?current_status] .
        
        BIND(IF(?motion="down",1, 4) as ?rack_bound) .
        
        BIND(IF(?current_rack_id = ?rack_bound,?sample-1000,?sample) as ?sample) .
        
        BIND(IF(!?current_status, ?sample-10,?sample) as ?sample) .
        }
        
        OPTIONAL {
        pomdp-ns:current_action rdfs:value pomdp-ns1:Action_perceive .
        
        [rdfs:type pomdp-ns:current_state;
        pomdp-ns1:_inspection_state ?current_inspection_state].
        
        [rdfs:type pomdp-ns:next_state;
        pomdp-ns1:_inspection_state ?next_inspection_state].
        
        BIND(IF(!?current_inspection_state+1 = ?next_inspection_state, 1000,?sample) as ?sample).        
        }
        
        OPTIONAL {
        pomdp-ns:current_action rdfs:value pomdp-ns1:Action_move .
        [pomdp-ns1:_motion ?motion] .
        FILTER(?motion="up" || ?motion = "down") .
        
        [rdfs:type pomdp-ns:current_state;
        pomdp-ns1:_rack_id ?current_rack_id;
        pomdp-ns1:_id 115] .
        
        BIND(IF(?motion="down",1, 4) as ?rack_bound) .
        
        BIND(IF(?current_rack_id = ?rack_bound,?sample-1000,?sample) as ?sample) .
        
        BIND(IF(!?current_status, ?sample-10,?sample) as ?sample) .
        }
    }
"""

ARGMAX_QUERY_D_R = """
   PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
    SELECT ?argmax
    WHERE {
        BIND(0 as ?argmax).
        
        OPTIONAL {
        pomdp-ns:current_action rdfs:value pomdp-ns1:Action_perceive .
        
        [rdfs:type pomdp-ns:current_state;
        pomdp-ns1:_complete_status ?current_status].
        
        [rdfs:type pomdp-ns:next_state;
        pomdp-ns1:_complete_status ?next_status].
        
        BIND(IF(!?current_status && ?next_status, 1000, 
        IF(?current_status && ?next_status,?argmax-10,10)) as ?argmax) .
        }
        
        OPTIONAL {
        pomdp-ns:current_action rdfs:value pomdp-ns1:Action_move .
        [pomdp-ns1:_motion ?motion] .
        FILTER(?motion="left" || ?motion = "right") .
        
        [rdfs:type pomdp-ns:current_state;
        pomdp-ns1:_direction ?current_direction] .
        
        BIND(IF(?motion = ?current_direction, ?argmax-1000, ?argmax) as ?argmax) .
        }
        
        OPTIONAL {
        pomdp-ns:current_action rdfs:value pomdp-ns1:Action_move .
        [pomdp-ns1:_motion ?motion] .
        FILTER(?motion="up" || ?motion = "down") .
        
        [rdfs:type pomdp-ns:current_state;
        pomdp-ns1:_rack_id ?current_rack_id;
        pomdp-ns1:_complete_status ?current_status] .
        
        BIND(IF(?motion="down",1, 4) as ?rack_bound) .
        
        BIND(IF(?current_rack_id = ?rack_bound,?argmax-1000,?argmax) as ?argmax) .
        
        BIND(IF(!?current_status, ?argmax-10,?argmax) as ?argmax) .
        }
        
        OPTIONAL {
        pomdp-ns:current_action rdfs:value pomdp-ns1:Action_perceive .
        
        [rdfs:type pomdp-ns:current_state;
        pomdp-ns1:_inspection_state ?current_inspection_state].
        
        [rdfs:type pomdp-ns:next_state;
        pomdp-ns1:_inspection_state ?next_inspection_state].
        
        BIND(IF(!?current_inspection_state+1 = ?next_inspection_state, 1000,?argmax) as ?argmax).        
        }
        
        OPTIONAL {
        pomdp-ns:current_action rdfs:value pomdp-ns1:Action_move .
        [pomdp-ns1:_motion ?motion] .
        FILTER(?motion="up" || ?motion = "down") .
        
        [rdfs:type pomdp-ns:current_state;
        pomdp-ns1:_rack_id ?current_rack_id;
        pomdp-ns1:_id 115] .
        
        BIND(IF(?motion="down",1, 4) as ?rack_bound) .
        
        BIND(IF(?current_rack_id = ?rack_bound,?argmax-1000,?argmax) as ?argmax) .
        
        BIND(IF(!?current_status, ?argmax-10,?argmax) as ?argmax) .
        }
    }
"""

PROBABILITY_QUERY_D_R = """
   PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
    SELECT ?probability
    WHERE {
        BIND(0 as ?rewardNew).
        pomdp-ns:current_reward rdfs:value ?current_reward .
        OPTIONAL {
        pomdp-ns:current_action rdfs:value pomdp-ns1:Action_perceive .
        
        [rdfs:type pomdp-ns:current_state;
        pomdp-ns1:_complete_status ?current_status].
        
        [rdfs:type pomdp-ns:next_state;
        pomdp-ns1:_complete_status ?next_status].
        
        BIND(IF(!?current_status && ?next_status, 1000, 
        IF(?current_status && ?next_status,?rewardNew-10,10)) as ?rewardNew) .
        }
        
        OPTIONAL {
        pomdp-ns:current_action rdfs:value pomdp-ns1:Action_move .
        [pomdp-ns1:_motion ?motion] .
        FILTER(?motion="left" || ?motion = "right") .
        
        [rdfs:type pomdp-ns:current_state;
        pomdp-ns1:_direction ?current_direction] .
        
        BIND(IF(?motion = ?current_direction, ?rewardNew-1000, ?rewardNew) as ?rewardNew) .
        }
        
        OPTIONAL {
        pomdp-ns:current_action rdfs:value pomdp-ns1:Action_move .
        [pomdp-ns1:_motion ?motion] .
        FILTER(?motion="up" || ?motion = "down") .
        
        [rdfs:type pomdp-ns:current_state;
        pomdp-ns1:_rack_id ?current_rack_id;
        pomdp-ns1:_complete_status ?current_status] .
        
        BIND(IF(?motion="down",1, 4) as ?rack_bound) .
        
        BIND(IF(?current_rack_id = ?rack_bound,?rewardNew-1000,?rewardNew) as ?rewardNew) .
        
        BIND(IF(!?current_status, ?rewardNew-10,?rewardNew) as ?rewardNew) .
        }
        
        OPTIONAL {
        pomdp-ns:current_action rdfs:value pomdp-ns1:Action_perceive .
        
        [rdfs:type pomdp-ns:current_state;
        pomdp-ns1:_inspection_state ?current_inspection_state].
        
        [rdfs:type pomdp-ns:next_state;
        pomdp-ns1:_inspection_state ?next_inspection_state].
        
        BIND(IF(!?current_inspection_state+1 = ?next_inspection_state, 1000,?rewardNew) as ?rewardNew).        
        }
        
        OPTIONAL {
        pomdp-ns:current_action rdfs:value pomdp-ns1:Action_move .
        [pomdp-ns1:_motion ?motion] .
        FILTER(?motion="up" || ?motion = "down") .
        
        [rdfs:type pomdp-ns:current_state;
        pomdp-ns1:_rack_id ?current_rack_id;
        pomdp-ns1:_id 115] .
        
        BIND(IF(?motion="down",1, 4) as ?rack_bound) .
        
        BIND(IF(?current_rack_id = ?rack_bound,?rewardNew-1000,?rewardNew) as ?rewardNew) .
        
        BIND(IF(!?current_status, ?rewardNew-10,?rewardNew) as ?rewardNew) .
        }
        BIND(IF(?rewardNew=?current_reward, 1.0, 0.0) as ?probability) .
    }
"""

DATA_D_R = """
<http://www.dfki.de/pomdp-ns#RewardModel> <http://www.dfki.de/pomdp-ns#attributes>
    _:node1hldl8pt5x29 .

_:node1hldl8pt5x29 <http://www.dfki.de/pomdp-ns/_drone_id> 100;
  <http://www.dfki.de/pomdp-ns/_shelf_id> <http://www.w3.org/1999/02/22-rdf-syntax-ns#nil>;
  <http://www.dfki.de/pomdp-ns/_big> 1000;
  <http://www.dfki.de/pomdp-ns/_small> 10 .
"""