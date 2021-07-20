"""
Challenge details

https://edabit.com/challenge/KveKxSD9t8fX7ybSt

Count the Countdown Sequences

A countdown sequence is a descending sequence of k integers from k
down to 1 (e.g. 5, 4, 3, 2, 1). Write a function that returns a list [x, y] where
x is the number that represents how many of countdown sequences are in a given list
and y is a list of those sequences in order which they appear in the list.

Example:
    final_countdown([4, 4, 5, 4, 3, 2, 1, 8, 3, 2, 1]) ➞ [2, [[5, 4, 3, 2, 1], [3, 2, 1]]]

Notes
[1] is a valid countdown sequence.
All numbers will be greater than 0.

"""
import unittest


def final_countdown(checking_list):
    i = 0
    k = 1
    series_len = len(checking_list)
    sequences_result = []
    sequences_counter = 0
    while k < series_len:
        j = 0
        draft_list = []
        while checking_list[i+j] - checking_list[k] == 1:
            print(i, j, k)
            print(checking_list[i+j], checking_list[k])
            draft_list.extend([checking_list[i+j], checking_list[k]])
            j += 1
            k += 1
            if k == series_len:
                break
        sequences_counter += 1
        sequences_result.append(sorted(list(set(draft_list)), reverse=True))
        print(sequences_result)
        i = k
        k += 1
    return [sequences_counter, sequences_result]


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
