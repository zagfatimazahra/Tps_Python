import unittest
from mon_projet.src.math_operations import add, subtract, multiply, divide

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 6), 16)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, -7), -7)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-5, -10), 5)

    def test_multiply(self):
        self.assertEqual(multiply(1, -1), -1)
        self.assertEqual(multiply(0, 9), 0)
        self.assertEqual(multiply(2, 4), 8)

    def test_divide(self):
        self.assertEqual(divide(20, 2), 10)
        self.assertEqual(divide(12, -4), -3)
        with self.assertRaises(ValueError):
            divide(100, 0)

if __name__ == "__main__":
    unittest.main()
