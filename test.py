import unittest
from matrix import Matrix

class MatrixTest(unittest.TestCase):

    m_rows = ['catt', 'aata', 'tatc']
    m_columns = ['cat', 'aaa', 'ttt', 'tac']
    m_back_diagonals = ['t', 'aa', 'cat', 'atc', 'ta', 't']
    m_forw_diagonals = ['c', 'at', 'tta', 'tat', 'aa', 'c']

    def setUp(self):
        self.matrix = Matrix(3, 4)
        for i, values in enumerate(self.m_rows):
            self.matrix.fillRow(i, list(values))

    def test_initError(self):
        with self.assertRaisesRegex(ValueError, 'rows must be greater than or equal to 2'):
            Matrix(1, 3)
        with self.assertRaisesRegex(ValueError, 'cols must be greater than or equal to 2'):
            Matrix(3, 1)

    def test_numRows(self):
        self.assertEqual(3, self.matrix.numRows)

    def test_numColumns(self):
        self.assertEqual(4, self.matrix.numColumns)

    def test_get(self):
        self.assertEqual(self.matrix.get(0, 0), 'c')
        self.assertEqual(self.matrix.get(2, 4), None)

    def test_set(self):
        self.matrix.set(0, 0, 'z')
        self.assertEqual(self.matrix.get(0, 0), 'z')

    def test_getRows(self):
        rows = [list(r) for r in self.m_rows]
        self.assertEqual(rows, self.matrix.getRows())

    def test_getColumns(self):
        cols = [list(c) for c in self.m_columns]
        self.assertEqual(cols, self.matrix.getColumns())

    def test_getRow(self):
        self.assertEqual(self.matrix.getRow(0), list(self.m_rows[0]))

    def test_getColumn(self):
        self.assertEqual(self.matrix.getColumn(2), list(self.m_columns[2]))
        
    def test_fillRow(self):
        row = ['a', 'b', 'c', 'd']
        self.matrix.fillRow(0, row)
        self.assertEqual(self.matrix.getRow(0), row)

    def test_fillColumn(self):
        col = ['a', 'b', 'c']
        self.matrix.fillColumn(0, col)
        self.assertEqual(self.matrix.getColumn(0), col)

    def test_getDiagonal_forward(self):
        pass

    def test_getDiagonal_backward(self):
        pass

    def test_getDiagonals_forward(self):
        diagonals = [list(x) for x in self.m_forw_diagonals]
        self.assertEqual(sorted(diagonals), sorted(self.matrix.getDiagonals(forward=True)))

    def test_getDiagonals_backward(self):
        diagonals = [list(x) for x in self.m_back_diagonals]
        self.assertEqual(sorted(diagonals), sorted(self.matrix.getDiagonals()))

if __name__ == '__main__':
    unittest.main()