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

    def test_magicSquare_allDiff(self):
        self.assertEqual(magicSquare(self.squareAllDiff), False)
    def test_magicSquare_singleValue(self):
        self.assertEqual(magicSquare(self.squareSingleValue), True)
