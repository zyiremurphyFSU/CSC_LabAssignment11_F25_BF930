import unittest

from list_sum import sum_list


class TestSumList(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_list([1, 2, 3, 4, 5]), 15)

    def test_with_negative_numbers(self):
        self.assertEqual(sum_list([5, 19, 2, 33, -5, 2]), 56)

    def test_empty_list(self):
        self.assertEqual(sum_list([]), 0)

    def test_single_element(self):
        self.assertEqual(sum_list([10]), 10)

    def test_large_numbers(self):
        self.assertEqual(sum_list([1000000, 2000000, 3000000]), 6000000)


if __name__ == "__main__":
    unittest.main()
