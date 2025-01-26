import unittest
from conversion import dollars_to_dirhams, meters_to_kilometers

class TestConversion(unittest.TestCase):

    def test_dollars_to_dirhams(self):
        self.assertEqual(dollars_to_dirhams(1), 10)
        self.assertEqual(dollars_to_dirhams(0), 0)
        self.assertAlmostEqual(dollars_to_dirhams(2.0), 20.0)
        with self.assertRaises(ValueError):
            dollars_to_dirhams(-10)

    def test_meters_to_kilometers(self):
        self.assertEqual(meters_to_kilometers(2000), 2)
        self.assertEqual(meters_to_kilometers(0), 0)
        self.assertAlmostEqual(meters_to_kilometers(4000), 4)
        with self.assertRaises(ValueError):
            meters_to_kilometers(-339)

if __name__ == "__main__":
    unittest.main()