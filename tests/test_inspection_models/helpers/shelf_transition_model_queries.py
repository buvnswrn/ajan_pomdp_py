
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
        pomdp-ns1:_inspection_state ?current_inspection_state] .
        
        [rdfs:type pomdp-ns:next_state;
        pomdp-ns1:_inspection_state ?next_inspection_state] .
        BIND(IF(?current_inspection_state+1<=2, ?current_inspection_state+1, ?current_inspection_state) as ?temp_inspection_state) .
        BIND(IF(?next_inspection_state=?temp_inspection_state,1.0-1e-09, 1e-09) as ?probability) .
        }
        
        OPTIONAL {
        pomdp-ns:current_action rdfs:value pomdp-ns1:Action_move .
        [pomdp-ns1:_motion ?motion] .
        
        [rdfs:type pomdp-ns:current_state;
        pomdp-ns1:_rack_id ?current_rack_id;
        pomdp-ns1:_inspection_state ?current_inspection_state] .
        
        [rdfs:type pomdp-ns:next_state;
        pomdp-ns1:_rack_id ?next_rack_id;
        pomdp-ns1:_inspection_state ?next_inspection_state] .
        
        BIND(IF(?current_rack_id+1<=4,?current_rack_id+1,?current_rack_id) as ?rack_id_up ) .
        BIND(IF(?current_rack_id-1>=1, ?current_rack_id-1, ?current_rack_id) as ?rack_id_down) .
        
        
        BIND(IF(?motion="up" && ?next_rack_id = ?rack_id_up,1.0,
            IF(?motion="down" && ?next_rack_id=?rack_id_down,1.0,
            IF((?motion = "left" || ?motion = "right") 
            && (?current_rack_id=?next_rack_id && ?current_inspection_state=?next_inspection_state),1.0,0.0))) as ?probability) .
        }
    } 
"""

DATA_S_T = """
<http://www.dfki.de/pomdp-ns#TransitionModel> <http://www.dfki.de/pomdp-ns#attributes>
    _:node1hldl1iovx27 .

_:node1hldl1iovx27 <http://www.dfki.de/pomdp-ns/_shelf_id> 115;
  <http://www.dfki.de/pomdp-ns/_epsilon> 1.0E-9 .
"""