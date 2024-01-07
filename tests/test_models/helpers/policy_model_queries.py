SAMPLE_QUERY = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    CONSTRUCT {pomdp-ns:Action rdf:value ?actionNode .
        ?actionNode pomdp-ns:attributes ?attributeNode .
        ?attributeNode ?attribute ?attrValue .
    } WHERE {
    {SELECT DISTINCT ?actionNode WHERE {
        pomdp-ns:Action rdf:value ?actionNode .
    } ORDER BY RAND() LIMIT 1}
    OPTIONAL {
    {SELECT DISTINCT ?attributeNode WHERE {
    ?actionNode pomdp-ns:attributes ?attributeNode .
    }ORDER BY RAND() LIMIT 1}
    ?attributeNode ?attribute ?attrValue . 
    }
    }
"""

ROLLOUT_QUERY = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    CONSTRUCT {pomdp-ns:Action rdf:value ?actionNode .
        ?actionNode pomdp-ns:attributes ?attributeNode .
        ?attributeNode ?attribute ?attrValue .
    } WHERE {
    {SELECT DISTINCT ?actionNode WHERE {
        pomdp-ns:Action rdf:value ?actionNode .
    } ORDER BY RAND() LIMIT 1}
    OPTIONAL {
    {SELECT DISTINCT ?attributeNode WHERE {
    ?actionNode pomdp-ns:attributes ?attributeNode .
    }ORDER BY RAND() LIMIT 1}
    ?attributeNode ?attribute ?attrValue . 
    }
    }
"""

GET_ALL_ACTIONS_QUERY = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    CONSTRUCT {pomdp-ns:Action rdf:value ?actionNode .
        ?actionNode pomdp-ns:attributes ?attributeNode .
        ?attributeNode ?attribute ?attrValue .
    } WHERE {
    {SELECT DISTINCT ?actionNode WHERE {
        pomdp-ns:Action rdf:value ?actionNode .
    }}
    OPTIONAL {
    {SELECT DISTINCT ?attributeNode WHERE {
    ?actionNode pomdp-ns:attributes ?attributeNode .
    }}
    ?attributeNode ?attribute ?attrValue . 
    }
    }
"""

DATA = """
<http://www.dfki.de/pomdp-ns#Action> <http://www.w3.org/1999/02/22-rdf-syntax-ns#value>
    <http://www.dfki.de/pomdp-ns/Action_perceive>, <http://www.dfki.de/pomdp-ns/Action_move> .

<http://www.dfki.de/pomdp-ns/Action_perceive> <http://www.dfki.de/pomdp-ns#name> "perceive";
  <http://www.dfki.de/pomdp-ns#to_print> <http://www.w3.org/1999/02/22-rdf-syntax-ns#nil> .

<http://www.dfki.de/pomdp-ns/Action_move> <http://www.dfki.de/pomdp-ns#name> "move";
  <http://www.dfki.de/pomdp-ns#to_print> _:node1hjifhtgax13, _:node1hjifhtgax17;
  <http://www.dfki.de/pomdp-ns#attributes> _:node1hjifhtgax14, _:node1hjifhtgax18 .

_:node1hjifhtgax13 <http://www.w3.org/1999/02/22-rdf-syntax-ns#value> "motion" .

_:node1hjifhtgax14 <http://www.dfki.de/pomdp-ns/_motion> "right" .

_:node1hjifhtgax17 <http://www.w3.org/1999/02/22-rdf-syntax-ns#value> "motion" .

_:node1hjifhtgax18 <http://www.dfki.de/pomdp-ns/_motion> "left" .
"""