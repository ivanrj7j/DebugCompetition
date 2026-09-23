import unittest
from problems.problem_8 import simplify_path

class TestProblem8(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(simplify_path("/home/"), "/home")

    def test_example_2(self):
        self.assertEqual(simplify_path("/../"), "/")

    def test_example_3(self):
        self.assertEqual(simplify_path("/home//foo/"), "/home/foo")

    def test_parent_dirs(self):
        self.assertEqual(simplify_path("/a/./b/../../c/"), "/c")

    def test_multiple_slashes(self):
        self.assertEqual(simplify_path("/a//b////c/d//././/.."), "/a/b/c")

if __name__ == "__main__":
    unittest.main()
