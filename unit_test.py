import unittest
from my_main import add_func,minuse_func

class CalculatorTestCase(unittest.TestCase):
    
    def test_plus(self):
        expected = 8;
        result = add_func(3,5);
        self.assertEqual(expected, result);

    def test_minus(self):
        expected = -2;
        result = minuse_func(3,5);
        self.assertEqual(expected, result);
        
if __name__=='__main__':
    unittest.main()