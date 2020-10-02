import unittest
from combinations import print_sum_combinations


class CombinationsTests(unittest.TestCase):

    def test_initial(self):
        self.assertEqual(True, print_sum_combinations())
