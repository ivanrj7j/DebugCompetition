import unittest
from problems.problem_1 import min_sub_array_len

class TestProblem1(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(min_sub_array_len(7, [2, 3, 1, 2, 4, 3]), 2)

    def test_example_2(self):
        self.assertEqual(min_sub_array_len(4, [1, 4, 4]), 1)

    def test_example_3(self):
        self.assertEqual(min_sub_array_len(11, [1, 1, 1, 1, 1, 1, 1, 1]), 0)

    def test_exact_match(self):
        self.assertEqual(min_sub_array_len(5, [2, 3, 1, 1, 1]), 2)

    def test_single_element_pass(self):
        self.assertEqual(min_sub_array_len(3, [3]), 1)

    def test_single_element_fail(self):
        self.assertEqual(min_sub_array_len(5, [3]), 0)

    def test_entire_array(self):
        self.assertEqual(min_sub_array_len(15, [1, 2, 3, 4, 5]), 5)

if __name__ == "__main__":
    unittest.main()
