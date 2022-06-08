import unittest
from magicSquare import magicSquare

class Test(unittest.TestCase):
    def setUp(self):
        self.squareAllDiff = [[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]]
        self.squareSingleValue = [[1, 1, 1],
                                  [1, 1, 1],
                                  [1, 1, 1]]
        self.squareAllDiffValid = [[8, 1, 6],
                                   [3, 5, 7],
                                   [4, 9, 2]]

    def test_magicSquare_allDiff(self):
        self.assertEqual(magicSquare(self.squareAllDiff), False)
    def test_magicSquare_singleValue(self):
        self.assertEqual(magicSquare(self.squareSingleValue), True)
    def test_magicSquare_sumColumnsValid(self):
        self.assertEqual(magicSquare(self.squareAllDiffValid), True)
