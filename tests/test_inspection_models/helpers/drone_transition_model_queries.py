
SAMPLE_QUERY_D_T = """
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
        ?state pomdp-ns:type "agent" .
        
        ?state pomdp-ns:attributes [
                pomdp-ns1:_id ?stateId ;
                pomdp-ns1:_rack_id ?rack_id ;
                pomdp-ns1:_direction ?direction ;
                pomdp-ns1:_complete_status ?complete_status ] .
                
        ?state pomdp-ns:to_print [ rdfs:value "complete_status";
                                    rdfs:value "direction";
                                    rdfs:value "rack_id"] .
    }
    WHERE{
        pomdp-ns:current_state rdfs:value ?state .
        pomdp-ns:current_action rdfs:value ?action .
        ?state pomdp-ns:id ?stateId .
        [pomdp-ns1:_rack_id ?rack_id ;
         pomdp-ns1:_direction ?direction;
         pomdp-ns1:_complete_status ?complete_status] .

        OPTIONAL {
            pomdp-ns:current_action rdfs:value pomdp-ns1:Action_perceive .
            BIND( IF(RAND() > 0.5, true, false) as ?complete_status) .
        }
        OPTIONAL {
            [pomdp-ns1:_motion "up" ].
            BIND(IF(?rack_id+1<=4, ?rack_id+1, ?rack_id) as ?rack_id) .
        }
        
        OPTIONAL {
            [pomdp-ns1:_motion "down" ].
            BIND(IF(?rack_id-1>=1, ?rack_id-1, ?rack_id) as ?rack_id) .
        }
        
        OPTIONAL {
            [pomdp-ns1:_motion "left" ] .
            BIND("left" as ?direction) .
        }
        
        OPTIONAL {
            [pomdp-ns1:_motion "right" ] .
            BIND("right" as ?direction) .
        }
    }
"""


ARGMAX_QUERY_D_T = """
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
        ?state pomdp-ns:type "agent" .
        
        ?state pomdp-ns:attributes [
                pomdp-ns1:_id ?stateId ;
                pomdp-ns1:_rack_id ?rack_id ;
                pomdp-ns1:_direction ?direction ;
                pomdp-ns1:_complete_status ?complete_status ] .
                
        ?state pomdp-ns:to_print [ rdfs:value "complete_status";
                                    rdfs:value "direction";
                                    rdfs:value "rack_id"] .
    }
    WHERE{
        pomdp-ns:current_state rdfs:value ?state .
        pomdp-ns:current_action rdfs:value ?action .
        ?state pomdp-ns:id ?stateId .
        [pomdp-ns1:_rack_id ?rack_id ;
         pomdp-ns1:_direction ?direction;
         pomdp-ns1:_complete_status ?complete_status] .

        OPTIONAL {
            pomdp-ns:current_action rdfs:value pomdp-ns1:Action_perceive .
            BIND( IF(RAND() > 0.5, true, false) as ?complete_status) .
        }
        OPTIONAL {
            [pomdp-ns1:_motion "up" ].
            BIND(IF(?rack_id+1<=4, ?rack_id+1, ?rack_id) as ?rack_id) .
        }
        
        OPTIONAL {
            [pomdp-ns1:_motion "down" ].
            BIND(IF(?rack_id-1>=1, ?rack_id-1, ?rack_id) as ?rack_id) .
        }
        
        OPTIONAL {
            [pomdp-ns1:_motion "left" ] .
            BIND("left" as ?direction) .
        }
        
        OPTIONAL {
            [pomdp-ns1:_motion "right" ] .
            BIND("right" as ?direction) .
        }
    }
"""


PROBABILITY_QUERY_D_T = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX pomdp-data-ns:<http://www.dfki.de/pomdp-ns/POMDP/data/>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

    SELECT ?probability WHERE {
     
        BIND(0.0 as ?probability) .
        
        OPTIONAL {
        pomdp-ns:current_action rdfs:value pomdp-ns1:Action_perceive .
        
        [rdfs:type pomdp-ns:current_state;
        pomdp-ns1:_direction ?current_direction;
        pomdp-ns1:_rack_id ?current_rack_id;
        pomdp-ns1:_complete_status ?current_status] .
        
        [rdfs:type pomdp-ns:next_state;
        pomdp-ns1:_direction ?next_direction;
        pomdp-ns1:_rack_id ?next_rack_id;
        pomdp-ns1:_complete_status ?next_status] .
        
        BIND(IF(?current_direction = ?next_direction && (?current_rack_id = ?next_rack_id),
            IF(!?current_status, 0.5,
            IF(?current_status && ?next_status, 1.0, 0.0)),
            0.0) as ?probability) .
        }
        
        OPTIONAL {
        pomdp-ns:current_action rdfs:value pomdp-ns1:Action_move .
        [pomdp-ns1:_motion ?motion] .
        
        [rdfs:type pomdp-ns:current_state;
        pomdp-ns1:_direction ?current_direction;
        pomdp-ns1:_rack_id ?current_rack_id;
        pomdp-ns1:_complete_status ?current_status] .
        
        [rdfs:type pomdp-ns:next_state;
        pomdp-ns1:_direction ?next_direction;
        pomdp-ns1:_rack_id ?next_rack_id;
        pomdp-ns1:_complete_status ?next_status] .
        
        BIND(IF(?current_rack_id+1<=4,?current_rack_id+1,?current_rack_id) as ?rack_id_up ) .
        BIND(IF(?current_rack_id-1>=1, ?current_rack_id-1, ?current_rack_id) as ?rack_id_down) .
        
        BIND(IF(?current_rack_id=?next_rack_id && ?motion!="up" && ?motion!="down",
                    IF(?motion = "left" || ?motion = "right",
                            IF(?next_direction=?motion, 1.0,0.0)
                        ,0.0),
                        
                IF(?next_direction = ?current_direction,
                    IF(?motion="up" && ?next_rack_id = ?rack_id_up, 1.0,
                        IF(?motion="down" && ?next_rack_id = ?rack_id_down,1.0,0.0)),0.0)
                    )  as ?probability) .
        }
    }       
"""


DATA_D_T = """
<http://www.dfki.de/pomdp-ns#TransitionModel> <http://www.dfki.de/pomdp-ns#attributes>
    _:node1hldl5j5dx28 .

_:node1hldl5j5dx28 <http://www.dfki.de/pomdp-ns/_drone_id> 100;
  <http://www.dfki.de/pomdp-ns/_epsilon> 1.0E-9 .
"""