SAMPLE_QUERY_POLICY = """
"""

ROLLOUT_QUERY_POLICY = """
"""

GET_ALL_ACTIONS_QUERY = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    CONSTRUCT {pomdp-ns:Action rdf:value ?actionNode .
        ?actionNode pomdp-ns:attributes ?attributeNode .
        ?attributeNode ?attribute ?attrValue .
    } WHERE {
    
    {
    
    [pomdp-ns1:_complete_status ?complete_status] .
    [pomdp-ns1:_direction ?direction].
    [pomdp-ns1:_inspection_state ?inspection_state] .
    [pomdp-ns1:_rack_id ?rack_id].
    
    BIND (IF(!?complete_status && (?inspection_state = 0 || ?inspection_state = 1), pomdp-ns1:Action_perceive,pomdp-ns1:Action_move) AS ?actionNode) .
    }
    
    UNION {
    [pomdp-ns1:_inspection_state ?inspection_state] .
    [pomdp-ns1:_rack_id ?rack_id] .
    FILTER(?inspection_state = 2) .
    FILTER(?rack_id > 1) .
    ?actionNode pomdp-ns:attributes ?attributeNode .
    ?attributeNode pomdp-ns1:_motion "down" . 
    ?attributeNode ?attribute ?attrValue .
    }
    
    UNION {
    [pomdp-ns1:_inspection_state ?inspection_state] .
    [pomdp-ns1:_rack_id ?rack_id] .
    FILTER(?inspection_state = 2) .
    FILTER(?rack_id < 4) .
    ?actionNode pomdp-ns:attributes ?attributeNode .
    ?attributeNode pomdp-ns1:_motion "up" . 
    ?attributeNode ?attribute ?attrValue .
    }
    UNION {
    [pomdp-ns1:_complete_status ?complete_status] .
    [pomdp-ns1:_direction ?direction] .
    FILTER(?complete_status) .
    [pomdp-ns1:_inspection_state ?inspection_state] .
    FILTER(?inspection_state != 2) .
    ?actionNode pomdp-ns:attributes ?attributeNode .
    BIND(IF(?direction="left", "right", "left") as ?action_motion) . 
    ?attributeNode pomdp-ns1:_motion ?action_motion . 
    ?attributeNode ?attribute ?attrValue .
    }
    
    UNION {
    pomdp-ns:Action rdf:value ?actionNode .
    OPTIONAL {
    ?actionNode pomdp-ns:attributes ?attributeNode .
    ?attributeNode ?attribute ?attrValue .
    }
    FILTER NOT EXISTS {
    [pomdp-ns1:_complete_status ?complete_status] .
    [pomdp-ns1:_direction ?direction].
    [pomdp-ns1:_inspection_state ?inspection_state] .
    [pomdp-ns1:_rack_id ?rack_id].
    }
    }
    
    } 
"""

DATA_POLICY = """
<http://www.dfki.de/pomdp-ns#PolicyModel> <http://www.dfki.de/pomdp-ns#attributes>
    _:node1hldkvmbdx25 .

_:node1hldkvmbdx25 <http://www.dfki.de/pomdp-ns/_drone_id> 100;
  <http://www.dfki.de/pomdp-ns/_shelf_id> 115 .

<http://www.dfki.de/pomdp-ns#Action> <http://www.w3.org/1999/02/22-rdf-syntax-ns#value>
    <http://www.dfki.de/pomdp-ns/Action_perceive>, <http://www.dfki.de/pomdp-ns/Action_move> .

<http://www.dfki.de/pomdp-ns/Action_perceive> <http://www.dfki.de/pomdp-ns#name> "perceive";
  <http://www.dfki.de/pomdp-ns#to_print> <http://www.w3.org/1999/02/22-rdf-syntax-ns#nil> .

<http://www.dfki.de/pomdp-ns/Action_move> <http://www.dfki.de/pomdp-ns#name> "move";
  <http://www.dfki.de/pomdp-ns#to_print> _:node1hldkvmbdx11, _:node1hldkvmbdx15, _:node1hldkvmbdx19,
    _:node1hldkvmbdx23;
  <http://www.dfki.de/pomdp-ns#attributes> _:node1hldkvmbdx12, _:node1hldkvmbdx16, _:node1hldkvmbdx20,
    _:node1hldkvmbdx24 .

_:node1hldkvmbdx11 <http://www.w3.org/1999/02/22-rdf-syntax-ns#value> "motion" .

_:node1hldkvmbdx12 <http://www.dfki.de/pomdp-ns/_motion> "right" .

_:node1hldkvmbdx15 <http://www.w3.org/1999/02/22-rdf-syntax-ns#value> "motion" .

_:node1hldkvmbdx16 <http://www.dfki.de/pomdp-ns/_motion> "left" .

_:node1hldkvmbdx19 <http://www.w3.org/1999/02/22-rdf-syntax-ns#value> "motion" .

_:node1hldkvmbdx20 <http://www.dfki.de/pomdp-ns/_motion> "up" .

_:node1hldkvmbdx23 <http://www.w3.org/1999/02/22-rdf-syntax-ns#value> "motion" .

_:node1hldkvmbdx24 <http://www.dfki.de/pomdp-ns/_motion> "down" .
"""
