import unittest
from problems.problem_6 import check_subarray_sum

class TestProblem6(unittest.TestCase):
    def test_example_1(self):
        self.assertTrue(check_subarray_sum([23, 2, 4, 6, 7], 6))

    def test_example_2(self):
        self.assertTrue(check_subarray_sum([23, 2, 6, 4, 7], 6))

    def test_example_3(self):
        self.assertFalse(check_subarray_sum([23, 2, 6, 4, 7], 13))

    def test_zeros(self):
        self.assertTrue(check_subarray_sum([0, 0], 1))

    def test_length_two(self):
        self.assertTrue(check_subarray_sum([5, 5], 5))

if __name__ == "__main__":
    unittest.main()
