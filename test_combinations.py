import unittest
from combinations import print_sum_combinations


class CombinationsTests(unittest.TestCase):

    def test_zero_ignored(self):
        self.assertEqual([], print_sum_combinations([1], 0))

    def test_prints_indicies_equals_4(self):
        numbers = [1, 1, 2, 2, 4]
        self.assertEqual(
            ["0 1 2", "0 1 3", "2 3", "4"],
            sorted(print_sum_combinations(numbers, 4))
        )

    def test_prints_indicies_equals_6(self):
        numbers = [1, 1, 2, 7, 12]
        self.assertEqual(
            [],
            sorted(print_sum_combinations(numbers, 6))
        )
