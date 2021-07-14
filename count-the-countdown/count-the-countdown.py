"""
Challenge details

https://edabit.com/challenge/KveKxSD9t8fX7ybSt

"""
import unittest


def final_countdown(checking_list):
    return 1


class TestStringMethods(unittest.TestCase):

    def test_countdown(self):
        self.assertEqual(final_countdown([5, 4, 3, 2, 1]), [1, [[5, 4, 3, 2, 1]]])
        self.assertEqual(final_countdown([2, 5, 4, 3, 2, 1, 2]), [1, [[5, 4, 3, 2, 1]]])
        self.assertEqual(final_countdown([2, 3, 2, 1, 4, 3, 2, 1]), [2, [[3, 2, 1], [4, 3, 2, 1]]])
        self.assertEqual(final_countdown([4, 3, 2, 5, 4, 3]), [0, []])
        self.assertEqual(final_countdown([4, 3, 2, 5, 4, 3, 1]), [1, [[1]]])
        self.assertEqual(final_countdown([3, 2, 1, 5, 5, 3, 2, 1, 5, 5]), [2, [[3, 2, 1], [3, 2, 1]]])
        self.assertEqual(final_countdown([4, 8, 3, 2, 1, 2]), [1, [[3, 2, 1]]])
        self.assertEqual(final_countdown([4, 4, 5, 4, 3, 2, 1, 8, 3, 2, 1]), [2, [[5, 4, 3, 2, 1], [3, 2, 1]]])
        self.assertEqual(final_countdown([4, 3, 2, 1, 3, 2, 1, 1]), [3, [[4, 3, 2, 1], [3, 2, 1], [1]]])
        self.assertEqual(final_countdown([1, 2, 1, 1]), [3, [[1], [2, 1], [1]]])
        self.assertEqual(final_countdown([1, 2, 3, 4, 3, 2, 1]), [2, [[1], [4, 3, 2, 1]]])
        self.assertEqual(final_countdown([]), [0, []])
        self.assertEqual(final_countdown([2, 1, 2, 1]), [2, [[2, 1], [2, 1]]])


if __name__ == '__main__':
    unittest.main()