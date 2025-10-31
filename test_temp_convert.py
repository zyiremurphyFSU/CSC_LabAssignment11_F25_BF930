import unittest
from unittest.mock import patch
from io import StringIO
from temp_convert import *


class TestTemperatureFunctions(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40)
        self.assertAlmostEqual(celsius_to_fahrenheit(36.5), 97.7)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100)
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40)
        self.assertAlmostEqual(fahrenheit_to_celsius(101.3), 38.5, places=1)

    @patch("sys.stdout", new_callable=StringIO)
    def test_main_print_output(self, mock_stdout):
        main()
        output = mock_stdout.getvalue()

        self.assertIn("97.7", output)
        self.assertIn("38.5", output)


if __name__ == "__main__":
    unittest.main()
