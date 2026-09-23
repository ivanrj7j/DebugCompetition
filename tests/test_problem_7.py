import unittest
from problems.problem_7 import check_inclusion

class TestProblem7(unittest.TestCase):
    def test_example_1(self):
        self.assertTrue(check_inclusion("ab", "eidbaooo"))

    def test_example_2(self):
        self.assertFalse(check_inclusion("ab", "eidboaoo"))

    def test_exact_match(self):
        self.assertTrue(check_inclusion("adc", "dcda"))

    def test_single_char(self):
        self.assertTrue(check_inclusion("a", "a"))

    def test_s1_longer(self):
        self.assertFalse(check_inclusion("hello", "hi"))

if __name__ == "__main__":
    unittest.main()
