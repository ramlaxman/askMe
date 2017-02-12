#!/usr/bin/env python
from __future__ import print_function
import unittest


def zero_out(matrix):
    """For each zero element in the given matrix, the function will zero

       out the column and the row of that element.
    """
    num_of_cols = len(matrix[0])
    zero_rows = [row_num for row_num, row in enumerate(matrix) if not all(row)]
    zero_cols = [
        col_num for col_num, col in enumerate(zip(*matrix)) if not all(col)]
    for row_num in zero_rows:
        matrix[row_num] = [0] * num_of_cols
    for col_num in zero_cols:
        for row in matrix:
            row[col_num] = 0


class TestZeroOut(unittest.TestCase):

    def test_zero_out(self):

        matrix = [[1, 2, 3, 4],
                  [2, 0, 3, 0],
                  [0, 1, 2, 3]]
        zero_out_matrix = [[0, 0, 3, 0],
                           [0, 0, 0, 0],
                           [0, 0, 0, 0]]
        zero_out(matrix)
        self.assertEqual(matrix, zero_out_matrix)

if __name__ == '__main__':
    unittest.main()
