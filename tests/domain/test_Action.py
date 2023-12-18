import unittest

from POMDPService.ajan_pomdp_planning.oopomdp.domain.action import AjanAction


class TestAjanAction(unittest.TestCase):
    def test_eq(self):
        action1 = AjanAction("perceive")
        action2 = AjanAction("perceive")
        self.assertEqual(action1, action2)

    def test_eq_with_attributes(self):
        action1 = AjanAction("move", attributes={"motion": "left"})
        action2 = AjanAction("move", attributes={"motion": "right"})
        self.assertNotEqual(action1, action2)

    def test_str(self):
        action = AjanAction("move", attributes={"motion": "left"})
        self.assertEqual(str(action), "move")

    def test_repr(self):
        action = AjanAction("move", attributes={"motion": "left"})
        self.assertEqual(repr(action), "AjanAction(move)")

    def test_repr_with_attributes(self):
        action = AjanAction("move", attributes={"motion": "left"}, for_hash=["motion"])
        self.assertEqual(repr(action), "AjanAction(move, left)")

    def test_hash(self):
        action = AjanAction("move")
        self.assertEqual(hash(action), hash("AjanAction(move)"))

    def test_hash_with_attributes(self):
        action = AjanAction("move", attributes={"motion": "left"})
        self.assertEqual(hash(action), hash("AjanAction(move)"))

    def test_actions_hash_with_attributes(self):
        action1 = AjanAction("move", attributes={"motion": "left"}, for_hash=["motion"])
        action2 = AjanAction("move", attributes={"motion": "right"}, for_hash=["motion"])
        self.assertNotEqual(hash(action1), hash(action2))


if __name__ == '__main__':
    unittest.main()
