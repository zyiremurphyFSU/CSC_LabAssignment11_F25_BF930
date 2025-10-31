import unittest
from rectangle_info import rectangle_info


class TestRectangleInfo(unittest.TestCase):
    def test_basic_rectangle(self):
        """Test with simple positive numbers"""
        a, p, d = rectangle_info(3, 4)
        self.assertEqual(a, 12)
        self.assertEqual(p, 14)
        self.assertAlmostEqual(d, 5.0, places=5)

    def test_square(self):
        """Test with a square (width == height)"""
        a, p, d = rectangle_info(5, 5)
        self.assertEqual(a, 25)
        self.assertEqual(p, 20)
        self.assertAlmostEqual(d, 7.07107, places=5)

    def test_float_values(self):
        """Test with float dimensions"""
        a, p, d = rectangle_info(2.5, 4.0)
        self.assertAlmostEqual(a, 10.0)
        self.assertAlmostEqual(p, 13.0)
        self.assertAlmostEqual(d, 4.71699, places=5)

    def test_zero_dimension(self):
        """Test when one dimension is zero"""
        a, p, d = rectangle_info(0, 5)
        self.assertEqual(a, 0)
        self.assertEqual(p, 10)
        self.assertEqual(d, 5)

    def test_negative_values(self):
        """Test when width or height is negative (geometrically invalid but allowed)"""
        a, p, d = rectangle_info(-3, 4)
        self.assertEqual(a, -12)
        self.assertEqual(p, 2)
        self.assertAlmostEqual(d, 5.0, places=5)


if __name__ == "__main__":
    unittest.main()
