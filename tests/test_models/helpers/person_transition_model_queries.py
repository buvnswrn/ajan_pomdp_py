

SAMPLE_QUERY = """
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
        ?state pomdp-ns:to_print ?to_print_node .
        ?to_print_node rdfs:value "gesture" .
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
            ?poseNode rdfs:x ?xValue .
            ?poseNode rdfs:y ?yValue .
            BIND(pomdp-data-ns:2dVector as ?poseType) .
            ?action pomdp-ns:attributes ?actionAttributes .
            ?actionAttributes pomdp-ns1:_motion ?motionType .
        }

        BIND(BNODE() as ?attributes) .
        BIND(BNODE() as ?to_print_node) .
        BIND(IF(?action=pomdp-ns1:Action_perceive, rdfs:nil, BNODE()) as ?pose) .

        BIND(IF(?action=pomdp-ns1:Action_perceive, 
                IF(RAND()>0.5,
                    IF(RAND()>0.5, "left",rdfs:nil)
                    ,"right"), 
                ?gesture) as ?gestureValue) .
        ?s ?p ?o  .
    }
"""

ARGMAX_QUERY = """
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
        ?state pomdp-ns:to_print ?to_print_node .
        ?to_print_node rdfs:value "gesture" .
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
            ?poseNode rdfs:x ?xValue .
            ?poseNode rdfs:y ?yValue .
            BIND(pomdp-data-ns:2dVector as ?poseType) .
            ?action pomdp-ns:attributes ?actionAttributes .
            ?actionAttributes pomdp-ns1:_motion ?motionType .
        }

        BIND(BNODE() as ?attributes) .
        BIND(BNODE() as ?to_print_node) .
        BIND(IF(?action=pomdp-ns1:Action_perceive, rdfs:nil, BNODE()) as ?pose) .

        BIND(IF(?action=pomdp-ns1:Action_perceive, 
                IF(RAND()>0.5,
                    IF(RAND()>0.5, "left",rdfs:nil)
                    ,"right"), 
                ?gesture) as ?gestureValue) .
        ?s ?p ?o  .
    }
"""

PROBABILITY_QUERY = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    SELECT ?probability
    WHERE{
        pomdp-ns:next_state rdf:value ?next_state .
        pomdp-ns:current_state rdf:value ?current_state .
        pomdp-ns:TransitionModel pomdp-ns:attributes ?attributesNode .
        ?attributesNode pomdp-ns1:_epsilon ?epsilon .
        BIND(IF(?next_state=?current_state, 1-?epsilon, ?epsilon) as ?probability) .
    }
"""

DATA = """
<http://www.dfki.de/pomdp-ns#TransitionModel> <http://www.dfki.de/pomdp-ns#attributes>
    _:node1hjfvnde8x20 .

_:node1hjfvnde8x20 <http://www.dfki.de/pomdp-ns/_person_id> 112;
  <http://www.dfki.de/pomdp-ns/_epsilon> 1.0E-9 .
"""