import unittest
from problems.problem_5 import erase_overlap_intervals

class TestProblem5(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]), 1)

    def test_example_2(self):
        self.assertEqual(erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]), 2)

    def test_example_3(self):
        self.assertEqual(erase_overlap_intervals([[1, 2], [2, 3]]), 0)

    def test_tricky_greedy(self):
        self.assertEqual(erase_overlap_intervals([[1, 100], [11, 22], [1, 11], [2, 12]]), 2)

if __name__ == "__main__":
    unittest.main()
