import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.models.reward_model import AjanRewardModel
from tests.test_models.helpers.drone_reward_model_queries import DATA, PROBABILITY_QUERY, SAMPLE_QUERY, ARGMAX_QUERY


class TestDroneRewardModelProbability(unittest.TestCase):

    drone_reward_model = AjanRewardModel(DATA, None, PROBABILITY_QUERY,
                                         SAMPLE_QUERY, ARGMAX_QUERY)
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
