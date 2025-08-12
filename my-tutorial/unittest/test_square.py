import unittest
from square import number_square

class NumberSquare(unittest.TestCase):

    def test_number_square(self):
        self.assertEqual(number_square(4), 16)
        self.assertEqual(number_square(0),0)

    def test_valid_input(self):
        self.assertIsInstance(number_square(4), int)
    

if __name__ == '__main__':
    unittest.main()