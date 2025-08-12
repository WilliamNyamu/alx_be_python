import unittest
import calculator

class TestCalc(unittest.TestCase):
    def test_add(self):
        result =  calculator.add(10,5)
        self.assertEqual(result, 15)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(-1, -1), 0)
        self.assertEqual(calculator.subtract(0, 2), -2)
    
    def test_multiply(self):
        self.assertEqual(calculator.multiply(10, 5), 50.00)
        self.assertEqual(calculator.multiply(0, 3), 0.00)
        self.assertEqual(calculator.multiply(3.3, 8.5), 28.05)
    
    def test_divide(self):
        self.assertEqual(calculator.divide(3, 3), 1)
        self.assertEqual(calculator.divide(-1, 1), -1)
        self.assertEqual(calculator.divide(-1, -1), 1)

        # When all the test are OK, then it shows that the ValueError was properly raised
        # Note how we don't pass arguments to the divide function
        self.assertRaises(ValueError, calculator.divide, 10, 0)

        # Better way
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)

if __name__ == '__main__':
    unittest.main()