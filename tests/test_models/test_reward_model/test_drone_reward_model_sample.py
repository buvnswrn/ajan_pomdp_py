import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.models.reward_model import AjanRewardModel


class TestDroneRewardModelSample(unittest.TestCase):

    reward_model = AjanRewardModel()

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
