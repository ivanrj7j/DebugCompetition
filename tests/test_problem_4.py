import unittest
from problems.problem_4 import daily_temperatures

class TestProblem4(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])

    def test_example_2(self):
        self.assertEqual(daily_temperatures([30, 40, 50, 60]), [1, 1, 1, 0])

    def test_example_3(self):
        self.assertEqual(daily_temperatures([30, 60, 90]), [1, 1, 0])

    def test_decreasing(self):
        self.assertEqual(daily_temperatures([90, 80, 70, 60]), [0, 0, 0, 0])

if __name__ == "__main__":
    unittest.main()
