import unittest

def area_square(n):
    return n * n

class AreaSquareTest(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(area_square(5), 25)
        self.assertEqual(area_square(10), 100)

    def test_negative_values(self):
        self.assertEqual(area_square(-5), 25)
        self.assertEqual(area_square(-10), 100)

    def test_zero_value(self):
        self.assertEqual(area_square(0), 0)

    def test_decimal_value(self):
        self.assertEqual(area_square(1.5), 2.25)
        self.assertAlmostEqual(area_square(2.5), 6.25, places=5)

if __name__ == '__main__':
    unittest.main()
