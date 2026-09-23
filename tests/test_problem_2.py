import unittest
from problems.problem_2 import min_window

class TestProblem2(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(min_window("ADOBECODEBANC", "ABC"), "BANC")

    def test_example_2(self):
        self.assertEqual(min_window("a", "a"), "a")

    def test_example_3(self):
        self.assertEqual(min_window("a", "aa"), "")

    def test_duplicates(self):
        self.assertEqual(min_window("AAADOBECODEBANC", "AABC"), "AAADOBEC")

    def test_no_match(self):
        self.assertEqual(min_window("ABCDEF", "XYZ"), "")

if __name__ == "__main__":
    unittest.main()
