SAMPLE_QUERY = """
PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
PREFIX pomdp-ns-data:<http://www.dfki.de/pomdp-ns/POMDP/data/>
PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ajan-math-ns:<http://www.ajan.de/ajan/functions/math-ns#>

CONSTRUCT {
    pomdp-ns:Observation pomdp-ns:attributes ?attributes .
    pomdp-ns:Observation pomdp-ns:for_hash ?for_hash .
    ?attributes pomdp-ns1:_person_id ?person_id .
    ?attributes pomdp-ns1:_pose ?poseNode .
    
    ?for_hash rdfs:value "person_id" .
    ?for_hash rdfs:value "pose" .
    
    
    ?poseNode rdfs:type ?poseType .
    
    ?poseNode rdfs:value ?keypoint9.
    ?poseNode rdfs:value ?keypoint10 .
    ?poseNode rdfs:value ?keypoint11 .
    ?poseNode rdfs:value ?keypoint12 .

    
    ?keypoint9 rdfs:x ?xValue9 .
    ?keypoint10 rdfs:x ?xValue10 .
    ?keypoint11 rdfs:x ?xValue11 .
    ?keypoint12 rdfs:x ?xValue12 .
    
    ?keypoint9 rdfs:y ?yValue9 .
    ?keypoint10 rdfs:y ?yValue10 .
    ?keypoint11 rdfs:y ?yValue11 .
    ?keypoint12 rdfs:y ?yValue12 .

}
WHERE{
    pomdp-ns:ObservationModel pomdp-ns:attributes ?attributesNode .
    ?attributesNode pomdp-ns1:_person_id ?person_id .
    pomdp-ns:current_action rdfs:value ?action .
    
    BIND(BNODE() as ?attributes) .
    BIND(BNODE() as ?for_hash) .
    BIND(IF(?action = pomdp-ns1:Action_perceive, BNODE(), rdfs:nil) as ?poseNode) .
    BIND(pomdp-ns-data:Point_9  as ?keypoint9) .
    BIND(pomdp-ns-data:Point_10 as ?keypoint10) .
    BIND(pomdp-ns-data:Point_11 as ?keypoint11) .
    BIND(pomdp-ns-data:Point_12 as ?keypoint12) .
    BIND(pomdp-ns-data:pandasDataFrame as ?poseType)
    BIND(ajan-math-ns:sample(0, 640) as ?xValue9) .
    BIND(ajan-math-ns:sample(0, 480) as ?yValue9) .
    BIND(ajan-math-ns:sample(0, 640) as ?xValue10) .
    BIND(ajan-math-ns:sample(0, 480) as ?yValue10) .
    BIND(ajan-math-ns:sample(0, 640) as ?xValue11) .
    BIND(ajan-math-ns:sample(0, 480) as ?yValue11) .
    BIND(ajan-math-ns:sample(0, 640) as ?xValue12) .
    BIND(ajan-math-ns:sample(0, 480) as ?yValue12) .
}
"""

