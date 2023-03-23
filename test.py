import unittest
from whiteboard import solution

class TestWhiteboard(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([2, 2, 3, 4]), 2)

    def test_2(self):
        self.assertEqual(solution([1, 2, 2, 3, 3, 3]), 3)

    def test_3(self):
        self.assertEqual(solution([1, 1, 1, 1, 1]), -1)

    def test_4(self):
        self.assertEqual(solution([4, 4, 4, 4, 3, 2, 1, 1]), 4)
    def test_5(self):
        self.assertEqual(solution([1]), 1)

if __name__ == "__main__":
    unittest.main()