

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
        ?state pomdp-ns:name "Drone" .
        ?state pomdp-ns:type "agent" .
        ?state pomdp-ns:attributes ?attributes .
        ?state pomdp-ns:to_print ?to_print_node .
        ?to_print_node rdfs:value "gesture_found" .
        ?attributes pomdp-ns1:_id ?stateId .

        ?attributes pomdp-ns1:_gesture_found ?gestureValue .

        ?attributes pomdp-ns1:_pose ?poseNew .
        ?poseNew rdfs:type pomdp-data-ns:2dVector .
        ?poseNew rdfs:x ?xValue .
        ?poseNew rdfs:y ?yValue .

    }
    WHERE{
        pomdp-ns:current_state rdfs:value ?state .
        pomdp-ns:current_action rdfs:value ?action .
        ?state pomdp-ns:id ?stateId .
        ?state pomdp-ns:attributes ?attributesNode .
        ?attributesNode pomdp-ns1:_pose ?poseNode .
        ?attributesNode pomdp-ns1:_gesture_found ?gesture .
        
        OPTIONAL {
            ?poseNode rdfs:x ?xPose .
            ?poseNode rdfs:y ?yPose .
        }
        
        OPTIONAL{    
            ?action pomdp-ns:attributes ?actionAttributes .
            ?actionAttributes pomdp-ns1:_motion ?motionType .
        }

        BIND(BNODE() as ?attributes) .
        BIND(BNODE() as ?to_print_node) .
        BIND(BNODE() as ?pose) .
        BIND(BNODE() as ?poseValue) .
        
        BIND(IF(?poseNode = rdfs:nil && ?action=pomdp-ns1:Action_perceive, rdfs:nil, ?pose) as ?poseNew) .

        BIND(IF (?action=pomdp-ns1:Action_move && ?motionType ="right",
                ?xPose+1,?xPose) as ?xValue) .
        BIND(IF (?action=pomdp-ns1:Action_move && ?motionType ="left",
                ?xPose-1,?xValue) as ?xValue) .
        BIND(IF(?action=pomdp-ns1:Action_move,?yPose+1,?yPose) as ?yValue) .
        BIND(IF(?action=pomdp-ns1:Action_perceive, 
                IF(RAND()>0.5,"true"^^xsd:boolean,"false"^^xsd:boolean), 
            "false"^^xsd:boolean) as ?gestureValue) .
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
        ?state pomdp-ns:name "Drone" .
        ?state pomdp-ns:type "agent" .
        ?state pomdp-ns:attributes ?attributes .
        ?state pomdp-ns:to_print ?to_print_node .
        ?to_print_node rdfs:value "gesture_found" .
        ?attributes pomdp-ns1:_id ?stateId .

        ?attributes pomdp-ns1:_gesture_found ?gestureValue .

        ?attributes pomdp-ns1:_pose ?poseNew .
        ?poseNew rdfs:type pomdp-data-ns:2dVector .
        ?poseNew rdfs:x ?xValue .
        ?poseNew rdfs:y ?yValue .

    }
    WHERE{
        pomdp-ns:current_state rdfs:value ?state .
        pomdp-ns:current_action rdfs:value ?action .
        ?state pomdp-ns:id ?stateId .
        ?state pomdp-ns:attributes ?attributesNode .
        ?attributesNode pomdp-ns1:_pose ?poseNode .
        ?attributesNode pomdp-ns1:_gesture_found ?gesture .
        
        OPTIONAL {
            ?poseNode rdfs:x ?xPose .
            ?poseNode rdfs:y ?yPose .
        }
        
        OPTIONAL{    
            ?action pomdp-ns:attributes ?actionAttributes .
            ?actionAttributes pomdp-ns1:_motion ?motionType .
        }

        BIND(BNODE() as ?attributes) .
        BIND(BNODE() as ?to_print_node) .
        BIND(BNODE() as ?pose) .
        BIND(BNODE() as ?poseValue) .
        
        BIND(IF(?poseNode = rdfs:nil && ?action=pomdp-ns1:Action_perceive, rdfs:nil, ?pose) as ?poseNew) .

        BIND(IF (?action=pomdp-ns1:Action_move && ?motionType ="right",
                ?xPose+1,?xPose) as ?xValue) .
        BIND(IF (?action=pomdp-ns1:Action_move && ?motionType ="left",
                ?xPose-1,?xValue) as ?xValue) .
        BIND(IF(?action=pomdp-ns1:Action_move,?yPose+1,?yPose) as ?yValue) .
        BIND(IF(?action=pomdp-ns1:Action_perceive, 
                IF(RAND()>0.5,"true"^^xsd:boolean,"false"^^xsd:boolean), 
            "false"^^xsd:boolean) as ?gestureValue) .
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
    _:node1hjfvg6grx21 .

_:node1hjfvg6grx21 <http://www.dfki.de/pomdp-ns/_drone_id> 100;
  <http://www.dfki.de/pomdp-ns/_epsilon> 1.0E-9 .
"""