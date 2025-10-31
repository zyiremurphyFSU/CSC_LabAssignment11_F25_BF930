import unittest
from random_numbers import generator


class TestGenerator(unittest.TestCase):
    def test_length(self):
        """Test if generated list has correct length"""
        result = generator(10, 1, 100)
        self.assertEqual(len(result), 10)

    def test_range(self):
        """Test if all numbers are within the given range"""
        result = generator(20, 5, 15)
        for num in result:
            self.assertGreaterEqual(num, 5)
            self.assertLessEqual(num, 15)

    def test_negative_range(self):
        """Test if generator works with negative ranges"""
        result = generator(10, -10, -1)
        for num in result:
            self.assertGreaterEqual(num, -10)
            self.assertLessEqual(num, -1)

    def test_randomness(self):
        """Test if two generated lists are not identical (very likely)"""
        r1 = generator(5, 1, 10)
        r2 = generator(5, 1, 10)
        self.assertNotEqual(r1, r2, "Two random lists happened to be identical")


if __name__ == "__main__":
    unittest.main()
