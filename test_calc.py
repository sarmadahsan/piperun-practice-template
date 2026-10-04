import unittest

from calc import add, average, percent_change, subtract


class CalcTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_average(self):
        self.assertAlmostEqual(average([2, 4, 6]), 4.0)

    def test_percent_change_from_50_to_75_is_50_percent(self):
        self.assertAlmostEqual(percent_change(50, 75), 50.0)


if __name__ == "__main__":
    unittest.main()
