import unittest
from simple_calculator import SimpleCalculator 

class SimpleCalculatorTest(unittest.TestCase):
    def test_addition(self):
        math = SimpleCalculator() 
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-5, 5), 0)
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_subtraction(self):
        math = SimpleCalculator()
        self.assertEqual(self.calc.subtract(5, 4), 1)
        self.assertEqual(self.calc.subtract(2, 10), -8)
        self.assertEqual(self.calc.subtract(5, 5), 0)

    def test_multiplication(self):
        math = SimpleCalculator()
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(-2, 5), -10)

    def test_division(self):
        math = SimpleCalculator()
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 0), None)
        self.assertEqual(self.calc.(-10, 5), -2)
