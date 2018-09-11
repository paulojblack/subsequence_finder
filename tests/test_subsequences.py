import unittest
import random
from subsequence_finder import subseq_finder

class Tester(unittest.TestCase):
    def test_given_list(self):
        test_array = [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]

        result = subseq_finder.find_consecutive_runs(test_array)

        self.assertEqual(result, [0, 4, 6, 7])

    def test_only_decreasing(self):
        test_array = [10, 9, 8, 7, 2, 3, 5, 4, 3]

        result = subseq_finder.find_consecutive_runs(test_array)

        self.assertEqual(result, [0, 1, 6])

    def test_only_increasing(self):
        test_array = [1, 3, 5, 6, 7, 8, 10, 9, 2, 3, 4]

        result = subseq_finder.find_consecutive_runs(test_array)

        self.assertEqual(result, [2, 3, 8])

    def test_ends_mid_sequence(self):
        test_array = [1, 5, 7, 6, 5, 4, 3]

        result = subseq_finder.find_consecutive_runs(test_array)

        self.assertEqual(result, [2, 3, 4])

    def test_single_sequence(self):
        test_array = [3, 4, 5]

        result = subseq_finder.find_consecutive_runs(test_array)

        self.assertEqual(result, [0])

