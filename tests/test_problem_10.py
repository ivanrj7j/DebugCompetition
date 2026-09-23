import unittest
from problems.problem_10 import character_replacement

class TestProblem10(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(character_replacement("ABAB", 2), 4)

    def test_example_2(self):
        self.assertEqual(character_replacement("AABABBA", 1), 4)

    def test_all_same(self):
        self.assertEqual(character_replacement("AAAA", 2), 4)

    def test_zero_k(self):
        self.assertEqual(character_replacement("ABAA", 0), 2)

if __name__ == "__main__":
    unittest.main()
