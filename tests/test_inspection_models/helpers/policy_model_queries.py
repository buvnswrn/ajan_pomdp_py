SAMPLE_QUERY_POLICY = """
"""

ROLLOUT_QUERY_POLICY = """
"""

GET_ALL_ACTIONS_QUERY = """
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
