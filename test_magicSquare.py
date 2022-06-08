import unittest
from magicSquare import magicSquare

class Test(unittest.TestCase):
    def setUp(self):
        self.square1 = [[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]]
        self.square2 = [[1, 1, 1],
                        [1, 1, 1],
                        [1, 1, 1]]

    def test_magicSquare(self):
        self.assertEqual(magicSquare(self.square1), False)
        self.assertEqual(magicSquare(self.square2), True)
