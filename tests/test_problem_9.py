import unittest
from problems.problem_9 import insert_interval

class TestProblem9(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(insert_interval([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])

    def test_example_2(self):
        self.assertEqual(insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]), [[1, 2], [3, 10], [12, 16]])

    def test_empty(self):
        self.assertEqual(insert_interval([], [5, 7]), [[5, 7]])

    def test_insert_beginning(self):
        self.assertEqual(insert_interval([[3, 5], [6, 8]], [1, 2]), [[1, 2], [3, 5], [6, 8]])

    def test_insert_end(self):
        self.assertEqual(insert_interval([[1, 2], [3, 5]], [6, 8]), [[1, 2], [3, 5], [6, 8]])

if __name__ == "__main__":
    unittest.main()
