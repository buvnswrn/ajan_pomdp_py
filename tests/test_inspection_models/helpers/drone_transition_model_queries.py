
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
"""


DATA_D_T = """
<http://www.dfki.de/pomdp-ns#TransitionModel> <http://www.dfki.de/pomdp-ns#attributes>
    _:node1hldl5j5dx28 .

_:node1hldl5j5dx28 <http://www.dfki.de/pomdp-ns/_drone_id> 100;
  <http://www.dfki.de/pomdp-ns/_epsilon> 1.0E-9 .
"""