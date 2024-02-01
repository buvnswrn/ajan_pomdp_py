
SAMPLE_QUERY_S_T = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX pomdp-data-ns:<http://www.dfki.de/pomdp-ns/POMDP/data/>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

    CONSTRUCT {
        pomdp-ns:State rdfs:value ?state .
        ?state rdfs:type pomdp-ns:State .
        ?state pomdp-ns:id ?stateId .
        ?state pomdp-ns:name "Shelf" .
        ?state pomdp-ns:type "env" .
        
        ?state pomdp-ns:attributes [
                pomdp-ns1:_id ?stateId ;
                pomdp-ns1:_rack_id ?rack_id ;
                pomdp-ns1:_inspection_state ?inspection_state ] .
                
        ?state pomdp-ns:to_print [ rdfs:value "inspection_state";
                                    rdfs:value "rack_id"] .
    }
    WHERE{
        pomdp-ns:current_state rdfs:value ?state .
        pomdp-ns:current_action rdfs:value ?action .
        ?state pomdp-ns:id ?stateId .
        [pomdp-ns1:_rack_id ?rack_id ;
         pomdp-ns1:_inspection_state ?inspection_state] .

        OPTIONAL {
            pomdp-ns:current_action rdfs:value pomdp-ns1:Action_perceive .
            BIND(IF(?inspection_state+1<=2, ?inspection_state+1,?inspection_state) as ?inspection_state) .
        }
        OPTIONAL {
            [pomdp-ns1:_motion "up" ].
            BIND(IF(?rack_id+1<=4, ?rack_id+1, ?rack_id) as ?rack_id) .
        }
        
        OPTIONAL {
            [pomdp-ns1:_motion "down" ].
            BIND(IF(?rack_id-1>=1, ?rack_id-1, ?rack_id) as ?rack_id) .
        }
    }
"""

ARGMAX_QUERY_S_T = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX pomdp-data-ns:<http://www.dfki.de/pomdp-ns/POMDP/data/>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

    CONSTRUCT {
        pomdp-ns:State rdfs:value ?state .
        ?state rdfs:type pomdp-ns:State .
        ?state pomdp-ns:id ?stateId .
        ?state pomdp-ns:name "Shelf" .
        ?state pomdp-ns:type "env" .
        
        ?state pomdp-ns:attributes [
                pomdp-ns1:_id ?stateId ;
                pomdp-ns1:_rack_id ?rack_id ;
                pomdp-ns1:_inspection_state ?inspection_state ] .
                
        ?state pomdp-ns:to_print [ rdfs:value "inspection_state";
                                    rdfs:value "rack_id"] .
    }
    WHERE{
        pomdp-ns:current_state rdfs:value ?state .
        pomdp-ns:current_action rdfs:value ?action .
        ?state pomdp-ns:id ?stateId .
        [pomdp-ns1:_rack_id ?rack_id ;
         pomdp-ns1:_inspection_state ?inspection_state] .

        OPTIONAL {
            pomdp-ns:current_action rdfs:value pomdp-ns1:Action_perceive .
            BIND(IF(?inspection_state+1<=2, ?inspection_state+1,?inspection_state) as ?inspection_state) .
        }
        OPTIONAL {
            [pomdp-ns1:_motion "up" ].
            BIND(IF(?rack_id+1<=4, ?rack_id+1, ?rack_id) as ?rack_id) .
        }
        
        OPTIONAL {
            [pomdp-ns1:_motion "down" ].
            BIND(IF(?rack_id-1>=1, ?rack_id-1, ?rack_id) as ?rack_id) .
        }
    }
"""

PROBABILITY_QUERY_S_T = """
"""

DATA_S_T = """
<http://www.dfki.de/pomdp-ns#TransitionModel> <http://www.dfki.de/pomdp-ns#attributes>
    _:node1hldl1iovx27 .

_:node1hldl1iovx27 <http://www.dfki.de/pomdp-ns/_shelf_id> 115;
  <http://www.dfki.de/pomdp-ns/_epsilon> 1.0E-9 .
"""