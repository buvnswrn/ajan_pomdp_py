SAMPLE_QUERY_OBS = """
PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
PREFIX pomdp-ns-data:<http://www.dfki.de/pomdp-ns/POMDP/data/>
PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ajan-math-ns:<http://www.ajan.de/ajan/functions/math-ns#>
PREFIX unity-ns: <http://www.dfki.de/unity-ns#>
PREFIX unity-ns1: <http://www.dfki.de/unity-ns/>

CONSTRUCT {
    pomdp-ns:Observation pomdp-ns:attributes [
    pomdp-ns1:_object_id 0;
    pomdp-ns1:_objects ?poseNode;
    ?keypoint9 [ rdfs:type ?keypoint9_type ;
                rdfs:x ?xValue9 ;
                rdfs:y ?yValue9 ;
                rdfs:w ?wValue9 ;
                rdfs:h ?hValue9 ];
    ?box_1_probability_Node ?Box_1_probability] .
    
    pomdp-ns:Observation pomdp-ns:for_hash ?for_hash .
    ?for_hash rdfs:value "object_id" .
    ?for_hash rdfs:value "objects" .
    
    ?poseNode rdfs:type ?objectsType .
    ?poseNode rdfs:value ?keypoint9.
}
WHERE{
    pomdp-ns:ObservationModel pomdp-ns:attributes ?attributesNode .
    pomdp-ns:current_action rdfs:value ?action .
    BIND(BNODE() as ?attributes) .
    BIND(BNODE() as ?for_hash) .
    BIND(IF(?action = pomdp-ns1:Action_perceive, BNODE(), rdfs:nil) as ?poseNode) .
    OPTIONAL {
    pomdp-ns:current_action rdfs:value pomdp-ns1:Action_perceive .
    BIND(unity-ns1:_Box_1  as ?keypoint9) .
    BIND(pomdp-ns-data:4dVector  as ?keypoint9_type) .
    BIND(pomdp-ns-data:Vector as ?objectsType)
    BIND(RAND() as ?xValue9) .
    BIND(RAND() as ?yValue9) .
    BIND(RAND() as ?wValue9) .
    BIND(RAND() as ?hValue9) .
    BIND(unity-ns1:Box_1_probability as ?box_1_probability_Node) .
    BIND(RAND() as ?Box_1_probability).
    }
}
"""

ARGMAX_QUERY_OBS = """
PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
PREFIX pomdp-ns-data:<http://www.dfki.de/pomdp-ns/POMDP/data/>
PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ajan-math-ns:<http://www.ajan.de/ajan/functions/math-ns#>
PREFIX unity-ns: <http://www.dfki.de/unity-ns#>
PREFIX unity-ns1: <http://www.dfki.de/unity-ns/>

CONSTRUCT {
    pomdp-ns:Observation pomdp-ns:attributes [
    pomdp-ns1:_object_id 0;
    pomdp-ns1:_objects ?poseNode;
    ?keypoint9 [ rdfs:type ?keypoint9_type ;
                rdfs:x ?xValue9 ;
                rdfs:y ?yValue9 ;
                rdfs:w ?wValue9 ;
                rdfs:h ?hValue9 ];
    ?box_1_probability_Node ?Box_1_probability] .
    
    pomdp-ns:Observation pomdp-ns:for_hash ?for_hash .
    ?for_hash rdfs:value "object_id" .
    ?for_hash rdfs:value "objects" .
    
    ?poseNode rdfs:type ?objectsType .
    ?poseNode rdfs:value ?keypoint9.
}
WHERE{
    pomdp-ns:ObservationModel pomdp-ns:attributes ?attributesNode .
    pomdp-ns:current_action rdfs:value ?action .
    BIND(BNODE() as ?attributes) .
    BIND(BNODE() as ?for_hash) .
    BIND(IF(?action = pomdp-ns1:Action_perceive, BNODE(), rdfs:nil) as ?poseNode) .
    OPTIONAL {
    pomdp-ns:current_action rdfs:value pomdp-ns1:Action_perceive .
    BIND(unity-ns1:_Box_1  as ?keypoint9) .
    BIND(pomdp-ns-data:4dVector  as ?keypoint9_type) .
    BIND(pomdp-ns-data:Vector as ?objectsType)
    BIND(RAND() as ?xValue9) .
    BIND(RAND() as ?yValue9) .
    BIND(RAND() as ?wValue9) .
    BIND(RAND() as ?hValue9) .
    BIND(unity-ns1:Box_1_probability as ?box_1_probability_Node) .
    BIND(RAND() as ?Box_1_probability).
    }
}
"""

PROBABILITY_QUERY_OBS = """
PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
PREFIX pomdp-ns1:<http://www.dfki.de/pomdp-ns/>
PREFIX rdfs:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?probability
WHERE{
    pomdp-ns:current_action rdfs:value ?action .
    [pomdp-ns1:_objects ?objectsNode] .
    BIND(IF(?objectsNode=rdfs:nil,1.0, 0) as ?probability) .
    
    OPTIONAL {
    {
    SELECT (AVG(?prob) as ?probability) {
    pomdp-ns:current_action rdfs:value pomdp-ns1:Action_perceive .
    FILTER(?objectsNode!=rdfs:nil) .
    ?objectsNode rdfs:value ?objects .
    BIND(URI(CONCAT(str(pomdp-ns1:), CONCAT("_", CONCAT(str(?objects), "_probability")))) as ?probURI) .
    [?probURI ?prob] .
    }
    }
    }
    
}
"""

DATA_OBS = """
<http://www.dfki.de/pomdp-ns#ObservationModel> <http://www.dfki.de/pomdp-ns#attributes>
    _:node1hldl1iovx26 .

_:node1hldl1iovx26 <http://www.dfki.de/pomdp-ns/_shelf_id> 115;
  <http://www.dfki.de/pomdp-ns/_epsilon> 1 .
"""