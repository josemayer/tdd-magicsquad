import unittest
from magicSquare import magicSquare

class Test(unittest.TestCase):
    def setUp(self):
        self.square1 = [[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]]

    def test_magicSquare(self):
        self.assertEquals(magicSquare(self.square1), False)
