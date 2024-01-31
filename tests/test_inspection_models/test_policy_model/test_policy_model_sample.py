import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.models.policy_model import AjanPolicyModel
from tests.test_inspection_models.helpers.policy_model_queries import DATA_POLICY, SAMPLE_QUERY_POLICY, \
    ROLLOUT_QUERY_POLICY, GET_ALL_ACTIONS_QUERY


class TestPolicyModelSample(unittest.TestCase):

    policy_model = AjanPolicyModel(DATA_POLICY, None, SAMPLE_QUERY_POLICY, ROLLOUT_QUERY_POLICY, GET_ALL_ACTIONS_QUERY)

    def test_sample_2_left_false_2_0(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
