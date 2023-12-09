import unittest

from rdflib import Graph

from POMDPService.ajan_pomdp_planning.helpers.to_graph import add_action_to_graph
from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction
from POMDPService.ajan_pomdp_planning.oopomdp.domain.state import AjanAgentState
from POMDPService.ajan_pomdp_planning.oopomdp.models.policy_model import AjanPolicyModel


class TestPolicyModel(unittest.TestCase):

    policy_model = None

    sample_query = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    CONSTRUCT {pomdp-ns:Action rdf:value ?actionNode .
        ?actionNode pomdp-ns:attributes ?attributeNode .
        ?attributeNode ?attribute ?attrValue .
    } WHERE {
    {SELECT DISTINCT ?actionNode WHERE {
        pomdp-ns:current_action rdf:value ?actionNode .
    } ORDER BY RAND() LIMIT 1}
    OPTIONAL {
    {SELECT DISTINCT ?attributeNode WHERE {
    ?actionNode pomdp-ns:attributes ?attributeNode .
    }ORDER BY RAND() LIMIT 1}
    ?attributeNode ?attribute ?attrValue . 
    }
    }
    """

    rollout_query = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    CONSTRUCT {pomdp-ns:Action rdf:value ?actionNode .
        ?actionNode pomdp-ns:attributes ?attributeNode .
        ?attributeNode ?attribute ?attrValue .
    } WHERE {
    {SELECT DISTINCT ?actionNode WHERE {
        pomdp-ns:current_action rdf:value ?actionNode .
    } ORDER BY RAND() LIMIT 1}
    OPTIONAL {
    {SELECT DISTINCT ?attributeNode WHERE {
    ?actionNode pomdp-ns:attributes ?attributeNode .
    }ORDER BY RAND() LIMIT 1}
    ?attributeNode ?attribute ?attrValue . 
    }
    }
    """

    get_all_actions_query = """
    PREFIX pomdp-ns:<http://www.dfki.de/pomdp-ns#>
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    CONSTRUCT {pomdp-ns:Action rdf:value ?actionNode .
        ?actionNode pomdp-ns:attributes ?attributeNode .
        ?attributeNode ?attribute ?attrValue .
    } WHERE {
    {SELECT DISTINCT ?actionNode WHERE {
        pomdp-ns:current_action rdf:value ?actionNode .
    }}
    OPTIONAL {
    {SELECT DISTINCT ?attributeNode WHERE {
    ?actionNode pomdp-ns:attributes ?attributeNode .
    }}
    ?attributeNode ?attribute ?attrValue . 
    }
    }
    """

    def test_init(self):
        perceive_action = AjanAction("perceive")
        move_left_action = AjanAction("move", {"motion": "Left"})
        move_right_action = AjanAction("move", {"motion": "Right"})
        actions_graph = Graph()
        add_action_to_graph(actions_graph, perceive_action)
        add_action_to_graph(actions_graph, move_left_action)
        add_action_to_graph(actions_graph, move_right_action)
        actions_graph_string = actions_graph.serialize(format='turtle')
        self.policy_model = AjanPolicyModel(actions_graph_string, [], self.sample_query, self.rollout_query,
                                            self.get_all_actions_query)
        self.assertNotEqual(self.policy_model, None, "Should not be None")  # add assertion here

    def test_sample(self):
        self.test_init()
        agent_state = AjanAgentState("Drone", 101)
        action = self.policy_model.sample(agent_state)
        perceive_action = AjanAction("perceive")
        move_left_action = AjanAction("move", {"motion": "Left"})
        move_right_action = AjanAction("move", {"motion": "Right"})
        self.assertIn(action, [perceive_action, move_right_action, move_left_action],
                      "Should be equal to some predefined actions")

    def test_rollout(self):
        self.test_init()
        agent_state = AjanAgentState("Drone", 101)
        action = self.policy_model.rollout(agent_state)
        perceive_action = AjanAction("perceive")
        move_left_action = AjanAction("move", {"motion": "Left"})
        move_right_action = AjanAction("move", {"motion": "Right"})
        self.assertIn(action, [perceive_action, move_right_action, move_left_action],
                      "Should be equal to some predefined actions")

    def test_get_all_actions(self):
        self.test_init()
        agent_state = AjanAgentState("Drone", 101)
        actions = self.policy_model.get_all_actions(agent_state)
        perceive_action = AjanAction("perceive")
        move_left_action = AjanAction("move", {"motion": "Left"})
        move_right_action = AjanAction("move", {"motion": "Right"})
        self.assertEqual(set(actions), {perceive_action, move_right_action, move_left_action},
                         "Should be equal to predefined actions")


if __name__ == '__main__':
    unittest.main()