ARGMAX_QUERY = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX pomdp-ns-data:<http://www.dfki.de/pomdp-ns/POMDP/data/>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX ajan-math-ns:<http://www.ajan.de/ajan/functions/math-ns#>
    
    CONSTRUCT {
        pomdp-ns:Observation pomdp-ns:attributes ?attributes .
        pomdp-ns:Observation pomdp-ns:for_hash ?for_hash .
        ?attributes pomdp-ns1:_person_id ?person_id .
        ?attributes pomdp-ns1:_pose ?poseNode .
        
        ?for_hash rdfs:value "person_id" .
        ?for_hash rdfs:value "pose" .
        
        
        ?poseNode rdfs:type ?poseType .
        
        ?poseNode rdfs:value ?keypoint9.
        ?poseNode rdfs:value ?keypoint10 .
        ?poseNode rdfs:value ?keypoint11 .
        ?poseNode rdfs:value ?keypoint12 .
    
        
        ?keypoint9 rdfs:x ?xValue9 .
        ?keypoint10 rdfs:x ?xValue10 .
        ?keypoint11 rdfs:x ?xValue11 .
        ?keypoint12 rdfs:x ?xValue12 .
        
        ?keypoint9 rdfs:y ?yValue9 .
        ?keypoint10 rdfs:y ?yValue10 .
        ?keypoint11 rdfs:y ?yValue11 .
        ?keypoint12 rdfs:y ?yValue12 .
    
    }
    WHERE{
        pomdp-ns:ObservationModel pomdp-ns:attributes ?attributesNode .
        ?attributesNode pomdp-ns1:_person_id ?person_id .
        pomdp-ns:current_action rdfs:value ?action .
        
        BIND(BNODE() as ?attributes) .
        BIND(BNODE() as ?for_hash) .
        BIND(IF(?action = pomdp-ns1:Action_perceive, BNODE(), rdfs:nil) as ?poseNode) .
        BIND(pomdp-ns-data:Point_9  as ?keypoint9) .
        BIND(pomdp-ns-data:Point_10 as ?keypoint10) .
        BIND(pomdp-ns-data:Point_11 as ?keypoint11) .
        BIND(pomdp-ns-data:Point_12 as ?keypoint12) .
        BIND(pomdp-ns-data:pandasDataFrame as ?poseType)
        BIND(ajan-math-ns:sample(0, 640) as ?xValue9) .
        BIND(ajan-math-ns:sample(0, 480) as ?yValue9) .
        BIND(ajan-math-ns:sample(0, 640) as ?xValue10) .
        BIND(ajan-math-ns:sample(0, 480) as ?yValue10) .
        BIND(ajan-math-ns:sample(0, 640) as ?xValue11) .
        BIND(ajan-math-ns:sample(0, 480) as ?yValue11) .
        BIND(ajan-math-ns:sample(0, 640) as ?xValue12) .
        BIND(ajan-math-ns:sample(0, 480) as ?yValue12) .
    }
"""

PROBABILITY_QUERY = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
    PREFIX pomdp-ns-data:<http://www.dfki.de/pomdp-ns/POMDP/data/>
    PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX ajan-math-ns:<http://www.ajan.de/ajan/functions/math-ns#>
    
    SELECT ?probability
    WHERE {
        pomdp-ns:current_action rdfs:value ?action .
        pomdp-ns:Observation pomdp-ns:attributes ?attributesNode .
        ?attributesNode pomdp-ns1:_pose ?pose .
        pomdp-ns:next_state rdfs:value ?next_state .
        ?next_state pomdp-ns:attributes ?stateAttributesNode .
        ?stateAttributesNode pomdp-ns1:_gesture ?next_gesture .
    
        BIND(IF(?action != pomdp-ns1:Action_perceive && ?pose = rdfs:nil, 1.0,0.0) as ?probability) .
        
        BIND(5 as ?sigma) .
        
        BIND(ajan-math-ns:distance(10, 11) as ?testDistance) .
        BIND(pomdp-ns-data:Point_9 as ?lwrist) .
        BIND(pomdp-ns-data:Point_11 as ?lhip) .
        BIND(pomdp-ns-data:Point_10 as ?rhip) .
        BIND(pomdp-ns-data:Point_12 as ?rwrist) .
        BIND(ajan-math-ns:distance(?lhip, ?lwrist) as ?leftDistance) .
        BIND(ajan-math-ns:distance(?rhip, ?rwrist) as ?rightDistance) .
        BIND(ajan-math-ns:calculate_near_probability(?leftDistance, ?sigma) as ?leftProbability) .
        BIND(ajan-math-ns:calculate_near_probability(?rightDistance, ?sigma) as ?rightProbability) .
        
        BIND(IF(?action = pomdp-ns1:Action_perceive,
                    IF(?pose = rdfs:nil, 1.0,
                                            IF(?next_gesture = "left", ?leftProbability,
                                            IF(?next_gesture = "right", ?rightProbability, 0.0))),?probability) 
        as ?probability) .
    }
"""

DATA = """
<http://www.dfki.de/pomdp-ns#ObservationModel> <http://www.dfki.de/pomdp-ns#attributes>
    _:node1hjikqhb9x19 .

_:node1hjikqhb9x19 <http://www.dfki.de/pomdp-ns/_person_id> 112;
  <http://www.dfki.de/pomdp-ns/_epsilon> 1 .
"""