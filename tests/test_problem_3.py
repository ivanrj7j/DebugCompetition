import unittest
from problems.problem_3 import top_k_frequent

class TestProblem3(unittest.TestCase):
    def test_example_1(self):
        self.assertCountEqual(top_k_frequent([1, 1, 1, 2, 2, 3], 2), [1, 2])

    def test_example_2(self):
        self.assertEqual(top_k_frequent([1], 1), [1])

    def test_negative_numbers(self):
        self.assertCountEqual(top_k_frequent([-1, -1, 2, 2, 2, 3], 2), [2, -1])

    def test_all_same_frequency(self):
        self.assertCountEqual(top_k_frequent([4, 5, 6], 2), [4, 5])

if __name__ == "__main__":
    unittest.main()
